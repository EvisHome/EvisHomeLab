---
tags:
  - dashboard
  - view
  - automated
---

# Storage

**Dashboard:** Main Dashboard  
**Path:** `storage`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_storage.png)



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:frigate-card`
* `custom:mushroom-light-card`
* `custom:mushroom-title-card`


## Configuration
```yaml+jinja
title: Storage
type: sections
layout:
  max_cols: 5
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: STORAGE
    alignment: center
    title_tap_action:
      action: navigate
      navigation_path: /lovelace
    subtitle: CONTROLS
  - type: custom:frigate-card
    cameras:
    - camera_entity: camera.storage_cam_high
    live:
      preload: true
    view:
      default: live
      timeout_seconds: 1200
    menu:
      style: outside
      position: bottom
      buttons:
        frigate:
          enabled: false
        substreams:
          enabled: false
        cameras:
          enabled: false
        snapshots:
          enabled: false
        recordings:
          enabled: false
          priority: 10
        clips:
          priority: 10
        timeline:
          enabled: false
        screenshot:
          enabled: true
      button_size: 48
    performance: {}
  - square: false
    type: grid
    cards:
    - type: custom:mushroom-light-card
      entity: light.storage_light
      icon: ''
      layout: vertical
      name: Storage Light
      tap_action:
        action: toggle
      hold_action:
        action: more-info
      double_tap_action:
        action: none
    columns: 1
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    subtitle: EVENTS
    alignment: center
  - type: custom:frigate-card
    cameras:
    - camera_entity: camera.storage_frigate
    live:
      preload: true
    view:
      default: clips
      timeout_seconds: 1200
    menu:
      style: outside
      position: bottom
      buttons:
        frigate:
          enabled: false
        substreams:
          enabled: false
        cameras:
          enabled: false
        snapshots:
          enabled: false
        recordings:
          enabled: false
          priority: 10
        clips:
          priority: 10
        timeline:
          enabled: false
        screenshot:
          enabled: true
      button_size: 48
    performance: {}
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    subtitle: CAMERA SETTINGS
    alignment: center
  - type: entities
    entities:
    - entity: binary_sensor.storage_cam_motion
    - entity: select.storage_cam_infrared_mode
    - entity: binary_sensor.storage_cam_is_dark
    - entity: switch.storage_cam_privacy_mode
    - entity: switch.storage_cam_detections_motion
    - entity: number.storage_cam_microphone_level
    - entity: select.storage_cam_hdr_mode
    - entity: switch.storage_cam_hdr_mode
    - entity: switch.storage_cam_overlay_show_date
    - entity: switch.storage_cam_overlay_show_name
    - entity: switch.storage_cam_overlay_show_nerd_mode
  - type: custom:mushroom-title-card
    title: ''
    subtitle: FRIGATE SETTINGS
    alignment: center
  - type: entities
    entities:
    - entity: sensor.storage_frigate_all_count
    - entity: switch.storage_frigate_detect
    - entity: switch.storage_frigate_motion
    - entity: binary_sensor.storage_frigate_motion
    - entity: sensor.storage_frigate_person_count
    - entity: binary_sensor.storage_frigate_person_occupancy
    - entity: switch.storage_frigate_recordings
    - entity: switch.storage_frigate_snapshots
  visibility:
  - condition: user
    users:
    - 5f4dd0e939344fd6b58ed4299cdafcd6
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: storage
    - area_name: Storage
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
max_columns: 5
path: storage

```
