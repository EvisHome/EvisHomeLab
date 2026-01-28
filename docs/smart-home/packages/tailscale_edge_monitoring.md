---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Tailscale Edge Monitoring

**Version:** 1.0.0  
**Description:** Configuration and helpers for managing Smart Speakers in Notification Center

<!-- START_IMAGE -->
![Package Diagram](assets/tailscale_edge_monitoring.png)
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
# Package: Tailscale Edge Monitoring
# Version: 1.0.0
# Description: Configuration and helpers for managing Smart Speakers in Notification Center
# /config/packages/halo_edge_tailscale.yaml
# ------------------------------------------------------------------------------

## ==============================================================================
# TAILSCALE EDGE MONITORING & SELF-HEALING
# ==============================================================================

# 1. MAINTENANCE TOGGLE
# Use this in your dashboard to stop reboots during manual work
input_boolean:
  edge_maintenance_mode:
    name: "Edge Maintenance Mode"
    icon: mdi:wrench

# 2. HEARTBEAT SENSOR
# Receives the pulse from the LXC and turns off after 2 minutes of silence
template:
  - trigger:
      - platform: webhook
        webhook_id: "tailscale_edge_heartbeat"
        local_only: true
    binary_sensor:
      - name: "Tailscale Edge Heartbeat"
        unique_id: "ts_edge_heartbeat_binary"
        device_class: connectivity
        state: "on"
        auto_off: "00:02:00"

# 3. SELF-HEALING AUTOMATION
# Reboots the LXC via Proxmox if heartbeat is lost for 5 minutes
automation:
  - alias: "Tailscale Edge Auto-Recover"
    id: "tailscale_edge_auto_recover"
    trigger:
      - platform: state
        entity_id: binary_sensor.tailscale_edge_heartbeat
        to: "off"
        for: "00:05:00"
    condition:
      - condition: and
        conditions:
          # Condition 1: Maintenance mode must be OFF
          - condition: state
            entity_id: input_boolean.edge_maintenance_mode
            state: "off"

          # Condition 2: HA's own Tailscale must be ON (The "Brain Check")
          # Replace with your actual entity ID from the Tailscale Integration
          - condition: state
            entity_id: binary_sensor.lxc_tailscale_edge_100_status
            state: "on"
    action:
      - service: button.press
        target:
          entity_id: button.lxc_tailscale_edge_100_reboot
      - service: notify.mobile_app_sm_f966b_Evis
        data:
          title: "⚠️ Tailscale EDGE Down"
          message: "Connectivity lost for 5m. Proxmox reboot command sent."

```
