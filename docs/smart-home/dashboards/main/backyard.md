---
tags:
  - dashboard
  - view
  - automated
---

# Backyard

**Dashboard:** Main Dashboard  
**Path:** `backyard`

![View Screenshot](../../../assets/images/dashboards/view_main_backyard.png)

## Configuration
```yaml
title: Backyard
type: sections
layout:
  max_cols: 5
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: BACKYARD
    alignment: center
    title_tap_action:
      action: navigate
      navigation_path: /lovelace
    subtitle: CONTROLS
  - type: custom:frigate-card
    cameras:
    - camera_entity: camera.backyard_frigate
    menu:
      style: outside
      position: bottom
      buttons:
        cameras:
          enabled: false
        frigate:
          enabled: false
        live:
          enabled: true
        recordings:
          enabled: false
          priority: 50
        expand:
          enabled: false
        play:
          enabled: true
        screenshot:
          enabled: true
        snapshots:
          enabled: false
        clips:
          priority: 30
          enabled: true
        timeline:
          priority: 40
          enabled: false
        mute:
          enabled: false
        microphone:
          enabled: false
        download:
          priority: 35
      alignment: left
      button_size: 48
    view:
      default: live
      timeout_seconds: 1200
    live:
      preload: true
      lazy_load: true
      zoomable: true
      draggable: false
      show_image_during_load: false
    media_gallery:
      controls:
        thumbnails: {}
  - type: custom:mushroom-light-card
    entity: light.backyard_plug
    icon: mdi:string-lights
    layout: vertical
    name: Backyard Light
    tap_action:
      action: toggle
    hold_action:
      action: more-info
    double_tap_action:
      action: none
    grid_options:
      columns: 3
      rows: 2
  - type: custom:mushroom-entity-card
    entity: binary_sensor.inner_back_door_contact
    fill_container: true
    layout: vertical
    tap_action:
      action: none
    hold_action:
      action: none
    double_tap_action:
      action: none
    icon: mdi:door
    name: Inner Door
    grid_options:
      columns: 3
      rows: 2
  - type: custom:mushroom-entity-card
    entity: binary_sensor.backyard_door_sensor_contact
    fill_container: true
    layout: vertical
    tap_action:
      action: none
    hold_action:
      action: none
    double_tap_action:
      action: none
    icon: mdi:door
    name: Backyard Door
    grid_options:
      columns: 3
      rows: 2
  - type: custom:mushroom-entity-card
    entity: binary_sensor.backyard_frigate_person_occupancy
    layout: vertical
    icon: mdi:account
    grid_options:
      columns: 3
      rows: 2
    name: Person(s)
  - type: custom:mushroom-title-card
    title: ''
    subtitle: ENVIRONMENT
    alignment: center
  - type: custom:mini-graph-card
    hours_to_show: 24
    name: Temperature
    entities:
    - sensor.backyard_temperature
    color_thresholds:
    - value: 0
      color: skyblue
    - value: 3
      color: white
    - value: 10
      color: yellow
    - value: 20
      color: orange
    - value: 25
      color: red
    layout_options:
      grid_columns: 2
  - type: custom:mini-graph-card
    name: Humidity
    entities:
    - sensor.backyard_humidity
    hours_to_show: 24
    color_thresholds:
    - value: 20
      color: '#FF535B'
    - value: 30
      color: '#5FE787'
    - value: 60
      color: '#03A9F4'
    layout_options:
      grid_columns: 2
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:mushroom-entity-card
    entity: input_select.backyard_presence
    layout: vertical
  - type: custom:mushroom-entity-card
    entity: input_boolean.backyard_occupancy
    layout: vertical
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
  - type: custom:scheduler-card
    include:
    - input_select.backyard_automation_mode
    - light.backyard_plug
    exclude: []
    discover_existing: false
    tags:
    - Backyard
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
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    subtitle: CAMERA SETTINGS
    alignment: center
  - type: entities
    entities:
    - entity: binary_sensor.backyard_cam_motion
    - entity: select.backyard_cam_infrared_mode
    - entity: binary_sensor.backyard_cam_is_dark
    - entity: switch.backyard_cam_privacy_mode
    - entity: switch.backyard_cam_detections_motion
    - entity: number.backyard_cam_microphone_level
    - entity: select.backyard_cam_hdr_mode
    - entity: switch.backyard_cam_hdr_mode
    - entity: switch.backyard_cam_overlay_show_date
    - entity: switch.backyard_cam_overlay_show_name
    - entity: switch.backyard_cam_overlay_show_nerd_mode
  - type: custom:mushroom-title-card
    title: ''
    subtitle: FRIGATE SETTINGS
    alignment: center
  - type: picture
    image_entity: image.backyard_frigate_person
    grid_options:
      columns: 3
      rows: auto
  - type: entities
    entities:
    - entity: sensor.backyard_frigate_all_count
    - entity: switch.backyard_frigate_detect
    - entity: switch.backyard_frigate_motion
    - entity: binary_sensor.backyard_frigate_motion
    - entity: sensor.backyard_frigate_person_count
    - entity: binary_sensor.backyard_frigate_person_occupancy
    - entity: switch.backyard_frigate_recordings
    - entity: switch.backyard_frigate_snapshots
  visibility:
  - condition: user
    users:
    - 5f4dd0e939344fd6b58ed4299cdafcd6
max_columns: 4
subview: false
path: backyard

```
