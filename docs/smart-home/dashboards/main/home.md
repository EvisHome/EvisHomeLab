---
tags:
  - dashboard
  - view
  - automated
---

# Home

**Dashboard:** Main Dashboard  
**Path:** `home`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_home.png)

## Related Packages
This view contains entities managed by:

* [Aqara W500](../../packages/aqara_w500.md)
* [Car](../../packages/car.md)
* [Dishwasher](../../packages/dishwasher.md)
* [Fingerprint Management](../../packages/fingerprint_management.md)
* [Nordpool Prices](../../packages/nordpool_prices.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:apexcharts-card`
* `custom:button-card`
* `custom:calendar-card-pro`
* `custom:card-mod`
* `custom:config-template-card`
* `custom:horizon-card`
* `custom:mushroom-entity-card`
* `custom:mushroom-template-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`


## Configuration
```yaml
title: Home
path: home
cards: []
type: sections
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: HOME
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - clock_size: medium
    time_zone: Europe/Helsinki
    time_format: '24'
    show_seconds: true
    type: clock
    grid_options:
      columns: 12
      rows: 2
  - entities:
    - entity: calendar.holidays
      color: '#e63946'
    - entity: calendar.family_calendar
      color: '#457b9d'
    - entity: calendar.energy_management
    days_to_show: 30
    compact_events_to_show: 5
    compact_events_complete_days: true
    filter_duplicates: true
    first_day_of_week: monday
    show_week_numbers: iso
    day_separator_width: 1px
    day_separator_color: '#444444'
    today_indicator: dot
    weekend_weekday_color: orange
    weekend_day_color: orange
    weekend_month_color: orange
    weather:
      position: date
      date:
        show_conditions: true
        show_high_temp: true
        show_low_temp: false
        icon_size: 14px
        font_size: 12px
        color: var(--primary-text-color)
      event:
        show_conditions: true
        show_temp: true
        icon_size: 14px
        font_size: 12px
        color: var(--primary-text-color)
    tap_action:
      action: expand
    hold_action:
      action: navigate
      navigation_path: /calendar
    type: custom:calendar-card-pro
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: WEATHER
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - show_current: true
    show_forecast: true
    type: weather-forecast
    entity: weather.openweathermap
    forecast_type: hourly
    tap_action:
      action: fire-dom-event
      browser_mod:
        service: browser_mod.popup
        data:
          title: Weather
          content:
            type: vertical-stack
            cards:
            - type: weather-forecast
              entity: weather.openweathermap
              show_current: true
              show_forecast: true
              forecast_type: hourly
            - type: entities
              entities:
              - entity: sensor.openweathermap_feels_like_temperature
                name: Feels Like
              - entity: sensor.openweathermap_wind_speed
                name: Wind
              - entity: sensor.backyard_humidity
                name: Backyard Humidity
              - entity: sensor.backyard_temperature
                name: Backyard Temperature
            - type: custom:horizon-card
            - type: weather-forecast
              show_current: false
              show_forecast: true
              entity: weather.forecast_home
              forecast_type: daily
              name: Forecast
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: ENERGY
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:mushroom-template-card
    entity: sensor.nord_pool_fi_current_price
    secondary: 'c/kWh

      NOW

      '
    icon: mdi:currency-eur
    badge_icon: ''
    badge_color: ''
    tap_action:
      action: more-info
    hold_action:
      action: none
    double_tap_action:
      action: none
    color: "{% set high = states('sensor.electricity_today_32nd_highest_price') |\
      \ float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price')\
      \ | float(0) %} {% set price = states(entity) | float(0) %}\n{% if price > high\
      \ %}\n  red\n{% elif price < low %}\n  green\n{% else %}\n  orange\n{% endif\
      \ %}"
    vertical: true
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    multiline_secondary: true
    primary: '{{ (states(entity) | float(0) * 100) | round(1) }} '
  - type: custom:mushroom-template-card
    entity: sensor.electricity_daily_average_cents
    primary: '{{ (states(entity) | float(0)) | round(1) }}'
    secondary: 'c/kWh

      Average'
    icon: mdi:equal
    badge_icon: ''
    badge_color: ''
    tap_action:
      action: more-info
    hold_action:
      action: none
    double_tap_action:
      action: none
    color: "{% set high = states('sensor.electricity_today_32nd_highest_price') |\
      \ float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price')\
      \ | float(0) %} {% set price = states(entity) | float(0) %}\n{% if price > high\
      \ %}\n  red\n{% elif price < low %}\n  green\n{% else %}\n  orange\n{% endif\
      \ %}"
    vertical: true
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    multiline_secondary: true
  - type: custom:mushroom-template-card
    primary: '{{ states(entity) | float(0) | round(0) }} W'
    secondary: NOW
    icon: mdi:flash
    entity: sensor.home_total_power
    badge_color: ''
    tap_action:
      action: more-info
    hold_action:
      action: none
    double_tap_action:
      action: none
    color: blue
    vertical: true
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    multiline_secondary: true
  - type: custom:mushroom-entity-card
    entity: sensor.dishwasher_status_clean
    name: Dishwasher Status
    icon: mdi:dishwasher
    secondary_info: state
    grid_options:
      columns: 12
      rows: 1
    card_mod:
      style: "ha-card {\n  --card-mod-icon-color: var(--blue-color);\n}\n"
    visibility:
    - condition: state
      entity: binary_sensor.dishwasher_active
      state: 'on'
  - type: custom:mushroom-template-card
    primary: Washing Machine Running
    secondary: '{{ states(''sensor.washing_machine_plug_power'') }} W'
    icon: mdi:washing-machine
    entity: sensor.washing_machine_status
    icon_color: blue
    layout: horizontal
    grid_options:
      columns: 12
      rows: 1
    visibility:
    - condition: state
      entity: sensor.washing_machine_status
      state_not: Stopped
  - type: custom:mushroom-entity-card
    entity: sensor.aqara_w500_bathroom_heating_hvac
    grid_options:
      columns: 12
      rows: 1
    visibility:
    - condition: state
      entity: sensor.aqara_w500_bathroom_heating_hvac
      state: heating
    name: Bathroom Floor Heating
    icon_color: pink
  - type: custom:config-template-card
    variables:
      PRICEHIGH: states['sensor.electricity_today_32nd_highest_price'].state
      PRICELOW: states['sensor.electricity_today_32nd_lowest_price'].state
    entities:
    - sensor.electricity_prices
    card:
      type: custom:apexcharts-card
      graph_span: 1d
      span:
        start: day
      apex_config:
        chart:
          height: 250px
          width: 115%
          offsetX: -30
        title:
          text: Energy Price Today
          align: center
          offsetY: 0
          margin: 30
          style:
            fontSize: 13px
            fontFamily: Verdana
            fontWeight: normal
        grid:
          show: true
          borderColor: rgba(255,255,255,0.2)
        stroke:
          dashArray: 4
          curve: smooth
        xaxis:
          position: bottom
          labels:
            format: H
            hideOverlappingLabels: true
            offsetX: 0
          axisTicks:
            offsetX: 0
          all_series_config:
            show:
              offset_in_name: true
        legend:
          show: false
          position: bottom
          horizontalAlign: left
          fontSize: 14px
          itemMargin:
            vertical: 10
            horizontal: 10
        tooltip:
          enabled: false
          style:
            fontSize: 14px
      header:
        title: Electricity Today
        standard_format: false
        show: false
        show_states: true
        colorize_states: true
      show:
        last_updated: true
      experimental:
        color_threshold: true
      now:
        show: true
      yaxis:
      - id: cost
        min: 0
        opposite: true
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: c/kWh
            rotate: 0
            offsetX: -25
            offsetY: -90
            style:
              fontSize: 10px
              fontFamily: verdana
              color: orange
      - id: energy
        max: ~0.5
        min: 0
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: kWh
            rotate: 0
            offsetX: 25
            offsetY: -90
            style:
              color: skyblue
              fontSize: 10px
              fontFamily: verdana
      series:
      - entity: sensor.electricity_prices
        name: Current Price
        yaxis_id: cost
        type: column
        opacity: 0.8
        stroke_width: 0
        show:
          legend_value: false
          extremas: true
          in_header: true
          header_color_threshold: true
        data_generator: "return entity.attributes.data.map(entry => {\n  return [new\
          \ Date(entry.start).getTime(), entry.price];\n});\n"
        color_threshold:
        - value: -10
          color: lightgreen
        - value: ${PRICELOW * 1}
          color: orange
        - value: ${PRICEHIGH * 1}
          color: darkred
      - entity: sensor.electricity_daily_average_cents
        name: Average Price
        yaxis_id: cost
        type: line
        color: yellow
        stroke_width: 1
        opacity: 0.8
        group_by:
          func: last
          duration: 24h
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: true
      - entity: sensor.home_total_energy_hourly
        name: Energy Usage (kWh)
        color: skyblue
        type: line
        opacity: 1
        yaxis_id: energy
        stroke_width: 2
        float_precision: 1
        unit: kWh
        group_by:
          duration: 15m
          func: delta
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: raw
          header_color_threshold: true
  - type: custom:config-template-card
    variables:
      PRICEHIGH: states['sensor.electricity_tomorrow_32nd_highest_price'].state
      PRICELOW: states['sensor.electricity_tomorrow_32nd_lowest_price'].state
    entities:
    - sensor.electricity_prices
    card:
      type: custom:apexcharts-card
      graph_span: 1d
      span:
        start: day
        offset: +1d
      apex_config:
        stroke:
          dashArray: 4
        chart:
          height: 225px
          width: 115%
          offsetX: -30
        title:
          text: Energy Price Tomorrow
          align: center
          offsetY: 10
          style:
            fontSize: 13px
            fontFamily: Verdana
            fontWeight: normal
        grid:
          show: true
          borderColor: rgba(255,255,255,0.2)
        xaxis:
          position: bottom
          labels:
            format: H
            hideOverlappingLabels: true
            offsetX: 0
          axisTicks:
            offsetX: 0
        legend:
          show: false
          itemMargin:
            vertical: 10
            horizontal: 10
        tooltip:
          enabled: false
          style:
            fontSize: 14px
      show:
        last_updated: true
      experimental:
        color_threshold: true
      header:
        show_states: true
        colorize_states: true
      now:
        show: true
      yaxis:
      - id: cost
        opposite: true
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: c/kWh
            rotate: 0
            offsetX: -25
            offsetY: -90
            style:
              fontSize: 10px
              fontFamily: verdana
              color: orange
      - id: energy
        max: ~2
        min: 0
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: kWh
            rotate: 0
            offsetX: 25
            offsetY: -90
            style:
              color: skyblue
              fontSize: 10px
              fontFamily: verdana
      series:
      - entity: sensor.electricity_prices
        name: Price
        yaxis_id: cost
        type: column
        opacity: 0.8
        stroke_width: 0
        show:
          extremas: true
          in_header: raw
          header_color_threshold: true
        data_generator: "const tomorrow = new Date();\ntomorrow.setHours(0, 0, 0,\
          \ 0);\ntomorrow.setDate(tomorrow.getDate() + 1);\n\nreturn entity.attributes.data\n\
          \  .filter(entry => new Date(entry.start) >= tomorrow)\n  .map(entry =>\
          \ [new Date(entry.start).getTime(), entry.price]);\n"
        color_threshold:
        - value: -10
          color: lightgreen
        - value: ${PRICELOW * 1}
          color: orange
        - value: ${PRICEHIGH * 1}
          color: darkred
      - entity: sensor.home_total_energy_hourly
        name: Energy (kWh)
        color: skyblue
        type: line
        opacity: 1
        yaxis_id: energy
        stroke_width: 2
        float_precision: 1
        extend_to: false
        unit: kWh
        group_by:
          duration: 1hour
          func: max
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: raw
          header_color_threshold: true
    visibility:
    - condition: state
      entity: sensor.electricity_tomorrow_valid
      state: 'True'
  - type: custom:mushroom-template-card
    entity: sensor.electricity_daily_average_cents
    primary: '{{ (states(entity) | float(0)) | round(1) }}'
    secondary: 'c/kWh

      Average'
    icon: mdi:arrow-up-circle
    badge_icon: ''
    badge_color: ''
    tap_action:
      action: more-info
    hold_action:
      action: none
    double_tap_action:
      action: none
    color: "{% set high = states('sensor.electricity_today_32nd_highest_price') |\
      \ float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price')\
      \ | float(0) %} {% set price = states(entity) | float(0) %}\n{% if price > high\
      \ %}\n  red\n{% elif price < low %}\n  green\n{% else %}\n  orange\n{% endif\
      \ %}"
    vertical: true
    features_position: bottom
    grid_options:
      columns: 4
      rows: 2
    multiline_secondary: true
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: OUTDOOR
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:streamline-card
    template: camera_area_card
    variables:
      camera_entity: camera.frontdoor_doorbell_frigate
      aspect_ratio: 75%
      video_zoom: 1
      area_title: Front Door
      navigation_path: /lovelace/front-door
      presence_entity: select.front_door_presence
      main_toggle_entity: light.front_door_rail_light
      temp_sensor_entity: sensor.backyard_temperature
      indicator_1_entity: light.front_door_rail_light
      indicator_1_icon: mdi:lightbulb
      indicator_1_state: 'on'
      indicator_1_active_color: yellow
      indicator_2_entity: lock.front_door_lock
      indicator_2_icon: mdi:lock-open
      indicator_2_state: unlocked
      indicator_2_active_color: '#FF4444'
      indicator_2_animation_on: blink 1s ease infinite
      indicator_3_entity: binary_sensor.front_door_lock_door
      indicator_3_icon: mdi:door-open
      indicator_3_state: 'on'
      indicator_3_active_color: '#FF4444'
      indicator_3_animation_on: blink 1s ease infinite
      indicator_4_entity: sensor.front_door_lock_battery
      indicator_4_icon: mdi:battery-alert
      indicator_4_state: '20'
      indicator_4_active_color: orange
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: camera_area_card
    variables:
      aspect_ratio: 75%
      video_zoom: 1
      area_title: Front Door
      navigation_path: /lovelace/front-door
      presence_entity: select.front_door_presence
      main_toggle_entity: light.front_door_rail_light
      temp_sensor_entity: sensor.backyard_temperature
      indicator_1_entity: light.front_door_rail_light
      indicator_1_icon: mdi:lightbulb
      indicator_1_state: 'on'
      indicator_1_active_color: yellow
      indicator_2_entity: lock.front_door_lock
      indicator_2_icon: mdi:lock-open
      indicator_2_state: unlocked
      indicator_2_active_color: '#FF4444'
      indicator_2_animation_on: blink 1s ease infinite
      indicator_3_entity: binary_sensor.front_door_lock_door
      indicator_3_icon: mdi:door-open
      indicator_3_state: 'on'
      indicator_3_active_color: '#FF4444'
      indicator_3_animation_on: blink 1s ease infinite
      indicator_4_entity: sensor.front_door_lock_battery
      indicator_4_icon: mdi:battery-alert
      indicator_4_state: '20'
      indicator_4_active_color: orange
      camera_entity: camera.front_porch_frigate
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: camera_area_card
    variables:
      camera_entity: camera.backyard_frigate
      aspect_ratio: 57%
      video_zoom: 1.5
      area_title: Backyard
      navigation_path: /lovelace/backyard
      presence_entity: select.backyard_presence
      main_toggle_entity: light.backyard_plug
      temp_sensor_entity: sensor.backyard_temperature
      indicator_1_entity: light.backyard_plug
      indicator_1_icon: mdi:string-lights
      indicator_1_state: 'on'
      indicator_1_active_color: yellow
      indicator_2_entity: binary_sensor.backyard_door_sensor_contact
      indicator_2_icon: mdi:door-open
      indicator_2_state: 'on'
      indicator_2_active_color: '#FF4444'
      indicator_2_animation_on: blink 1s ease infinite
      indicator_3_entity: binary_sensor.backyard_frigate_person_occupancy
      indicator_3_icon: mdi:account-alert
      indicator_3_state: 'on'
      indicator_3_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: camera_area_card
    variables:
      camera_entity: camera.storage_frigate
      aspect_ratio: 57%
      area_title: Storage
      navigation_path: /lovelace/storage
      presence_entity: select.storage_presence
      main_toggle_entity: light.storage_light
      temp_sensor_entity: sensor.storage_temperature
      indicator_1_entity: light.storage_light
      indicator_1_icon: mdi:lightbulb
      indicator_1_state: 'on'
      indicator_1_active_color: yellow
      indicator_2_entity: binary_sensor.storage_cam_motion
      indicator_2_icon: mdi:motion-sensor
      indicator_2_state: 'on'
      indicator_2_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: 2nd Floor
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: sauna
      area_title: Sauna
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.ruuvitag_8572_temperature
      indicator_1_entity: binary_sensor.sauna_door_contact
      indicator_1_icon: mdi:door
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 1s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: bathroom
      area_title: Bathroom
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_entity: sensor.washing_machine_status
      indicator_1_icon: mdi:washing-machine
      indicator_1_state: Running
      indicator_1_active_color: '#088CF8'
      indicator_1_animation_on: blink 2s ease infinite
      indicator_2_entity: input_select.bathroom_toilet_presence
      indicator_2_icon: mdi:toilet
      indicator_3_icon: mdi:shower-head
      indicator_3_active_color: '#088CF8'
      indicator_2_active_color: orange
      indicator_3_entity: input_select.shower_presence
      indicator_3_state: presence
      indicator_2_state: presence
      temp_sensor_entity: sensor.aqara_w500_temperature_smoothed
      indicator_6_entity: sensor.aqara_w500_bathroom_heating_hvac
      indicator_6_icon: mdi:heating-coil
      indicator_6_state: heating
      indicator_6_active_color: '#FF4444'
      indicator_6_animation_on: blink 2s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: office
      area_title: Office
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: bedroom
      area_title: Bedroom
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
      indicator_1_entity: cover.bedroom_window_blinds
      indicator_1_icon: mdi:window-shutter
      indicator_1_state: open
      indicator_1_active_color: lightgreen
      indicator_2_entity: cover.bedroom_window_roller_cover
      indicator_2_icon: mdi:blinds-open
      indicator_2_state: open
      indicator_2_active_color: lightgreen
      indicator_3_entity: input_boolean.bed_Evis_occupancy
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_4_entity: input_boolean.bed_Guest 1_occupancy
      indicator_4_icon: mdi:bed
      indicator_4_state: 'on'
      indicator_4_active_color: '#FF44C4'
      indicator_3_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Guest 2
      area_title: E Room
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_3_entity: binary_sensor.Guest 2_bed_fp2_presence_sensor
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Guest 2_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Guest 3
      area_title: A Room
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.Guest 3_temperature
      indicator_3_entity: binary_sensor.Guest 3_bed_fp2_presence_sensor
      indicator_3_icon: mdi:bed
      indicator_3_state: 'on'
      indicator_3_active_color: lightgreen
      indicator_4_entity: binary_sensor.Guest 3_desk_fp2_presence_sensor
      indicator_4_icon: mdi:chair-rolling
      indicator_4_state: 'on'
      indicator_4_active_color: '#088CF8'
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: stairs
      area_title: Stairs
      temperature_sensor: sensor.airthings_wave_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: lobby
      area_title: Lobby
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
    grid_options:
      columns: 6
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: 1st Floor
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: hallway
      area_title: Hallway
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.airthings_wave_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: kitchen
      area_title: Kitchen
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.kitchen_fridge_door_device_temperature
      indicator_1_entity: binary_sensor.kitchen_fridge_door_contact
      indicator_1_icon: mdi:fridge
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 0.5s ease infinite
      indicator_2_entity: binary_sensor.kitchen_fridge_leak_sensor_water_leak
      indicator_2_icon: mdi:fridge-alert
      indicator_2_state: 'on'
      indicator_2_active_color: '#088CF8'
      indicator_2_animation_on: blink 0.5s ease infinite
      indicator_3_entity: sensor.coffee_machine_state
      indicator_3_icon: mdi:coffee
      indicator_3_active_color: orange
      indicator_3_state: Running
      indicator_4_entity: switch.schedule_coffee_machine_schedule
      indicator_4_icon: mdi:coffee-to-go-outline
      indicator_4_state: 'on'
      indicator_3_animation_on: blink 2s ease infinite
      indicator_4_active_color: lightgreen
      indicator_5_entity: sensor.dishwasher_current_status
      indicator_5_icon: mdi:dishwasher
      indicator_5_state: running
      indicator_5_active_color: skyblue
      indicator_5_animation_on: blink 2s ease infinite
      indicator_6_entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
      indicator_6_icon: mdi:dishwasher-alert
      indicator_6_state: 'on'
      indicator_6_active_color: '#088CF8'
      indicator_6_animation_on: blink 0.5s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: Daughter
      area_title: Guest Room
      temperature_sensor: sensor.airthings_wave_temperature
      indicator_1_entity: binary_sensor.Daughter_bed_fp2_presence_sensor
      indicator_1_icon: mdi:bed-king
      indicator_1_state: 'on'
      indicator_1_active_color: lightgreen
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: living_room
      area_title: Living Room
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.airthings_wave_temperature
      indicator_1_entity: light.fireplace
      indicator_1_icon: mdi:fireplace
      indicator_1_state: 'on'
      indicator_1_active_color: orange
      indicator_1_animation_on: blink 2s ease infinite
      indicator_2_entity: media_player.70pus9005_12_2
      indicator_2_icon: mdi:television
      indicator_2_state: 'on'
      indicator_2_active_color: lightgreen
      indicator_2_animation_on: blink 2s ease infinite
      indicator_3_entity: input_select.sofa_presence
      indicator_3_icon: mdi:sofa
      indicator_3_state: presence
      indicator_3_active_color: lightgreen
      indicator_5_entity: binary_sensor.inner_back_door_contact
      indicator_5_icon: mdi:door
      indicator_5_state: 'on'
      indicator_6_entity: binary_sensor.backyard_door_sensor_contact
      indicator_6_icon: mdi:door
      indicator_6_state: 'on'
      indicator_6_active_color: '#FF4444'
      indicator_6_animation_on: blink 0.5s ease infinite
      indicator_5_active_color: '#FF4444'
      indicator_5_animation_on: blink 0.5s ease infinite
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: toilet
      area_title: Toilet
      temperature_sensor: sensor.airthings_wave_temperature
    grid_options:
      columns: 6
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: mud_room
      area_title: Mud Room
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.mud_room_motion_sensor_device_temperature
      indicator_1_entity: binary_sensor.front_door_lock_door
      indicator_1_icon: mdi:door
      indicator_1_state: 'on'
      indicator_1_active_color: '#FF4444'
      indicator_1_animation_on: blink 0.5s ease infinite
      indicator_2_entity: lock.front_door_lock
      indicator_2_icon: mdi:lock
      indicator_2_state: unlocked
      indicator_2_active_color: '#FF4444'
      indicator_2_animation_on: blink 0.5s ease infinite
      indicator_6_entity: binary_sensor.mud_room_door_sensor_contact
      indicator_6_icon: mdi:door
      indicator_6_state: 'on'
      indicator_6_active_color: orange
      indicator_6_animation_on: blink 1s ease infinite
    grid_options:
      columns: 6
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
        image: local/car/GLC-front.png
        style:
          left: 50%
          top: 50%
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
    grid_options:
      columns: 6
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: HOME
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: custom:mushroom-entity-card
    entity: input_boolean.home_occupancy
    tap_action:
      action: none
    hold_action:
      action: none
    double_tap_action:
      action: none
    layout: vertical
  - type: custom:mushroom-entity-card
    entity: input_select.home_occupancy_state
    tap_action:
      action: none
    hold_action:
      action: none
    double_tap_action:
      action: none
    layout: vertical
  - type: custom:mushroom-template-card
    primary: Home Occupancy
    secondary: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  Occupied\n\
      {% else %}\n  Unoccupied\n{% endif %}"
    icon: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  mdi:home-account\n\
      {% else %}\n  mdi:home-outline\n{% endif %}"
    icon_color: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  green\n\
      {% else %}\n  orange\n{% endif %}"
    entity: input_boolean.home_occupancy
    layout: vertical
  - type: custom:mushroom-template-card
    primary: Home Occupancy State
    secondary: '{{ states(entity) }}'
    icon: "{% set status = states(entity) %}\n{% if status == 'on' %}\n  mdi:home-account\n\
      {% else %}\n  mdi:home-outline\n{% endif %}"
    entity: input_select.home_occupancy_state
    color: "{% set status = states(entity) %}\n{% if status == 'sleeping' %}\n  blue\n\
      {% elif status == 'away' %}\n  orange\n{% elif status == 'home' %}\n  green\n\
      {% elif status == 'simulated' %}\n  purple\n{% else %}\n  gray\n{% endif %}"
    vertical: true
    features_position: bottom
  - type: custom:mushroom-title-card
    title: ''
    alignment: center
    subtitle: COTTAGE
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: picture-elements
    entity: camera.cottage_yard_high_resolution_channel
    camera_image: camera.cottage_yard_high_resolution_channel
    camera_view: live
    aspect_ratio: 57%
    elements:
    - type: custom:button-card
      name: Cottage YARD
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 2
        container-type: inline-size
      styles:
        card:
        - border-radius: 0px
        - border: 0px
        - height: 30%
        - background-color: rgb(0,0,0,0)
        - box-shadow: 0px 0px 2px rgb(255,255,255,0)
        - font-size: 5cqw
        name:
        - font-family: arial
        - font-weight: bold
        - text-transform: uppercase
        - justify-self: left
        - padding-left: 15px
        - color: rgb(255, 255, 255, 1)
        - text-shadow: 0px 0px 5px rgb(0,0,0,1)
    card_mod:
      style: "@keyframes blink {\n  {% if is_state('sensor.car_charging','on') %}\n\
        \    50% { opacity: 0; }\n  {% else %}\n    50% { opacity: 100; }\n  {% endif\
        \ %}\n}\n@keyframes pulse {\n  50% { opacity: 0.33; }\n}\nha-card {\n  border-top-left-radius:\
        \ 8px;\n  border-top-right-radius: 8px;\n  border-bottom-left-radius: 8px;\n\
        \  border-bottom-right-radius: 8px;\n  background: rgb(0,0,0);\n  z-index:0;\n\
        \  height: 100%\n  container-type: inline-size\n  {% if is_state('select.backyard_presence','presence')\
        \ %}\n    border: 3px solid rgba(36, 255, 0, 0.8);\n  {% elif is_state('select.backyard_presence','idle')\
        \ %}\n    border: 3px solid rgba(255, 163, 0, 0.8);\n  {% else %}\n    border:\
        \ 0px solid rgba(0, 0, 0, 0);\n  {% endif %}\n}\n"
    layout_options:
      grid_columns: 2
  - type: picture-elements
    entity: camera.cottage_medium_resolution_channel
    camera_image: camera.cottage_medium_resolution_channel
    camera_view: live
    aspect_ratio: 57%
    elements:
    - type: custom:button-card
      name: Cottage
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 2
        container-type: inline-size
      styles:
        card:
        - border-radius: 0px
        - border: 0px
        - height: 30%
        - background-color: rgb(0,0,0,0)
        - box-shadow: 0px 0px 2px rgb(255,255,255,0)
        - font-size: 5cqw
        name:
        - font-family: arial
        - font-weight: bold
        - text-transform: uppercase
        - justify-self: left
        - padding-left: 15px
        - color: rgb(255, 255, 255, 1)
        - text-shadow: 0px 0px 5px rgb(0,0,0,1)
    card_mod:
      style: "@keyframes blink {\n  {% if is_state('sensor.car_charging','on') %}\n\
        \    50% { opacity: 0; }\n  {% else %}\n    50% { opacity: 100; }\n  {% endif\
        \ %}\n}\n@keyframes pulse {\n  50% { opacity: 0.33; }\n}\nha-card {\n  border-top-left-radius:\
        \ 8px;\n  border-top-right-radius: 8px;\n  border-bottom-left-radius: 8px;\n\
        \  border-bottom-right-radius: 8px;\n  background: rgb(0,0,0);\n  z-index:0;\n\
        \  height: 100%\n  container-type: inline-size\n  {% if is_state('select.backyard_presence','presence')\
        \ %}\n    border: 3px solid rgba(36, 255, 0, 0.8);\n  {% elif is_state('select.backyard_presence','idle')\
        \ %}\n    border: 3px solid rgba(255, 163, 0, 0.8);\n  {% else %}\n    border:\
        \ 0px solid rgba(0, 0, 0, 0);\n  {% endif %}\n}\n"
    layout_options:
      grid_columns: 2
  - type: picture-elements
    entity: camera.cottage_driveway_high_resolution_channel
    camera_image: camera.cottage_driveway_high_resolution_channel
    camera_view: live
    aspect_ratio: 57%
    elements:
    - type: custom:button-card
      name: Cottage Drideway
      style:
        top: 50%
        left: 50%
        width: 100%
        height: 100%
        z-index: 2
        container-type: inline-size
      styles:
        card:
        - border-radius: 0px
        - border: 0px
        - height: 30%
        - background-color: rgb(0,0,0,0)
        - box-shadow: 0px 0px 2px rgb(255,255,255,0)
        - font-size: 5cqw
        name:
        - font-family: arial
        - font-weight: bold
        - text-transform: uppercase
        - justify-self: left
        - padding-left: 15px
        - color: rgb(255, 255, 255, 1)
        - text-shadow: 0px 0px 5px rgb(0,0,0,1)
    card_mod:
      style: "@keyframes blink {\n  {% if is_state('sensor.car_charging','on') %}\n\
        \    50% { opacity: 0; }\n  {% else %}\n    50% { opacity: 100; }\n  {% endif\
        \ %}\n}\n@keyframes pulse {\n  50% { opacity: 0.33; }\n}\nha-card {\n  border-top-left-radius:\
        \ 8px;\n  border-top-right-radius: 8px;\n  border-bottom-left-radius: 8px;\n\
        \  border-bottom-right-radius: 8px;\n  background: rgb(0,0,0);\n  z-index:0;\n\
        \  height: 100%\n  container-type: inline-size\n  {% if is_state('select.backyard_presence','presence')\
        \ %}\n    border: 3px solid rgba(36, 255, 0, 0.8);\n  {% elif is_state('select.backyard_presence','idle')\
        \ %}\n    border: 3px solid rgba(255, 163, 0, 0.8);\n  {% else %}\n    border:\
        \ 0px solid rgba(0, 0, 0, 0);\n  {% endif %}\n}\n"
    layout_options:
      grid_columns: 2
max_columns: 4

```
