---
tags:
  - dashboard
  - view
  - automated
---

# CAR

**Dashboard:** Persons  
**Path:** `car`

## Related Packages
This view contains entities managed by:

* [Car](../../packages/car.md)


![View Screenshot](../../../assets/images/dashboards/dashboard_dashboard-persons_car.png)

## Configuration
```yaml
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
      entity: switch.xpb_358_pre_entry_climate_control
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
                  secondary: '{{ states(''sensor.xpb_358_fuel_level'') }}% | {{ states(''sensor.xpb_358_range_liquid'')
                    }} km range'
                  icon: mdi:gas-station
                  features_position: bottom
                  color: "{% set fuel = states('sensor.xpb_358_fuel_level') | int\
                    \ %} {% if fuel < 20 %}\n  darkred\n{% elif fuel < 50 %}\n  yellow\n\
                    {% else %}\n  darkgreen\n{% endif %}\n"
                  card_mod:
                    style: "ha-card {\n  background: linear-gradient(\n    to right,\n\
                      \    orange {{ states('sensor.xpb_358_fuel_level') }}%,\n  \
                      \  var(--card-background-color) {{ states('sensor.xpb_358_fuel_level')\
                      \ }}%\n  );\n  );\n  background-size: 100% 100%;\n  background-repeat:\
                      \ no-repeat;\n  border-radius: 12px;\n}\n"
                - type: custom:mushroom-template-card
                  entity: sensor.ev_battery_level
                  primary: EV Charge
                  secondary: '{{ states(''sensor.xpb_358_state_of_charge'') }}% |
                    {{ states(''sensor.xpb_358_range_electric'') }} km range

                    '
                  icon: mdi:car-electric
                  tap_action:
                    action: more-info
                  hold_action:
                    action: more-info
                  color: "{% set charge = states('sensor.xpb_358_state_of_charge')\
                    \ | int %} {% if charge < 20 %}\n  red\n{% elif charge < 50 %}\n\
                    \  yellow\n{% else %}\n  lightgreen\n{% endif %}\n"
                  features_position: bottom
                  card_mod:
                    style: "ha-card {\n  --charge: {{ states('sensor.xpb_358_state_of_charge')\
                      \ }}%;\n  background: linear-gradient(\n    to right,\n    green\
                      \ var(--charge),\n    var(--card-background-color) var(--charge)\n\
                      \  );\n  background-size: 100% 100%;\n  background-repeat: no-repeat;\n\
                      \  border-radius: 12px;\n}\n"
              - type: custom:scheduler-card
                include:
                - switch.xpb_358_pre_entry_climate_control
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
                  style: "ha-card {\n  border-radius: 12px;\n  box-shadow: var(--ha-card-box-shadow);\n\
                    \  background-color: var(--card-background-color);\n  font-family:\
                    \ var(--mush-font-family, \"Roboto\", sans-serif);\n}\n.card-header\
                    \ {\n  font-size: 1.2em;\n  font-weight: 500;\n  padding-bottom:\
                    \ 8px;\n}\n.schedule-row {\n  border-bottom: 1px solid var(--divider-color);\n\
                    }\n"
              - type: map
                entities:
                - entity: person.car
                hours_to_show: 48
                aspect_ratio: '1.5'
                default_zoom: 15
                theme_mode: auto
      card_mod:
        style: "ha-card {\n  /* Moves border logic here from original for border display\
          \ */\n  {% if is_state('sensor.xpb_358_ignition_state','4') %}\n    border:\
          \ 3px solid rgba(36, 255, 0, 0.8);\n  {% elif is_state('sensor.xpb_358_ignition_state','2')\
          \ %}\n    border: 3px solid rgba(255, 163, 0, 0.8);\n  {% else %}\n    border:\
          \ 0px solid rgba(0, 0, 0, 0);\n  {% endif %}\n}\n"
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 4
    - type: conditional
      conditions:
      - entity: device_tracker.xbp_358_device_tracker
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
      - entity: device_tracker.xbp_358_device_tracker
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
      entity: sensor.xpb_358_state_of_charge
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
          - animation: "[[[\n  if (states['binary_sensor.xpb_358_charging_active'].state\
              \ == 'on') {\n    return 'blink 1s ease infinite';\n  } else {\n   \
              \ return 'none';\n  }\n]]]\n"
      - operator: ==
        value: 'off'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.xpb_358_park_brake_status
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
      entity: lock.xpb_358_lock
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
      entity: binary_sensor.xpb_358_windows_closed
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
      entity: binary_sensor.xpb_358_low_wash_water_warning
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
        style: ":host {\n  {% if '[[entity]]' == '' %}\n    display: none;\n  {% endif\
          \ %}\n}\n"
    - type: custom:button-card
      template: area_status_indicator
      entity: binary_sensor.xpb_358_tire_warning
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
      entity: switch.xpb_358_pre_entry_climate_control
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
    secondary: '{{ states(''sensor.xpb_358_fuel_level'') }}% | {{ states(''sensor.xpb_358_range_liquid'')
      }} km range'
    icon: mdi:gas-station
    features_position: bottom
    color: "{% set fuel = states('sensor.xpb_358_fuel_level') | int %} {% if fuel\
      \ < 20 %}\n  darkred\n{% elif fuel < 50 %}\n  yellow\n{% else %}\n  darkgreen\n\
      {% endif %}\n"
    card_mod:
      style: "ha-card {\n  background: linear-gradient(\n    to right,\n    orange\
        \ {{ states('sensor.xpb_358_fuel_level') }}%,\n    var(--card-background-color)\
        \ {{ states('sensor.xpb_358_fuel_level') }}%\n  );\n  );\n  background-size:\
        \ 100% 100%;\n  background-repeat: no-repeat;\n  border-radius: 12px;\n}\n"
  - type: custom:mushroom-template-card
    entity: sensor.ev_battery_level
    primary: EV Charge
    secondary: '{{ states(''sensor.xpb_358_state_of_charge'') }}% | {{ states(''sensor.xpb_358_range_electric'')
      }} km range

      '
    icon: mdi:car-electric
    tap_action:
      action: more-info
    hold_action:
      action: more-info
    color: "{% set charge = states('sensor.xpb_358_state_of_charge') | int %} {% if\
      \ charge < 20 %}\n  red\n{% elif charge < 50 %}\n  yellow\n{% else %}\n  lightgreen\n\
      {% endif %}\n"
    features_position: bottom
    card_mod:
      style: "ha-card {\n  --charge: {{ states('sensor.xpb_358_state_of_charge') }}%;\n\
        \  background: linear-gradient(\n    to right,\n    green var(--charge),\n\
        \    var(--card-background-color) var(--charge)\n  );\n  background-size:\
        \ 100% 100%;\n  background-repeat: no-repeat;\n  border-radius: 12px;\n}\n"
  - type: custom:mushroom-template-card
    primary: Doors
    secondary: "{% set status = states(entity) %}\n{% if status == 'open' %}\n  Open\n\
      {% else %}\n  Closed\n{% endif %}"
    icon: mdi:car-door
    tap_action:
      action: more-info
    double_tap_action:
      action: none
    hold_action:
      action: more-info
    entity: binary_sensor.car_doors
    badge_color: "{% set status = states('switch.car_doors') %}\n{% if status == 'off'\
      \ %}\n  red\n{% else %}\n  green\n{% endif %}"
    badge_icon: "{% set status = states('switch.car_doors') %}\n{% if status == 'off'\
      \ %}\n  mdi:lock-off-outline\n{% else %}\n  mdi:lock\n{% endif %}"
    color: "{% set status = states(entity) %}\n{% if status == 'open' %}\n  red\n\
      {% else %}\n  disabled\n{% endif %}"
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
  - type: custom:mushroom-template-card
    primary: Windows
    secondary: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  Open\n\
      {% else %}\n  Closed\n{% endif %}"
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
    color: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  red\n{%\
      \ else %}\n  disabled\n{% endif %}"
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
    icon_tap_action:
      action: more-info
  - type: custom:mushroom-template-card
    entity: switch.xpb_358_pre_entry_climate_control
    primary: Pre AC
    secondary: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  Off\n\
      {% else %}\n  On\n{% endif %}"
    icon: mdi:air-conditioner
    tap_action:
      action: more-info
    double_tap_action:
      action: more-info
    hold_action:
      action: more-info
    badge_icon: ''
    badge_color: ''
    color: "{% set status = states(entity) %}\n{% if status == 'off' %}\n  disabled\n\
      {% else %}\n  green\n{% endif %}"
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    vertical: true
    icon_tap_action:
      action: more-info
  - include:
    - switch.xpb_358_pre_entry_climate_control
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
      style: "ha-card {\n  border-radius: 12px;\n  box-shadow: var(--ha-card-box-shadow);\n\
        \  background-color: var(--card-background-color);\n  font-family: var(--mush-font-family,\
        \ \"Roboto\", sans-serif);\n}\n.card-header {\n  font-size: 1.2em;\n  font-weight:\
        \ 500;\n  padding-bottom: 8px;\n}\n.schedule-row {\n  border-bottom: 1px solid\
        \ var(--divider-color);\n}\n"
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
      entity: switch.xpb_358_pre_entry_climate_control
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
      entity: binary_sensor.xpb_358_low_brake_fluid_warning
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
      entity: sensor.xpb_358_starter_battery_state
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
      entity: binary_sensor.xpb_358_low_coolant_level_warning
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
      entity: binary_sensor.xpb_358_low_wash_water_warning
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
      entity: sensor.xpb_358_lock
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
      entity: sensor.xpb_358_tire_pressure_front_right
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
      entity: sensor.xpb_358_tire_pressure_rear_right
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
      entity: sensor.xpb_358_tire_pressure_front_left
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
      entity: sensor.xpb_358_tire_pressure_rear_left
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
          - animation: "[[[\n  if (states['binary_sensor.car_glc_door_front_right'].state\
              \ == 'off') {\n    return 'blink 1s ease infinite';\n  } else {\n  \
              \  return 'none';\n  }\n]]]\n"
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
          - animation: "[[[\n  if (states['binary_sensor.car_glc_door_rear_left'].state\
              \ == 'off') {\n    return 'blink 1s ease infinite';\n  } else {\n  \
              \  return 'none';\n  }\n]]]\n"
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
          - animation: "[[[\n  if (states['binary_sensor.car_glc_door_front_left'].state\
              \ == 'off') {\n    return 'blink 1s ease infinite';\n  } else {\n  \
              \  return 'none';\n  }\n]]]\n"
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
          - animation: "[[[\n  if (states['binary_sensor.car_glc_door_rear_right'].state\
              \ == 'off') {\n    return 'blink 1s ease infinite';\n  } else {\n  \
              \  return 'none';\n  }\n]]]\n"
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
          - animation: "[[[\n  if (states['binary_sensor.xpb_358_charging_active'].state\
              \ == 'on') {\n    return 'blink 1s ease infinite';\n  } else {\n   \
              \ return 'none';\n  }\n]]]\n"
      - operator: ==
        value: 'off'
        icon: mdi:ev-plug-type2
        styles:
          icon:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.xpb_358_charging_power
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
        - display: "[[[\n  // Get the state of the power sensor\n  var power = states['sensor.xpb_358_charging_power'].state;\n\
            \n  // Hide if power is 0 OR if the main entity is 0\n  if (parseFloat(power)\
            \ == 0 || entity.state == '0') {\n    return 'none';\n  } else {\n   \
            \ return 'block'; // Show the card\n  }\n]]]\n"
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.xpb_358_charging_power
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
        - display: "[[[\n  // Get the state of the power sensor\n  var power = states['sensor.xpb_358_charging_power'].state;\n\
            \n  // Hide if power is 0 OR if the main entity is 0\n  if (parseFloat(power)\
            \ == 0 || entity.state == '0') {\n    return 'none';\n  } else {\n   \
            \ return 'block'; // Show the card\n  }\n]]]\n"
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
        - display: "[[[\n  // Get the state of the power sensor\n  var power = states['sensor.xpb_358_charging_power'].state;\n\
            \n  // Hide if power is 0 OR if the main entity is 0\n  if (parseFloat(power)\
            \ == 0 || entity.state == '0') {\n    return 'none';\n  } else {\n   \
            \ return 'block'; // Show the card\n  }\n]]]\n"
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
        icon: "[[[\n  var soc = states['sensor.xpb_358_state_of_charge'].state;\n\
          \  if (soc > 75) {\n    return 'mdi:battery-charging-high';\n  } else if\
          \ (soc > 25) {\n    return 'mdi:battery-charging-medium';\n  } else {\n\
          \    return 'mdi:battery-charging-low';\n  }\n]]]\n"
        styles:
          icon:
          - color: "[[[\n  var soc = states['sensor.xpb_358_state_of_charge'].state;\n\
              \  if (soc > 75) {\n    return 'lightgreen';\n  } else if (soc > 25)\
              \ {\n    return 'orange';\n  } else {\n    return 'red';\n  }\n]]]\n"
          - animation: "[[[\n  if (states['binary_sensor.xpb_358_charging_active'].state\
              \ == 'on') {\n    return 'blink 1s ease infinite';\n  } else {\n   \
              \ return 'none';\n  }\n]]]\n"
      - operator: ==
        value: 'on'
        styles:
          card:
          - display: none
    - type: custom:button-card
      template: area_status_indicator
      entity: sensor.xpb_358_state_of_charge
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
    - entity: sensor.xpb_358_odometer
      name: Odometer
      secondary_info: none
    - entity: sensor.xpb_358_electric_consumption_reset
      name: Fuel Consumption
    - entity: sensor.xpb_358_liquid_consumption_reset
      name: Electric Consumption
max_columns: 4
path: car
subview: true

```
