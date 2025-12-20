---
tags:
  - dashboard
  - view
  - automated
---

# Room Management

**Dashboard:** Room Management  
**Path:** `room-management`

<!-- START_DESCRIPTION -->
Admin interface for creating, deleting, and managing room configurations and automation helpers.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_room_management.png)

## Summary
<!-- START_SUMMARY -->
The Room Management dashboard serves as the administrative backend for the home's room logic. It allows users to initialize new rooms (creating necessary helper entities) or delete existing ones. It features a dynamic "Configured Rooms" section powered by `auto-entities`, which automatically lists all configured rooms and provides collapsible controls for their automation modes, occupancy sensors, and timeouts.
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Room Manager](../../packages/room_manager.md)
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`


## Configuration
```yaml
title: Room Management
icon: ''
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
      template: "        {% set ns = namespace(rows=[]) %}\n        {% set mode_selectors\
        \ = states.select | selectattr('entity_id','search','automation_mode') | sort(attribute='entity_id')\
        \ | list %}\n\n        {% for sel in mode_selectors %}\n          {# Extract\
        \ base id and normalize to room_key #}\n          {% set raw_id = sel.entity_id.split('.')[1]\
        \ %}\n          {% set base = raw_id.replace('_automation_mode','') %}\n \
        \         {% if base.startswith('room_') %}\n            {% set room_key =\
        \ base[5:] %}\n          {% else %}\n            {% set room_key = base %}\n\
        \          {% endif %}\n          {% set name = room_key.replace('_',' ')\
        \ | title %}\n\n          {# Compose downstream entity ids with exactly one\
        \ room_ prefix #}\n          {% set state_select = 'select.room_' ~ room_key\
        \ ~ '_state' %}\n          {% set occ_sensor   = 'binary_sensor.room_' ~ room_key\
        \ ~ '_occupancy' %}\n          {% set idle_entity  = 'number.room_' ~ room_key\
        \ ~ '_presence_idle_time' %}\n          {% set delay_entity = 'number.room_'\
        \ ~ room_key ~ '_lights_presence_delay' %}\n          {% set bed_s       \
        \ = 'text.room_' ~ room_key ~ '_bed_sensor' %}\n          {% set sleep_entry\
        \  = 'number.room_' ~ room_key ~ '_sleep_entry_delay' %}\n          {% set\
        \ sleep_exit   = 'number.room_' ~ room_key ~ '_sleep_exit_delay' %}\n    \
        \      {% set occ_source   = 'select.room_' ~ room_key ~ '_occupancy_source'\
        \ %}\n\n          {# Build the collapsible group's entity list, conditionally\
        \ #}\n          {% set entities = [] %}\n          {% set entities = entities\
        \ + [{'entity': sel.entity_id, 'name': 'Mode'}] %}\n\n          {% if states[state_select]\
        \ is defined %}\n            {% set entities = entities + [{'entity': state_select,\
        \ 'name': 'Current State'}] %}\n          {% endif %}\n          {% if states[occ_sensor]\
        \ is defined %}\n            {% set entities = entities + [{'entity': occ_sensor,\
        \ 'name': 'Occupancy'}] %}\n          {% endif %}\n          {% if states[occ_source]\
        \ is defined %}\n            {% set entities = entities + [{'entity': occ_source,\
        \ 'name': 'Occupancy Sensor'}] %}\n          {% endif %}\n\n          {% if\
        \ states[idle_entity] is defined %}\n            {% set entities = entities\
        \ + [{'entity': idle_entity, 'name': 'Idle Time (sec)'}] %}\n          {%\
        \ endif %}\n          {% if states[delay_entity] is defined %}\n         \
        \   {% set entities = entities + [{'entity': delay_entity, 'name': 'Off Delay\
        \ (sec)'}] %}\n          {% endif %}\n\n          {# Bed sensor and sleep\
        \ timers only if bed sensor has a usable value #}\n          {% if states[bed_s]\
        \ is defined %}\n            {% set entities = entities + [{'entity': bed_s,\
        \ 'name': 'Bed Sensor ID'}] %}\n            {% set bed_val = states(bed_s)\
        \ | lower %}\n            {% if bed_val not in ['unknown','unavailable','','none']\
        \ %}\n              {% if states[sleep_entry] is defined %}\n            \
        \    {% set entities = entities + [{'entity': sleep_entry, 'name': 'Sleep\
        \ Entry Delay (sec)'}] %}\n              {% endif %}\n              {% if\
        \ states[sleep_exit] is defined %}\n                {% set entities = entities\
        \ + [{'entity': sleep_exit, 'name': 'Sleep Exit Delay (sec)'}] %}\n      \
        \        {% endif %}\n            {% endif %}\n          {% endif %}\n\n \
        \         {# Only add the group if it has rows (it always has at least Mode)\
        \ #}\n          {% set group = {\n            'type': 'custom:fold-entity-row',\n\
        \            'head': {'type':'section','label': name},\n            'entities':\
        \ entities\n          } %}\n          {% set ns.rows = ns.rows + [group] %}\n\
        \        {% endfor %}\n\n        {{ ns.rows | to_json }}"
    sort:
      method: none
- type: grid
  cards:
  - type: heading
    heading: New section
path: room-management
cards: []
header:
  card:
    type: markdown
    text_only: true
    content: '# Room Management Center

      '

```
