---
tags:
  - package
  - automated
version: Unknown
---

# Package: Ai Summary

**Version:** Unknown  
**Description:** No description provided.

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/ai_summary.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
This package acts as the **Frontend** and **Controller** for the external **[AI Log Reporter Integration](../integrations/ai_reporter.md)**.
1.  It provides the **Template Sensor** to display the summary.
2.  It handles the **Scheduling** (7:00 AM) and **SSH Connection** logic to trigger the remote analysis.
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
The diagram below illustrates the hand-off between this Home Assistant package and the external Docker container. For full implementation details of the remote system, see the **[AI Reporter Integration](../integrations/ai_reporter.md)** documentation.
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
```mermaid
sequenceDiagram
    participant Sched as ⏰ Schedule
    participant Script as 📜 Script
    participant SSH as 🔐 SSH Tunnel
    participant Remote as 📦 Remote Integration

    Sched->>Script: Trigger 7:00 AM
    Script->>SSH: Connect root@10.0.0.23
    SSH->>Remote: Trigger Docker Analysis
    Note over Remote: Processing...
    Remote-->>Script: (Async Event Return)
```
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# /config/packages/ai_summary.yaml (Updated)

template:
  - trigger:
      # This trigger listens for a custom event we will send from the script
      - platform: event
        event_type: "update_ai_summary"
    sensor:
      - name: "Daily System Summary"
        unique_id: ai_daily_summary_permanent
        # The state is just the timestamp of the last update
        state: "{{ now().strftime('%Y-%m-%d %H:%M') }}"
        icon: mdi:robot
        attributes:
          # This pulls the 'summary' text from the event data sent by your script
          summary: "{{ trigger.event.data.summary }}"

shell_command:
  generate_ai_log_summary: >
    ssh -i /config/.ssh/id_rsa_new 
    -o StrictHostKeyChecking=no 
    -o UserKnownHostsFile=/dev/null 
    root@10.0.0.23 
    'docker exec ai-log-reporter python /app/reporter.py'

script:
  run_ai_summary_now:
    alias: "Run AI Log Summary Now"
    icon: mdi:robot
    sequence:
      - action: shell_command.generate_ai_log_summary # Service changed to Action in 2024.12+
      - action: notify.persistent_notification # Optional: popup in HA UI
        data:
          title: "AI Reporter"
          message: "Gemini is analyzing logs and updating your dashboard."

automation:
  - alias: "Daily AI System Summary"
    id: daily_ai_summary_automation
    trigger:
      - platform: time
        at: "07:00:00"
      - platform: homeassistant
        event: start # Triggers script whenever HA reboots
    action:
      - delay: "00:01:00" # Wait 1 min for network to be ready
      - action: script.run_ai_summary_now

  - alias: "Restore AI Notification on Startup"
    id: restore_ai_notification_on_startup
    trigger:
      - platform: homeassistant
        event: start
    action:
      - delay: "00:00:15" # Give the sensor a moment to restore its own state first
      - condition: template
        # Only restore if the sensor actually has a report saved
        value_template: "{{ state_attr('sensor.daily_system_summary', 'summary') not in [None, 'unknown', ''] }}"
      - action: persistent_notification.create
        data:
          title: "🤖 Daily Lab Report (Restored)"
          message: "{{ state_attr('sensor.daily_system_summary', 'summary') }}"
          notification_id: "daily_ai_summary"

```
