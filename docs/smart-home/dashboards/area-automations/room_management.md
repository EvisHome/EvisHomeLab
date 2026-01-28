---
tags:
  - dashboard
  - view
  - automated
---

# Room Management

**Dashboard:** Area Automations  
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
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`


## Configuration
```yaml
title: Room Management
icon: ''
type: sections
max_columns: 3
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
    heading: Configured Rooms
    icon: mdi:view-dashboard-outline
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

```
