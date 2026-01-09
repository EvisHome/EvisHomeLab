---
tags:
  - package
  - automated
version: Unknown
---

# Package: Tailscale Monitoring

**Version:** Unknown  
**Description:** No description provided.

<!-- START_IMAGE -->
![Package Diagram](../../assets/images/packages/tailscale_monitoring.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
*No linked dashboard views found (Automatic Scan).*
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ---------------------------------------------------------
# 1. The Listener (Dead Man's Switch)
#    - Listens for the webhook from the LXC container.
#    - Turns "On" when ping is received.
#    - Automatically turns "Off" if no ping for 130 seconds.
# ---------------------------------------------------------

template:
  - trigger:
      - platform: webhook
        webhook_id: tailscale_edge_keepalive
        local_only: true
    binary_sensor:
      - name: "Tailscale Edge Status"
        unique_id: tailscale_edge_status_heartbeat
        state: "on"
        device_class: connectivity
        auto_off: "00:03:10" # 3 mins 10s buffer (allows for 1 missed ping)

# ---------------------------------------------------------
# 2. The Enforcer (Reboot Automation)
#    - Watches the sensor above.
#    - If it goes 'off', it pushes the Proxmox Reboot button.
# ---------------------------------------------------------
automation:
  - alias: "Fix Tailscale Edge Node"
    id: fix_tailscale_edge_node # ID is required for debugging traces
    mode: single
    trigger:
      - platform: state
        entity_id: binary_sensor.tailscale_edge_status
        to: "off"
        for:
          minutes: 2 # Wait 2 extra minutes to be absolutely sure
    action:
      - service: notify.persistent_notification
        data:
          message: "Tailscale Edge heartbeat lost. Rebooting container..."
          title: "Tailscale Watchdog"

      # PRESS THE PROXMOX BUTTON
      # (Replace this entity ID with your actual Proxmox integration button)
      - service: button.press
        target:
          entity_id: button.tailscale_edge_reboot
# ---------------------------------------------------------
# 3. The Heartbeat Script (Tailscale Edge Node)
#    - Runs on the LXC container.
#    - Sends a webhook to Home Assistant when Tailscale is running.
#    - Logs errors to a file if Tailscale is not running.
# ---------------------------------------------------------
# Run in the Tailscale Edge Node

# ``` bash
# apt update && apt install -y curl
# ```

# ``` bash
# nano /usr/local/bin/ts-heartbeat.sh
# ```

# #File: /usr/local/bin/ts-heartbeat.sh
# #!/bin/bash
#
## CHANGE URL TO TAILSCALE EDGE ID
#HA_URL="http://192.168.1.X:8123/api/webhook/tailscale_edge_keepalive"
#
#if /usr/bin/tailscale status --json | grep -q 'BackendState.*Running'; then
#    /usr/bin/curl -X POST -d "" "$HA_URL"
#else
#    echo "$(date): Heartbeat failed." >> /var/log/ts-heartbeat.log
#fi

# chmod +x /usr/local/bin/ts-heartbeat.sh
# crontab -e -> * * * * * /usr/local/bin/ts-heartbeat.sh

# ---------------------------------------------------------
# 4. Log Rotation (Optional but Recommended)
#    - If using the log file method above, prevent it from filling the disk.
# ---------------------------------------------------------
# ``` bash
# nano /etc/logrotate.d/ts-heartbeat
# ```
#
# /var/log/ts-heartbeat.log {
#     size 1M
#     rotate 1
#     compress
#     missingok
#     notifempty
# }

# ---------------------------------------------------------
# 5. System Maintenance (Debian/LXC Best Practices)
#    - Prevent system logs (journald) directly filling the disk.
#    - Standard Debian logrotate handles /var/log/syslog, etc.
# ---------------------------------------------------------
#
# # 5.1 Limit Journald Size (Critical for small containers)
# ``` bash
# nano /etc/systemd/journald.conf
# ```
# # Uncomment and set:
# # SystemMaxUse=50M
#
# # Then restart:
# # systemctl restart systemd-journald
#
# # 5.2 Verify Logrotate is active
# # systemctl status logrotate
# # (It should be loaded and active as a timer)


```
