---
tags:
  - dashboard
  - view
  - automated
---

# Guest-3

**Dashboard:** Main Dashboard  
**Path:** `Guest-3`

<!-- START_DESCRIPTION -->
Controls for Guest-3 room (A Room) with environmental monitoring.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_guest_3.png)

## Summary
<!-- START_SUMMARY -->
This view manages the Guest-3 room (labeled 'A Room'). It provides comprehensive environmental monitoring (Temperature, Humidity, CO2). Presence is tracked at the bed and desk. The view also includes controls for ceiling and window lights, plus occupancy automation configuration.
<!-- END_SUMMARY -->



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mushroom-light-card`
* `custom:mushroom-title-card`
* `custom:streamline-card`


## Configuration
```yaml
theme: Backend-selected
title: Guest-3
path: Guest-3
type: sections
layout:
  max_cols: 4
subview: true
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Guest-3
      area_title: A Room
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.Guest-3_temperature
      indicator_3_entity: binary_sensor.Guest-3_bed_fp2_presence_sensor
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Guest-3_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
  - type: vertical-stack
    cards:
    - square: false
      type: grid
      cards:
      - type: custom:decluttering-card
        template: minigraph_co2
        variables:
        - sensor: sensor.Guest-3_carbon_dioxide
      - type: custom:decluttering-card
        template: minigraph_temperature
        variables:
        - sensor: sensor.Guest-3_temperature
      - type: custom:decluttering-card
        template: minigraph_humidity
        variables:
        - sensor: sensor.Guest-3_humidity
      columns: 3
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - square: false
      columns: 2
      type: grid
      cards:
      - type: custom:mushroom-light-card
        entity: light.Guest-3_ceiling_light
        show_brightness_control: true
        show_color_temp_control: false
      - type: custom:mushroom-light-card
        entity: light.Guest-3_window_light
        fill_container: true
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: Occupancy Settings
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: Guest-3
    - area_name: Guest-3
max_columns: 4

```
