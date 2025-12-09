---
tags:
  - dashboard
  - view
  - automated
---

# Hallway

**Dashboard:** Main Dashboard  
**Path:** `hallway`

![View Screenshot](../../../assets/images/dashboards/view_main_hallway.png)

## Configuration
```yaml
theme: Backend-selected
title: Hallway
path: hallway
type: sections
layout:
  max_cols: 5
subview: true
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: hallway
      area_title: Hallway
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.airthings_wave_temperature
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - type: vertical-stack
      cards:
      - square: false
        type: grid
        cards:
        - type: custom:mushroom-light-card
          entity: light.hallway_ceiling_light
          show_brightness_control: true
          name: Ceiling
          collapsible_controls: false
          layout: vertical
          show_color_temp_control: true
        - type: custom:mushroom-light-card
          entity: light.stairs_lights
          show_brightness_control: true
          show_color_control: true
          show_color_temp_control: true
          layout: vertical
        columns: 2
- type: grid
  cards:
  - type: entities
    entities:
    - entity: binary_sensor.hallway_fp2_presence_sensor
    - entity: binary_sensor.downstairs_hallway_fp2_presence_sensor
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: hallway
    - area_name: Hallway
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

```
