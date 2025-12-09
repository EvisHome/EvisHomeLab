---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Office. Pc

**Version:** 1.0.0  
**Description:** Office PC control (Audio, Displays, Power)

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/office._pc.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Office PC
# Version: 1.0.0
# Description: Office PC control (Audio, Displays, Power)
# Dependencies: IoT Link (switch.officepc_*, button.officepc_*)
# ------------------------------------------------------------------------------
template:
  - switch:
      - name: "Office PC Audio Device"
        unique_id: officepc_audio_device
        icon: >
          {% if is_state('switch.officepc_audio_device', 'on') %}
            mdi:speaker
          {% else %}
            mdi:headphones
          {% endif %}
        state: "{{ is_state('sensor.officepc_audio_default_device', 'Speakers (Realtek High Definition Audio)') }}"
        turn_on:
          service: button.press
          target:
            entity_id: button.officepc_speakers
        turn_off:
          service: button.press
          target:
            entity_id: button.officepc_headphones

      - name: "Office PC Audio Mute"
        unique_id: officepc_audio_mute
        icon: >
          {% if is_state('sensor.officepc_audio_default_device_muted', 'True') %}
            mdi:volume-mute
          {% else %}
            mdi:volume-high
          {% endif %}
        state: "{{ is_state('sensor.officepc_audio_default_device_muted', 'True') }}"
        turn_on:
          service: button.press
          target:
            entity_id: button.officepc_mute
        turn_off:
          service: button.press
          target:
            entity_id: button.officepc_mute

      - name: "Office PC Displays"
        unique_id: officepc_displays
        icon: >
          {% if is_state('sensor.officepc_monitorpowerstate', 'PowerOn') %}
            mdi:monitor
          {% else %}
            mdi:monitor-off
          {% endif %}
        state: "{{ is_state('sensor.officepc_monitorpowerstate', 'PowerOn') }}"
        turn_on:
          service: button.press
          target:
            entity_id: button.officepc_monitorwake
        turn_off:
          service: button.press
          target:
            entity_id: button.officepc_monitorsleep

switch:
  - platform: wake_on_lan
    name: "Office PC Power"
    mac: 24:4B:FE:B7:52:DD
    host: 10.0.0.140
    turn_off:
      service: button.press
      target:
        entity_id: button.officepc_sleep

```

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Office](../dashboards/main/office.md)** (Uses 3 entities)
<!-- END_DASHBOARD -->
