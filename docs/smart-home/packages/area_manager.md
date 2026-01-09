---
tags:
  - package
  - automated
version: 2.0.0 (Refactored from Room Manager)
---

# Package: Area Manager

**Version:** 2.0.0 (Refactored from Room Manager)  
**Description:** Dynamic creation of AREA settings via MQTT (Replaces Room Manager)

<!-- START_IMAGE -->
![Package Diagram](../../assets/images/packages/area_manager.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Living Room](../dashboards/main/living_room.md)**: *The Living Room dashboard is a media and comfort hub. It features in-depth environmental monitoring (Radon, VOCs, CO2) via Airthings Wave, displaying historical trends. Entertainment controls are central, with remotes for the TV and Soundbar, plus power management for the media wall. The view also includes specific controls for the fireplace, air purifier modes, and various lighting scenes, alongside standard occupancy settings.* (Uses 1 entities)
* **[Notifications Management](../dashboards/notification-center/notifications_management.md)**: *The Notification Center dashboard provides a comprehensive interface for managing the smart home's notification system. Administrators can add or remove users for mobile app notifications and define notification categories (e.g., 'Garage', 'Electricity'). The view allows for granular control over subscriptions, enabling individual users to opt-in or out of specific notification types, and includes tools to map and monitor notification-related automations.* (Uses 1 entities)
* **[Room Management](../dashboards/room-management/room_management.md)**: *The Room Management dashboard serves as the administrative backend for the home's room logic. It allows users to initialize new rooms (creating necessary helper entities) or delete existing ones. It features a dynamic "Configured Rooms" section powered by `auto-entities`, which automatically lists all configured rooms and provides collapsible controls for their automation modes, occupancy sensors, and timeouts.* (Uses 1 entities)
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# Package: Area Automation Manager
# Version: 2.0.0 (Refactored from Room Manager)
# Description: Dynamic creation of AREA settings via MQTT (Replaces Room Manager)
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1. GLOBAL CUSTOMIZATION (Force Text Boxes)
# ------------------------------------------------------------------------------
homeassistant:
  customize_glob:
    "number.area_*_presence_idle_time":
      mode: box
    "number.area_*_lights_presence_delay":
      mode: box
    "number.area_*_sleep_entry_delay":
      mode: box
    "number.area_*_sleep_exit_delay":
      mode: box

# ------------------------------------------------------------------------------
# 2. HELPERS (Dashboard Inputs)
# ------------------------------------------------------------------------------
input_text:
  area_mgmt_name:
    name: "Area Name"
    icon: mdi:door-open
  area_mgmt_slug:
    name: "Area ID (slug)"
    icon: mdi:identifier

input_select:
  # SOURCE: Native Home Assistant Areas
  area_mgmt_create_select:
    name: "Select Area to Initialize"
    icon: mdi:map-plus
    options:
      - "unknown"

  # SOURCE: Existing Created Areas
  area_mgmt_delete_select:
    name: "Select Area to Delete"
    icon: mdi:delete-sweep
    options:
      - "unknown"

# ------------------------------------------------------------------------------
# 3. SCRIPTS
# ------------------------------------------------------------------------------
script:
  # --- REFRESH AREA OPTIONS ---
  refresh_area_options:
    alias: "System: Refresh Area Options"
    mode: single
    sequence:
      - service: automation.trigger
        target:
          entity_id: automation.system_populate_area_list

  # --- CREATE AREA SETTINGS ---
  create_area_settings:
    alias: "System: Create Area Settings"
    icon: mdi:home-plus
    mode: single
    sequence:
      - variables:
          target_slug: "{{ area_slug if area_slug is defined else states('input_select.area_mgmt_create_select') }}"
          area_name: "{{ area_name(target_slug) or target_slug | replace('_', ' ') | title }}"
          # Clean variable
          area_slug: "{{ target_slug }}"
          # Pre-calculate Sensor Options (DEBUG: Minimal List to test Pipeline)
          sensor_options: >-
            {{ ['-Select-'] | to_json }}

      - service: system_log.write
        data:
          message: "Creating Area Settings for: {{ area_slug }} (v5 - Minimal)"
          level: warning

      # 1. Create Automation Mode Selector (Select)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_mode/config"
          payload: >-
            {
              "name": "{{ area_name }} Automation Mode",
              "object_id": "area_{{ area_slug }}_automation_mode",
              "unique_id": "area_select_{{ area_slug }}_mode_v5",
              "icon": "mdi:home-lightning-bolt-outline",
              "options": ["presence-control", "absence-detection", "manual-control", "schedule-mode"],
              "command_topic": "area/{{ area_slug }}/mode/set",
              "state_topic": "area/{{ area_slug }}/mode/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "payload_available": "online",
              "device": {
                "identifiers": ["area_settings_{{ area_slug }}"],
                "name": "{{ area_name }} Settings",
                "manufacturer": "Home Assistant",
                "model": "Area Controller"
              }
            }
      # Set default
      - if:
          - condition: template
            value_template: "{{ states('select.area_' ~ area_slug ~ '_automation_mode') in ['unknown', 'unavailable', 'none'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "area/{{ area_slug }}/mode/state"
              payload: "presence-control"
      - delay: "00:00:00.050"

      # 2. Create Idle Time (Number)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_idle/config"
          payload: >-
            {
              "name": "{{ area_name }} Presence Idle Time",
              "object_id": "area_{{ area_slug }}_presence_idle_time",
              "unique_id": "area_number_{{ area_slug }}_idle_v5",
              "device_class": "duration",
              "icon": "mdi:timer-sand",
              "min": 0,
              "max": 3600,
              "step": 1,
              "unit_of_measurement": "s",
              "command_topic": "area/{{ area_slug }}/idle/set",
              "state_topic": "area/{{ area_slug }}/idle/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - if:
          - condition: template
            value_template: "{{ states('number.area_' ~ area_slug ~ '_presence_idle_time') in ['unknown', 'unavailable', 'none'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "area/{{ area_slug }}/idle/state"
              payload: "15"
      - delay: "00:00:00.050"

      # 3. Create Delay Time (Number)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_delay/config"
          payload: >-
            {
              "name": "{{ area_name }} Lights Presence Delay",
              "object_id": "area_{{ area_slug }}_lights_presence_delay",
              "unique_id": "area_number_{{ area_slug }}_delay_v5",
              "device_class": "duration",
              "icon": "mdi:lightbulb-clock",
              "min": 0,
              "max": 3600,
              "step": 1,
              "unit_of_measurement": "s",
              "command_topic": "area/{{ area_slug }}/delay/set",
              "state_topic": "area/{{ area_slug }}/delay/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - if:
          - condition: template
            value_template: "{{ states('number.area_' ~ area_slug ~ '_lights_presence_delay') in ['unknown', 'unavailable', 'none'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "area/{{ area_slug }}/delay/state"
              payload: "120"
      - delay: "00:00:00.050"

      # 4. Create Timer Display (Timestamp Sensor)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/sensor/area_{{ area_slug }}_timer/config"
          payload: >-
            {
              "name": "{{ area_name }} Timer",
              "object_id": "area_{{ area_slug }}_timer",
              "unique_id": "area_sensor_{{ area_slug }}_timer_v5",
              "icon": "mdi:progress-clock",
              "device_class": "timestamp",
              "value_template": "{{ '{{' }} value if value not in ['unknown', 'unavailable', ''] else None {{ '}}' }}",
              "state_topic": "area/{{ area_slug }}/timer/state",
              "json_attributes_topic": "area/{{ area_slug }}/timer/attributes",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - delay: "00:00:00.050"
      # 5. Create Area State (Select)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_state/config"
          payload: >-
            {
              "name": "{{ area_name }} State",
              "object_id": "area_{{ area_slug }}_state",
              "unique_id": "area_select_state_v5_{{ area_slug }}",
              "icon": "mdi:eye-outline",
              "options": ["Occupied", "Idle", "Absence", "Sleep", "DND"],
              "command_topic": "area/{{ area_slug }}/state/set",
              "state_topic": "area/{{ area_slug }}/state/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "payload_available": "online",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - service: mqtt.publish
        data:
          retain: true
          topic: "area/{{ area_slug }}/state/state"
          payload: "Absence"
      - delay: "00:00:00.050"

      # 6. Create Occupancy (Binary Sensor)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/binary_sensor/area_{{ area_slug }}_occupancy/config"
          payload: >-
            {
              "name": "{{ area_name }} Occupancy",
              "object_id": "area_{{ area_slug }}_occupancy",
              "unique_id": "area_occupancy_v5_{{ area_slug }}",
              "icon": "mdi:motion-sensor",
              "device_class": "occupancy",
              "state_topic": "area/{{ area_slug }}/occupancy/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - delay: "00:00:00.050"
      # 7. Create Automation Switch
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/switch/area_{{ area_slug }}_automation/config"
          payload: >-
            {
              "name": "{{ area_name }} Automation",
              "object_id": "area_{{ area_slug }}_automation",
              "unique_id": "area_switch_automation_v5_{{ area_slug }}",
              "icon": "mdi:robot",
              "command_topic": "area/{{ area_slug }}/automation/set",
              "state_topic": "area/{{ area_slug }}/automation/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - service: mqtt.publish
        data:
          retain: true
          topic: "area/{{ area_slug }}/automation/state"
          payload: "ON"
      - delay: "00:00:00.050"

      # 8. Create Bed Sensor (Select)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_bed_sensor/config"
          payload: >-
            {
              "name": "{{ area_name }} Bed Sensor",
              "object_id": "area_{{ area_slug }}_bed_sensor",
              "unique_id": "area_select_bed_{{ area_slug }}_v5",
              "options": {{ sensor_options }},
              "command_topic": "area/{{ area_slug }}/bed_sensor/set",
              "state_topic": "area/{{ area_slug }}/bed_sensor/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - delay: "00:00:00.050"
      # 9. Create Sleep ENTRY Delay (Number)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_sleep_entry_delay/config"
          payload: >-
            {
              "name": "{{ area_name }} Sleep Entry Delay",
              "object_id": "area_{{ area_slug }}_sleep_entry_delay",
              "unique_id": "area_number_{{ area_slug }}_sleep_entry_v5",
              "device_class": "duration",
              "icon": "mdi:bed-clock",
              "min": 0,
              "max": 3600,
              "step": 1,
              "unit_of_measurement": "s",
              "command_topic": "area/{{ area_slug }}/sleep_entry_delay/set",
              "state_topic": "area/{{ area_slug }}/sleep_entry_delay/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - if:
          - condition: template
            value_template: "{{ states('number.area_' ~ area_slug ~ '_sleep_entry_delay') in ['unknown', 'unavailable', 'none'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "area/{{ area_slug }}/sleep_entry_delay/state"
              payload: "300"
      - delay: "00:00:00.050"

      # 10. Create Sleep EXIT Delay (Number)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_sleep_exit_delay/config"
          payload: >-
            {
              "name": "{{ area_name }} Sleep Exit Delay",
              "object_id": "area_{{ area_slug }}_sleep_exit_delay",
              "unique_id": "area_number_{{ area_slug }}_sleep_exit_v5",
              "device_class": "duration",
              "icon": "mdi:run-fast",
              "min": 0,
              "max": 3600,
              "step": 1,
              "unit_of_measurement": "s",
              "command_topic": "area/{{ area_slug }}/sleep_exit_delay/set",
              "state_topic": "area/{{ area_slug }}/sleep_exit_delay/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - if:
          - condition: template
            value_template: "{{ states('number.area_' ~ area_slug ~ '_sleep_exit_delay') in ['unknown', 'unavailable', 'none'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "area/{{ area_slug }}/sleep_exit_delay/state"
              payload: "60"
      - delay: "00:00:00.050"

      # 11. Set Online
      - service: mqtt.publish
        data:
          retain: true
          topic: "area/{{ area_slug }}/availability"
          payload: "online"

      # 12. Create Occupancy Source (Select)
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_occupancy_source/config"
          payload: >-
            {
              "name": "{{ area_name }} Occupancy Sensor",
              "object_id": "area_{{ area_slug }}_occupancy_source",
              "unique_id": "area_select_occ_source_v5_{{ area_slug }}",
              "options": {{ sensor_options }},
              "command_topic": "area/{{ area_slug }}/occupancy_source/set",
              "state_topic": "area/{{ area_slug }}/occupancy_source/state",
              "availability_topic": "area/{{ area_slug }}/availability",
              "device": { "identifiers": ["area_settings_{{ area_slug }}"] }
            }
      - delay: "00:00:00.050"
      - service: script.refresh_area_options

  # --- DELETE AREA SETTINGS ---
  delete_area_settings:
    alias: "System: Delete Area Settings"
    icon: mdi:home-remove
    mode: single
    sequence:
      - variables:
          raw_slug: "{{ states('input_select.area_mgmt_delete_select') }}"
          # SAFETY: If slug starts with 'area_', strip it
          area_slug: "{{ raw_slug | replace('area_', '') if raw_slug.startswith('area_') else raw_slug }}"

      # Clear Config Topics
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_mode/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_idle/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_delay/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/sensor/area_{{ area_slug }}_timer/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_state/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/binary_sensor/area_{{ area_slug }}_occupancy/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/switch/area_{{ area_slug }}_automation/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_bed_sensor/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_sleep_entry_delay/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/number/area_{{ area_slug }}_sleep_exit_delay/config"
          payload: ""
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/area_{{ area_slug }}_occupancy_source/config"
          payload: ""

      # Delete Availability to 'offline'
      - service: mqtt.publish
        data:
          retain: true
          topic: "area/{{ area_slug }}/availability"
          payload: ""
      - service: script.refresh_area_options

# ------------------------------------------------------------------------------
# 4. AUTOMATIONS
# ------------------------------------------------------------------------------
automation:
  # POPULATE DROPDOWNS ("Manage Areas")
  - alias: "System: Populate Area List"
    id: system_populate_area_list
    trigger:
      - platform: homeassistant
        event: start
      - platform: time_pattern
        hours: "/1"
    action:
      # 1. Populate 'Create' from HA Areas
      - service: input_select.set_options
        target:
          entity_id: input_select.area_mgmt_create_select
        data:
          options: >-
            {% set areas = areas() | sort %}
            {{ areas if areas else ['unknown'] }}

      # 2. Populate 'Delete' from created 'area_*_automation_mode' entities
      - service: input_select.set_options
        target:
          entity_id: input_select.area_mgmt_delete_select
        data:
          options: >-
            {% set mode_selectors = states.select | selectattr('object_id', 'search', '_automation_mode$') | list %}
            {% set ns = namespace(areas=[]) %}
            {% for sel in mode_selectors %}
               {% set raw_id = sel.entity_id.split('.')[1] %}
               {% set base = raw_id | replace('_automation_mode', '') %}
               {% if base.startswith('area_') %}
                  {% set slug = base[5:] %}
               {% else %}
                  {% set slug = base %}
               {% endif %}
               {% set ns.areas = ns.areas + [slug] %}
            {% endfor %}
            {{ ns.areas | unique | list if ns.areas else ['unknown'] }}

            # END OF POPULATION

  # MQTT PERSISTENCE
  - alias: "System: Area MQTT Persistence"
    id: system_area_mqtt_persistence
    mode: queued
    trigger:
      - platform: mqtt
        topic: "area/+/+/set"
      - platform: mqtt
        topic: "area/+/+/+/set"
    action:
      - variables:
          target_topic: "{{ trigger.topic | replace('/set', '/state') }}"
      - service: mqtt.publish
        data:
          topic: "{{ target_topic }}"
          payload: "{{ trigger.payload }}"
          retain: true

```
