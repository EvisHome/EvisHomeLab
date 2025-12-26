# AI Log Summary: Turning Noise into Insights

**Project Status:** ✅ Operational  
**Components:** Grafana Loki, Google Gemini 2.0 Flash, Home Assistant, Unraid, Python

### 1. The Problem: Log Fatigue
In a distributed homelab (Unraid, Proxmox VE, Edge Servers, DNS (Adguard + Unbound), Traefik, Unifi Network, Tailscale ...), logs are scattered everywhere.

* **Volume:** My servers generate ~1GB of text logs daily.
* **Visibility:** I only looked at logs *after* I noticed something was broken.
* **Noise:** 99% of logs are "Info", masking the 1% "Critical" errors.

I needed a system that wouldn't just *store* logs, but actively *analyze* them and tap me on the shoulder only when it found something I actually needed to see.

### 2. The Solution
I built a centralized logging pipeline using **Grafana** and **Loki** (for storage) and a custom **Python + Gemini** script (for analysis).

Instead of feeding raw logs to an LLM (which is slow and expensive), I implemented a **"Pre-processing Engine"** that:

1.  **Fetches** the last 24 hours of history.
2.  **Deduplicates** repetitive errors (e.g., compressing 5,000 "Connection Refused" lines into 1 line).
3.  **Summarizes** the context using Google Gemini.
4.  **Reports** the findings to my Home Assistant dashboard.

![type:video](/ai-log-summary/ai-home-assistant-dashboard.mp4)

<a href="../ai-log-summary/ai-home-assistant-dashboard.mp4" target="_blank" title="Click to watch full screen">
  <video width="100%" autoplay loop muted playsinline style="cursor: pointer;">
    <source src="../ai-log-summary/ai-home-assistant-dashboard.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</a>
<p style="text-align: center; font-size: 0.8em; color: grey;">
  <i>(Click video to enlarge)</i>
</p>

### 3. Architecture Diagram

```mermaid
graph TD
    %% --- LEVEL 1: EDGE ---
    subgraph Edge ["Edge Nodes (Collectors)"]
        direction TB
        Docker[Docker Logs] & System[System Logs] --> Promtail[Promtail Agent]
    end

    %% --- LEVEL 2: UNRAID ---
    subgraph Unraid ["Unraid Server (The Brain)"]
        direction TB
        Promtail -->|Push| Loki[Loki DB]
        
        %% The Fork: Human vs AI
        Loki -->|Visualise| Grafana[Grafana UI]
        Loki -->|Fetch| Script[Python Script]
        
        Script <-->|Analyze| Gemini[Gemini API]
    end

    %% --- LEVEL 3: HA ---
    subgraph HA ["Home Assistant (Interface)"]
        direction TB
        Script -->|Webhook| Core[Home Assistant]
        Core --> Phone[Mobile Alert]
        Core --> Wall[Dashboard]
    end

    %% --- THE FIX: INVISIBLE STRUT ---
    %% Forces HA to stay at the bottom
    Gemini ~~~ Core

    %% --- STYLING ---
    style Loki fill:#f9f,stroke:#333,stroke-width:2px
    style Script fill:#ff9,stroke:#333,stroke-width:2px
    style Gemini fill:#4285f4,stroke:#fff,stroke-width:2px,color:#fff
    style Grafana fill:#ff9900,stroke:#333,stroke-width:2px,color:white
```

### 4. Key Features
* **Cost Efficient:** Uses client-side deduplication to reduce token usage by ~95%.
* **Massive Context:** Can analyze up to 50,000 log lines per run.
* **Self-Healing:** If the report fails, Home Assistant retains the last known state.
* **Privacy:** Only anonymized/filtered error logs are sent to the AI; raw logs stay local.

***
<!--
### File 2: `02-implementation.md`
*Use this file for the technical setup steps and code.*
-->
<br>
<br>


## Implementation Guide

This guide details how to reproduce the "AI Log SRE" stack.

### Prerequisites
* **Unraid Server** (or any Docker host).
* **Google Gemini API Key** (Free tier is sufficient, Paid recommended for high limits).
* **Home Assistant** (for notifications).

---

### Step 1: Central Server (Unraid)
We run the `loki` database and the `ai-reporter` script in a single stack.

#### Docker Compose
```yaml
services:
  loki:
    image: grafana/loki:3.1.0
    container_name: loki
    user: "0:0"
    volumes:
      - /mnt/docker/appdata/loki:/loki
    command: -config.file=/loki/local-config.yaml
    network_mode: host
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - /mnt/docker/appdata/grafana:/var/lib/grafana
    restart: unless-stopped

  ai-log-reporter:
    image: python:3.11-slim
    container_name: ai-log-reporter
    volumes:
      - /mnt/docker/appdata/ai-reporter:/app
    environment:
      - LOKI_URL=http://localhost:3100
      - GEMINI_API_KEY=your_gemini_key_here
      - HA_URL=[http://[HA-IP]:8123](http://[HA-IP]:8123)
      - HA_TOKEN=your_ha_long_lived_token
    # Installs dependencies and runs script on demand
    command: >
      sh -c "pip install requests google-genai && 
      tail -f /dev/null"
    network_mode: host
    restart: unless-stopped
```

**Loki Configuration** (local-config.yaml)
*Critical:* The `max_entries_limit_per_query` must be increased to allow the AI to see full history.

```yaml
auth_enabled: false

server:
  http_listen_port: 3100

common:
  instance_addr: 0.0.0.0
  path_prefix: /loki
  storage:
    filesystem:
      chunks_directory: /loki/chunks
      rules_directory: /loki/rules
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2024-04-01
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

compactor:
  working_directory: /loki/boltdb-shipper-compactor
  retention_enabled: true

limits_config:
  retention_period: 720h  # 30 Days

  # --- Rate Limiting  ---
  reject_old_samples: true
  reject_old_samples_max_age: 168h
  ingestion_rate_mb: 20
  ingestion_burst_size_mb: 40
  per_stream_rate_limit: 20MB
  per_stream_rate_limit_burst: 40MB

  max_entries_limit_per_query: 50000  # <--- CRITICAL FOR AI
```

#### Step 2: Log Collection (Edge Nodes)
On every other server (Proxmox, Pi, Edge), we run **Promtail** to ship logs to Unraid.

**Promtail Config** (config.yml)
```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  # Your Unraid IP
  - url: http://[UNRAID-IP]:3100/loki/api/v1/push

scrape_configs:
  # --- SYSTEM LOGS ---
  - job_name: system
    static_configs:
    - targets:
        - localhost
      labels:
        host: docker-server-edge          # <--- UPDATED for Node 63
        service_name: os-system
        __path__: /var/log/*.log

  # --- DOCKER LOGS (Smart Proxy Mode) ---
  - job_name: docker
    docker_sd_configs:
      - host: tcp://docker-socket-proxy:2375
        refresh_interval: 5s

    relabel_configs:
      # 1. Get Container Name
      - source_labels: ['__meta_docker_container_name']
        regex: '/(.*)'
        target_label: 'container_name'

      # 2. Get Container ID
      - source_labels: ['__meta_docker_container_id']
        target_label: 'container_id'

      # 3. FORCE the "host" label
      - target_label: 'host'
        replacement: 'docker-server-edge' # <--- UPDATED for Node 63

      # 4. Force Service Name (AI Reporter)
      - target_label: 'service_name'
        replacement: 'docker'

      # 5. Force Job Label
      - target_label: 'job'
        replacement: 'docker'

    pipeline_stages:
      # 1. Standard Docker Unwrap
      - docker: {}

      # 2. Socket Proxy Level Detection (200=info)
      - match:
          selector: '{container_name="docker-socket-proxy"}'
          stages:
            - regex:
                expression: '\s\d+/\d+/\d+/\d+/\d+\s+(?P<status_code>\d{3})\s'
            - template:
                source: level
                template: '{{ if hasPrefix "2" .status_code }}info{{ else if hasPrefix "3" .status_code }}inftatus_code }}warn{{ else if hasPrefix "5" .status_code }}error{{ else }}unknown{{ end }}'
            - labels:
                level:

      # 3. Standard Level Detection
      - regex:
          expression: '(?i)(?:level|lvl|severity)=(?P<level>\w+)|\[(?P<level>\w+)\]'
      - labels:
          level:

```

#### Step 3: The Intelligence (Python Script)
This script runs inside the `ai-log-reporter` container.

**Key Logic:**

1. Fetches last 24h of logs (level=error or warn).
2. Uses a defaultdict to count duplicates.
3. Truncates output if > 90k chars.

(See repository for full reporter.py source code)

***

Step 4: Home Assistant Package
The automation that triggers the report and displays it.

```yaml
shell_command:
  generate_ai_log_summary: >
    ssh -i /config/.ssh/id_rsa -o StrictHostKeyChecking=no root@[UNRAID-IP] 'docker exec ai-log-reporter python /app/reporter.py'

automation:
  - alias: "Daily AI System Summary"
    trigger:
      - platform: time
        at: "07:00:00"
      - platform: homeassistant
        event: start
    action:
      - delay: "00:01:00"
      - action: script.run_ai_summary_now
```

***

<!--
### File 3: `03-user-manual.md`
*Use this file to explain how to interpret the results.*
-->

<br>
<br>


## User Manual & Operations

### How to Read the Daily Report
The AI Summary appears in Home Assistant every morning at 07:00.

#### The Iconography
* 🔴 **CRITICAL:** Immediate action required.
    * *Examples:* Database corruption, Disk failure (SMART), Service boot loops.
    * *Action:* Check Grafana immediately.
* 🛡️ **SECURITY:** Passive protection info.
    * *Examples:* "CrowdSec blocked 50 IPs", "Brute force attempt on SSH".
    * *Action:* None (System is doing its job).
* 🟡 **WARNING:** Non-critical noise.
    * *Examples:* Timeouts, configuration deprecation warnings.
    * *Action:* Add to "Technical Debt" to-do list.

### Troubleshooting
**"Report says: No critical errors found."**
* **Good News:** Your system is healthy!
* **Verification:** Check the `ai-log-reporter` container logs to ensure it actually ran and didn't just fail to fetch data.

**"Report is Empty or Unknown"**
* Check Home Assistant logs for `Shell Command` errors.
* Ensure the SSH key in Home Assistant allows connection to Unraid without a password.

### Grafana Deep Dive
When the AI reports a "Critical" error, use Grafana to investigate.

**Recommended LogQL Query:**
To see the raw data the AI analyzed:
```logql
{job=~".+"} != "docker-socket-proxy" |= "error"