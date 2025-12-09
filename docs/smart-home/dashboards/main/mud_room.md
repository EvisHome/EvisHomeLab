---
tags:
  - dashboard
  - view
  - automated
---

# Mud Room

**Dashboard:** Main Dashboard  
**Path:** `mud_room`

## Related Packages
This view contains entities managed by:

* [Fingerprint Management](../../packages/fingerprint_management.md)


![View Screenshot](../../../assets/images/dashboards/dashboard_main_mud_room.png)

## Configuration
```yaml
theme: Backend-selected
title: Mud Room
path: mud_room
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
      area_name: mud_room
      area_title: Mud Room
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.mud_room_motion_sensor_device_temperature
      indicator_1_entity: binary_sensor.front_door_lock_door
      indicator_1_icon: mdi:door
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 0.5s ease infinite
      indicator_2_entity: lock.front_door_lock
      indicator_2_icon: mdi:lock
      indicator_2_state: unlocked
      indicator_2_active_color: '#FF4444'
      indicator_2_animation_on: blink 0.5s ease infinite
      indicator_6_entity: binary_sensor.mud_room_door_sensor_contact
      indicator_6_icon: mdi:door
      indicator_6_state: 'on'
      indicator_6_active_color: orange
      indicator_6_animation_on: blink 1s ease infinite
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHT
      alignment: center
    - type: vertical-stack
      cards:
      - square: false
        type: grid
        cards:
        - type: custom:mushroom-light-card
          entity: light.mud_room_ceiling_light
          layout: vertical
          fill_container: true
          use_light_color: true
        columns: 1
  - type: custom:mushroom-entity-card
    entity: binary_sensor.mud_room_motion_sensor_occupancy
    layout: vertical
    name: Mudroom Occupancy
    icon: mdi:account
    grid_options:
      columns: 12
      rows: 2
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: mud_room
    - area_name: Mud Room
  - type: custom:mushroom-title-card
    title: ''
    subtitle: SCHEDULES
    alignment: center
  - type: markdown
    content: These schedules work when they are set on and _Presence Automation Mode_
      is set to _Schedule Mode_
  - type: custom:scheduler-card
    include:
    - input_select.mud_room_automation_mode
    - light.mud_room_ceiling_light
    - light.mud_room_lights
    exclude: []
    discover_existing: false
    tags:
    - mud-room
    title: false
    display_options:
      primary_info: default
      secondary_info:
      - relative-time
      - time
      - additional-tasks
      icon: action
    sort_by:
    - state
    - relative-time
    time_step: 5
    show_header_toggle: false
max_columns: 4

```
