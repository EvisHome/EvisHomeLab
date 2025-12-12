---
tags:
  - dashboard
  - view
  - automated
---

# Lobby

**Dashboard:** Main Dashboard  
**Path:** `lobby`

<!-- START_DESCRIPTION -->
Entry lobby controls for lights and automation modes.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_lobby.png)

## Summary
<!-- START_SUMMARY -->
This view manages the Lobby area. It offers basic control over the ceiling light. The primary focus is on automation scheduling, allowing users to define when the lobby lights operate and to schedule changes to the room's overall 'Automation Mode' based on time or sun position.
<!-- END_SUMMARY -->



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mushroom-light-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`


## Configuration
```yaml
theme: Backend-selected
title: Lobby
path: lobby
type: sections
subview: true
layout:
  max_cols: 5
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: lobby
      area_title: Lobby
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - square: false
    type: grid
    cards:
    - type: custom:mushroom-light-card
      entity: light.lobby_ceiling_light
      fill_container: true
      layout: vertical
      show_brightness_control: true
      use_light_color: true
    columns: 1
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: OCCUPANCY SETTINGS
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: lobby
    - area_name: Lobby
  - type: custom:mushroom-title-card
    title: ''
    subtitle: SCHEDULES
    alignment: center
  - type: markdown
    content: These schedules work when they are set on and _Presence Automation Mode_
      is set to _Schedule Mode_
  - type: custom:scheduler-card
    include:
    - input_select.office_automation_mode
    - light.lobby_light
    - light.lobby_lights
    - sensor.presence_sensor_fp2_65ab_light_sensor_light_level
    exclude: []
    discover_existing: false
    tags:
    - Lobby
    time_step: 1
    show_header_toggle: false
    title: false
  - type: custom:mushroom-title-card
    title: ''
    subtitle: AUTOMATION MODE SCHEDULES
    alignment: center
  - type: markdown
    content: Automation Mode Changes, based on time or sun.
  - type: custom:scheduler-card
    include:
    - input_select.lobby_automation_mode
    exclude: []
    discover_existing: false
    tags:
    - lobby-mode-control
    - office-mode-control
    time_step: 1
    show_header_toggle: false
    title: false
max_columns: 4

```
