---
tags:
  - dashboard
  - view
  - automated
---

# Grandpa

**Dashboard:** Main Dashboard  
**Path:** `Grandpa`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_grandpa.png)



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mini-graph-card`
* `custom:mushroom-light-card`
* `custom:mushroom-title-card`
* `custom:streamline-card`


## Configuration
```yaml
theme: Backend-selected
title: Grandpa
path: Grandpa
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
      area_name: Grandpa
      area_title: E Room
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_3_entity: binary_sensor.Grandpa_bed_fp2_presence_sensor
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Grandpa_desk_fp2_presence_sensor
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
      entity: light.Grandpa_ceiling_light
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
        - entity: sensor.Grandpa_window_outlet_power
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
    - area: Grandpa
    - area_name: Grandpa
max_columns: 4

```
