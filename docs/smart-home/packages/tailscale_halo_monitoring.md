---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Tailscale Halo Monitoring

**Version:** 1.0.0  
**Description:** Configuration and helpers for managing Smart Speakers in Notification Center

<!-- START_IMAGE -->
![Package Diagram](assets/tailscale_halo_monitoring.png)
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
# Package: Tailscale Monitoring
# Version: 1.0.0
# Description: Configuration and helpers for managing Smart Speakers in Notification Center
# /config/packages/tailscale_halo_monitoring.yaml
# ------------------------------------------------------------------------------

## ==============================================================================
# TAILSCALE HALO MONITORING & SELF-HEALING
# ==============================================================================

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
    'pct exec 101 -- bash -c "DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y tailscale"'

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
        unique_id: "tailscale_halo_heartbeat"
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

          # Condition 2: HA's own Tailscale must be ON (The "Brain Check")
          # Replace with your actual entity ID from the Tailscale Integration
          - condition: state
            entity_id: binary_sensor.lxc_tailscale_halo_101_status
            state: "on"
    action:
      - service: button.press
        target:
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
          agent_id: conversation.gemini_web_advisor # Common ID for Google Gemini. Check yours in Settings!
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
