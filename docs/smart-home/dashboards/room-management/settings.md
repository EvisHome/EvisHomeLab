---
tags:
  - dashboard
  - view
  - automated
---

# Settings

**Dashboard:** Room Management  
**Path:** `settings`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_settings.png)

## Related Packages
This view contains entities managed by:

* [Room Automation](../../packages/room_automation.md)
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`


## Configuration
```yaml
title: Settings
icon: mdi:home-cog
type: sections
max_columns: 3
sections:
- type: grid
  cards:
  - type: heading
    heading: Add / Update Room
    icon: mdi:home-plus
  - type: markdown
    content: '**Instructions:**


      1. Select a **Native Area** from the list.

      2. Click **Initialize** to create helpers for it.


      *Uses Home Assistant Areas as the source.*

      '
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_select.room_mgmt_create_select
      name: Select Area
    - type: call-service
      icon: mdi:refresh
      name: Refresh Area List
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_room_list
        skip_condition: true
  - type: tile
    entity: input_select.room_mgmt_create_select
    name: Initialize Area
    icon: mdi:content-save
    color: green
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.create_room_settings
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--green-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
  - type: heading
    heading: Danger Zone
    icon: mdi:alert-circle-outline
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_select.room_mgmt_delete_select
      name: Select Room to Delete
    - type: call-service
      icon: mdi:refresh
      name: Refresh Lists
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_room_list
        skip_condition: true
  - type: tile
    entity: input_select.room_mgmt_delete_select
    name: Delete Room Config
    icon: mdi:delete
    color: red
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.delete_room_settings
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--red-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\
        \ /* Icon visibility fix */\n}\n"
- type: grid
  cards:
  - type: heading
    heading: Configured Rooms
    icon: mdi:view-dashboard-outline
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      show_header_toggle: false
    filter:
      template: "{% set ns = namespace(cards=[]) %}\n{# Broader search for any select\
        \ entity with 'automation_mode' in the ID #}\n{% set mode_selectors = states.select\
        \ | selectattr('entity_id', 'search', 'automation_mode') | list %}\n\n{% for\
        \ sel in mode_selectors %}\n  {# Extract slug. Handles \"select.bathroom_automation_mode\"\
        \ or \"select.room_bathroom_automation_mode\" #}\n  {% set raw_id = sel.entity_id.split('.')[1]\
        \ %}\n  {% if raw_id.startswith('room_') %}\n     {% set slug = raw_id.replace('room_',\
        \ '').replace('_automation_mode', '') %}\n  {% else %}\n     {% set slug =\
        \ raw_id.replace('_automation_mode', '') %}\n  {% endif %}\n  \n  {# UPDATED:\
        \ Generate Name purely from Slug (Cleaner) #}\n  {% set name = slug.replace('_',\
        \ ' ') | title %}\n  \n  {# --- Header --- #}\n  {% set ns.cards = ns.cards\
        \ + [{'type': 'section', 'label': name}] %}\n  \n  {# --- Controls --- #}\n\
        \  \n  {# Mode Selector #}\n  {% set ns.cards = ns.cards + [{'entity': sel.entity_id,\
        \ 'name': 'Mode'}] %}\n  \n  {# Room State #}\n  {% set state_select = 'select.room_'\
        \ ~ slug ~ '_state' %}\n  {% if states[state_select] is defined %}\n    {%\
        \ set ns.cards = ns.cards + [{'entity': state_select, 'name': 'Current State'}]\
        \ %}\n  {% endif %}\n\n  {# Occupancy #}\n  {% set occ_sensor = 'binary_sensor.room_'\
        \ ~ slug ~ '_occupancy' %}\n  {% if states[occ_sensor] is defined %}\n   \
        \ {% set ns.cards = ns.cards + [{'entity': occ_sensor, 'name': 'Occupancy'}]\
        \ %}\n  {% endif %}\n  \n  {# Idle Time #}\n  {% set idle_entity = 'number.'\
        \ ~ slug ~ '_presence_idle_time' %}\n  {% if states[idle_entity] is defined\
        \ %}\n    {% set ns.cards = ns.cards + [{'entity': idle_entity, 'name': 'Idle\
        \ Time (sec)'}] %}\n  {% endif %}\n  \n  {# Off Delay #}\n  {% set delay_entity\
        \ = 'number.' ~ slug ~ '_lights_presence_delay' %}\n  {% if states[delay_entity]\
        \ is defined %}\n    {% set ns.cards = ns.cards + [{'entity': delay_entity,\
        \ 'name': 'Off Delay (sec)'}] %}\n  {% endif %}\n  \n  {# Lux Sensor #}\n\
        \  {% set lux_s = 'text.room_' ~ slug ~ '_lux_sensor' %}\n  {% if states[lux_s]\
        \ is defined %}\n    {% set ns.cards = ns.cards + [{'entity': lux_s, 'name':\
        \ 'Lux Sensor ID'}] %}\n  {% endif %}\n  \n  {# Lux Threshold #}\n  {% set\
        \ lux_t = 'number.room_' ~ slug ~ '_lux_threshold' %}\n  {% if states[lux_t]\
        \ is defined %}\n     {% set ns.cards = ns.cards + [{'entity': lux_t, 'name':\
        \ 'Lux Threshold (lx)'}] %}\n  {% endif %}\n  \n  {# Bed Sensor #}\n  {% set\
        \ bed_s = 'text.room_' ~ slug ~ '_bed_sensor' %}\n  {% if states[bed_s] is\
        \ defined %}\n    {% set ns.cards = ns.cards + [{'entity': bed_s, 'name':\
        \ 'Bed Sensor ID'}] %}\n  \n    {# Only show sleep timers if a bed sensor\
        \ ID is entered #}\n    {% if states(bed_s) not in ['unknown', 'unavailable',\
        \ '', 'none'] %}\n       {% set sleep_entry = 'number.room_' ~ slug ~ '_sleep_entry_delay'\
        \ %}\n       {% if states[sleep_entry] is defined %}\n         {% set ns.cards\
        \ = ns.cards + [{'entity': sleep_entry, 'name': 'Sleep Entry Delay (sec)'}]\
        \ %}\n       {% endif %}\n       \n       {% set sleep_exit = 'number.room_'\
        \ ~ slug ~ '_sleep_exit_delay' %}\n       {% if states[sleep_exit] is defined\
        \ %}\n         {% set ns.cards = ns.cards + [{'entity': sleep_exit, 'name':\
        \ 'Sleep Exit Delay (sec)'}] %}\n       {% endif %}\n    {% endif %}\n  {%\
        \ endif %}\n  \n{% endfor %}\n{{ ns.cards | to_json }}\n"
    sort:
      method: none

```
