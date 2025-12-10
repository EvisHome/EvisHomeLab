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
    content: |-
      **Instructions:**

      1. Select a **Native Area** from the list.
      2. Click **Initialize** to create helpers for it.

      *Uses Home Assistant Areas as the source.*
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
      style: |-
        ha-card {
          border: none;
          background: var(--green-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
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
      style: |-
        ha-card {
          border: none;
          background: var(--red-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black; /* Icon visibility fix */
        }
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
      template: |-
        {% set ns = namespace(rows=[]) %} {% set mode_selectors = states.select | selectattr('entity_id','search','automation_mode') | list %}
        {% for sel in mode_selectors %}
          {# Extract base id and normalize to room_key #}
          {% set raw_id = sel.entity_id.split('.')[1] %}
          {% set base = raw_id.replace('_automation_mode','') %}
          {% if base.startswith('room_') %}
            {% set room_key = base[5:] %}
          {% else %}
            {% set room_key = base %}
          {% endif %}
          {% set name = room_key.replace('_',' ') | title %}

          {# Compose downstream entity ids with exactly one room_ prefix #}
          {% set state_select = 'select.room_' ~ room_key ~ '_state' %}
          {% set occ_sensor   = 'binary_sensor.room_' ~ room_key ~ '_occupancy' %}
          {% set idle_entity  = 'number.room_' ~ room_key ~ '_presence_idle_time' %}
          {% set delay_entity = 'number.room_' ~ room_key ~ '_lights_presence_delay' %}
          {% set lux_s        = 'text.room_' ~ room_key ~ '_lux_sensor' %}
          {% set lux_t        = 'number.room_' ~ room_key ~ '_lux_threshold' %}
          {% set bed_s        = 'text.room_' ~ room_key ~ '_bed_sensor' %}
          {% set sleep_entry  = 'number.room_' ~ room_key ~ '_sleep_entry_delay' %}
          {% set sleep_exit   = 'number.room_' ~ room_key ~ '_sleep_exit_delay' %}

          {# Build the collapsible group's entity list, conditionally #}
          {% set entities = [] %}
          {% set entities = entities + [{'entity': sel.entity_id, 'name': 'Mode'}] %}

          {% if states[state_select] is defined %}
            {% set entities = entities + [{'entity': state_select, 'name': 'Current State'}] %}
          {% endif %}
          {% if states[occ_sensor] is defined %}
            {% set entities = entities + [{'entity': occ_sensor, 'name': 'Occupancy'}] %}
          {% endif %}
          {% if states[idle_entity] is defined %}
            {% set entities = entities + [{'entity': idle_entity, 'name': 'Idle Time (sec)'}] %}
          {% endif %}
          {% if states[delay_entity] is defined %}
            {% set entities = entities + [{'entity': delay_entity, 'name': 'Off Delay (sec)'}] %}
          {% endif %}
          {% if states[lux_s] is defined %}
            {% set entities = entities + [{'entity': lux_s, 'name': 'Lux Sensor ID'}] %}
          {% endif %}
          {% if states[lux_t] is defined %}
            {% set entities = entities + [{'entity': lux_t, 'name': 'Lux Threshold (lx)'}] %}
          {% endif %}

          {# Bed sensor and sleep timers only if bed sensor has a usable value #}
          {% if states[bed_s] is defined %}
            {% set entities = entities + [{'entity': bed_s, 'name': 'Bed Sensor ID'}] %}
            {% set bed_val = states(bed_s) | lower %}
            {% if bed_val not in ['unknown','unavailable','','none'] %}
              {% if states[sleep_entry] is defined %}
                {% set entities = entities + [{'entity': sleep_entry, 'name': 'Sleep Entry Delay (sec)'}] %}
              {% endif %}
              {% if states[sleep_exit] is defined %}
                {% set entities = entities + [{'entity': sleep_exit, 'name': 'Sleep Exit Delay (sec)'}] %}
              {% endif %}
            {% endif %}
          {% endif %}

          {# Only add the group if it has rows (it always has at least Mode) #}
          {% set group = {
            'type': 'custom:fold-entity-row',
            'head': {'type':'section','label': name},
            'entities': entities
          } %}
          {% set ns.rows = ns.rows + [group] %}
        {% endfor %}
        {{ ns.rows | to_json }}
    sort:
      method: none
- type: grid
  cards:
  - type: heading
    heading: Configured Rooms
    icon: mdi:view-dashboard-outline
    heading_style: title
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      show_header_toggle: false
    filter:
      template: |-
        {% set ns = namespace(cards=[]) %}
        {# Broader search for any select entity with 'automation_mode' in the ID #}
        {% set mode_selectors = states.select | selectattr('entity_id', 'search', 'automation_mode') | list %}

        {% for sel in mode_selectors %}
          {# Extract slug. Handles "select.bathroom_automation_mode" or "select.room_bathroom_automation_mode" #}
        {% set raw_id = sel.entity_id.split('.')[1] %}
        {% if raw_id.startswith('room_') %}
           {% set slug = raw_id[5:] | replace('_automation_mode','') %}
        {% else %}
           {% set slug = raw_id.replace('_automation_mode','') %}
        {% endif %}


          {# UPDATED: Generate Name purely from Slug (Cleaner) #}
          {% set name = slug.replace('_', ' ') | title %}

          {# --- Header --- #}
          {% set ns.cards = ns.cards + [{'type': 'section', 'label': name}] %}

          {# --- Controls --- #}

          {# Mode Selector #}
          {% set ns.cards = ns.cards + [{'entity': sel.entity_id, 'name': 'Mode'}] %}

          {# Room State #}
          {% set state_select = 'select.room_' ~ slug ~ '_state' %}
          {% if states[state_select] is defined %}
            {% set ns.cards = ns.cards + [{'entity': state_select, 'name': 'Current State'}] %}
          {% endif %}

          {# Occupancy #}
          {% set occ_sensor = 'binary_sensor.room_' ~ slug ~ '_occupancy' %}
          {% if states[occ_sensor] is defined %}
            {% set ns.cards = ns.cards + [{'entity': occ_sensor, 'name': 'Occupancy'}] %}
          {% endif %}

          {# Idle Time #}
          {% set idle_entity = 'number.room_' ~ slug ~ '_presence_idle_time' %}
          {% if states[idle_entity] is defined %}
            {% set ns.cards = ns.cards + [{'entity': idle_entity, 'name': 'Idle Time (sec)'}] %}
          {% endif %}

          {# Off Delay #}
          {% set delay_entity = 'number.room_' ~ slug ~ '_lights_presence_delay' %}
          {% if states[delay_entity] is defined %}
            {% set ns.cards = ns.cards + [{'entity': delay_entity, 'name': 'Off Delay (sec)'}] %}
          {% endif %}

          {# Lux Sensor #}
          {% set lux_s = 'text.room_' ~ slug ~ '_lux_sensor' %}
          {% if states[lux_s] is defined %}
            {% set ns.cards = ns.cards + [{'entity': lux_s, 'name': 'Lux Sensor ID'}] %}
          {% endif %}

          {# Lux Threshold #}
          {% set lux_t = 'number.room_' ~ slug ~ '_lux_threshold' %}
          {% if states[lux_t] is defined %}
             {% set ns.cards = ns.cards + [{'entity': lux_t, 'name': 'Lux Threshold (lx)'}] %}
          {% endif %}

          {# Bed Sensor #}
          {% set bed_s = 'text.room_' ~ slug ~ '_bed_sensor' %}
          {% if states[bed_s] is defined %}
            {% set ns.cards = ns.cards + [{'entity': bed_s, 'name': 'Bed Sensor ID'}] %}

            {# Only show sleep timers if a bed sensor ID is entered #}
            {% if states(bed_s) not in ['unknown', 'unavailable', '', 'none'] %}
               {% set sleep_entry = 'number.room_' ~ slug ~ '_sleep_entry_delay' %}
               {% if states[sleep_entry] is defined %}
                 {% set ns.cards = ns.cards + [{'entity': sleep_entry, 'name': 'Sleep Entry Delay (sec)'}] %}
               {% endif %}

               {% set sleep_exit = 'number.room_' ~ slug ~ '_sleep_exit_delay' %}
               {% if states[sleep_exit] is defined %}
                 {% set ns.cards = ns.cards + [{'entity': sleep_exit, 'name': 'Sleep Exit Delay (sec)'}] %}
               {% endif %}
            {% endif %}
          {% endif %}

        {% endfor %}
        {{ ns.cards | to_json }}
    sort:
      method: none

```
