---
tags:
  - dashboard
  - view
  - automated
---

# Front Door

**Dashboard:** Main Dashboard  
**Path:** `front-door`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_front-door.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Fingerprint Management](../../packages/fingerprint_management.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:decluttering-card`
* `custom:frigate-card`
* `custom:mushroom-alarm-control-panel-card`
* `custom:mushroom-entity-card`
* `custom:mushroom-light-card`
* `custom:mushroom-lock-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`


## Configuration
```yaml
title: Front Door
path: front-door
type: sections
layout:
  max_cols: 5
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:frigate-card
      cameras:
      - camera_entity: camera.g4_doorbell_pro_poe_high_resolution_channel
      view:
        default: live
        interaction_seconds: 1200
      live:
        preload: true
        controls:
          builtin: true
        lazy_load: true
        show_image_during_load: false
      performance:
        style:
          box_shadow: true
          border_radius: true
      image:
        zoomable: true
      menu:
        position: bottom
        button_size: 48
        buttons:
          cameras:
            enabled: false
          snapshots:
            enabled: false
          clips:
            enabled: true
            priority: 30
          substreams:
            enabled: false
          timeline:
            enabled: false
          microphone:
            enabled: false
          frigate:
            enabled: false
          download:
            priority: 35
          screenshot:
            enabled: true
        style: outside
        alignment: left
      media_gallery:
        controls:
          thumbnails:
            show_details: false
      timeline:
        show_recordings: true
    - type: custom:frigate-card
      cameras:
      - camera_entity: camera.front_porch_frigate
      view:
        default: live
        timeout_seconds: 1200
      live:
        preload: true
        controls:
          builtin: true
        lazy_load: true
        show_image_during_load: false
      performance:
        style:
          box_shadow: true
          border_radius: true
      image:
        zoomable: true
      menu:
        position: bottom
        button_size: 48
        buttons:
          cameras:
            enabled: false
          snapshots:
            enabled: false
          clips:
            enabled: true
            priority: 30
          substreams:
            enabled: false
          timeline:
            enabled: false
          microphone:
            enabled: false
          frigate:
            enabled: false
          download:
            priority: 35
          screenshot:
            enabled: true
        style: outside
        alignment: left
      media_gallery:
        controls:
          thumbnails:
            show_details: false
      timeline:
        show_recordings: true
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-light-card
        entity: light.front_door_rail_light
        icon: mdi:string-lights
        layout: vertical
        name: Front Door Light
        tap_action:
          action: more-info
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        use_light_color: false
      - type: custom:mushroom-light-card
        entity: light.mud_room_ceiling_light
        icon: ''
        layout: vertical
        name: Mud Room Light
        tap_action:
          action: more-info
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        use_light_color: false
      columns: 2
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-lock-card
        entity: lock.front_door_lock
        layout: vertical
        name: Lock
      - type: custom:mushroom-entity-card
        entity: binary_sensor.front_porch_frigate_person_occupancy
        layout: vertical
        name: Persons
        icon: mdi:account
        fill_container: true
      - type: custom:mushroom-entity-card
        entity: binary_sensor.front_door_lock_door
        icon: mdi:door
        layout: vertical
        name: Lock Contact
        fill_container: true
      - type: custom:mushroom-entity-card
        entity: binary_sensor.front_door_lock_door
        icon: mdi:door
        layout: vertical
        name: Contact
        fill_container: true
      columns: 4
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-entity-card
        entity: input_select.home_front_door_occupancy_state
        name: Front State
        fill_container: true
        layout: vertical
      - type: custom:mushroom-alarm-control-panel-card
        entity: alarm_control_panel.front_door
        states:
        - armed_home
        - armed_away
        - armed_night
        - armed_custom_bypass
        fill_container: true
        layout: vertical
      columns: 2
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: EVENTS
      alignment: center
    - type: custom:frigate-card
      cameras:
      - camera_entity: camera.frontdoor_doorbell
      view:
        default: clips
        update_cycle_camera: false
        dark_mode: 'on'
        timeout_seconds: 1200
        update_seconds: 120
      menu:
        buttons:
          frigate:
            enabled: true
            alignment: matching
            icon: mdi:view-grid
          live:
            enabled: false
          camera_ui:
            enabled: true
          cameras:
            enabled: false
          clips:
            enabled: false
          timeline:
            enabled: false
          snapshots:
            enabled: false
          screenshot:
            enabled: true
        style: outside
        position: bottom
        alignment: left
      timeline:
        media: all
        controls:
          thumbnails:
            size: 100
      media_gallery:
        controls:
          thumbnails:
            size: 125
            show_details: false
      dimensions:
        aspect_ratio: '4:3'
    - type: custom:frigate-card
      cameras:
      - camera_entity: camera.front_porch_frigate
      view:
        default: clips
        update_cycle_camera: false
        dark_mode: 'on'
        timeout_seconds: 1200
        update_seconds: 120
      menu:
        buttons:
          frigate:
            enabled: true
            alignment: matching
            icon: mdi:view-grid
          live:
            enabled: false
          camera_ui:
            enabled: true
          cameras:
            enabled: false
          clips:
            enabled: false
          timeline:
            enabled: false
          snapshots:
            enabled: false
          screenshot:
            enabled: true
        style: outside
        position: bottom
        alignment: left
      timeline:
        media: all
        controls:
          thumbnails:
            size: 100
      media_gallery:
        controls:
          thumbnails:
            size: 125
            show_details: false
      dimensions:
        aspect_ratio: '4:3'
    - type: custom:auto-entities
      card:
        type: entities
      filter:
        include:
        - entity_id: '*front_door_battery*'
        - entity_id: '*keypad_battery*'
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: front_door
    - area_name: Front Door
  - type: custom:mushroom-title-card
    title: ''
    subtitle: SCHEDULES
    alignment: center
  - type: markdown
    content: These schedules work when they are set on and _Presence Automation Mode_
      is set to _Schedule Mode_
  - type: custom:scheduler-card
    include:
    - input_select.front_door_automation_mode
    - light.front_door_light
    - light.front_door_rail_light
    exclude: []
    discover_existing: false
    title: ''
    time_step: 5
    display_options:
      primary_info: default
      secondary_info:
      - relative-time
      - time
      - additional-tasks
      icon: action
    tags:
    - Front Door
max_columns: 4

```
