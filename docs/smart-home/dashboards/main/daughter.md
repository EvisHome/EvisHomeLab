---
tags:
  - dashboard
  - view
  - automated
---

# Daughter

**Dashboard:** Main Dashboard  
**Path:** `Daughter`



![View Screenshot](../../../assets/images/dashboards/dashboard_daughter.png)

## Configuration
```yaml
theme: Backend-selected
title: Daughter
path: Daughter
type: sections
layout: max_cols:5
subview: true
badges: []
cards: []
max_columns: 5
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Daughter
      area_title: Guest Room
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_entity: binary_sensor.Daughter_bed_fp2_presence_sensor
      indicator_1_icon: mdi:bed-king
      indicator_1_state: 'on'
      indicator_1_active_color: lightgreen
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.Daughter_ceiling_light
    use_light_color: false
    show_brightness_control: true
    show_color_temp_control: true
    collapsible_controls: false
    layout: vertical
    fill_container: true
    grid_options:
      columns: 12
      rows: 2
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: OCCUPANCY SETTINGS
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: Daughter
    - area_name: Daughter
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
    - input_select.Daughter_automation_mode
    - light.Daughter_ceiling_light
    - light.Daughter_lights
    exclude: []
    discover_existing: false
    tags:
    - Daughter
    time_step: 1
    show_header_toggle: false
    title: false

```
