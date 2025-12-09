---
tags:
  - package
  - automated
version: 2.0.3
---

# Package: Car

**Version:** 2.0.3  
**Description:** Unified logic for Mercedes GLC. Normalizes sensors (Windows/Doors), wrapper switches, and Status Notifications.

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/car.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
The `Car` package provides a unified interface for the Mercedes GLC, leveraging the `mbapi2020` integration. It normalizes proprietary attribute data (e.g., window status codes, specific lock states) into standard Home Assistant binary sensors and device classes. The package includes a comprehensive automation suite (`notify_car_status_glc`) that monitors critical vehicle states—such as charging progress, pre-entry climate control, and fluid warnings—and dispatches actionable notifications via the `notify_smart_master` script.
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
### How It Works
*   **Real-time Monitoring:** The system continuously checks the status of your car's doors, windows, and locks. You can instantly see if the car is secure or if the engine is running.
*   **Remote Control:** You can lock or unlock the doors and close the windows directly from your dashboard. Additionally, the "Pre-entry A/C" switch allows you to heat or cool the car before you leave.
*   **Smart Notifications:**
    *   **Charging:** Receive alerts when the car is plugged in, when charging starts (with estimated completion time), and when the battery is full.
    *   **Safety & Maintenance:** The system watches for warning signs like low tire pressure, low brake fluid, or low washer fluid and sends critical alerts to your phone if attention is needed.
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[CAR](../dashboards/dashboard-persons/car.md)**: *This view provides a comprehensive dashboard for monitoring and controlling the Mercedes-Benz car. It allows users to check fuel, EV battery, tire pressure, and lock status, verify door and window sensors, control pre-entry climate, and track the vehicle's location.* (Uses 1 entities)
* **[Home](../dashboards/main/home.md)** (Uses 1 entities)
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
The architecture relies on the `mbapi2020` integration to poll data from the Mercedes Cloud. The `Car` package acts as a transformation layer, converting complex attribute data (like raw status codes for windows and doors) into discrete, easy-to-use binary sensors. This normalized data feeds into a central automation (`notify_car_status_glc`), which evaluates state changes—such as a charging cable connection or a low fluid warning—and routes the appropriate message priority to the user through the `notify_smart_master` script.
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
```mermaid
sequenceDiagram
    participant Mercedes as Mercedes Cloud
    participant Integration as HA Integration (mbapi2020)
    participant Package as Car Package
    participant User as User (Notification)

    Note over Arrow: Polling Cycle
    Mercedes->>Integration: Vehicle Status Update
    Integration->>Package: Update Entity Attributes (Windows, Locks, Odometer)
    Package->>Package: Normalize Attributes to Binary Sensors

    Note over Package: Automation Logic
    alt Critical Warning (e.g., Low Brake Fluid)
        Package->>User: 🚨 Critical Alert via script.notify_smart_master
    else Standard Event (e.g., Charging Started)
        Package->>User: ⚡ Info Notification (Power & Est. Time)
    end

    Note over User: User Action
    User->>Package: Toggle "Pre-entry A/C"
    Package->>Integration: Call Service (preheat_start)
    Integration->>Mercedes: Send Command
```
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Car GLC
# Version: 2.0.3
# Description: Unified logic for Mercedes GLC. Normalizes sensors (Windows/Doors), wrapper switches, and Status Notifications.
# Dependencies:
#   - Integration: ReneNulschDE/mbapi2020 (HACS)
#   - Script: script.notify_smart_master
# ------------------------------------------------------------------------------

# ==============================================================================
# 1. TEMPLATE SENSORS & BINARY SENSORS
# ==============================================================================
template:
  - binary_sensor:
      # --- Windows (Normalized from Attribute) ---
      - name: "Car GLC Window Front Left"
        unique_id: car_glc_window_front_left
        device_class: window
        state: >
          {{ state_attr('binary_sensor.[LICENSE_PLATE]_windows_closed', 'Windowstatusfrontleft') != '2' }}

      - name: "Car GLC Window Front Right"
        unique_id: car_glc_window_front_right
        device_class: window
        state: >
          {{ state_attr('binary_sensor.[LICENSE_PLATE]_windows_closed', 'Windowstatusfrontright') != '2' }}

      - name: "Car GLC Window Rear Left"
        unique_id: car_glc_window_rear_left
        device_class: window
        state: >
          {{ state_attr('binary_sensor.[LICENSE_PLATE]_windows_closed', 'Windowstatusrearleft') != '2' }}

      - name: "Car GLC Window Rear Right"
        unique_id: car_glc_window_rear_right
        device_class: window
        state: >
          {{ state_attr('binary_sensor.[LICENSE_PLATE]_windows_closed', 'Windowstatusrearright') != '2' }}

      # --- Doors (Normalized from Attribute) ---
      - name: "Car GLC Door Front Left"
        unique_id: car_glc_door_front_left
        device_class: door
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door front left') != 'closed' }}

      - name: "Car GLC Door Front Right"
        unique_id: car_glc_door_front_right
        device_class: door
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door front right') != 'closed' }}

      - name: "Car GLC Door Rear Left"
        unique_id: car_glc_door_rear_left
        device_class: door
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door rear left') != 'closed' }}

      - name: "Car GLC Door Rear Right"
        unique_id: car_glc_door_rear_right
        device_class: door
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door rear right') != 'closed' }}

      - name: "Car GLC Deck Lid"
        unique_id: car_glc_deck_lid
        device_class: opening
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Deck lid') != 'closed' }}

      # --- Locks (Normalized from Attribute) ---
      - name: "Car GLC Lock Front Left"
        unique_id: car_glc_lock_front_left
        device_class: lock
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door lock front left') != 'locked' }}

      - name: "Car GLC Lock Front Right"
        unique_id: car_glc_lock_front_right
        device_class: lock
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door lock front right') != 'locked' }}

      - name: "Car GLC Lock Rear Left"
        unique_id: car_glc_lock_rear_left
        device_class: lock
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door lock rear left') != 'locked' }}

      - name: "Car GLC Lock Rear Right"
        unique_id: car_glc_lock_rear_right
        device_class: lock
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Door lock rear right') != 'locked' }}

      - name: "Car GLC Gas Lock"
        unique_id: car_glc_gas_lock
        device_class: lock
        state: >
          {{ state_attr('sensor.[LICENSE_PLATE]_lock', 'Gas lock') != 'locked' }}

      # --- Logic Sensors (Consolidated Status) ---
      - name: "Car Charge Plug"
        unique_id: car_charge_plug
        device_class: plug
        state: >
          {% set value = state_attr('sensor.[LICENSE_PLATE]_range_electric', 'chargingstatus') | float(0) %}
          {{ value != 3 }}
        icon: >
          {% set value = state_attr('sensor.[LICENSE_PLATE]_range_electric', 'chargingstatus') | float(0) %}
          {% if value == 3 %}
            mdi:power-plug-off
          {% else %}
            mdi:power-plug
          {% endif %}

      - name: "Car Charging"
        unique_id: car_charging_active
        device_class: power
        state: >
          {% set value = states('sensor.[LICENSE_PLATE]_charging_power') | float(0) %}
          {{ value != 0 }}
        icon: >
          {% if states('sensor.[LICENSE_PLATE]_charging_power') | float(0) == 0 %}
            mdi:power-off
          {% else %}
            mdi:power-on
          {% endif %}

      - name: "Car Engine"
        unique_id: car_engine_status
        device_class: running
        state: >
          {% set value = states('sensor.[LICENSE_PLATE]_ignition_state') | float(0) %}
          {{ value >= 2 }}
        icon: >
          {% if states('sensor.[LICENSE_PLATE]_ignition_state') | float(0) < 2 %}
            mdi:engine-off
          {% else %}
            mdi:engine
          {% endif %}

      - name: "Car Doors"
        unique_id: car_doors_status
        device_class: door
        state: >
          {% set value = state_attr('sensor.[LICENSE_PLATE]_lock', 'doorStatusOverall') %}
          {{ value == 0 }}
        icon: >
          {% if state_attr('sensor.[LICENSE_PLATE]_lock', 'doorStatusOverall') == 0 %}
            mdi:car-door
          {% else %}
            mdi:car-door-lock
          {% endif %}

  - sensor:
      - name: "Car Charge Ready"
        unique_id: car_charge_ready_time
        state: >
          {% set end = state_attr('sensor.[LICENSE_PLATE]_range_electric', 'endofchargetime') %}
          {% if end %}
            {{ as_datetime(end).strftime('%H:%M') }}
          {% else %}
            unknown
          {% endif %}

# ==============================================================================
# 2. SWITCHES (Wrappers for API Calls)
# ==============================================================================
switch:
  - name: "Car Pre-entry A/C"
    unique_id: car_pre_entry_ac
    icon: mdi:air-conditioner
    state: "{{ is_state_attr('sensor.[LICENSE_PLATE]_range_electric', 'precondNow', 1) }}"
    turn_on:
      service: mbapi2020.preheat_start
      data:
        type: "0"
        vin: !secret [REDACTED]
    turn_off:
      service: mbapi2020.preheat_stop
      data:
        vin: !secret [REDACTED]

  - name: "Car Windows"
    unique_id: car_windows
    icon: mdi:car-door
    state: "{{ is_state('binary_sensor.[LICENSE_PLATE]_windows_closed', 'on') }}"
    turn_on:
      service: mbapi2020.windows_close
      data:
        vin: !secret [REDACTED]
    turn_off:
      service: mbapi2020.windows_open
      data:
        vin: !secret [REDACTED]

  - name: "Car Door Locks"
    unique_id: car_doors
    icon: mdi:car-door
    state: "{{ is_state('sensor.[LICENSE_PLATE]_lock', '2') }}"
    turn_on:
      service: mbapi2020.doors_unlock
      data:
        vin: !secret [REDACTED]
    turn_off:
      service: mbapi2020.doors_lock
      data:
        vin: !secret [REDACTED]

# ==============================================================================
# 3. AUTOMATION (Notifications)
# ==============================================================================
automation:
  - alias: "Notify: Car Status"
    id: notify_car_status_glc
    description: "Manages mobile notifications for critical car events including charging status, pre-conditioning, tire pressure warnings, and fluid levels. Uses the 'notify_smart_master' script."
    trigger:
      - entity_id: binary_sensor.car_charge_plug
        from: "off"
        to: "on"
        id: plug_in
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_charging_active
        from: "off"
        to: "on"
        id: charging_start
        platform: state
      - entity_id: sensor.[LICENSE_PLATE]_state_of_charge
        above: 99
        id: charging_full
        platform: numeric_state
      - entity_id: binary_sensor.[LICENSE_PLATE]_preclimate_status
        from: "off"
        to: "on"
        id: climate_started
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_preclimate_status
        from: "on"
        to: "off"
        id: climate_stopped
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_tire_warning
        to: "on"
        id: warn_tire
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_low_brake_fluid_warning
        to: "on"
        id: warn_brake
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_low_coolant_level_warning
        to: "on"
        id: warn_coolant
        platform: state
      - entity_id: binary_sensor.[LICENSE_PLATE]_low_wash_water_warning
        to: "on"
        id: warn_wash_water
        platform: state
    action:
      - choose:
          - conditions:
              - condition: trigger
                id: charging_start
            sequence:
              - wait_for_trigger:
                  - entity_id: sensor.[LICENSE_PLATE]_charging_power
                    above: 0
                    platform: numeric_state
                timeout: "00:02:00"
                continue_on_timeout: true
      - variables:
          notification_data: |
            {% if trigger.id == 'plug_in' %}
              {
                "title": "🔌 Car Connected",
                "message": "Charging cable connected.",
                "tag": "car_charging",
                "critical": false
              }
            {% elif trigger.id == 'charging_start' %}
              {% set power = states('sensor.[LICENSE_PLATE]_charging_power') %}
              {% set raw_end = state_attr('sensor.[LICENSE_PLATE]_end_of_charge', 'original_value') %}
              
              {# Convert raw timestamp to HH:MM format (Local Time) #}
              {% if raw_end not in ['unknown', 'unavailable', None] %}
                  {% set end_time = as_timestamp(raw_end) | timestamp_custom('%H:%M') %}
              {% else %}
                  {% set end_time = 'Calculating...' %}
              {% endif %}

              {
                "title": "⚡ Car Charging Started",
                "message": "Charging at {{ power }} kW. Ready by: {{ end_time }}",
                "tag": "car_charging",
                "critical": false
              }
            {% elif trigger.id == 'charging_full' %}
              {% set range = states('sensor.[LICENSE_PLATE]_range_electric') %}
              {
                "title": "🔋 Car Fully Charged",
                "message": "Battery is 100%. Range: {{ range }} km.",
                "tag": "car_charging",
                "critical": false
              }
            {% elif trigger.id == 'climate_started' %}
              {
                "title": "🚗 Car Climate",
                "message": "Pre-conditioning has started.",
                "tag": "car_climate",
                "critical": false
              }
            {% elif trigger.id == 'climate_stopped' %}
              {
                "title": "🚗 Car Climate",
                "message": "Pre-conditioning finished.",
                "tag": "car_climate",
                "critical": false
              }
            {% elif trigger.id == 'warn_tire' %}
              {
                "title": "⚠️ Car Warning",
                "message": "Check Tire Pressure!",
                "tag": "car_warning",
                "critical": false
              }
            {% elif trigger.id == 'warn_brake' %}
              {
                "title": "🚨 Car Critical",
                "message": "Low Brake Fluid Warning! Check immediately.",
                "tag": "car_warning",
                "critical": true
              }
            {% elif trigger.id == 'warn_coolant' %}
              {
                "title": "⚠️ Car Warning",
                "message": "Low Coolant Level.",
                "tag": "car_warning",
                "critical": true
              }
            {% elif trigger.id == 'warn_wash_water' %}
              {
                "title": "💧 Car Warning",
                "message": "Low Washer Fluid Level.",
                "tag": "car_warning",
                "critical": false
              }
            {% endif %}
      - service: script.notify_smart_master
        data:
          category: car
          title: "{{ (notification_data | from_json).title }}"
          message: "{{ (notification_data | from_json).message }}"
          tag: "{{ (notification_data | from_json).tag }}"
          critical: "{{ (notification_data | from_json).critical }}"
    mode: queued
# ------------------------------------------------------------------------------
# Changelog
# ------------------------------------------------------------------------------
# 2.0.3 (2025-12-07): Added Changelog footer.
# 2.0.2 (2025-12-07): Added unique_id to automation for UI editing.
# 2.0.1 (2025-12-07): Moved VIN to secrets. Updated automation description.
# 2.0.0 (2025-12-07): Initial consolidation of Package A, B, and UI Automation.
# ------------------------------------------------------------------------------

```
