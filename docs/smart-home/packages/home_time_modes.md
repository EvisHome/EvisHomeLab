---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Home Time Modes

**Version:** 1.0.0  
**Description:** Parametric Time-of-Day Logic

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/home_time_modes.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
*No linked dashboard views found (Automatic Scan).*
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Home Time Modes
# Version: 1.0.0
# Description: Parametric Time-of-Day Logic
# Dependencies: input_datetime, sun.sun
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1. SETTINGS (Editable from Dashboard)
# ------------------------------------------------------------------------------
input_datetime:
  mode_time_morning:
    name: "Morning Start Time"
    has_date: false
    has_time: true
    initial: "06:30"

  mode_time_day:
    name: "Day Start Time"
    has_date: false
    has_time: true
    initial: "09:00"

  mode_time_evening_fixed:
    name: "Evening Fixed Time"
    has_date: false
    has_time: true
    initial: "18:00"

  mode_time_night:
    name: "Night Start Time"
    has_date: false
    has_time: true
    initial: "23:00"

input_select:
  # RENAMED: Clearer distinction
  house_mode:
    name: "Home Time Mode"
    icon: mdi:home-clock
    options:
      - Morning
      - Day
      - Evening
      - Night

  mode_evening_strategy:
    name: "Evening Strategy"
    icon: mdi:weather-sunset
    options:
      - "Fixed Time"
      - "Sunset + Offset"

input_number:
  mode_evening_sun_offset:
    name: "Sunset Offset (Minutes)"
    icon: mdi:timer-sand
    min: -120
    max: 120
    step: 10
    unit_of_measurement: min
    mode: box

# ------------------------------------------------------------------------------
# 2. LOGIC
# ------------------------------------------------------------------------------
automation:
  - alias: "System: Manager Home Time Modes"
    id: system_manager_home_time_modes
    mode: restart
    trigger:
      # Trigger on Time Inputs
      - platform: time
        at: input_datetime.mode_time_morning
        id: "Morning"
      - platform: time
        at: input_datetime.mode_time_day
        id: "Day"
      - platform: time
        at: input_datetime.mode_time_night
        id: "Night"
      - platform: time
        at: input_datetime.mode_time_evening_fixed
        id: "Evening_Fixed"

      # Trigger on Sun
      - platform: sun
        event: sunset
        id: "Evening_Sun"

      # Failsafe
      - platform: time_pattern
        minutes: "/15"
        id: "Heartbeat"

    action:
      - choose:
          # --- MORNING ---
          - conditions:
              - condition: trigger
                id: "Morning"
            sequence:
              - service: input_select.select_option
                target:
                  entity_id: input_select.house_mode
                data: { option: "Morning" }

          # --- DAY ---
          - conditions:
              - condition: trigger
                id: "Day"
            sequence:
              - service: input_select.select_option
                target:
                  entity_id: input_select.house_mode
                data: { option: "Day" }

          # --- NIGHT ---
          - conditions:
              - condition: trigger
                id: "Night"
            sequence:
              - service: input_select.select_option
                target:
                  entity_id: input_select.house_mode
                data: { option: "Night" }

          # --- EVENING (Complex Logic) ---
          - conditions:
              - condition: or
                conditions:
                  # Fixed Strategy
                  - condition: and
                    conditions:
                      - condition: trigger
                        id: "Evening_Fixed"
                      - condition: state
                        entity_id: input_select.mode_evening_strategy
                        state: "Fixed Time"
                  # Sun Strategy
                  - condition: and
                    conditions:
                      - condition: trigger
                        id: "Evening_Sun"
                      - condition: state
                        entity_id: input_select.mode_evening_strategy
                        state: "Sunset + Offset"
            sequence:
              # Handle Offset
              - if:
                  - condition: state
                    entity_id: input_select.mode_evening_strategy
                    state: "Sunset + Offset"
                then:
                  - delay:
                      minutes: "{{ states('input_number.mode_evening_sun_offset') | int(0) }}"

              - service: input_select.select_option
                target:
                  entity_id: input_select.house_mode
                data: { option: "Evening" }

```
