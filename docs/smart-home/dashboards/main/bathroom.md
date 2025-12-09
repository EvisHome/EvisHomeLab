---
tags:
  - dashboard
  - view
  - automated
---

# Bathroom

**Dashboard:** Main Dashboard  
**Path:** `bathroom`

![View Screenshot](../../../assets/images/dashboards/dashboard_bathroom.png)

## Related Packages
This view contains entities managed by:

* [Aqara W500](../../packages/aqara_w500.md)
* [Nordpool Prices](../../packages/nordpool_prices.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`
* `custom:mushroom-entity-card`
* `custom:mushroom-light-card`
* `custom:mushroom-number-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`
* `custom:timer-bar-card`


## Configuration
```yaml
theme: Backend-selected
title: Bathroom
path: bathroom
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
      area_name: bathroom
      area_title: Bathroom
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_entity: sensor.washing_machine_status
      indicator_1_icon: mdi:washing-machine
      indicator_1_state: Running
      indicator_1_active_color: '#088CF8'
      indicator_1_animation_on: blink 2s ease infinite
      indicator_2_entity: input_select.bathroom_toilet_presence
      indicator_2_icon: mdi:toilet
      indicator_3_icon: mdi:shower-head
      indicator_3_active_color: '#088CF8'
      indicator_2_active_color: orange
      indicator_3_entity: input_select.shower_presence
      indicator_3_state: presence
      indicator_2_state: presence
      temp_sensor_entity: sensor.aqara_w500_temperature_smoothed
      indicator_6_entity: sensor.aqara_w500_bathroom_heating_hvac
      indicator_6_icon: mdi:heating-coil
      indicator_6_state: heating
      indicator_6_active_color: '#FF4444'
      indicator_6_animation_on: blink 2s ease infinite
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.bathroom_wall_box_switch_right
    name: Sauna
    layout: vertical
    grid_options:
      columns: 4
      rows: 2
  - type: custom:mushroom-light-card
    entity: light.bathroom_lightstrip
    layout: vertical
    name: Table
    grid_options:
      columns: 4
      rows: 2
  - type: custom:mushroom-light-card
    name: Ceiling
    layout: vertical
    grid_options:
      columns: 4
      rows: 2
    entity: light.bathroom_wall_box_switch_right
  - type: custom:mushroom-title-card
    title: ''
    subtitle: APPLIANCES
    alignment: center
  - type: custom:mushroom-entity-card
    entity: sensor.washing_machine_status
    grid_options:
      columns: 12
      rows: 1
  - type: custom:mushroom-title-card
    title: ''
    subtitle: HEATING
    alignment: center
  - type: thermostat
    entity: climate.aqara_w500
    name: Bathroom Floor
    show_current_as_primary: false
    features:
    - type: climate-hvac-modes
  - type: history-graph
    show_names: true
    entities:
    - entity: sensor.aqara_w500_state
      name: ' '
    - entity: climate.aqara_w500
    - entity: sensor.aqara_w500_temperature_smoothed
    hours_to_show: 24
    logarithmic_scale: false
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: Occupancy
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: bathroom
    - area_name: Bathroom
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
  - type: heading
    heading: Floor Heating Automations
    heading_style: title
  - type: custom:scheduler-card
    title: Floor Heating
    discover_existing: false
    time_step: 5
    tags:
    - Bathroom
    include:
    - climate.aqara_w500
    - sensor.nord_pool_fi_current_price
    display_options:
      secondary_info:
      - relative-time
    default_editor: single
    sort_by:
    - state
    - relative-time
    show_header_toggle: false
  - type: markdown
    content: '*Default Temperature* is the heating base temperature.


      If the thermostate is turned higher than the default, the *Heating Timer* will
      keep this new temperature until the timer runs out.


      The *Heating Timer* tells how long the heating will still run'
  - type: custom:timer-bar-card
    entity: timer.bathroom_floor_heating_timer
  - type: custom:mushroom-number-card
    entity: input_number.bathroom_floor_heat_default_temperature
    name: Default Temperature
    grid_options:
      columns: 6
      rows: 2
    icon_color: accent
  - type: custom:mushroom-number-card
    entity: input_number.bathroom_floor_heat_target_temperature
    name: Target Temperature
    grid_options:
      columns: 6
      rows: 2
    icon_color: red
  - type: custom:mushroom-number-card
    entity: input_number.bathroom_floor_heat_override_duration
    name: Heating Timer
    grid_options:
      columns: 12
      rows: 2
    icon_color: teal
max_columns: 4

```
