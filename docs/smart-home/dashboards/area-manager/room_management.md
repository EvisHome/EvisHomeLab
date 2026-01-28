---
tags:
  - dashboard
  - view
  - automated
---

# Room Management

**Dashboard:** Area Manager  
**Path:** `room_management`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_room_management.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Area Manager](../../packages/area_manager.md)
* [Dishwasher](../../packages/dishwasher.md)
* [Smart Notifications](../../packages/smart_notifications.md)
* [Washing Machine](../../packages/washing_machine.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`
* `custom:streamline-card`


## Configuration
```yaml
title: Room Management
icon: ''
type: sections
max_columns: 4
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
    title: Manage Areas
  - type: heading
    heading: Add / Update Room
    icon: mdi:home-plus
  - type: markdown
    content: '**Instructions:**

      1. Select a **Native Area** from the list.

      2. Click **Initialize** to create helpers for it.

      *Uses Home Assistant Areas as the source.*

      3. If scene sare not showing, reinitialize the area

      *Settings are preserved*

      '
  - type: entities
    show_header_toggle: false
    title: Register New Area
    entities:
    - entity: input_select.area_mgmt_create_select
      name: Select Area (from HA)
    - type: call-service
      icon: mdi:refresh
      name: Refresh List
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_area_list
        skip_condition: true
  - type: tile
    entity: input_select.area_mgmt_create_select
    name: Initialize Area
    icon: mdi:content-save
    color: green
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.create_area_settings
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--green-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 9
      rows: 1
  - type: heading
    heading: Danger Zone
    icon: mdi:alert-circle-outline
  - type: entities
    show_header_toggle: false
    title: Delete Area
    entities:
    - entity: input_select.area_mgmt_delete_select
      name: Select Area to Delete
    - type: call-service
      icon: mdi:refresh
      name: Refresh List
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_area_list
        skip_condition: true
  - type: tile
    entity: input_select.area_mgmt_delete_select
    name: Delete Room Config
    icon: mdi:delete
    color: red
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.delete_area_settings
      confirmation:
        text: Are you sure you want to delete this Area configuration?
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--red-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\
        \ /* Icon visibility fix */\n}\n"
    grid_options:
      columns: 9
      rows: 1
- type: grid
  cards:
  - type: custom:mushroom-title-card
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
    title: Area Configurations
  - type: heading
    heading: Configured Areas
    icon: mdi:view-dashboard-outline
    heading_style: title
  - type: custom:auto-entities
    card:
      type: entities
      title: Area Configurations
      show_header_toggle: false
    filter:
      template: "{% set ns = namespace(rows=[]) %} \n{# STRICT FILTER: Only look for\
        \ selectors starting with 'select.area_' #} \n{% set mode_selectors = states.select\
        \ \n    | selectattr('entity_id', 'search', '^select\\\\.area_.*_automation_mode$')\
        \ \n    | sort(attribute='entity_id') \n    | list %}\n{% for sel in mode_selectors\
        \ %}\n  {# Extract slug: select.area_kitchen_automation_mode -> kitchen #}\n\
        \  {% set raw_id = sel.entity_id.split('.')[1] %}\n  {# Remove prefix and\
        \ suffix to get the slug #}\n  {% set area_key = raw_id.replace('area_', '').replace('_automation_mode',\
        \ '') %}\n  \n  {# SMART NAMING: Use the Entity Name (e.g. \"Area 51 Automation\
        \ Mode\") and strip suffix #}\n  {# FIX: Handle redundancy \"Toilet Settings\
        \ Toilet...\" by splitting at ' Settings' #}\n  {% set raw_name = state_attr(sel.entity_id,\
        \ 'friendly_name') %}\n  {% set name = raw_name.split(' Settings')[0] | replace('\
        \ Automation Mode', '') %}\n  \n  {# Define Entity IDs using new 'area_' schema\
        \ #}\n  {% set state_select = 'select.area_' ~ area_key ~ '_state' %}\n  {%\
        \ set auto_switch  = 'switch.area_' ~ area_key ~ '_automation' %}\n  {% set\
        \ occ_sensor   = 'binary_sensor.area_' ~ area_key ~ '_occupancy' %}\n  {%\
        \ set idle_entity  = 'number.area_' ~ area_key ~ '_presence_idle_time' %}\n\
        \  {% set delay_entity = 'number.area_' ~ area_key ~ '_lights_presence_delay'\
        \ %}\n  {% set bed_s        = 'select.area_' ~ area_key ~ '_bed_sensor' %}\n\
        \  {% set sleep_entry  = 'number.area_' ~ area_key ~ '_sleep_entry_delay'\
        \ %}\n  {% set sleep_exit   = 'number.area_' ~ area_key ~ '_sleep_exit_delay'\
        \ %}\n  {% set occ_source   = 'select.area_' ~ area_key ~ '_occupancy_source'\
        \ %}\n  {% set timer_entity = 'sensor.area_' ~ area_key ~ '_timer' %}\n  {%\
        \ set entities = [] %}\n  \n  {# 1. Mode #}\n  {% set entities = entities\
        \ + [{'entity': sel.entity_id, 'name': 'Mode'}] %}\n  {# 2. Switch #}\n  {%\
        \ if states[auto_switch] is defined %}\n    {% set entities = entities + [{'entity':\
        \ auto_switch, 'name': 'Automation Enabled'}] %}\n  {% endif %}\n  {# 3. State\
        \ #}\n  {% if states[state_select] is defined %}\n    {% set entities = entities\
        \ + [{'entity': state_select, 'name': 'Current State'}] %}\n  {% endif %}\n\
        \  {# 4. Occupancy #}\n  {% if states[occ_sensor] is defined %}\n    {% set\
        \ entities = entities + [{'entity': occ_sensor, 'name': 'Occupancy'}] %}\n\
        \  {% endif %}\n  {# 5. Occupancy Source #}\n  {% if states[occ_source] is\
        \ defined %}\n    {% set entities = entities + [{'entity': occ_source, 'name':\
        \ 'Occupancy Sensor'}] %}\n  {% endif %}\n  {# 6. Timer Bar (Conditional Row)\
        \ #}\n  {% if states[timer_entity] is defined %}\n     {% set entities = entities\
        \ + [{\n        'type': 'conditional',\n        'conditions': [\n        \
        \  {'entity': timer_entity, 'state_not': 'unavailable'},\n          {'entity':\
        \ timer_entity, 'state_not': 'unknown'},\n          {'entity': timer_entity,\
        \ 'state_not': 'none'},\n          {'entity': timer_entity, 'state_not': ''}\n\
        \        ],\n        'row': {\n           'entity': timer_entity,\n      \
        \     'name': 'Timer'\n        }\n     }] %}\n  {% endif %}\n  {# 7. Config\
        \ Numbers #}\n  {% if states[idle_entity] is defined %}\n    {% set entities\
        \ = entities + [{'entity': idle_entity, 'name': 'Idle Time (sec)'}] %}\n \
        \ {% endif %}\n  {% if states[delay_entity] is defined %}\n    {% set entities\
        \ = entities + [{'entity': delay_entity, 'name': 'Off Delay (sec)'}] %}\n\
        \  {% endif %}\n  {# 8. Bed Sensor & Sleep Timers (Conditional) #}\n  {% if\
        \ states[bed_s] is defined %}\n    {% set entities = entities + [{'entity':\
        \ bed_s, 'name': 'Bed Occupancy Sensor'}] %}\n    \n    {# Sleep Entry Delay\
        \ #}\n    {% if states[sleep_entry] is defined %}\n      {% set entities =\
        \ entities + [{\n         'type': 'conditional',\n         'conditions': [\n\
        \            {'entity': bed_s, 'state_not': '-Select-'},\n            {'entity':\
        \ bed_s, 'state_not': 'unknown'},\n            {'entity': bed_s, 'state_not':\
        \ 'unavailable'}\n         ],\n         'row': {\n            'entity': sleep_entry,\n\
        \            'name': 'Sleep Entry Delay (sec)'\n         }\n      }] %}\n\
        \    {% endif %}\n    {# Sleep Exit Delay #}\n    {% if states[sleep_exit]\
        \ is defined %}\n      {% set entities = entities + [{\n         'type': 'conditional',\n\
        \         'conditions': [\n            {'entity': bed_s, 'state_not': '-Select-'},\n\
        \            {'entity': bed_s, 'state_not': 'unknown'},\n            {'entity':\
        \ bed_s, 'state_not': 'unavailable'}\n         ],\n         'row': {\n   \
        \         'entity': sleep_exit,\n            'name': 'Sleep Exit Delay (sec)'\n\
        \         }\n      }] %}\n    {% endif %}\n  {% endif %}\n  {# Create the\
        \ Group #}\n  {% set group = {\n    'type': 'custom:fold-entity-row',\n  \
        \  'head': {'type':'section', 'label': name, 'card_mod': {\n      'style':\
        \ \".label { color: orange !important; }\"\n    }},\n    'entities': entities\n\
        \  } %}\n  {% set ns.rows = ns.rows + [group] %}\n{% endfor %} {{ ns.rows\
        \ | to_json }}\n"
- type: grid
  cards:
  - type: custom:mushroom-title-card
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
    title: Area Automations
  - type: heading
    heading: Configured Area Automations
    icon: mdi:view-dashboard-outline
    heading_style: title
  - type: custom:auto-entities
    card:
      type: entities
      title: Area Automations
      show_header_toggle: false
    filter:
      template: "{% set ns = namespace(rows=[]) %} \n{# STRICT FILTER: Only look for\
        \ selectors starting with 'select.area_' #} \n{% set mode_selectors = states.select\
        \ \n    | selectattr('entity_id', 'search', '^select\\\\.area_.*_automation_mode$')\
        \ \n    | sort(attribute='entity_id') \n    | list %}\n{% for sel in mode_selectors\
        \ %}\n  {# Extract slug: select.area_kitchen_automation_mode -> kitchen #}\n\
        \  {% set raw_id = sel.entity_id.split('.')[1] %}\n  {# Remove prefix and\
        \ suffix to get the slug #}\n  {% set area_key = raw_id.replace('area_', '').replace('_automation_mode',\
        \ '') %}\n  \n  {# SMART NAMING #}\n  {% set raw_name = state_attr(sel.entity_id,\
        \ 'friendly_name') %}\n  {% set name = raw_name.split(' Settings')[0] | replace('\
        \ Automation Mode', '') %}\n  \n  {# Define new helper schema #}\n  {% set\
        \ dnd_switch   = 'switch.area_' ~ area_key ~ '_dnd' %}\n  {% set morning_s\
        \    = 'select.area_' ~ area_key ~ '_morning_scene' %}\n  {% set day_s   \
        \     = 'select.area_' ~ area_key ~ '_day_scene' %}\n  {% set evening_s  \
        \  = 'select.area_' ~ area_key ~ '_evening_scene' %}\n  {% set night_s   \
        \   = 'select.area_' ~ area_key ~ '_night_scene' %}\n  {% set absence_act\
        \  = 'select.area_' ~ area_key ~ '_absence_action' %}\n  {% set sleep_act\
        \    = 'select.area_' ~ area_key ~ '_sleep_action' %}\n  {% set off_delay_act\
        \ = 'select.area_' ~ area_key ~ '_off_delay_action' %}\n  \n  {% set occ_sensor\
        \   = 'binary_sensor.area_' ~ area_key ~ '_occupancy' %}\n  {% set state_select\
        \ = 'select.area_' ~ area_key ~ '_state' %}\n  \n  {% set entities = [] %}\n\
        \  \n  {# 1. Mode #}\n  {% set entities = entities + [{'entity': sel.entity_id,\
        \ 'name': 'Automation Mode'}] %}\n  \n  {# 2. DND #}\n  {% if states[dnd_switch]\
        \ is defined %}\n    {% set entities = entities + [{'entity': dnd_switch,\
        \ 'name': 'Do Not Disturb'}] %}\n  {% endif %}\n\n  {# 3. Status #}\n  {%\
        \ if states[state_select] is defined %}\n    {% set entities = entities +\
        \ [{'entity': state_select, 'name': 'Current State'}] %}\n  {% endif %}\n\n\
        \  {# 4. Scenes Section #}\n  {% set entities = entities + [{'type': 'section',\
        \ 'label': 'Time-Based Scenes'}] %}\n  {% if states[morning_s] is defined\
        \ %} {% set entities = entities + [{'entity': morning_s, 'name': 'Morning'}]\
        \ %} {% endif %}\n  {% if states[day_s] is defined %}     {% set entities\
        \ = entities + [{'entity': day_s, 'name': 'Day'}] %}         {% endif %}\n\
        \  {% if states[evening_s] is defined %} {% set entities = entities + [{'entity':\
        \ evening_s, 'name': 'Evening'}] %} {% endif %}\n  {% if states[night_s] is\
        \ defined %}   {% set entities = entities + [{'entity': night_s, 'name': 'Night'}]\
        \ %}     {% endif %}\n\n  {# 5. Actions Section #}\n  {% set entities = entities\
        \ + [{'type': 'section', 'label': 'Special Actions'}] %}\n  {% if states[off_delay_act]\
        \ is defined %} {% set entities = entities + [{'entity': off_delay_act, 'name':\
        \ 'Off Delay Action'}] %} {% endif %}\n  {% if states[absence_act] is defined\
        \ %}   {% set entities = entities + [{'entity': absence_act, 'name': 'Absence\
        \ Action'}] %}   {% endif %}\n  {% if states[sleep_act] is defined %}    \
        \ {% set entities = entities + [{'entity': sleep_act, 'name': 'Sleep Action'}]\
        \ %}       {% endif %}\n  \n  {# Create the Group #}\n  {% set group = {\n\
        \    'type': 'custom:fold-entity-row',\n    'head': {'type':'section', 'label':\
        \ name, 'card_mod': {\n      'style': \".label { color: orange !important;\
        \ }\"\n    }},\n    'entities': entities\n  } %}\n  {% set ns.rows = ns.rows\
        \ + [group] %}\n{% endfor %} {{ ns.rows | to_json }}\n"
- type: grid
  cards:
  - type: custom:mushroom-title-card
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
    title: Active Areas
  - type: custom:mushroom-title-card
    alignment: center
    subtitle: 2nd Floor
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: sauna
      area_title: Sauna
      temp_sensor_entity: sensor.ruuvitag_8572_temperature
      indicator_1_entity: binary_sensor.sauna_door_contact
      indicator_1_icon: mdi:door
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 1s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: bathroom
      area_title: Bathroom
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_state: Running
      indicator_1_active_color: '#088CF8'
      indicator_1_animation_on: blink 2s ease infinite
      indicator_3_state: presence
      indicator_3_active_color: '#088CF8'
      indicator_5_state: 'on'
      indicator_5_active_color: '#FF4444'
      indicator_1_entity: input_select.washing_machine_status
      indicator_1_icon: mdi:washing-machine
      indicator_2_entity: input_select.bathroom_toilet_presence
      indicator_2_icon: mdi:toilet
      indicator_2_state: presence
      indicator_2_active_color: orange
      indicator_3_entity: input_select.shower_presence
      indicator_3_icon: presence
      indicator_6_entity: sensor.aqara_w500_bathroom_heating_hvac
      indicator_6_icon: mdi:heating-coil
      indicator_6_state: heating
      indicator_6_active_color: '#FF4444'
      indicator_6_animation_on: blink 2s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: office
      area_title: Office
      temp_sensor_entity: sensor.bedroom_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: bedroom
      area_title: Bedroom
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_state: open
      indicator_1_active_color: lightgreen
      temp_sensor_entity: sensor.bedroom_temperature
      indicator_1_entity: cover.bedroom_window_blinds
      indicator_1_icon: mdi:window-shutter
      indicator_2_entity: cover.bedroom_window_roller_cover
      indicator_2_icon: mdi:blinds-open
      indicator_2_state: open
      indicator_2_active_color: lightgreen
      indicator_3_entity: input_boolean.bed_Evis_occupancy
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: '#088CF8'
      indicator_4_entity: input_boolean.bed_Guest-1_occupancy
      indicator_4_icon: mdi:bed
      indicator_4_state: 'on'
      indicator_4_active_color: '#FF44C4'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Guest-2
      area_title: E Bedroom
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_entity: binary_sensor.Guest-2_bed_fp2_presence_sensor
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Guest-2_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Guest-3
      area_title: A Bedroom
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_entity: binary_sensor.Guest-3_bed_fp2_presence_sensor
      indicator_3_active_color: lightgreen
      temp_sensor_entity: sensor.Guest-3_temperature
      indicator_4_entity: binary_sensor.Guest-3_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: stairs
      area_title: Stairs
      temp_sensor_entity: sensor.airthings_wave_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: lobby
      area_title: Lobby
    grid_options:
      columns: 6
  - type: custom:mushroom-title-card
    alignment: center
    subtitle: 1st Floor
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: hallway
      area_title: Hallway
      temp_sensor_entity: sensor.airthings_wave_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: kitchen
      area_title: Kitchen
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
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Daughter
      area_title: Guest Room
      temp_sensor_entity: sensor.airthings_wave_temperature
      indicator_1_entity: binary_sensor.Daughter_bed_fp2_presence_sensor
      indicator_1_icon: mdi:bed-king
      indicator_1_state: 'on'
      indicator_1_active_color: lightgreen
    grid_options:
      columns: 6
cards: []

```
