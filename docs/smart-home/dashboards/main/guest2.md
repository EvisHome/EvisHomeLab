---
tags:
  - dashboard
  - view
  - automated
---

# Guest 2

**Dashboard:** Main Dashboard  
**Path:** `Guest 2`



![View Screenshot](../../../assets/images/dashboards/dashboard_main_guest2.png)

## Configuration
```yaml
theme: Backend-selected
title: Guest 2
path: Guest 2
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
      area_name: Guest 2
      area_title: E Room
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_3_entity: binary_sensor.Guest 2_bed_fp2_presence_sensor
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Guest 2_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - type: custom:mushroom-light-card
      entity: light.Guest 2_ceiling_light
      use_light_color: false
      show_brightness_control: true
      show_color_temp_control: true
      collapsible_controls: false
      layout: horizontal
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: POWER
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:mini-graph-card
        entities:
        - entity: sensor.Guest 2_window_outlet_power
          name: Energy
      columns: 2
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: Occupancy Settings
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: Guest 2
    - area_name: Guest 2
max_columns: 4

```
