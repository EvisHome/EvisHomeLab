---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Smart Speakers

**Version:** 1.0.0  
**Description:** Configuration and helpers for managing Smart Speakers in Notification Center

<!-- START_IMAGE -->
![Package Diagram](../../assets/images/packages/smart_speakers.png)
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

* **[Notifications Management](../dashboards/notification-center/notifications_management.md)**: *The Notification Center dashboard provides a comprehensive interface for managing the smart home's notification system. Administrators can add or remove users for mobile app notifications and define notification categories (e.g., 'Garage', 'Electricity'). The view allows for granular control over subscriptions, enabling individual users to opt-in or out of specific notification types, and includes tools to map and monitor notification-related automations.* (Uses 1 entities)
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
# Package: Smart Speaker Manager
# Version: 1.0.0
# Description: Configuration and helpers for managing Smart Speakers in Notification Center
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1. HELPERS (Dashboard Inputs)
# ------------------------------------------------------------------------------
input_text:
  speaker_mgmt_name:
    name: "Speaker Name"
    icon: mdi:rename-box
    initial: "New Speaker"

input_select:
  # List of available Media Players (Auto-Populated)
  speaker_mgmt_entity:
    name: "Select Media Player"
    icon: mdi:speaker
    options:
      - "unknown"

  # List of Areas (Auto-Populated from Area Manager)
  speaker_mgmt_area:
    name: "Select Coverage Area"
    icon: mdi:map-marker
    options:
      - "unknown"

  # List of Registered Speakers (For Deletion/Management)
  speaker_mgmt_registered_list:
    name: "Registered Speakers"
    icon: mdi:speaker-multiple
    options:
      - "unknown"

# ------------------------------------------------------------------------------
# 2. SCRIPTS
# ------------------------------------------------------------------------------
script:
  # --- REGISTER SPEAKER ---
  create_smart_speaker:
    alias: "Speaker: Register Entity"
    icon: mdi:speaker-plus
    mode: single
    sequence:
      - variables:
          friendly_name: "{{ states('input_text.speaker_mgmt_name') }}"
          media_player: "{{ states('input_select.speaker_mgmt_entity') }}"
          # Slugify the friendly name for the ID
          speaker_slug: "{{ friendly_name | slugify }}"

      - service: system_log.write
        data:
          message: "DEBUG: Registering speaker {{ friendly_name }} (slug: {{ speaker_slug }})"
          level: warning

      # 1. Publish Config Entity (Text) - REMOVED
      # We now attach attributes to the Quiet Mode switch for simplicity and reliability.
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/text/speaker_{{ speaker_slug }}_config/config"
          payload: ""

      # 2. Publish DND Switch
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/switch/speaker_{{ speaker_slug }}_quiet_mode/config"
          payload: >-
            {{
              {
                "name": "Quiet Mode",
                "object_id": "speaker_" ~ speaker_slug ~ "_quiet_mode",
                "unique_id": "speaker_dnd_" ~ speaker_slug ~ "_v4",
                "icon": "mdi:volume-off",
                "command_topic": "speaker/" ~ speaker_slug ~ "/quiet/set",
                "state_topic": "speaker/" ~ speaker_slug ~ "/quiet/state",
                "payload_on": "ON",
                "payload_off": "OFF",
                "json_attributes_topic": "speaker/" ~ speaker_slug ~ "/config/attributes",
                "device": {
                  "identifiers": ["smart_speaker_" ~ speaker_slug],
                  "name": friendly_name,
                  "manufacturer": "Smart Home",
                  "model": "NotiSpeaker"
                }
              } | to_json
            }}

      # 3. Publish Notification Switches (Categories)
      # We iterate dynamic categories from the Smart Notification package
      - repeat:
          for_each: "{{ states('input_text.notify_mgmt_categories').split(',') | map('trim') | list }}"
          sequence:
            - service: mqtt.publish
              data:
                retain: true
                topic: "homeassistant/switch/speaker_{{ speaker_slug }}_notify_{{ repeat.item }}/config"
                payload: >-
                  {{
                    {
                      "name": repeat.item | title,
                      "default_entity_id": "switch.speaker_" ~ speaker_slug ~ "_notify_" ~ repeat.item,
                      "unique_id": "speaker_notif_" ~ speaker_slug ~ "_" ~ repeat.item ~ "_v4",
                      "icon": "mdi:bell-ring",
                      "command_topic": "speaker/" ~ speaker_slug ~ "/notify_" ~ repeat.item ~ "/set",
                      "state_topic": "speaker/" ~ speaker_slug ~ "/notify_" ~ repeat.item ~ "/state",
                      "payload_on": "ON",
                      "payload_off": "OFF",
                      "device": { "identifiers": ["smart_speaker_" ~ speaker_slug] }
                    } | to_json
                  }}
            # Set Default ON
            - service: mqtt.publish
              data:
                retain: true
                topic: "speaker/{{ speaker_slug }}/notify_{{ repeat.item }}/state"
                payload: "ON"

      # 4. Save Initial State & Attributes
      - service: mqtt.publish
        data:
          retain: true
          topic: "speaker/{{ speaker_slug }}/config/state"
          payload: "{{ media_player }}"

      - service: mqtt.publish
        data:
          retain: true
          topic: "speaker/{{ speaker_slug }}/config/attributes"
          payload: >-
            {{
              {
                "entity_id": media_player,
                "speaker_slug": speaker_slug,
                "linked_areas": []
              } | to_json
            }}

      - if:
          - condition: template
            value_template: "{{ states('input_select.speaker_mgmt_area') not in ['unknown', 'unavailable'] }}"
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "speaker/{{ speaker_slug }}/config/attributes"
              payload: >-
                {{
                  {
                    "entity_id": media_player,
                    "speaker_slug": speaker_slug,
                    "linked_areas": [states('input_select.speaker_mgmt_area')]
                  } | to_json
                }}

      - service: mqtt.publish
        data:
          retain: true
          topic: "speaker/{{ speaker_slug }}/quiet/state"
          payload: "OFF"

      - delay: "00:00:01"
      - service: script.refresh_speaker_list

  # --- REFRESH LISTS ---
  refresh_speaker_list:
    alias: "Speaker: Refresh Lists"
    mode: single
    sequence:
      # 1. Populate Media Players
      - service: input_select.set_options
        target:
          entity_id: input_select.speaker_mgmt_entity
        data:
          options: >-
            {{ (states.media_player | map(attribute='entity_id') | list | sort) or ['unknown'] }}

      # 2. Populate Areas (Safe fetch from Area Manager selects)
      - variables:
          areas: >-
            {{ states.select 
               | selectattr('entity_id', 'match', 'select\.area_.*_state') 
               | map(attribute='entity_id') 
               | map('regex_replace', 'select\.area_(.*)_state', '\\1') 
               | list | sort }}
      - service: input_select.set_options
        target:
          entity_id: input_select.speaker_mgmt_area
        data:
          options: "{{ areas or ['unknown'] }}"

      # 3. Populate Registered Speakers
      - variables:
          # Find all switches that have a 'speaker_slug' attribute (Robust finding)
          speakers: >-
            {{ states.switch 
               | selectattr('attributes.speaker_slug', 'defined') 
               | map(attribute='attributes.speaker_slug') 
               | list | sort }}
      - service: input_select.set_options
        target:
          entity_id: input_select.speaker_mgmt_registered_list
        data:
          options: "{{ speakers or ['unknown'] }}"

  # --- DELETE SPEAKER ---
  delete_smart_speaker:
    alias: "Speaker: Delete Entity"
    mode: single
    sequence:
      - variables:
          # Expects input from speaker_mgmt_registered_list or similar
          # For now, let's assume we pass a slug or get it from a select
          # FIX: Prioritize passed variable, fallback to input_select
          target_slug: "{{ speaker_slug if speaker_slug is defined else states('input_select.speaker_mgmt_registered_list') }}"
          # Re-assign to ensure downstream usage is consistent
          speaker_slug: "{{ target_slug }}"

      # Remove Config
      - service: mqtt.publish
        data:
          topic: "homeassistant/text/speaker_{{ speaker_slug }}_config/config"
          payload: ""

      # Remove Quiet Mode
      - service: mqtt.publish
        data:
          topic: "homeassistant/switch/speaker_{{ speaker_slug }}_quiet_mode/config"
          payload: ""

      # Remove Categories
      - repeat:
          for_each: ["info", "alarm", "doorbell", "security", "system"]
          sequence:
            - service: mqtt.publish
              data:
                topic: "homeassistant/switch/speaker_{{ speaker_slug }}_notify_{{ repeat.item }}/config"
                payload: ""
            # Legacy cleanup (Remove old schema too)
            - service: mqtt.publish
              data:
                topic: "homeassistant/switch/notify_speaker_{{ speaker_slug }}_{{ repeat.item }}/config"
                payload: ""

  # --- MANAGE COVERAGE: ADD AREA ---
  speaker_add_area:
    alias: "Speaker: Add Coverage Area"
    mode: single
    sequence:
      - variables:
          # Inputs: Speaker Slug, and Area Slug to ADD
          speaker_slug: "{{ states('input_select.speaker_mgmt_registered_list') }}"
          area_to_add: "{{ states('input_select.speaker_mgmt_area') }}"

      - if:
          - condition: template
            value_template: >-
              {{ speaker_slug not in ['unknown', 'unavailable', '', none] 
                 and area_to_add not in ['unknown', 'unavailable', '', none] }}
        then:
          # Get Current Config (from Quiet Mode Switch)
          # Use default([], true) to handle None if attribute is missing
          - variables:
              current_areas: "{{ state_attr('switch.speaker_' ~ speaker_slug ~ '_quiet_mode', 'linked_areas') | default([], true) }}"
              entity_id: "{{ state_attr('switch.speaker_' ~ speaker_slug ~ '_quiet_mode', 'entity_id') }}"

          - if:
              - condition: template
                value_template: "{{ area_to_add not in current_areas }}"
            then:
              - variables:
                  new_areas: "{{ (current_areas + [area_to_add]) | unique | list }}"
              - service: mqtt.publish
                data:
                  retain: true
                  topic: "speaker/{{ speaker_slug }}/config/attributes"
                  payload: >-
                    {
                      "entity_id": "{{ entity_id }}",
                      "speaker_slug": "{{ speaker_slug }}",
                      "linked_areas": {{ new_areas | to_json }}
                    }
        else:
          - service: system_log.write
            data:
              message: "Speaker Add Area Failed: Invalid Input"
              level: warning

  # --- SYSTEM: PURGE ALL SPEAKERS (Cleanup Tool) ---
  purge_all_speakers:
    alias: "System: Purge All Speakers"
    icon: mdi:nuke
    mode: single
    sequence:
      - variables:
          # 1. Gather slugs from Switch attributes (New System)
          slugs_from_switches: >-
            {{ states.switch 
               | selectattr('attributes.speaker_slug', 'defined')
               | map(attribute='attributes.speaker_slug')
               | list }}
          # 2. Gather slugs from Input Select (Old System/Lists)
          slugs_from_list: >-
            {{ state_attr('input_select.speaker_mgmt_registered_list', 'options') 
               | reject('eq', 'unknown') 
               | list }}
          # 3. Combine and Unique
          all_slugs: "{{ (slugs_from_switches + slugs_from_list) | unique | list }}"

      - if:
          - condition: template
            value_template: "{{ all_slugs | length > 0 }}"
        then:
          - service: system_log.write
            data:
              message: "Purging Speakers: {{ all_slugs }}"
              level: warning
          - repeat:
              for_each: "{{ all_slugs }}"
              sequence:
                - service: script.delete_smart_speaker
                  data:
                    speaker_slug: "{{ repeat.item }}"
                - delay: "00:00:00.500"
        else:
          - service: system_log.write
            data:
              message: "No speakers found to purge."
              level: info

  # --- MANAGE COVERAGE: REMOVE AREA ---
  speaker_remove_area:
    alias: "Speaker: Remove Coverage Area"
    mode: single
    sequence:
      - variables:
          speaker_slug: "{{ states('input_select.speaker_mgmt_registered_list') }}"
          # For removal, we might want to select FROM the speaker's room list?
          # Or just use the global area selector to pick which one to remove.
          # Let's use the global area selector for simplicity, or complex UI logic later.
          area_to_remove: "{{ states('input_select.speaker_mgmt_area') }}"

      - if:
          - condition: template
            value_template: >-
              {{ speaker_slug not in ['unknown', 'unavailable', '', none] 
                 and area_to_remove not in ['unknown', 'unavailable', '', none] }}
        then:
          - variables:
              current_areas: "{{ state_attr('switch.speaker_' ~ speaker_slug ~ '_quiet_mode', 'linked_areas') | default([], true) }}"
              entity_id: "{{ state_attr('switch.speaker_' ~ speaker_slug ~ '_quiet_mode', 'entity_id') }}"

          - if:
              - condition: template
                # Ensure current_areas is iterable
                value_template: "{{ area_to_remove in current_areas }}"
            then:
              - variables:
                  new_areas: "{{ current_areas | reject('eq', area_to_remove) | list }}"
              - service: mqtt.publish
                data:
                  retain: true
                  topic: "speaker/{{ speaker_slug }}/config/attributes"
                  payload: >-
                    {
                      "entity_id": "{{ entity_id }}",
                      "speaker_slug": "{{ speaker_slug }}",
                      "linked_areas": {{ new_areas | to_json }}
                    }
        else:
          - service: system_log.write
            data:
              message: "Speaker Remove Area Failed: Invalid Input"
              level: warning

# ------------------------------------------------------------------------------
# 3. AUTOMATIONS
# ------------------------------------------------------------------------------
automation:
  # Keeps the MQTT Switches in sync (State Persistence)
  - alias: "Speaker: MQTT Persistence"
    id: speaker_mqtt_persistence
    mode: parallel
    trigger:
      - platform: mqtt
        topic: "speaker/#"
    condition:
      - condition: template
        value_template: "{{ trigger.topic.endswith('/set') }}"
    action:
      - service: mqtt.publish
        data:
          topic: "{{ trigger.topic[:-4] }}/state"
          payload: "{{ trigger.payload }}"
          retain: true

  - alias: "Speaker: Auto Populate Lists"
    id: speaker_auto_populate_lists
    trigger:
      - platform: homeassistant
        event: start
      - platform: time_pattern
        hours: "/1"
    action:
      - delay: "00:00:30"
      - service: script.refresh_speaker_list

```
