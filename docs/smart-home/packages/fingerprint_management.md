---
tags:
  - package
  - automated
version: 2.5.1 (Variable Scope Fix & Debug)
---

# Package: Fingerprint Management

**Version:** 2.5.1 (Variable Scope Fix & Debug)  
**Description:** Fixed variable scoping issue prevents switches from being created.

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/fingerprint_management.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v2.5.1 (Variable Scope Fix & Debug).

*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v2.5.1 (Variable Scope Fix & Debug).

*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v2.5.1 (Variable Scope Fix & Debug).

*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v2.5.1 (Variable Scope Fix & Debug).

*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Fingerprint Access Control
# Version: 2.5.1 (Variable Scope Fix & Debug)
# Description: Fixed variable scoping issue prevents switches from being created.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1. HELPERS & SCHEDULES
# ------------------------------------------------------------------------------
input_select:
  fingerprint_delete_id:
    name: "Select ID to Delete"
    icon: mdi:delete-empty
    options: ["-select-"]

# SCHEDULES (Guest Only)
input_datetime:
  fp_guest_start:
    name: "Guest Start Time"
    has_date: false
    has_time: true
    icon: mdi:clock-start
    initial: "09:00"
  fp_guest_end:
    name: "Guest End Time"
    has_date: false
    has_time: true
    icon: mdi:clock-end
    initial: "21:00"

input_boolean:
  fp_guest_mon:
    name: "Mon"
    icon: mdi:calendar
  fp_guest_tue:
    name: "Tue"
    icon: mdi:calendar
  fp_guest_wed:
    name: "Wed"
    icon: mdi:calendar
  fp_guest_thu:
    name: "Thu"
    icon: mdi:calendar
  fp_guest_fri:
    name: "Fri"
    icon: mdi:calendar
  fp_guest_sat:
    name: "Sat"
    icon: mdi:calendar
  fp_guest_sun:
    name: "Sun"
    icon: mdi:calendar

# ------------------------------------------------------------------------------
# 2. AUTOMATIONS
# ------------------------------------------------------------------------------
automation:
  # --- ACCESS CONTROL LOGIC ---
  - alias: "Access: Fingerprint Entry Logic"
    id: access_fingerprint_entry_logic
    mode: single
    trigger:
      - event_type: state_changed
        event_data:
          entity_id: event.front_door_fingerprint
        trigger: event
    variables:
      raw_id: >-
        {{ trigger.event.data.new_state.attributes.ulp_id | default('unknown') }}
      slug_id: "{{ raw_id | replace('-', '_') | lower }}"
      assigned_user: "{{ states('select.fingerprint_' ~ slug_id) }}"
      # DYNAMIC SWITCH LOOKUP
      user_switch: "switch.fp_access_{{ assigned_user | slugify }}"
    action:
      - target:
          entity_id: camera.g4_doorbell_pro_poe_high_resolution_channel
        data:
          filename: /config/www/front_door_unlock_snapshot.jpg
        action: camera.snapshot
      
      - delay: "00:00:02"

      - choose:
          # ROLE 1: GUEST
          - conditions:
              - condition: template
                value_template: "{{ assigned_user == 'Guest' }}"
            sequence:
              - if:
                  - condition: template
                    value_template: >
                      {# 1. Check Dynamic Kill Switch #}
                      {% set access_enabled = states(user_switch) != 'off' %}
                      
                      {# 2. Check Schedule #}
                      {% set current_day = now().strftime('%a')|lower %}
                      {% set is_day_allowed = is_state('input_boolean.fp_guest_' ~ current_day, 'on') %}
                      {% set current_time = now().strftime('%H:%M:%S') %}
                      {% set start_time = states('input_datetime.fp_guest_start') %}
                      {% set end_time = states('input_datetime.fp_guest_end') %}
                      {% set is_time_allowed = (current_time >= start_time) and (current_time <= end_time) %}

                      {{ access_enabled and is_day_allowed and is_time_allowed }}
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Guest Entry
                      message: "Guest entered during authorized schedule."
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: ⛔ Access Denied
                      message: >
                        {% if states(user_switch) == 'off' %}
                          Guest access is manually DISABLED.
                        {% else %}
                          Guest tried to enter outside allowed schedule.
                        {% endif %}
                      critical: true
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock_denied

          # ROLE 2: STANDARD USER
          - conditions:
              - condition: template
                value_template: >
                  {{ assigned_user not in ['unknown', 'unavailable', 'none', 'Unknown', '-Unassigned-', '-unassigned-'] }}
            sequence:
              - if:
                  - condition: template
                    value_template: "{{ states(user_switch) != 'off' }}"
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Front Door Unlocked
                      message: "Unlocked by: {{ assigned_user }}"
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: ⛔ Access Disabled
                      message: "Fingerprint valid, but {{ assigned_user }}'s access is switched OFF."
                      critical: true
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock_denied

          # ROLE 3: AUTO-LEARN
          - conditions:
              - condition: template
                value_template: "{{ raw_id != 'unknown' and raw_id != '' }}"
            sequence:
              - action: script.add_fingerprint_entity
                data:
                  ulp_id: "{{ raw_id }}"
                  current_user: Unknown
              - action: script.notify_smart_master
                data:
                  category: system
                  title: 🖐️ New Fingerprint Detected
                  message: |-
                    ID: {{ raw_id }}
                    Added to Access Dashboard as 'Unknown'. Please assign a user.
                  image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                  tag: door_lock_unknown
                  clickAction: /lovelace/access-control
    mode: single

  # --- SYSTEM PERSISTENCE ---
  - alias: "System: Fingerprint MQTT Persistence"
    id: system_fingerprint_mqtt_persistence
    mode: parallel
    trigger:
      - platform: mqtt
        topic: "fingerprint/+/user/set"
      - platform: mqtt
        topic: "fingerprint/access/+/set"
    action:
      - service: mqtt.publish
        data:
          topic: "{{ trigger.topic | replace('/set', '/state') }}"
          payload: "{{ trigger.payload }}"
          retain: true

# ------------------------------------------------------------------------------
# 3. SCRIPTS
# ------------------------------------------------------------------------------
script:
  # --- ADD / UPDATE FINGERPRINT & CREATE ACCESS SWITCHES ---
  add_fingerprint_entity:
    alias: "System: Add Fingerprint"
    mode: parallel
    fields:
      ulp_id:
        description: "The Long ID from Unifi"
        required: true
      current_user:
        description: "Current selected user"
        default: "-unassigned-"
    sequence:
      - variables:
          slug: "{{ ulp_id | replace('-', '_') | lower }}"
          user_list: >-
            {% set ns = namespace(users=['-Unassigned-', 'Guest']) %}
            {% for p in states.person %}
              {% set ns.users = ns.users + [p.attributes.friendly_name] %}
            {% endfor %}
            {{ ns.users | unique | sort | list }}
          # Clean User Name
          clean_current_user: >-
            {% set step1 = current_user | replace(' Notify Service', '') | replace(' Notifications', '') %}
            {% set parts = step1.split(' ') %}
            {% if parts|length > 1 and parts[0] == parts[-1] %}
               {{ parts[0] }}
            {% else %}
               {{ step1 }}
            {% endif %}

      # --- 1. PUBLISH FINGERPRINT CONFIG ---
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/fp_{{ slug }}/config"
          payload: >-
            {
              "name": "Fingerprint {{ ulp_id[:4] }}...",
              "object_id": "fingerprint_{{ slug }}",
              "unique_id": "fingerprint_{{ slug }}",
              "icon": "mdi:fingerprint",
              "options": {{ user_list | to_json }},
              "command_topic": "fingerprint/{{ slug }}/user/set",
              "state_topic": "fingerprint/{{ slug }}/user/state",
              "availability_topic": "fingerprint/{{ slug }}/availability",
              "payload_available": "online",
              "json_attributes_topic": "fingerprint/{{ slug }}/attributes",
              "device": {
                "identifiers": ["fingerprint_manager"],
                "name": "Fingerprint Database",
                "manufacturer": "Home Assistant",
                "model": "Biometric DB"
              }
            }
      - service: mqtt.publish
        data:
          retain: true
          topic: "fingerprint/{{ slug }}/attributes"
          payload: >-
            { "ulp_id": "{{ ulp_id }}" }
      
      # --- 2. UPDATE ASSIGNMENT ---
      - if:
          - condition: template
            value_template: >-
              {{ states('select.fingerprint_' ~ slug) in ['-unassigned-', 'unknown', 'unavailable', 'none'] or states('select.fingerprint_' ~ slug) != clean_current_user }}
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "fingerprint/{{ slug }}/user/state"
              payload: "{{ clean_current_user }}"
      
      # --- 3. CREATE ACCESS SWITCH (FIXED) ---
      # We calculate user_slug INSIDE the sequence to ensure variable scope is correct.
      - variables:
          user_slug: "{{ clean_current_user | slugify }}"

      - if:
          - condition: template
            value_template: "{{ clean_current_user not in ['-Unassigned-', 'Unknown', 'unknown'] }}"
        then:
          # Debug Notification: Let the user know we are creating a switch
          - service: notify.persistent_notification
            data:
              title: "Fingerprint System"
              message: "Creating Access Switch for: {{ clean_current_user }} (slug: {{ user_slug }})"
          
          - service: mqtt.publish
            data:
              retain: true
              topic: "homeassistant/switch/fp_access_{{ user_slug }}/config"
              payload: >-
                {
                  "name": "Access: {{ clean_current_user }}",
                  "object_id": "fp_access_{{ user_slug }}",
                  "unique_id": "fp_access_switch_{{ user_slug }}",
                  "icon": "mdi:account-check",
                  "command_topic": "fingerprint/access/{{ user_slug }}/set",
                  "state_topic": "fingerprint/access/{{ user_slug }}/state",
                  "device": { "identifiers": ["fingerprint_manager"] }
                }
          # Init to ON if it doesn't exist
          - if:
              - condition: template
                value_template: "{{ states('switch.fp_access_' ~ user_slug) in ['unknown', 'unavailable', 'none'] }}"
            then:
              - service: mqtt.publish
                data:
                  retain: true
                  topic: "fingerprint/access/{{ user_slug }}/state"
                  payload: "ON"

      # --- 4. SET ONLINE ---
      - service: mqtt.publish
        data:
          retain: true
          topic: "fingerprint/{{ slug }}/availability"
          payload: "online"

  # --- REFRESH ALL USERS ---
  refresh_fingerprint_users:
    alias: "System: Refresh Fingerprint Users"
    mode: single
    sequence:
      - repeat:
          for_each: >-
            {{ states.select | selectattr('entity_id', 'search', '^select\.fingerprint_') | list }}
          sequence:
            - service: script.add_fingerprint_entity
              data:
                ulp_id: "{{ state_attr(repeat.item.entity_id, 'ulp_id') }}"
                current_user: "{{ repeat.item.state }}"
```

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Fingerprints](../dashboards/home-access/fingerprints.md)** (Uses 4 entities)
* **[Front Door](../dashboards/main/front-door.md)** (Uses 1 entities)
* **[Home](../dashboards/main/home.md)** (Uses 1 entities)
* **[Mud Room](../dashboards/main/mud_room.md)** (Uses 1 entities)
<!-- END_DASHBOARD -->
