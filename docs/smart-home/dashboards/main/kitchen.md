---
tags:
  - dashboard
  - view
  - automated
---

# Kitchen

**Dashboard:** Main Dashboard  
**Path:** `kitchen`

![View Screenshot](../../../assets/images/dashboards/view_main_kitchen.png)

## Configuration
```yaml
title: Kitchen
path: kitchen
type: sections
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: kitchen
      area_title: Kitchen
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.kitchen_fridge_door_device_temperature
      indicator_1_entity: binary_sensor.kitchen_fridge_door_contact
      indicator_1_icon: mdi:fridge
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 0.5s ease infinite
      indicator_2_entity: binary_sensor.kitchen_fridge_leak_sensor_water_leak
      indicator_2_icon: mdi:fridge-alert
      indicator_2_state: 'on'
      indicator_2_active_color: '#088CF8'
      indicator_2_animation_on: blink 0.5s ease infinite
      indicator_3_entity: sensor.coffee_machine_state
      indicator_3_icon: mdi:coffee
      indicator_3_active_color: orange
      indicator_3_state: Running
      indicator_4_entity: switch.schedule_coffee_machine_schedule
      indicator_4_icon: mdi:coffee-to-go-outline
      indicator_4_state: 'on'
      indicator_3_animation_on: blink 2s ease infinite
      indicator_4_active_color: lightgreen
      indicator_5_entity: sensor.dishwasher_current_status
      indicator_5_icon: mdi:dishwasher
      indicator_5_state: running
      indicator_5_active_color: skyblue
      indicator_5_animation_on: blink 2s ease infinite
      indicator_6_entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
      indicator_6_icon: mdi:dishwasher-alert
      indicator_6_state: 'on'
      indicator_6_active_color: '#088CF8'
      indicator_6_animation_on: blink 0.5s ease infinite
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.kitchen_ceiling_light
    show_brightness_control: true
    show_color_control: false
    show_color_temp_control: false
    fill_container: false
    tap_action:
      action: toggle
  - type: custom:mushroom-light-card
    entity: light.kitchen_sink_light
    show_color_temp_control: false
    show_brightness_control: true
    tap_action:
      action: toggle
  - type: custom:mushroom-entity-card
    entity: switch.kitchen_wall_box_switch_left
    name: Ceiling Light Switch
    icon: mdi:light-switch
  - type: custom:mushroom-title-card
    title: ''
    subtitle: DISHWASHER
    alignment: center
  - type: custom:mushroom-entity-card
    entity: sensor.dishwasher_state
    layout: vertical
    name: Dishwasher
    icon: mdi:dishwasher
    fill_container: true
  - type: custom:mushroom-entity-card
    entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
    name: Leak Sensor
    layout: vertical
  - type: custom:mushroom-entity-card
    entity: binary_sensor.dishwasher_door
    layout: vertical
    name: Dishwasher Door
    icon: mdi:dishwasher
    fill_container: true
  - type: custom:mushroom-entity-card
    entity: sensor.dishwasher_current_status
    layout: vertical
    name: Dishwasher Status
    icon: mdi:dishwasher
    fill_container: true
  - type: custom:mushroom-entity-card
    entity: sensor.dishwasher_remaining_time
    layout: vertical
    name: Dishwasher Remaining Time
    icon: mdi:dishwasher
    fill_container: true
  - type: custom:mushroom-entity-card
    entity: sensor.dishwasher_total_time
    layout: vertical
    name: Dishwasher Run Time
    icon: mdi:dishwasher
    fill_container: true
  - type: custom:mushroom-title-card
    title: ''
    subtitle: APPLIANCES
    alignment: center
  - type: custom:mushroom-template-card
    primary: Fridge Door
    secondary: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  Closed\n\
      {% else %}\n  Open\n{% endif %}"
    icon: mdi:fridge
    entity: binary_sensor.kitchen_fridge_door_contact
    fill_container: true
    layout: vertical
    icon_color: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  green\n\
      {% else %}\n  red\n{% endif %}"
  - type: custom:mushroom-template-card
    primary: Coffee Machine
    secondary_info: last-changed
    secondary: "{% set status = states(entity) %}\n{% if status == 'Running' %}\n\
      \  Running\n{% else %}\n  {{ (as_timestamp(now()) - as_timestamp(states.sensor.coffee_machine_state.last_changed\
      \ | default(0)) | int ) | timestamp_custom(\"%Hh %Mm\", false) }} ago\n{% endif\
      \ %}"
    icon: mdi:coffee
    entity: sensor.coffee_machine_state
    fill_container: true
    layout: vertical
    icon_color: "{% set status = states(entity) %}\n{% if status == 'Running' %}\n\
      \  red\n{% else %}\n  green\n{% endif %}"
  - type: custom:mushroom-title-card
    title: ''
    subtitle: POWER
    alignment: center
  - type: custom:mushroom-entity-card
    entity: sensor.kitchen_coffee_machine_outlet_power
    layout: vertical
    name: Coffee Machine Power
    icon_color: accent
    tap_action:
      action: none
    double_tap_action:
      action: none
    hold_action:
      action: more-info
    fill_container: true
  - type: custom:mushroom-entity-card
    entity: switch.kitchen_coffee_machine_outlet
    layout: vertical
    name: Coffee Machine Outlet
    icon_color: green
    tap_action:
      action: none
    double_tap_action:
      action: none
    hold_action:
      action: more-info
    fill_container: true
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHT SETTINGS
    alignment: center
  - type: entities
    entities:
    - entity: light.kitchen_sink_light
    - entity: light.kitchen_ceiling_light
    - type: section
      label: Ceiling Bulbs
    - type: buttons
      entities:
      - entity: light.kitchen_ceiling_light_1
        name: Ceiling Light 1
      - entity: light.kitchen_ceiling_light_2
        name: Ceiling Light 2
      - entity: light.kitchen_ceiling_light_3
        name: Ceiling Light 3
  - type: custom:mushroom-title-card
    title: ''
    subtitle: BATTERY LEVELS
    alignment: center
  - type: custom:auto-entities
    card:
      type: entities
    filter:
      include:
      - entity_id: sensor.kitchen*battery*
      - entity_id: sensor.dishwasher*battery
      exclude: []
  - type: custom:mushroom-title-card
    title: ''
    subtitle: COFFEE MACHINE AUTOMATION
    alignment: center
  - type: entities
    entities:
    - entity: switch.kitchen_coffee_machine_outlet
      secondary_info: last-changed
      icon: mdi:coffee
  - type: custom:scheduler-card
    include:
    - switch.kitchen_coffee_machine_outlet
    exclude: []
- type: grid
  cards:
  - type: heading
    heading: New section
  - type: markdown
    content: <li>{{ expand('light.kitchen_ceiling_light')|map(attribute='name')|list|join('<li>')
      }}
  - square: false
    columns: 1
    type: grid
    cards:
    - type: custom:mushroom-title-card
      title: SETTINGS
      alignment: center
      subtitle: OCCUPANCY SETTINGS
  - type: history-graph
    entities:
    - entity: input_boolean.kitchen_occupancy
      name: Presence
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_6
      name: Entrance
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_4
      name: Table
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_3
      name: Cooking
    hours_to_show: 12
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: kitchen
    - area_name: Kitchen
  - type: entities
    entities:
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_1
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_6
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_5
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_4
    - entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_3
max_columns: 4
subview: true
cards: []

```
