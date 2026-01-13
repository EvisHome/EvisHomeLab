---
title: Self-Healing Tailscale Nodes
date: 2026-01-13
description: Stabilize Tailscale Exit Nodes running as Proxmox LXCs and integrate them into Home Assistant for active monitoring and automated recovery.
image: self-healing-tailscale-nodes/tailscale-main.png
highlight: true
tags:
  - Tailscale
  - Home Assistant
  - Proxmox
  - LXC
  - Automation
  - AI
---

# Self-Healing Tailscale Nodes

This guide documents how to stabilize Tailscale Exit Nodes running as Proxmox LXCs and integrate them into Home Assistant for active monitoring and automated recovery.

![Self-Healing Tailscale Nodes](../self-healing-tailscale-nodes/tailscale-main.png)

## Prerequisites

Before starting, ensure you have:

*   **Proxmox VE**: Hosting your Tailscale LXC container.
*   **Home Assistant**: Running and connected to your network.
*   **Proxmox Integration**: Installed in Home Assistant (via HACS or Official) and configured with permissions to restart LXCs.
*   **Tailscale**: Installed on both the LXC and Home Assistant.
*   **SSH/Console Access**: To the Proxmox LXC to create scripts.

## 1. Proxmox LXC Resource Settings

To keep these nodes "lightweight" but stable as Exit Nodes, we used the following hardware allocation in Proxmox:

![Proxmox Resources](../self-healing-tailscale-nodes/proxmox-tailscale-resources.png)

*   **Template**: `debian-12-standard` (or similar Ubuntu/Debian template).
*   **CPU**: 1 Core (Tailscale is very efficient; one core is plenty for a 1Gbps tunnel).
*   **Memory**: 512 MB (You can go as low as 256MB, but 512MB ensures the netcheck and ping scripts run smoothly without OOM issues).
*   **Disk**: 4 GB (Tailscale and its logs take up very little space).
*   **Unprivileged Container**: Yes (For security).
*   **Features**: Ensure **Nesting** is checked. (Required for Tailscale's internal networking).

## 2. The Critical Networking Fix (DHCPv6 Loop)

Before running any commands, we had to fix the Proxmox network configuration to prevent the "Death Loop."

By default, many Linux LXC templates negotiate both IPv4 and IPv6 DHCP. If your router (e.g., UniFi) isn't providing a DHCPv6 lease, the networking service enters an infinite `XMT: Solicit` loop and crashes.

In **Proxmox GUI** go to **LXC > Network > Edit eth0**:

![Proxmox Network Config](../self-healing-tailscale-nodes/proxmox-network.png)

*   **IPv4**: DHCP (Assigned via UniFi with a Static IP Reservation).
*   **IPv6**: Static, but with **all fields left completely blank**.

*Why? This prevents systemd-networkd from waiting for a DHCPv6 lease that never comes.*

## 3. Installation & Initial Setup

Once the LXC was started, we ran these commands in the terminal:

**Update the OS:**
```bash
apt update && apt upgrade -y
```

**Install Tailscale:**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

**Enable the Service (Persistence):**
```bash
systemctl enable --now tailscaled
```

## 4. Authenticating as an Exit Node

To make these nodes useful for your travel router or remote access, we initialized them with specific flags:

```bash
tailscale up --advertise-exit-node --accept-routes=false
```

*   `--advertise-exit-node`: Tells your Tailnet this node can act as an internet gateway.
*   `--accept-routes=false`: (**Crucial for LXCs**) Prevents the node from trying to route local subnet traffic through the tunnel, which often breaks SSH access to the container.

## 5. Enabling IP Forwarding (The "Engine")

For an Exit Node to actually pass traffic from other devices to the internet, Linux needs "IP Forwarding" enabled.

Run these to enable it immediately and permanently:

```bash
# Enable for IPv4
echo 'net.ipv4.ip_forward = 1' | tee -a /etc/sysctl.conf
# Enable for IPv6
echo 'net.ipv6.conf.all.forwarding = 1' | tee -a /etc/sysctl.conf
# Apply changes
sysctl -p
```



## 6. The Heartbeat Script

This script is the brain of the self-healing mechanism. Unlike a simple "is the process running" check, it validates the actual data path and reporting health status to Home Assistant.

We use a Bash script inside the LXC to perform a multi-stage check:
1.  **Daemon Check**: If `tailscaled` is stopped, it attempts to start it immediately.
2.  **Connectivity Check**: It pings Home Assistant to verify the tunnel is actually passing traffic.

### Create the script

Create the file at `/usr/local/bin/ts-heartbeat.sh`:

```bash
#!/bin/bash
TAILSCALE="/usr/bin/tailscale"
CURL="/usr/bin/curl"
HA_WEBHOOK_URL="http://10.0.0.105:8123/api/webhook/tailscale_halo_heartbeat"
HA_TAILSCALE_IP="100.92.181.98"

# 1. RECOVERY: If Tailscale is stopped, force it up with your Exit Node flags
if [[ $($TAILSCALE status) == *"Tailscale is stopped."* ]]; then
    $TAILSCALE up --advertise-exit-node --accept-routes=false > /dev/null 2>&1
    sleep 5
fi

# 2. INTEL: Refresh only the Tailscale repo to see if a new version exists
# This keeps the 'Candidate' version in apt-cache accurate for Gemini
apt-get update -o Dir::Etc::sourcelist="sources.list.d/tailscale.list" \
               -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0" > /dev/null 2>&1

# 3. GATHER DATA
CURRENT_VER=$($TAILSCALE version | head -n 1)
LATEST_VER=$(apt-cache policy tailscale | grep Candidate | awk '{print $2}')
# Extract Health warnings (converts JSON array to a comma-separated string)
HEALTH_DATA=$($TAILSCALE status --json | jq -r '.Health | join(", ")')
[[ -z "$HEALTH_DATA" || "$HEALTH_DATA" == "null" ]] && HEALTH_DATA="Healthy"

# 4. DEEP PULSE: Ping the HA Tailscale and send the JSON payload
if $TAILSCALE ping -c 1 -timeout 2s $HA_TAILSCALE_IP > /dev/null 2>&1; then
    $CURL -s -X POST "$HA_WEBHOOK_URL" \
      -H "Content-Type: application/json" \
      -d "{
        \"current\": \"$CURRENT_VER\", 
        \"latest\": \"$LATEST_VER\", 
        \"health\": \"$HEALTH_DATA\"
      }" > /dev/null 2>&1
fi
```

### Apply Permissions & Enable Service

The script must be executable, and the Tailscale service must be enabled to start on boot (critical for reboots):

```bash
chmod +x /usr/local/bin/ts-heartbeat.sh
systemctl enable tailscaled
```


## Methodology: Why ping Home Assistant?

We specifically check strict connectivity to **Home Assistant** rather than the general Internet (`netcheck`) or peer-to-peer (`Halo <-> Edge`):

1.  **Verifies Data Plane**: `tailscale status` only checks if the daemon is running. `tailscale ping` confirms packets can actually flow through the tunnel.
2.  **ISP Outage Proof**: Tailscale can route traffic over the local LAN even if the Internet is down. By pinging a local peer (Home Assistant), we prevent the node from rebooting in a loop during a simple ISP outage.
3.  **Fail-Safe**: If Home Assistant goes down, the automation engine (Watchdog) is also down. This creates a natural fail-safe where the node won't be rebooted accidentally if the monitoring server itself crashes.

## Scheduling with Cron

To ensure the pulse is consistent, we schedule the script to run every minute using the root user's crontab.

1.  Open crontab: `crontab -e`
2.  Add the following line at the bottom (ensure there is a blank line after it):

```plaintext
* * * * * /usr/local/bin/ts-heartbeat.sh
```

## Home Assistant Integration (The Package)

Instead of scattered sensors, we bundle the logic into a single Home Assistant Package. This includes a template binary sensor, a maintenance toggle, and the self-healing automation.

**File:** `/config/packages/halo_tailscale.yaml`

```yaml
# 0. SSH COMMANDS
shell_command:
  update_tailscale_halo: >
    ssh -i /config/.ssh/id_rsa
    -o IdentitiesOnly=yes
    -o BatchMode=yes
    -o ConnectTimeout=10
    -o StrictHostKeyChecking=no
    -o UserKnownHostsFile=/dev/null
    root@10.0.0.89
    'pct exec 101 -- tailscale update --yes'

script:
  update_tailscale_halo_node:
    alias: "Action: Update Tailscale Halo"
    icon: mdi:cloud-upload
    sequence:
      - action: shell_command.update_tailscale_halo
      - action: script.notify_smart_master
        data:
          title: "Tailscale Halo"
          message: "Update command sent to Proxmox Host (10.0.0.89). LXC 101 will reboot shortly."
          category: "system"
          tag: "tailscale_halo"

# 1. MAINTENANCE TOGGLE
# Use this in your dashboard to stop reboots during manual work
input_boolean:
  halo_maintenance_mode:
    name: "Halo Maintenance Mode"
    icon: mdi:wrench

# 2. HEARTBEAT SENSOR
# Receives the pulse from the LXC and turns off after 2 minutes of silence
template:
  - trigger:
      - platform: webhook
        webhook_id: "tailscale_halo_heartbeat"
        local_only: true
    binary_sensor:
      - name: "Tailscale Halo Heartbeat"
        state: "on"
        auto_off: "00:02:00"
        attributes:
          current_version: "{{ trigger.json.current }}"
          latest_version: "{{ trigger.json.latest }}"
          update_available: "{{ trigger.json.current != trigger.json.latest }}"
          health_status: "{{ trigger.json.health | default('Healthy') }}"

# 3. SELF-HEALING AUTOMATION
# Reboots the LXC via Proxmox if heartbeat is lost for 5 minutes
automation:
  - alias: "Tailscale Halo Auto-Recover"
    id: "tailscale_halo_auto_recover"
    trigger:
      - platform: state
        entity_id: binary_sensor.tailscale_halo_heartbeat
        to: "off"
        for: "00:05:00"
    condition:
      - condition: and
        conditions:
          # Condition 1: Maintenance mode must be OFF
          - condition: state
            entity_id: input_boolean.halo_maintenance_mode
            state: "off"

          # Condition 2: Container must be running (Proxmox Status)
          - condition: state
            entity_id: binary_sensor.lxc_tailscale_halo_101_status
            state: "on"
    action:
      - service: button.press
        target:
          # Verify your specific entity ID in HA
          entity_id: button.lxc_tailscale_halo_101_reboot
      - action: script.notify_smart_master
        data:
          title: "⚠️ Tailscale Halo Down"
          message: "Connectivity lost for 5m. Proxmox reboot command sent."
          category: "system"
          critical: true
          tag: "tailscale_halo"

  # 4. GEMINI ADVISOR (Updates & Health Issues)
  - alias: "Tailscale Gemini Advisor"
    id: "ts_gemini_advisor"
    trigger:
      # Trigger A: New version detected
      - platform: state
        entity_id: binary_sensor.tailscale_halo_heartbeat
        attribute: update_available
        to: true
      # Trigger B: Health status is no longer "Healthy"
      - platform: template
        value_template: >
          {{ state_attr('binary_sensor.tailscale_halo_heartbeat', 'health_status') not in ['Healthy', 'OK', 'null', none] }}
    action:
      - action: conversation.process
        data:
          agent_id: conversation.gemini_web_advisor # Dedicated Agent with Google Search enabled
          text: >
            Analyzing Tailscale Halo Node status.
            Update available: {{ state_attr('binary_sensor.tailscale_halo_heartbeat', 'update_available') }}
            Current Health: "{{ state_attr('binary_sensor.tailscale_halo_heartbeat', 'health_status') }}"
            Running Version: {{ state_attr('binary_sensor.tailscale_halo_heartbeat', 'current_version') }}
            Latest Version: {{ state_attr('binary_sensor.tailscale_halo_heartbeat', 'latest_version') }}

            If there is a health error, explain potential fixes for a Proxmox LXC context.
            If there is an update, search the web for the Tailscale changelog. Summarize the major changes and check for any breaking changes related to Subnet Routers or Exit Nodes.

            IMPORTANT: Keep your response extremely concise (max 3 sentences) as it will be sent as a phone notification.
        response_variable: gemini_result
      - action: script.notify_smart_master
        data:
          title: "🚀 Gemini Tailscale Advice"
          message: "{{ gemini_result.response.speech.plain.speech }}"
          category: "system"
          tag: "tailscale_halo"
          sticky: true
          actions:
            - action: "UPDATE_TAILSCALE_HALO"
              title: "Update Now"
              activationMode: "background"

  # 5. HANDLE NOTIFICATION ACTION
  - alias: "Tailscale Halo: Action Handler"
    id: "tailscale_halo_action_handler"
    trigger:
      - platform: event
        event_type: mobile_app_notification_action
        event_data:
          action: "UPDATE_TAILSCALE_HALO"
    action:
      - action: script.update_tailscale_halo_node
```


## 7. AI-Driven Maintenance: The Gemini Advisor

Rather than blindly updating our infrastructure, we utilize the Google Gemini integration in Home Assistant to perform a "Pre-Flight Check" and diagnose health issues.

> [!NOTE]
> **Requirement:** You must enable the **Google Search Tool** in your Google Gemini integration settings for the agent to look up real-time changelogs.

This automation triggers in two scenarios:
1.  **Version Mismatch**: Gemini searches the web for the latest Tailscale changelogs and checks for breaking changes specific to Proxmox LXC environments.
2.  **Health Warnings**: If `tailscale status` reports an error (e.g., specific sub-service failure), Gemini explains the error and suggests a fix.

This provides a human-readable recommendation directly to your mobile device before you ever touch the terminal.

![Gemini Advisor](../self-healing-tailscale-nodes/tailscale-notification.png)

## Verification & Testing

To verify the system is working:


1.  **Verify Pulse**: Check the "Last Updated" attribute of the `binary_sensor` in HA; it should refresh every 60 seconds.
2.  **Test Failure**: Edit the crontab (`crontab -e`) and comment out the script line to simulate a total failure.
3.  **Confirm Automation**: Within 2 minutes, the HA sensor should flip to "Disconnected." After 5 minutes, you should receive a notification and see the LXC reboot in Proxmox.