---
tags:
  - dashboard
  - view
  - automated
---

# Toilet

**Dashboard:** Main Dashboard  
**Path:** `toilet`

<!-- START_DESCRIPTION -->
Toilet room controls and detailed motion sensor calibration.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_toilet.png)

## Summary
<!-- START_SUMMARY -->
This dashboard manages the Toilet room. It offers basic light control and occupancy settings. A key feature is the detailed sensor settings section, allowing fine-tuning of the mmWave and PIR motion sensors, including distance and latency adjustments to optimize presence detection.
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
title: Toilet
path: toilet
type: sections
subview: true
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: toilet
      area_title: Toilet
      temperature_sensor: sensor.airthings_wave_temperature
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - type: custom:mushroom-light-card
      entity: light.toilet_wall_box_switch
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: toilet
    - area_name: Toilet
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SENSOR SETTINGS
      alignment: center
  - type: entities
    entities:
    - entity: binary_sensor.toilet_mmwave
    - entity: binary_sensor.toilet_pir
    - entity: number.toilet_distance
    - entity: number.toilet_latency
max_columns: 4

```
