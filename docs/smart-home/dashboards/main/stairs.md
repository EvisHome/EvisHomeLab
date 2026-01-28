---
tags:
  - dashboard
  - view
  - automated
---

# Stairs

**Dashboard:** Main Dashboard  
**Path:** `stairs`

<!-- START_DESCRIPTION -->
Staircase lighting controls including WLED effects.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_stairs.png)

## Summary
<!-- START_SUMMARY -->
This view manages the Stairs area. It features specific control for the WLED strip lighting on the stairs, allowing users to toggle power, adjust brightness, and select WLED presets/effects. Standard occupancy settings and scheduling options are also available.
<!-- END_SUMMARY -->



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mushroom-light-card`
* `custom:mushroom-select-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`


## Configuration
```yaml
title: Stairs
path: stairs
type: sections
max_columns: 5
subview: true
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: stairs
      area_title: Stairs
      temperature_sensor: sensor.airthings_wave_temperature
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.stairs_wled
    layout: vertical
    icon: mdi:led-strip-variant
    fill_container: true
    show_brightness_control: true
    show_color_control: false
    use_light_color: true
    grid_options:
      columns: 6
      rows: 3
  - type: custom:mushroom-select-card
    entity: select.stairs_wled_preset
    name: Stairs Preset
    fill_container: true
    layout: vertical
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: OCCUPANCY SETTINGS
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: stairs
    - area_name: Stairs
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
  - type: custom:scheduler-card
    include:
    - input_select.stairs_automation_mode
    - light.stairs_lights
    - light.stairs_wled
    exclude: []
    discover_existing: false
    tags:
    - stairs
    time_step: 1
    show_header_toggle: false
    title: false
cards: []

```
