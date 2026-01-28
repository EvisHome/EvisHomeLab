---
tags:
  - dashboard
  - view
  - automated
---

# Bedroom

**Dashboard:** Main Dashboard  
**Path:** `bedroom`

<!-- START_DESCRIPTION -->
Bedroom management including lighting, window blinds, and detailed sleep tracking sensors.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_bedroom.png)

## Summary
<!-- START_SUMMARY -->
The Bedroom dashboard focuses on comfort and sleep tracking. It provides controls for the ceiling and bed lights, as well as both window blinds and roller covers. Environmental health is monitored via CO2, temperature, and humidity graphs. A specialized section covers 'Bed Occupancy', aggregating data from pressure sensors and mmWave (FP2) sensors to accurately detect presence in bed for both sides, enabling advanced sleep automations.
<!-- END_SUMMARY -->



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:decluttering-card`
* `custom:mushroom-cover-card`
* `custom:mushroom-light-card`
* `custom:mushroom-template-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`


## Configuration
```yaml
theme: Backend-selected
title: Bedroom
path: bedroom
subview: true
type: sections
layout:
  max_cols: 5
badges: []
cards: []
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: bedroom
      area_title: Bedroom
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
      indicator_1_entity: cover.bedroom_window_blinds
      indicator_1_icon: mdi:window-shutter
      indicator_1_state: open
      indicator_1_active_color: lightgreen
      indicator_2_entity: cover.bedroom_window_roller_cover
      indicator_2_icon: mdi:blinds-open
      indicator_2_state: open
      indicator_2_active_color: lightgreen
      indicator_3_entity: input_boolean.bed_Evis_occupancy
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_4_entity: input_boolean.bed_Guest-1_occupancy
      indicator_4_icon: mdi:bed
      indicator_4_state: 'on'
      indicator_4_active_color: '#FF44C4'
      indicator_3_active_color: '#088CF8'
  - type: custom:mushroom-title-card
    title: ''
    subtitle: ENVIRONMENT
    alignment: center
  - type: vertical-stack
    cards:
    - square: false
      type: grid
      cards:
      - type: custom:decluttering-card
        template: minigraph_co2
        variables:
        - sensor: sensor.bedroom_carbon_dioxide
      - type: custom:decluttering-card
        template: minigraph_temperature
        variables:
        - sensor: sensor.bedroom_temperature
      - type: custom:decluttering-card
        template: minigraph_humidity
        variables:
        - sensor: sensor.bedroom_humidity
      columns: 3
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.bedroom_ceiling_light
    name: Ceiling
    layout: vertical
    show_brightness_control: true
    use_light_color: true
    grid_options:
      columns: 6
      rows: 3
  - type: custom:mushroom-light-card
    entity: light.bedroom_bed_light
    layout: vertical
    show_color_control: false
    show_brightness_control: true
    name: Bed
    use_light_color: true
  - type: custom:mushroom-title-card
    title: ''
    subtitle: WINDOW COVERS
    alignment: center
  - type: custom:mushroom-cover-card
    entity: cover.bedroom_window_blinds
    show_position_control: true
    show_buttons_control: false
    tap_action:
      action: none
    name: Blinds
    layout: vertical
  - type: custom:mushroom-cover-card
    entity: cover.bedroom_window_roller_cover
    fill_container: false
    show_position_control: false
    show_buttons_control: true
    tap_action:
      action: none
    name: Roller Blind
    layout: vertical
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:scheduler-card
        tags:
        - Bedroom
        title: false
        discover_existing: false
        show_header_toggle: false
        display_options:
          primary_info: default
          secondary_info:
          - relative-time
          - additional-tasks
          icon: action
        include:
        - cover
        - light
        exclude: []
      columns: 1
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: Sensors
      alignment: center
    - type: entities
      entities:
      - entity: sensor.bedroom_noise
        name: Bedroom Noise
      - entity: sensor.bedroom_temperature
        name: Bedroom Temperature
      - entity: sensor.bedroom_carbon_dioxide
        name: Bedroom CO2
      - entity: sensor.bedroom_humidity
        name: Bedroom Humidity
      show_header_toggle: false
      state_color: true
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: null
      alignment: center
      subtitle: Battery Levels
    - type: custom:auto-entities
      card:
        type: entities
      filter:
        include:
        - entity_id: sensor.bedroom*battery*
        exclude: []
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: Occupancy Settings
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: bedroom
    - area_name: Bedroom
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: Bed Occupancy
      alignment: center
    - type: custom:mushroom-template-card
      primary: "Bed {% set status = states(entity) %}\n{% if status == 'on' %}\n \
        \ Occupied\n{% else %}\n  Unoccupied\n{% endif %}"
      secondary: ''
      icon: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  mdi:bed-king\n\
        {% else %}\n  mdi:bed-king-outline\n{% endif %}"
      layout: vertical
      entity: input_boolean.bedroom_bed_occupancy
      icon_color: "{% set status = states(entity) %}\n{% if status == 'on' %}\n green\n\
        {% else %}\n  white\n{% endif %}"
      fill_container: true
      tap_action:
        action: none
      hold_action:
        action: more-info
      double_tap_action:
        action: none
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-template-card
        primary: "Evis {% set status = states(entity) %}\n{% if status == 'on' %}\n\
          \  in Bed\n{% else %}\n  not in Bed\n{% endif %}"
        secondary: ''
        icon: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  mdi:bed\n\
          {% else %}\n  mdi:bed-empty\n{% endif %}"
        layout: vertical
        entity: binary_sensor.master_bed_sensor_master_bed_occupancy_left
        icon_color: "{% set status = states(entity) %}\n{% if status == 'on' %}\n\
          \  blue\n{% else %}\n  white\n{% endif %}"
        fill_container: true
        tap_action:
          action: none
        hold_action:
          action: more-info
        double_tap_action:
          action: none
      - type: custom:mushroom-template-card
        primary: "Guest-1 {% set status = states(entity) %}\n{% if status == 'on'\
          \ %}\n  in Bed\n{% else %}\n  not in Bed\n{% endif %}"
        secondary: ''
        icon: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  mdi:bed\n\
          {% else %}\n  mdi:bed-empty\n{% endif %}"
        layout: vertical
        entity: binary_sensor.master_bed_sensor_master_bed_occupancy_right
        icon_color: "{% set status = states(entity) %}\n{% if status == 'on' %}\n\
          \  red\n{% else %}\n  white\n{% endif %}"
        fill_container: true
        tap_action:
          action: none
        hold_action:
          action: more-info
        double_tap_action:
          action: none
      - type: entities
        entities:
        - entity: binary_sensor.bedroom_bed_1_pressure_sensor
          name: Pressure
          icon: mdi:bed-outline
          state_color: true
        - entity: binary_sensor.bedroom_bed_Evis_fp2_occupancy
          name: Bed FP2
          icon: mdi:bed
          state_color: true
        - entity: binary_sensor.bedroom_bedside_Evis_fp2_sensor
          name: Bedside
          icon: mdi:walk
          state_color: true
        - entity: binary_sensor.bedroom_office_fp2_occupancy
          name: Office FP2
          icon: mdi:desk
          state_color: true
        - entity: sensor.master_bed_sensor_master_bed_occupancy_left_value
      - type: entities
        entities:
        - entity: binary_sensor.bedroom_bed_2_pressure_sensor
          name: Pressure
          icon: mdi:bed-outline
          state_color: true
        - entity: binary_sensor.bedroom_bed_Guest-1_fp2_occupancy
          name: Bed FP2
          icon: mdi:bed
          state_color: true
        - entity: binary_sensor.bedroom_bedside_Guest-1_fp2_sensor
          name: Bedside
          icon: mdi:walk
          state_color: true
        - entity: binary_sensor.bedroom_office_fp2_occupancy
          name: Office FP2
          icon: mdi:desk
          state_color: true
        - entity: sensor.master_bed_sensor_master_bed_occupancy_right_value
      columns: 2
max_columns: 4

```
