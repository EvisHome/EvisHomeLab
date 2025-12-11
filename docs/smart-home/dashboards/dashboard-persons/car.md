---
tags:
  - dashboard
  - view
  - automated
---

# CAR

**Dashboard:** Persons  
**Path:** `car`

<!-- START_SUMMARY -->
The **Car Dashboard** provides a centralized command center for the Mercedes GLC, unifying vehicle health monitoring and remote control. It combines real-time data metrics (fuel, battery, tire pressure) with actionable controls (locks, climate pre-conditioning). The interface features a visual "Digital Twin" of the car to intuitively display status alerts, warning indicators (low fluids, unlocked doors), and charging progress, alongside a real-time location tracker.
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_car.png)

## Related Packages
This view contains entities managed by:

* [Car](../../packages/car.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:button-card`
* `custom:card-mod`
* `custom:mushroom-template-card`
* `custom:scheduler-card`


## Configuration
```yaml+jinja
title: CAR
badges: []
cards: []
type: sections
sections:
- type: grid
  cards:
  - type: picture-elements
    image: local/car/Car-BG.png
    elements:
    - type: custom:button-card
      template:
      - area_base_overlay
      entity: switch.[LICENSE_PLATE]_pre_entry_climate_control
      tap_action:
        action: navigate
        navigation_path: /dashboard-persons/car
      hold_action:
        action: toggle
      double_tap_action:
        action: fire-dom-event
        browser_mod:
          service: browser_mod.popup
          data:
            title: CAR
            content:
              type: vertical-stack
              cards:
              - type: horizontal-stack
                cards:
                - type: custom:mushroom-template-card
                  entity: sensor.fuel_level
                  primary: Fuel Level
                  secondary: '{{ states(''sensor.[LICENSE_PLATE]_fuel_level'') }}%
                    | {{ states(''sensor.[LICENSE_PLATE]_range_liquid'') }} km range'
                  icon: mdi:gas-station
                  features_position: bottom
                  color: |-
                    {% set fuel = states('sensor.[LICENSE_PLATE]_fuel_level') | int %} {% if fuel < 20 %}
                      darkred
                    {% elif fuel < 50 %}
                      yellow
                    {% else %}
                      darkgreen
                    {% endif %}
                  card_mod:
                    style: |-
                      ha-card {
                        background: linear-gradient(
                          to right,
                          orange {{ states('sensor.[LICENSE_PLATE]_fuel_level') }}%,
                          var(--card-background-color) {{ states('sensor.[LICENSE_PLATE]_fuel_level') }}%
                        );
                        );
                        background-size: 100% 100%;
                        background-repeat: no-repeat;
                        border-radius: 12px;
                      }
                - type: custom:mushroom-template-card
                  entity: sensor.ev_battery_level
                  primary: EV Charge
                  secondary: '{{ states(''sensor.[LICENSE_PLATE]_state_of_charge'')
                    }}% | {{ states(''sensor.[LICENSE_PLATE]_range_electric'') }}
                    km range'
                  icon: mdi:car-electric
                  tap_action:
                    action: more-info
                  hold_action:
                    action: more-info
                  color: |-
                    {% set charge = states('sensor.[LICENSE_PLATE]_state_of_charge') | int %} {% if charge < 20 %}
                      red
                    {% elif charge < 50 %}
                      yellow
                    {% else %}
                      lightgreen
                    {% endif %}
                  features_position: bottom
                  card_mod:
                    style: |-
                      ha-card {
                        --charge: {{ states('sensor.[LICENSE_PLATE]_state_of_charge') }}%;
                        background: linear-gradient(
                          to right,
                          green var(--charge),
                          var(--card-background-color) var(--charge)
                        );
                        background-size: 100% 100%;
                        background-repeat: no-repeat;
                        border-radius: 12px;
                      }
              - type: custom:scheduler-card
                include:
                - switch.[LICENSE_PLATE]_pre_entry_climate_control
                exclude: []
                discover_existing: false
                title: true
                show_header_toggle: false
                time_step: 5
                default_editor: single
                display_options:
                  primary_info: default
                  secondary_info:
                  - time
                  icon: action
                sort_by:
                - state
                - relative-time
                customize: {}
                tags:
                - Car
                exclude_tags: []
                card_mod:
                  style: |-
                    ha-card {
                      border-radius: 12px;
                      box-shadow: var(--ha-card-box-shadow);
                      background-color: var(--card-background-color);
                      font-family: var(--mush-font-family, "Roboto", sans-serif);
                    }
                    .card-header {
                      font-size: 1.2em;
                      font-weight: 500;
                      padding-bottom: 8px;
                    }
                    .schedule-row {
                      border-bottom: 1px solid var(--divider-color);
                    }
              - type: map
                entities:
                - entity: person.car
                hours_to_show: 48
                aspect_ratio: '1.5'
                default_zoom: 15
                theme_mode: auto
      card_mod:
        style: |-
          ha-card {
            /* Moves border logic here from original for border display */
            {% if is_state('sensor.[LICENSE_PLATE]_ignition_state','4') %}
              border: 3px solid rgba(36, 255, 0, 0.8);
            {% elif is_state('sensor.[LICENSE_PLATE]_ignition_state','2') %}
              border: 3px solid rgba(255, 163, 0, 0.8);
            {% else %}
              border: 0px solid rgba(0, 0, 0, 0);
            {% endif %}
          }
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 4
    - type: conditional
      conditions:
      - entity: device_tracker.[LICENSE_PLATE]_device_tracker
        state: home
      elements:
      - type: image
        image: local/car/GLC-home.png
        style:
          left: 50%
          top: 30%
          width: 80%
          opacity: 100%
          z-index: 2
    - type: conditional
      conditions:
      - entity: device_tracker.[LICENSE_PLATE]_device_tracker
        state: not_home
      elements:
      - type: image
        image: local/car/GLC-back.png
        style:
          left: 50%
          top: 50%
          width: 65%
          opacity: 100%
          z-index: 2
    - type: conditional
      conditions:
      - entity: binary_sensor.car_engine
        state: 'on'
      elements:
      - type: image
        image: local/car/road.png
        style:
          left: 50%
          top: 65%
          width: 100%
          opacity: 100%
          z-index: 2
    - type: custom:button-card
      template:
      - area_text_element
      name: Car
      style:
        top: 0%
        left: 50%
        width: 100%
        height: 100%
        z-index: 2
        container-type: inline-size
    - type: custom:button-card
      template: area_text_element
      entity: sensor.[LICENSE_PLATE]_state_of_charge
      show_name: false
      show_icon: false
      show_state: true
      style:
        top: 0%
        left: 50%
        width: 100%
        height: 100%
        z-index: 2
        container-type: inline-size
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_charge_plug
      icon: mdi:ev-plug-type2
      layout: vertical
      style:
        top: 44%
        left: 90%
        width: 12%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: '#088CF8'
          - animation: |-
              [[[
                if (states['binary_sensor.[LICENSE_PLATE]_charging_active'].state == 'on') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_park_brake_status
      layout: vertical
      style:
        top: 75%
        left: 10%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: orange
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: lock.[LICENSE_PLATE]_lock
      icon: mdi:lock-open-variant
      layout: vertical
      style:
        top: 75%
        left: 26%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: unlocked
        styles:
          icon:
          - animation: blink 0.5s linear infinite
            color: rgba(253,89,89,1)
      - operator: ==
        value: locked
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_windows_closed
      layout: vertical
      style:
        top: 75%
        left: 42%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        styles:
          icon:
          - animation: blink 0.5s ease infinite
            color: rgba(253,89,89,1)
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_low_wash_water_warning
      layout: vertical
      style:
        top: 75%
        left: 58%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - animation: blink 1s ease infinite
            color: '#088CF8'
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
      card_mod:
        style: |-
          :host {
            {% if '[[entity]]' == '' %}
              display: none;
            {% endif %}
          }
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_tire_warning
      icon: mdi:tire
      layout: vertical
      style:
        top: 75%
        left: 74%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: rgba(253,89,89,1)
            animation: blink 1s ease infinite
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: switch.[LICENSE_PLATE]_pre_entry_climate_control
      icon: mdi:fan
      layout: vertical
      style:
        top: 75%
        left: 90%
        width: 14%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - animation: rotating 1s linear infinite
            color: '#21ff21'
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: switch.schedule_car_pre_entry_climate_control
      icon: mdi:clock-outline
      layout: vertical
      style:
        top: 85%
        left: 94%
        width: 6%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: orange
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
  - type: custom:mushroom-template-card
    entity: sensor.fuel_level
    primary: Fuel Level
    secondary: '{{ states(''sensor.[LICENSE_PLATE]_fuel_level'') }}% | {{ states(''sensor.[LICENSE_PLATE]_range_liquid'')
      }} km range'
    icon: mdi:gas-station
    features_position: bottom
    color: |-
      {% set fuel = states('sensor.[LICENSE_PLATE]_fuel_level') | int %} {% if fuel < 20 %}
        darkred
      {% elif fuel < 50 %}
        yellow
      {% else %}
        darkgreen
      {% endif %}
    card_mod:
      style: |-
        ha-card {
          background: linear-gradient(
            to right,
            orange {{ states('sensor.[LICENSE_PLATE]_fuel_level') }}%,
            var(--card-background-color) {{ states('sensor.[LICENSE_PLATE]_fuel_level') }}%
          );
          );
          background-size: 100% 100%;
          background-repeat: no-repeat;
          border-radius: 12px;
        }
  - type: custom:mushroom-template-card
    entity: sensor.ev_battery_level
    primary: EV Charge
    secondary: '{{ states(''sensor.[LICENSE_PLATE]_state_of_charge'') }}% | {{ states(''sensor.[LICENSE_PLATE]_range_electric'')
      }} km range'
    icon: mdi:car-electric
    tap_action:
      action: more-info
    hold_action:
      action: more-info
    color: |-
      {% set charge = states('sensor.[LICENSE_PLATE]_state_of_charge') | int %} {% if charge < 20 %}
        red
      {% elif charge < 50 %}
        yellow
      {% else %}
        lightgreen
      {% endif %}
    features_position: bottom
    card_mod:
      style: |-
        ha-card {
          --charge: {{ states('sensor.[LICENSE_PLATE]_state_of_charge') }}%;
          background: linear-gradient(
            to right,
            green var(--charge),
            var(--card-background-color) var(--charge)
          );
          background-size: 100% 100%;
          background-repeat: no-repeat;
          border-radius: 12px;
        }
  - type: custom:mushroom-template-card
    primary: Doors
    secondary: |-
      {% set status = states(entity) %}
      {% if status == 'open' %}
        Open
      {% else %}
        Closed
      {% endif %}
    icon: mdi:car-door
    tap_action:
      action: more-info
    double_tap_action:
      action: none
    hold_action:
      action: more-info
    entity: binary_sensor.car_doors
    badge_color: |-
      {% set status = states('switch.car_doors') %}
      {% if status == 'off' %}
        red
      {% else %}
        green
      {% endif %}
    badge_icon: |-
      {% set status = states('switch.car_doors') %}
      {% if status == 'off' %}
        mdi:lock-off-outline
      {% else %}
        mdi:lock
      {% endif %}
    color: |-
      {% set status = states(entity) %}
      {% if status == 'open' %}
        red
      {% else %}
        disabled
      {% endif %}
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
  - type: custom:mushroom-template-card
    primary: Windows
    secondary: |-
      {% set status = states(entity) %}
      {% if status == 'off' %}
        Open
      {% else %}
        Closed
      {% endif %}
    icon: mdi:car-door
    tap_action:
      action: more-info
    double_tap_action:
      action: none
    entity: switch.car_windows
    badge_icon: ''
    badge_color: ''
    hold_action:
      action: more-info
    color: |-
      {% set status = states(entity) %}
      {% if status == 'off' %}
        red
      {% else %}
        disabled
      {% endif %}
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
    icon_tap_action:
      action: more-info
  - type: custom:mushroom-template-card
    entity: switch.[LICENSE_PLATE]_pre_entry_climate_control
    primary: Pre AC
    secondary: |-
      {% set status = states(entity) %}
      {% if status == 'off' %}
        Off
      {% else %}
        On
      {% endif %}
    icon: mdi:air-conditioner
    tap_action:
      action: more-info
    double_tap_action:
      action: more-info
    hold_action:
      action: more-info
    badge_icon: ''
    badge_color: ''
    color: |-
      {% set status = states(entity) %}
      {% if status == 'off' %}
        disabled
      {% else %}
        green
      {% endif %}
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
    icon_tap_action:
      action: more-info
  - include:
    - switch.[LICENSE_PLATE]_pre_entry_climate_control
    exclude: []
    discover_existing: false
    title: true
    show_header_toggle: false
    time_step: 5
    default_editor: single
    display_options:
      primary_info: default
      secondary_info:
      - time
      icon: action
    sort_by:
    - state
    - relative-time
    customize: {}
    tags:
    - Car
    exclude_tags: []
    type: custom:scheduler-card
    card_mod:
      style: |-
        ha-card {
          border-radius: 12px;
          box-shadow: var(--ha-card-box-shadow);
          background-color: var(--card-background-color);
          font-family: var(--mush-font-family, "Roboto", sans-serif);
        }
        .card-header {
          font-size: 1.2em;
          font-weight: 500;
          padding-bottom: 8px;
        }
        .schedule-row {
          border-bottom: 1px solid var(--divider-color);
        }
  - type: map
    entities:
    - entity: person.car
    hours_to_show: 48
    aspect_ratio: '1.5'
    default_zoom: 15
    theme_mode: auto
- type: grid
  cards:
  - type: picture-elements
    image: local/car/Car-BG.png
    aspect_ratio: '1:1'
    elements:
    - type: custom:button-card
      template:
      - area_base_overlay
      entity: switch.[LICENSE_PLATE]_pre_entry_climate_control
      tap_action:
        action: navigate
        navigation_path: /dashboard-persons/car
      hold_action:
        action: toggle
      double_tap_action:
        action: fire-dom-event
        browser_mod:
          service: browser_mod.popup
          data:
            title: CAR
            content:
              type: vertical-stack
              cards:
              - type: custom:scheduler-card
                include:
                - switch.car_pre_entry_ac
                exclude: []
                title: Schedules
                discover_existing: false
                tags:
                - Car
                time_step: 5
                sort_by:
                - state
                - relative-time
                display_options:
                  primary_info: default
                  secondary_info:
                  - time
                  - days
                  - additional-tasks
                  icon: action
                show_header_toggle: false
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 4
    - type: image
      image: local/car/GLC-top.png
      style:
        left: 50.5%
        top: 54%
        width: 140%
        opacity: 100%
        z-index: 2
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_low_brake_fluid_warning
      layout: vertical
      style:
        top: 9%
        left: 30%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: orange
            animation: blink 1s ease infinite
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_starter_battery_state
      layout: vertical
      style:
        top: 9%
        left: 40%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: '>'
        value: '0'
        styles:
          icon:
          - color: orange
            animation: blink 1s ease infinite
      - operator: ==
        value: '0'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_low_coolant_level_warning
      layout: vertical
      style:
        top: 9%
        left: 60%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: orange
            animation: blink 1s ease infinite
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.[LICENSE_PLATE]_low_wash_water_warning
      layout: vertical
      style:
        top: 9%
        left: 70%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: orange
            animation: blink 1s ease infinite
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_lock
      icon: mdi:lock
      layout: vertical
      style:
        top: 9%
        left: 50%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: '2'
        styles:
          icon:
          - color: lightgreen
      - operator: '!='
        value: '2'
        icon: mdi:lock-open-variant
        styles:
          icon:
          - color: orange
            animation: blink 1s ease infinite
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_tire_pressure_front_right
      icon: mdi:tire
      show_state: true
      layout: vertical
      style:
        top: 25%
        left: 80%
        width: 12%
        z-index: 2
        container-type: inline-size
      state:
      - operator: '>'
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: lightgreen
      - operator: <=
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: orange
            animate: blink 1s ease infinite
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_tire_pressure_rear_right
      icon: mdi:tire
      show_state: true
      layout: vertical
      style:
        top: 75%
        left: 80%
        width: 12%
        z-index: 2
        container-type: inline-size
      state:
      - operator: '>'
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: lightgreen
      - operator: <=
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: orange
            animate: blink 1s ease infinite
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_tire_pressure_front_left
      icon: mdi:tire
      show_state: true
      layout: vertical
      style:
        top: 25%
        left: 20%
        width: 12%
        z-index: 2
        container-type: inline-size
      state:
      - operator: '>'
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: lightgreen
      - operator: <=
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: orange
            animate: blink 1s ease infinite
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_tire_pressure_rear_left
      icon: mdi:tire
      show_state: true
      layout: vertical
      style:
        top: 75%
        left: 20%
        width: 12%
        z-index: 2
        container-type: inline-size
      state:
      - operator: '>'
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: lightgreen
      - operator: <=
        value: '2'
        styles:
          card:
          - font-size: 24cqw
          icon:
          - color: orange
            animate: blink 1s ease infinite
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_glc_lock_front_right
      icon: mdi:car-door
      layout: vertical
      style:
        top: 45%
        left: 25%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        styles:
          icon:
          - color: orange
          - transform: scaleX(1) rotate(90deg)
          - animation: |-
              [[[
                if (states['binary_sensor.car_glc_door_front_right'].state == 'off') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_glc_lock_rear_left
      icon: mdi:car-door
      layout: vertical
      style:
        top: 55%
        left: 25%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        styles:
          icon:
          - color: orange
          - transform: scaleX(-1) rotate(-90deg)
          - animation: |-
              [[[
                if (states['binary_sensor.car_glc_door_rear_left'].state == 'off') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_glc_lock_front_left
      icon: mdi:car-door
      layout: vertical
      style:
        top: 45%
        left: 75%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        styles:
          icon:
          - color: orange
          - transform: scaleX(-1) rotate(90deg)
          - animation: |-
              [[[
                if (states['binary_sensor.car_glc_door_front_left'].state == 'off') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_glc_lock_rear_right
      icon: mdi:car-door
      layout: vertical
      style:
        top: 55%
        left: 75%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        styles:
          icon:
          - color: orange
          - transform: scaleX(1) rotate(-90deg)
          - animation: |-
              [[[
                if (states['binary_sensor.car_glc_door_rear_right'].state == 'off') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_charge_plug
      icon: mdi:ev-plug-type2
      layout: vertical
      style:
        top: 92%
        left: 50%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'on'
        styles:
          icon:
          - color: '#088CF8'
          - animation: |-
              [[[
                if (states['binary_sensor.[LICENSE_PLATE]_charging_active'].state == 'on') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'off'
        icon: mdi:ev-plug-type2
        styles:
          icon:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_charging_power
      show_icon: false
      show_state: true
      layout: vertical
      style:
        top: 89%
        left: 62%
        width: 25%
        z-index: 2
        container-type: inline-size
      styles:
        state:
        - font-size: 13cqw
          color: '#088CF8'
        card:
        - display: |-
            [[[
              // Get the state of the power sensor
              var power = states['sensor.[LICENSE_PLATE]_charging_power'].state;

              // Hide if power is 0 OR if the main entity is 0
              if (parseFloat(power) == 0 || entity.state == '0') {
                return 'none';
              } else {
                return 'block'; // Show the card
              }
            ]]]
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_charging_power
      show_icon: false
      show_name: true
      show_state: false
      name: 100% @
      layout: vertical
      style:
        top: 95%
        left: 63%
        width: 25%
        z-index: 2
        container-type: inline-size
      styles:
        state:
        - font-size: 13cqw
          color: '#088CF8'
        card:
        - display: |-
            [[[
              // Get the state of the power sensor
              var power = states['sensor.[LICENSE_PLATE]_charging_power'].state;

              // Hide if power is 0 OR if the main entity is 0
              if (parseFloat(power) == 0 || entity.state == '0') {
                return 'none';
              } else {
                return 'block'; // Show the card
              }
            ]]]
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.car_charge_ready
      show_icon: false
      show_state: true
      layout: vertical
      style:
        top: 95%
        left: 75%
        width: 25%
        z-index: 2
        container-type: inline-size
      styles:
        state:
        - font-size: 13cqw
          color: '#088CF8'
        card:
        - display: |-
            [[[
              // Get the state of the power sensor
              var power = states['sensor.[LICENSE_PLATE]_charging_power'].state;

              // Hide if power is 0 OR if the main entity is 0
              if (parseFloat(power) == 0 || entity.state == '0') {
                return 'none';
              } else {
                return 'block'; // Show the card
              }
            ]]]
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.car_charge_plug
      icon: mdi:battery-charging-high
      layout: vertical
      style:
        top: 92%
        left: 50%
        width: 8%
        z-index: 2
        container-type: inline-size
      state:
      - operator: ==
        value: 'off'
        icon: |-
          [[[
            var soc = states['sensor.[LICENSE_PLATE]_state_of_charge'].state;
            if (soc > 75) {
              return 'mdi:battery-charging-high';
            } else if (soc > 25) {
              return 'mdi:battery-charging-medium';
            } else {
              return 'mdi:battery-charging-low';
            }
          ]]]
        styles:
          icon:
          - color: |-
              [[[
                var soc = states['sensor.[LICENSE_PLATE]_state_of_charge'].state;
                if (soc > 75) {
                  return 'lightgreen';
                } else if (soc > 25) {
                  return 'orange';
                } else {
                  return 'red';
                }
              ]]]
          - animation: |-
              [[[
                if (states['binary_sensor.[LICENSE_PLATE]_charging_active'].state == 'on') {
                  return 'blink 1s ease infinite';
                } else {
                  return 'none';
                }
              ]]]
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.[LICENSE_PLATE]_state_of_charge
      show_icon: false
      show_state: true
      layout: vertical
      style:
        top: 92%
        left: 38%
        width: 25%
        z-index: 2
        container-type: inline-size
      styles:
        card:
        - font-size: 18cqw
      state:
      - operator: '>'
        value: 75
        styles:
          card:
          - color: lightgreen
      - operator: '>'
        value: 25
        styles:
          card:
          - color: orange
      - operator: default
        styles:
          card:
          - color: red
  - type: entities
    entities:
    - entity: sensor.[LICENSE_PLATE]_odometer
      name: Odometer
      secondary_info: none
    - entity: sensor.[LICENSE_PLATE]_electric_consumption_reset
      name: Fuel Consumption
    - entity: sensor.[LICENSE_PLATE]_liquid_consumption_reset
      name: Electric Consumption
max_columns: 4
path: car
subview: true

```
