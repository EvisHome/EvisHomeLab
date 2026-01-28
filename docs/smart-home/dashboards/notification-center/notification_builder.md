---
tags:
  - dashboard
  - view
  - automated
---

# Notification Builder

**Dashboard:** Notification Center  
**Path:** `notification-builder`

<!-- START_DESCRIPTION -->
Advanced tools for creating notifications and monitoring the active registry.
<!-- END_DESCRIPTION -->

## Summary
<!-- START_SUMMARY -->
This view is designed for the "Architect" or "Developer" persona. It provides a full registry of all configured system notifications (scanned from YAML) and an AI-Powered builder interface to generate new notification code.
<!-- END_SUMMARY -->

## Configuration
```yaml
title: Notification Builder
icon: mdi:robot-confused
type: sections
max_columns: 2
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: AI Notification Builder
    alignment: center
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Describe & Build
    icon: mdi:robot
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--purple-color);\n\
        \  --secondary-text-color: var(--purple-color);\n  --card-mod-icon-color:\
        \ var(--purple-color);\n}\n"
  - type: markdown
    content: "**AI Builder Instructions:**\n\n1. Describe your **Trigger** (e.g., 'When the washing machine power drops below 2W for 5 mins').\n2. Enter Title & Message.\n3. Click **Generate Prompt**.\n4. Copy the result from the notification to your AI Assistant to get the code."
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_text.ai_notify_trigger_desc
      name: Trigger Description
      icon: mdi:flash-auto
    - entity: input_text.ai_notify_title
      name: Notification Title
      icon: mdi:format-title
    - entity: input_text.ai_notify_message
      name: Notification Message
      icon: mdi:text
    - type: call-service
      icon: mdi:creation
      name: Generate Prompt
      action_name: BUILD
      service: pyscript.generate_ai_notification_prompt
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--purple-color);\n\
        }\n"

- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Active Notifications Registry
    alignment: center
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Active Notifications Registry
    icon: mdi:clipboard-list
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--orange-color);\n\
        \  --secondary-text-color: var(--orange-color);\n  --card-mod-icon-color:\
        \ var(--orange-color);\n}\n"
  - type: custom:flex-table-card
    title: System Notifications
    icon: mdi:clipboard-list
    entities:
      include: sensor.notification_registry
    columns:
      - name: Cat
        data: notifications
        modify: x.category
        align: left
      - name: Title
        data: notifications
        modify: x.title
        align: left
      - name: Crit
        data: notifications
        modify: "x.critical ? '🔴' : ''"
        align: center
      - name: Stick
        data: notifications
        modify: "x.sticky ? '📌' : ''"
        align: center
      - name: File
        data: notifications
        modify: x.source
        align: right
    card_mod:
      style: |
        ha-card {
          border: none;
          --primary-text-color: var(--orange-color);
        }
  - type: button
    icon: mdi:refresh
    name: Scan System
    tap_action:
      action: call-service
      service: pyscript.system_scan_notifications
    card_mod:
      style: |
        ha-card {
          border: none;
          background: none;
          --primary-text-color: var(--primary-color);
        }
```
