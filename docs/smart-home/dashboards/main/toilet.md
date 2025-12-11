---
tags:
  - dashboard
  - view
  - automated
---

# Toilet

**Dashboard:** Main Dashboard  
**Path:** `toilet`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_toilet.png)



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mushroom-light-card`
* `custom:mushroom-title-card`
* `custom:streamline-card`


## Configuration
```yaml+jinja
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
    - area: backyard
    - area_name: Backyard
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
