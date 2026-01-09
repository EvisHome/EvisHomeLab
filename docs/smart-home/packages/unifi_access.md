---
tags:
  - package
  - automated
version: 1.1.0
---

# Package: Unifi Access

**Version:** 1.1.0  
**Description:** Unified management for G4 Doorbell Pro Fingerprint & NFC.

<!-- START_IMAGE -->
![Package Diagram](../../assets/images/packages/unifi_access.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
The **Unifi Access** package implements a unified access control layer on top of the Ubiquiti G4 Doorbell Pro. It abstracts distinct hardware events (NFC, Fingerprint) into a single logical "Unified User" entity backed by MQTT discovery. The system provides granular, per-credential access management (switches), a centralized Guest Schedule (input_helpers), and "Fail-Closed" authorization logic. State persistence is handled via MQTT Retain to ensure reliability across reboots.
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
1.  **Scan**: A user scans their fingerprint or NFC tag at the doorbell.
2.  **Identify**: The system instantly recognizes the person (e.g., "Dad" or "Guest").
3.  **Check Permissions**:
    *   **Family**: Checks if their specific access (Fingerprint or Card) is currently switched ON.
    *   **Guests**: Checks if they are allowed today **AND** if it is currently within the "Guest Hours".
4.  **Unlock**: If valid, the door unlocks and a snapshot is sent to your phone. If denied, a security alert is triggered.
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Home Access Center](../dashboards/home-access/home_access_center.md)**: *The **Home Access Center** serves as the central administrative hub for managing physical security and entry credentials. Its primary function is to maintain a unified user registry where distinct hardware identifiers—such as Fingerprints and NFC tags—are mapped to specific individuals. This abstraction allows homeowners to easily enroll new keys, assign them to family members or guests, and instantly revoke permissions if a credential is lost or compromised.* (Uses 8 entities)
* **[Front Door](../dashboards/main/front_door.md)**: *This view is the central security hub for the Front Door. It features live feeds and event clips from Frigate cameras (Doorbell and Porch). Users can control the smart lock, arm/disarm the alarm system, and manage the front entry lights. It also monitors door status and presence, with settings for occupancy-based automations.* (Uses 1 entities)
* **[Home](../dashboards/main/home.md)**: *The Home dashboard serves as the central information hub. It features a large clock and family calendars, alongside detailed weather forecasts. Key home stats are highlighted, including real-time energy prices, power usage, and the status of major appliances like the dishwasher and washing machine. The view also provides a high-level overview of the entire house, displaying camera feeds and status summaries for all key rooms (Sauna, Bathroom, Bedroom, etc.) using 'Streamline' area cards.* (Uses 1 entities)
* **[Mud Room](../dashboards/main/mud_room.md)**: *This dashboard manages the Mud Room. It provides control for the ceiling light and visualizes occupancy status via motion sensors. The view includes standard settings for occupancy automations and light scheduling.* (Uses 1 entities)
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
The sequence starts when the G4 Doorbell Pro broadcasts a hardware event (fingerprint or NFC) to Home Assistant. The automation logic intercepts this event and resolves the raw ID to a "Unified User" using a mapped MQTT lookup. Once the user is identified, the system performs a multi-stage authorization check: first verifying the specific credential type is enabled (e.g., is NFC allowed for this user?), and then—if the user is a Guest—verifying the request against the global Guest Schedule. A "Pass" decision triggers the Z-Wave lock and logs the entry; a "Fail" decision prevents access and logs a security warning.
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
```mermaid
sequenceDiagram
    participant User
    participant G4 as G4 Doorbell Pro
    participant HA as Home Assistant
    participant Logic as Access Logic
    participant MQTT as MQTT Broker
    participant Lock as Yale Lock
    participant Notify as Notification Svc

    User->>G4: Scans Fingerprint / NFC
    G4->>HA: Event (ulp_id)
    HA->>Logic: Trigger Automation
    
    rect rgb(240, 240, 240)
        Note over Logic: Identity Resolution
        Logic->>MQTT: Query User for ulp_id
        MQTT-->>Logic: Returns "Unified User"
    end

    rect rgb(230, 245, 255)
        Note over Logic: Authorization Check
        alt is Unknown ID
            Logic->>Logic: Auto-Learn (Create "Unknown")
            Logic->>Notify: Alert "New ID Found"
        else is Known User
            Logic->>Logic: Check Access Switch (FP/NFC)
            opt is Guest
                Logic->>Logic: Validate Schedule (Time/Day)
            end
            
            alt Access Granted
                Logic->>Lock: Unlock Command
                Logic->>Notify: Send "Unlocked" Snapshot
            else Access Denied
                Logic->>Notify: Send Critical Alert
            end
        end
    end
```
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Unifi Unified Access Control
# Version: 1.1.0
# Description: Unified management for G4 Doorbell Pro Fingerprint & NFC.
#              - Shared Identity: 'select.unifi_user_ID'
#              - Separate Access: 'switch.fp_access_USER' & 'switch.nfc_access_USER'
#              - Unified Schedule: 'input_datetime.guest_access_...'
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1. HELPERS & SCHEDULES
# ------------------------------------------------------------------------------
input_select:
  unifi_delete_id:
    name: "Select ID to Delete"
    icon: mdi:delete-empty
    options: ["-select-"]

# --- UNIFIED GUEST SCHEDULE ---
input_datetime:
  guest_access_start:
    name: "Guest Access Start"
    has_date: false
    has_time: true
    icon: mdi:clock-start
    initial: "09:00"
  guest_access_end:
    name: "Guest Access End"
    has_date: false
    has_time: true
    icon: mdi:clock-end
    initial: "21:00"

input_boolean:
  guest_access_mon:
    name: "Mon"
    icon: mdi:calendar
  guest_access_tue:
    name: "Tue"
    icon: mdi:calendar
  guest_access_wed:
    name: "Wed"
    icon: mdi:calendar
  guest_access_thu:
    name: "Thu"
    icon: mdi:calendar
  guest_access_fri:
    name: "Fri"
    icon: mdi:calendar
  guest_access_sat:
    name: "Sat"
    icon: mdi:calendar
  guest_access_sun:
    name: "Sun"
    icon: mdi:calendar

# ------------------------------------------------------------------------------
# 2. AUTOMATIONS
# ------------------------------------------------------------------------------
automation:
  # --- LOGIC 1: FINGERPRINT ENTRY ---
  - alias: "Access: Fingerprint Entry Logic"
    id: access_fingerprint_entry_logic
    mode: single
    trigger:
      - platform: state
        entity_id: event.front_door_fingerprint
        not_from:
          - "unknown"
          - "unavailable"
        not_to:
          - "unknown"
          - "unavailable"
    variables:
      raw_id: >-
        {{ trigger.to_state.attributes.ulp_id | default('unknown') }}
      slug_id: "{{ raw_id | replace('-', '_') | lower }}"
      # SHARED IDENTITY ENTITY
      assigned_user: "{{ states('select.unifi_user_' ~ slug_id) }}"
      # FP ACCESS SWITCH
      user_switch: "switch.fp_access_{{ assigned_user | slugify }}"
    action:
      - target:
          entity_id: camera.g4_doorbell_pro_poe_high_resolution_channel
        data:
          filename: /config/www/front_door_unlock_snapshot.jpg
        action: camera.snapshot

      - choose:
          # ROLE 1: GUEST
          - conditions:
              - condition: template
                value_template: "{{ 'guest' in assigned_user | lower }}"
            sequence:
              - if:
                  - condition: template
                    value_template: >
                      {# FAIL CLOSED: Switch MUST be ON #}
                      {% set access_enabled = is_state(user_switch, 'on') %}
                      {# SCHEDULE CHECK (UNIFIED) #}
                      {% set current_day = now().strftime('%a')|lower %}
                      {% set is_day_allowed = is_state('input_boolean.guest_access_' ~ current_day, 'on') %}
                      {% set current_time = now().strftime('%H:%M:%S') %}
                      {% set start_time = states('input_datetime.guest_access_start') %}
                      {% set end_time = states('input_datetime.guest_access_end') %}
                      {% set is_time_allowed = (current_time >= start_time) and (current_time <= end_time) %}

                      {{ access_enabled and is_day_allowed and is_time_allowed }}
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Guest Entry (Fingerprint)
                      message: "Guest entered via Fingerprint."
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: ⛔ Access Denied (Fingerprint)
                      message: >
                        {% if not is_state(user_switch, 'on') %}
                          Guest FP access manually DISABLED.
                        {% else %}
                          Guest outside allowed schedule.
                        {% endif %}
                      critical: true
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock_denied

          # ROLE 2: STANDARD USER
          - conditions:
              - condition: template
                value_template: >
                  {{ assigned_user not in ['unknown', 'unavailable', 'none', 'Unknown', '-Unassigned-', '-unassigned-', 'Guest'] }}
            sequence:
              - if:
                  - condition: template
                    # FAIL CLOSED: Switch MUST be ON
                    value_template: "{{ is_state(user_switch, 'on') }}"
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "🔓 Guest {{ assigned_user }} entered via Fingerprint."
                      entity_id: lock.front_door_lock_cloud
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "🔓 {{ assigned_user }} unlocked via Fingerprint."
                      entity_id: lock.front_door_lock_cloud
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Front Door Unlocked
                      message: "Unlocked by: {{ assigned_user }}"
                      image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "⛔ Guest Access Denied (Fingerprint): {{ assigned_user }}."
                      entity_id: lock.front_door_lock_cloud
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "⛔ Access Disabled (Fingerprint): {{ assigned_user }}."
                      entity_id: lock.front_door_lock_cloud
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
              - action: script.add_unifi_user_entity
                data:
                  ulp_id: "{{ raw_id }}"
                  current_user: Unknown
              - action: script.notify_smart_master
                data:
                  category: system
                  title: 🖐️ New Fingerprint ID
                  message: "ID: {{ raw_id }}\nAdded to User Management as 'Unknown'."
                  image: /local/front_door_unlock_snapshot.jpg?t={{ now().timestamp() }}
                  tag: door_lock_unknown
                  clickAction: /lovelace/access-control

  # --- LOGIC 2: NFC ENTRY ---
  - alias: "Access: NFC Entry Logic"
    id: access_nfc_entry_logic
    mode: single
    trigger:
      - platform: state
        entity_id: event.front_door_nfc
        not_from:
          - "unknown"
          - "unavailable"
        not_to:
          - "unknown"
          - "unavailable"
    variables:
      raw_id: >-
        {{ trigger.to_state.attributes.ulp_id | default('unknown') }}
      slug_id: "{{ raw_id | replace('-', '_') | lower }}"
      # SHARED IDENTITY ENTITY
      assigned_user: "{{ states('select.unifi_user_' ~ slug_id) }}"
      # NFC ACCESS SWITCH
      user_switch: "switch.nfc_access_{{ assigned_user | slugify }}"
    action:
      - target:
          entity_id: camera.g4_doorbell_pro_poe_high_resolution_channel
        data:
          filename: /config/www/front_door_nfc_snapshot.jpg
        action: camera.snapshot

      - choose:
          # ROLE 1: GUEST
          - conditions:
              - condition: template
                value_template: "{{ 'guest' in assigned_user | lower }}"
            sequence:
              - if:
                  - condition: template
                    value_template: >
                      {# FAIL CLOSED: Switch MUST be ON #}
                      {% set access_enabled = is_state(user_switch, 'on') %}
                      {# SCHEDULE CHECK (UNIFIED) #}
                      {% set current_day = now().strftime('%a')|lower %}
                      {% set is_day_allowed = is_state('input_boolean.guest_access_' ~ current_day, 'on') %}
                      {% set current_time = now().strftime('%H:%M:%S') %}
                      {% set start_time = states('input_datetime.guest_access_start') %}
                      {% set end_time = states('input_datetime.guest_access_end') %}
                      {% set is_time_allowed = (current_time >= start_time) and (current_time <= end_time) %}

                      {{ access_enabled and is_day_allowed and is_time_allowed }}
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "🔓 Guest {{ assigned_user }} entered via NFC."
                      entity_id: lock.front_door_lock_cloud
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Guest Entry (NFC)
                      message: "Guest entered via NFC."
                      image: /local/front_door_nfc_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "⛔ Guest Access Denied (NFC): {{ assigned_user }}."
                      entity_id: lock.front_door_lock_cloud
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: ⛔ Access Denied (NFC)
                      message: >
                        {% if not is_state(user_switch, 'on') %}
                          Guest NFC access manually DISABLED.
                        {% else %}
                          Guest outside allowed schedule.
                        {% endif %}
                      critical: true
                      image: /local/front_door_nfc_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock_denied

          # ROLE 2: STANDARD USER
          - conditions:
              - condition: template
                value_template: >
                  {{ assigned_user not in ['unknown', 'unavailable', 'none', 'Unknown', '-Unassigned-', '-unassigned-', 'Guest'] }}
            sequence:
              - if:
                  - condition: template
                    # FAIL CLOSED
                    value_template: "{{ is_state(user_switch, 'on') }}"
                then:
                  - action: lock.unlock
                    target:
                      entity_id: lock.front_door_lock
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "🔓 {{ assigned_user }} unlocked via NFC."
                      entity_id: lock.front_door_lock_cloud
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: 🔓 Front Door Unlocked (NFC)
                      message: "Unlocked by: {{ assigned_user }}"
                      image: /local/front_door_nfc_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock
                else:
                  - action: logbook.log
                    data:
                      name: "Front Door Access"
                      message: "⛔ Access Disabled (NFC): {{ assigned_user }}."
                      entity_id: lock.front_door_lock_cloud
                  - action: script.notify_smart_master
                    data:
                      category: security
                      title: ⛔ Access Disabled
                      message: "NFC valid, but {{ assigned_user }}'s NFC access is switched OFF."
                      critical: true
                      image: /local/front_door_nfc_snapshot.jpg?t={{ now().timestamp() }}
                      tag: door_lock_denied

          # ROLE 3: AUTO-LEARN
          - conditions:
              - condition: template
                value_template: "{{ raw_id != 'unknown' and raw_id != '' }}"
            sequence:
              - action: script.add_unifi_user_entity
                data:
                  ulp_id: "{{ raw_id }}"
                  current_user: Unknown
              - action: script.notify_smart_master
                data:
                  category: system
                  title: 🏷️ New NFC ID
                  message: "ID: {{ raw_id }}\nAdded to User Management as 'Unknown'."
                  image: /local/front_door_nfc_snapshot.jpg?t={{ now().timestamp() }}
                  tag: door_lock_unknown
                  clickAction: /lovelace/access-control

  # --- SYSTEM PERSISTENCE (Universal) ---
  - alias: "System: Unifi Access MQTT Persistence"
    id: system_unifi_access_mqtt_persistence
    mode: parallel
    trigger:
      - platform: mqtt
        topic: "unifi_access/+/user/set"
      - platform: mqtt
        topic: "unifi_access/access/+/set"
      - platform: mqtt
        topic: "fingerprint/access/+/set" # Legacy/Compatibility
      - platform: mqtt
        topic: "nfc/access/+/set" # Legacy/Compatibility
    action:
      - service: mqtt.publish
        data:
          topic: "{{ trigger.topic | replace('/set', '/state') }}"
          payload: "{{ trigger.payload }}"
          retain: true

  # --- AUTO-CREATE SWITCHES ON ASSIGNMENT CHANGE ---
  - alias: "System: Unifi User Assignment Update"
    id: system_unifi_user_assignment_update
    mode: parallel
    trigger:
      - platform: mqtt
        topic: "unifi_access/+/user/set"
    action:
      - variables:
          slug: "{{ trigger.topic.split('/')[1] }}"
          entity_id: "select.unifi_user_{{ slug }}"
      - delay: "00:00:00.200"
      - service: script.add_unifi_user_entity
        data:
          ulp_id: "{{ state_attr(entity_id, 'ulp_id') | default(slug) }}"
          current_user: "{{ trigger.payload }}"
      - delay: "00:00:00.200"
      - service: script.cleanup_unused_unifi_switches

# ------------------------------------------------------------------------------
# 3. SCRIPTS
# ------------------------------------------------------------------------------
script:
  # --- ADD / UPDATE USER & CREATE BOTH SWITCHES ---
  add_unifi_user_entity:
    alias: "System: Add Unifi User"
    mode: parallel
    fields:
      ulp_id:
        description: "The Unifi ID (Member ID)"
        required: true
      current_user:
        description: "Current assigned user"
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

          # Clean Name
          clean_current_user: >-
            {% set step1 = current_user | replace(' Notify Service', '') | replace(' Notifications', '') %}
            {% set parts = step1.split(' ') %}
            {% if parts|length > 1 and parts[0] == parts[-1] %}
               {{ parts[0] }}
            {% else %}
               {{ step1 }}
            {% endif %}

      # --- 1. PUBLISH SHARED IDENTITY SELECT ---
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/select/unifi_user_{{ slug }}/config"
          payload: >-
            {
              "name": "Unifi User {{ ulp_id[:4] }}...",
              "object_id": "unifi_user_{{ slug }}",
              "unique_id": "unifi_user_{{ slug }}",
              "icon": "mdi:account-key",
              "options": {{ user_list | to_json }},
              "command_topic": "unifi_access/{{ slug }}/user/set",
              "state_topic": "unifi_access/{{ slug }}/user/state",
              "availability_topic": "unifi_access/{{ slug }}/availability",
              "payload_available": "online",
              "json_attributes_topic": "unifi_access/{{ slug }}/attributes",
              "device": {
                "identifiers": ["unifi_access_manager"],
                "name": "Unifi Access DB",
                "manufacturer": "Home Assistant",
                "model": "Unified ID DB"
              }
            }
      - service: mqtt.publish
        data:
          retain: true
          topic: "unifi_access/{{ slug }}/attributes"
          payload: >-
            { "ulp_id": "{{ ulp_id }}" }

      # --- 2. UPDATE STATE ---
      - if:
          - condition: template
            value_template: >-
              {{ states('select.unifi_user_' ~ slug) != clean_current_user }}
        then:
          - service: mqtt.publish
            data:
              retain: true
              topic: "unifi_access/{{ slug }}/user/state"
              payload: "{{ clean_current_user }}"

      # --- 3. CREATE SWITCHES (FP & NFC) ---
      - variables:
          user_slug: "{{ clean_current_user | slugify }}"

      - if:
          - condition: template
            value_template: "{{ clean_current_user not in ['-Unassigned-', 'Unknown', 'unknown'] }}"
        then:
          # --- SWITCH 1: FINGERPRINT ACCESS ---
          - service: mqtt.publish
            data:
              retain: true
              topic: "homeassistant/switch/fp_access_{{ user_slug }}/config"
              payload: >-
                {
                  "name": "FP Access: {{ clean_current_user }}",
                  "object_id": "fp_access_{{ user_slug }}",
                  "unique_id": "fp_access_switch_{{ user_slug }}",
                  "icon": "mdi:fingerprint",
                  "command_topic": "fingerprint/access/{{ user_slug }}/set",
                  "state_topic": "fingerprint/access/{{ user_slug }}/state",
                  "device": { "identifiers": ["unifi_access_manager"] }
                }
          # Init FP ON
          - if:
              - condition: template
                value_template: "{{ states('switch.fp_access_' ~ user_slug) in ['unknown', 'unavailable', 'none'] }}"
            then:
              - service: mqtt.publish
                data:
                  retain: true
                  topic: "fingerprint/access/{{ user_slug }}/state"
                  payload: "ON"

          # --- SWITCH 2: NFC ACCESS ---
          - service: mqtt.publish
            data:
              retain: true
              topic: "homeassistant/switch/nfc_access_{{ user_slug }}/config"
              payload: >-
                {
                  "name": "NFC Access: {{ clean_current_user }}",
                  "object_id": "nfc_access_{{ user_slug }}",
                  "unique_id": "nfc_access_switch_{{ user_slug }}",
                  "icon": "mdi:tag-check",
                  "command_topic": "nfc/access/{{ user_slug }}/set",
                  "state_topic": "nfc/access/{{ user_slug }}/state",
                  "device": { "identifiers": ["unifi_access_manager"] }
                }
          # Init NFC ON
          - if:
              - condition: template
                value_template: "{{ states('switch.nfc_access_' ~ user_slug) in ['unknown', 'unavailable', 'none'] }}"
            then:
              - service: mqtt.publish
                data:
                  retain: true
                  topic: "nfc/access/{{ user_slug }}/state"
                  payload: "ON"

      # --- 4. SET ONLINE ---
      - service: mqtt.publish
        data:
          retain: true
          topic: "unifi_access/{{ slug }}/availability"
          payload: "online"

  # --- REFRESH ALL USERS ---
  refresh_unifi_users:
    alias: "System: Refresh Unifi Users"
    mode: single
    sequence:
      - repeat:
          for_each: >-
            {{ states.select | selectattr('entity_id', 'search', '^select\\.unifi_user_') | list }}
          sequence:
            - service: script.add_unifi_user_entity
              data:
                ulp_id: "{{ state_attr(repeat.item.entity_id, 'ulp_id') }}"
                current_user: "{{ repeat.item.state }}"
      - service: script.cleanup_unused_unifi_switches

  # --- CLEANUP ORPHANED SWITCHES (FP & NFC) ---
  cleanup_unused_unifi_switches:
    alias: "System: Cleanup Unused Unifi Switches"
    mode: single
    sequence:
      - variables:
          active_user_slugs: >-
            {% set ns = namespace(slugs=[]) %}
            {% for s in states.select | selectattr('entity_id', 'search', '^select\\.unifi_user_') %}
               {% if s.state not in ['-Unassigned-', 'Unknown', 'unknown', 'unavailable', 'none'] %}
                 {% set ns.slugs = ns.slugs + [s.state | slugify] %}
               {% endif %}
            {% endfor %}
            {{ ns.slugs | unique | list }}

          # Find all existing switches
          fp_switches: "{{ states.switch | selectattr('entity_id', 'search', '^switch\\.fp_access_') | map(attribute='entity_id') | list }}"
          nfc_switches: "{{ states.switch | selectattr('entity_id', 'search', '^switch\\.nfc_access_') | map(attribute='entity_id') | list }}"

      # Cleanup FP Switches
      - repeat:
          for_each: "{{ fp_switches }}"
          sequence:
            - variables:
                switch_slug: "{{ repeat.item.replace('switch.fp_access_', '') }}"
            - if:
                - condition: template
                  value_template: "{{ switch_slug not in active_user_slugs }}"
              then:
                - service: mqtt.publish
                  data:
                    topic: "homeassistant/switch/fp_access_{{ switch_slug }}/config"
                    payload: ""
                    retain: true
                - service: mqtt.publish
                  data:
                    topic: "fingerprint/access/{{ switch_slug }}/state"
                    payload: ""
                    retain: true

      # Cleanup NFC Switches
      - repeat:
          for_each: "{{ nfc_switches }}"
          sequence:
            - variables:
                switch_slug: "{{ repeat.item.replace('switch.nfc_access_', '') }}"
            - if:
                - condition: template
                  value_template: "{{ switch_slug not in active_user_slugs }}"
              then:
                - service: mqtt.publish
                  data:
                    topic: "homeassistant/switch/nfc_access_{{ switch_slug }}/config"
                    payload: ""
                    retain: true
                - service: mqtt.publish
                  data:
                    topic: "nfc/access/{{ switch_slug }}/state"
                    payload: ""
                    retain: true

```
