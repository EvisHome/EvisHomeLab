---
tags:
  - dashboard
  - view
  - automated
---

# Sauna

**Dashboard:** Main Dashboard  
**Path:** `sauna`

![View Screenshot](../../../assets/images/dashboards/view_main_sauna.png)

## Configuration
```yaml
theme: Backend-selected
title: Sauna
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
      area_name: sauna
      area_title: Sauna
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.ruuvitag_8572_temperature
      indicator_1_entity: binary_sensor.sauna_door_contact
      indicator_1_icon: mdi:door
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 1s ease infinite
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.bathroom_wall_box_switch_left
    name: Sauna
    layout: vertical
    grid_options:
      columns: full
      rows: 2
  - type: custom:mushroom-title-card
    title: ''
    subtitle: ENVIRONMENT
    alignment: center
  - type: vertical-stack
    cards:
    - square: false
      type: grid
      cards:
      - type: custom:decluttering-card
        template: minigraph_temperature
        variables:
        - sensor: sensor.ruuvitag_8572_temperature
      - type: custom:decluttering-card
        template: minigraph_humidity
        variables:
        - sensor: sensor.ruuvitag_8572_humidity
      columns: 2
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: sauna
    - area_name: Sauna
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
max_columns: 4
path: sauna

```
