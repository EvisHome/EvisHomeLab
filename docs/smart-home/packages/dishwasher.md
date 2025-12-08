---
tags:
  - package
  - automated
version: 1.1.0
---

# Package: Dishwasher

**Version:** 1.1.0  
**Description:** Logic, sensors, flags, and automations for the LG Dishwasher. Handles normalization of LG ThinQ data, maintenance reminders, and leak detection.



<!-- PACKAGE_SUMMARY_SLOT -->



## Architecture Diagram


<!-- PACKAGE_MERMAID_SLOT -->



## Configuration
```yaml
# ------------------------------------------------------------------------------
# Package: Dishwasher
# Version: 1.1.0
# Description: Logic, sensors, flags, and automations for the LG Dishwasher. Handles normalization of LG ThinQ data, maintenance reminders, and leak detection.
# Dependencies:
#   - Integration: LG ThinQ (SmartThinQ LGE Sensors)
#   - Entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
#   - Script: script.notify_smart_master
# ------------------------------------------------------------------------------

# ==============================================================================
# 1. HELPERS
# ==============================================================================
input_boolean:
  # Flag: Tracks if the 'Machine Clean' cycle is due.
  # Logic:
  #   - Turned ON by automation when 'binary_sensor.dishwasher_machine_clean_reminder' goes high.
  #   - Turned OFF by automation when a 'machine_clean' cycle is actually started.
  dishwasher_needs_cleaning:
    name: "Dishwasher Needs Cleaning"
    icon: mdi:spray-bottle

# ==============================================================================
# 2. TEMPLATE SENSORS (Normalize the LG Data)
# ==============================================================================
template:
  - binary_sensor:
      - name: "Dishwasher Active"
        unique_id: dishwasher_active_normalized
        state: >
          {{ states('sensor.dishwasher_current_status') not in ['unavailable', 'unknown', 'initial', 'power_off'] }}
        icon: mdi:dishwasher

      - name: "Dishwasher Door Open"
        unique_id: dishwasher_door_normalized
        device_class: door
        state: >
          {{ is_state('binary_sensor.dishwasher_door', 'on') }}

  - sensor:
      - name: "Dishwasher Status Clean"
        unique_id: dishwasher_status_clean
        icon: mdi:dishwasher
        state: >
          {% set status = states('sensor.dishwasher_current_status') %}
          {% if status in ['unavailable', 'unknown', 'power_off'] %}
            Off
          {% else %}
            {{ status | replace('_', ' ') | title }}
          {% endif %}

      - name: "Dishwasher Remaining Time Human"
        unique_id: dishwasher_remaining_time_human
        icon: mdi:timer-outline
        state: >
          {% set finish_time = states('sensor.dishwasher_remaining_time') %}
          {% if finish_time in ['unavailable', 'unknown', 'none'] %}
            --:--
          {% else %}
            {# Calculate difference between finish time and now #}
            {% set time_diff = as_timestamp(finish_time) - as_timestamp(now()) %}
            {% if time_diff > 0 %}
              {# Convert seconds to H:MM #}
              {{ time_diff | timestamp_custom('%-H:%M', false) }}
            {% else %}
              0:00
            {% endif %}
          {% endif %}

# ==============================================================================
# 3. AUTOMATIONS
# ==============================================================================
automation:
  # --- DISHWASHER STARTED ---
  # Notify when the dishwasher starts, with a wait for the time remaining sensor.
  - alias: "Notify: Dishwasher Started"
    id: notify_dishwasher_started_pkg
    description: Notify when dishwasher starts a cycle, waiting for time remaining to be available.
    trigger:
      - entity_id: sensor.dishwasher_current_status
        from: initial
        to: running
        platform: state
      - entity_id: sensor.dishwasher_current_status
        from: power_off
        to: running
        platform: state
    action:
      # Wait up to 2 minutes for a valid time from the sensor.
      - wait_for_trigger:
          - platform: template
            value_template: >
              {{ states('sensor.dishwasher_remaining_time_human') not in ['unknown', 'unavailable', '--:--'] }}
        timeout:
          minutes: 2
        continue_on_timeout: true

      - service: script.notify_smart_master
        data:
          category: info
          title: 💦 Dishwasher Started
          # Use a conditional message in case the wait timed out.
          message: >
            {% set remaining = states('sensor.dishwasher_remaining_time_human') %}
            {% if remaining not in ['unknown', 'unavailable', '--:--'] %}
              Cycle: {{ states('sensor.dishwasher_current_cycle') | replace('_', ' ') | title }}
              Ready in: {{ remaining }} hours.
            {% else %}
              Dishwasher started. Time remaining not yet available.
            {% endif %}
          tag: dishwasher
          clickAction: /lovelace/kitchen
    mode: single

  # --- DISHWASHER DONE ---
  # Notify when dishwasher finishes. Triggers if door opens while status is 'end'.
  - alias: "Notify: Dishwasher Done"
    id: notify_dishwasher_done_pkg
    description: Notify when dishwasher finishes, including run time.
    trigger:
      - entity_id: sensor.dishwasher_current_status
        to: end
        id: cycle_end
        platform: state
      - entity_id: binary_sensor.dishwasher_door
        from: "off"
        to: "on"
        id: door_open
        platform: state
    condition:
      - condition: or
        conditions:
          - condition: trigger
            id: cycle_end
          - condition: and
            conditions:
              - condition: trigger
                id: door_open
              - condition: state
                entity_id: sensor.dishwasher_current_status
                state: end
    action:
      # Calculate run time, handling unknown values safely.
      - variables:
          run_time_raw: "{{ states('sensor.dishwasher_total_time') }}"
          run_time: |-
            {% if run_time_raw not in ['unknown', 'unavailable', 'none'] %}
              {{ run_time_raw }} min
            {% else %}
              Unknown time
            {% endif %}
      - service: script.notify_smart_master
        data:
          category: info
          title: ✨ Dishes are Clean
          message: "The cycle has finished. Total run time: {{ run_time }}."
          tag: dishwasher
          clickAction: app://com.lgeha.nuts
          actions:
            - action: URI
              title: Open LG App
              uri: app://com.lgeha.nuts
    mode: single

  # --- DISHWASHER MAINTENANCE ---
  # Alerts when machine clean is needed and resets the flag when a clean cycle is started.
  - alias: "Notify: Dishwasher Maintenance"
    id: notify_dishwasher_maintenance_pkg
    description: Alerts when machine clean is needed and resets when done.
    trigger:
      - entity_id: binary_sensor.dishwasher_machine_clean_reminder
        to: "on"
        id: needs_clean
        platform: state
      - entity_id: sensor.dishwasher_current_cycle
        to: machine_clean
        id: clean_cycle_started
        platform: state
    action:
      - choose:
          # Case 1: Reminder turns ON and we haven't acknowledged it yet.
          - conditions:
              - condition: trigger
                id: needs_clean
              - condition: state
                entity_id: input_boolean.dishwasher_needs_cleaning
                state: "off"
            sequence:
              - service: input_boolean.turn_on
                target:
                  entity_id: input_boolean.dishwasher_needs_cleaning
              - service: script.notify_smart_master
                data:
                  category: info
                  title: 🧼 Dishwasher Maintenance
                  message: The dishwasher needs a Machine Clean cycle.
                  tag: dishwasher_maintenance
                  sticky: true
          # Case 2: A 'machine_clean' cycle is started, so we reset the flag.
          - conditions:
              - condition: trigger
                id: clean_cycle_started
            sequence:
              - service: input_boolean.turn_off
                target:
                  entity_id: input_boolean.dishwasher_needs_cleaning
    mode: single

  # --- DISHWASHER LEAK DETECTION ---
  # Critical alarm if the external leak sensor detects water.
  - alias: "Notify: Dishwasher Leak"
    id: notify_dishwasher_leak_pkg
    description: Critical alarm triggered by the kitchen leak sensor.
    trigger:
      - platform: state
        entity_id: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
        to: "on"
    action:
      - service: script.notify_smart_master
        data:
          category: alarm
          title: "💧 Dishwasher Leak Detected!"
          message: "CRITICAL: Water detected under the dishwasher. Check immediately!"
          tag: dishwasher_leak
          critical: true
          sticky: true
          clickAction: /lovelace/kitchen
    mode: single
# ------------------------------------------------------------------------------
# Changelog
# ------------------------------------------------------------------------------
# 1.1.0 (2025-12-09): Added critical leak detection automation.
# 1.0.0 (2025-12-07): Initial package creation with status, time logic, and maintenance reminders.
# ------------------------------------------------------------------------------

```



## Dashboard Connections
<!-- DASHBOARD_CONNECTIONS_SLOT -->

