# Lovelace Dashboards

This section documents the Lovelace dashboards configuration found in .storage.

## Overview

**ID**: $Id | **URL**: /lovelace | **File**: $F`n
### View: Home

Path: $(@{title=Home; path=home; cards=System.Object[]; type=sections; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_home.png)

`yaml
title: Home
path: home
cards:
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: HOME
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        clock_size: medium
        time_zone: Europe/Helsinki
        time_format: 24
        show_seconds: True
        type: clock
        grid_options:
          columns: 12
          rows: 2
      -
        entities:
          -
            entity: calendar.holidays
            color: #e63946
          -
            entity: calendar.family_calendar
            color: #457b9d
          -
            entity: calendar.energy_management
        days_to_show: 30
        compact_events_to_show: 5
        compact_events_complete_days: True
        filter_duplicates: True
        first_day_of_week: monday
        show_week_numbers: iso
        day_separator_width: 1px
        day_separator_color: #444444
        today_indicator: dot
        weekend_weekday_color: orange
        weekend_day_color: orange
        weekend_month_color: orange
        weather:
          position: date
          date:
            show_conditions: True
            show_high_temp: True
            show_low_temp: False
            icon_size: 14px
            font_size: 12px
            color: var(--primary-text-color)
          event:
            show_conditions: True
            show_temp: True
            icon_size: 14px
            font_size: 12px
            color: var(--primary-text-color)
        tap_action:
          action: expand
        hold_action:
          action: navigate
          navigation_path: /calendar
        type: custom:calendar-card-pro
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: WEATHER
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        show_current: True
        show_forecast: True
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
                  -
                    type: weather-forecast
                    entity: weather.openweathermap
                    show_current: True
                    show_forecast: True
                    forecast_type: hourly
                  -
                    type: entities
                    entities:
                      -
                        entity: sensor.openweathermap_feels_like_temperature
                        name: Feels Like
                      -
                        entity: sensor.openweathermap_wind_speed
                        name: Wind
                      -
                        entity: sensor.backyard_humidity
                        name: Backyard Humidity
                      -
                        entity: sensor.backyard_temperature
                        name: Backyard Temperature
                  -
                    type: custom:horizon-card
                  -
                    type: weather-forecast
                    show_current: False
                    show_forecast: True
                    entity: weather.forecast_home
                    forecast_type: daily
                    name: Forecast
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: ENERGY
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:mushroom-template-card
        entity: sensor.nord_pool_fi_current_price
        secondary: c/kWh
NOW

        icon: mdi:currency-eur
        badge_icon: 
        badge_color: 
        tap_action:
          action: more-info
        hold_action:
          action: none
        double_tap_action:
          action: none
        color: {% set high = states('sensor.electricity_today_32nd_highest_price') | float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price') | float(0) %} {% set price = states(entity) | float(0) %}
{% if price > high %}
  red
{% elif price < low %}
  green
{% else %}
  orange
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        multiline_secondary: True
        primary: {{ (states(entity) | float(0) * 100) | round(1) }} 
      -
        type: custom:mushroom-template-card
        entity: sensor.electricity_daily_average_cents
        primary: {{ (states(entity) | float(0)) | round(1) }}
        secondary: c/kWh
Average
        icon: mdi:equal
        badge_icon: 
        badge_color: 
        tap_action:
          action: more-info
        hold_action:
          action: none
        double_tap_action:
          action: none
        color: {% set high = states('sensor.electricity_today_32nd_highest_price') | float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price') | float(0) %} {% set price = states(entity) | float(0) %}
{% if price > high %}
  red
{% elif price < low %}
  green
{% else %}
  orange
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        multiline_secondary: True
      -
        type: custom:mushroom-template-card
        primary: {{ states(entity) | float(0) | round(0) }} W
        secondary: NOW
        icon: mdi:flash
        entity: sensor.home_total_power
        badge_color: 
        tap_action:
          action: more-info
        hold_action:
          action: none
        double_tap_action:
          action: none
        color: blue
        vertical: True
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        multiline_secondary: True
      -
        type: custom:mushroom-entity-card
        entity: sensor.dishwasher_status_clean
        name: Dishwasher Status
        icon: mdi:dishwasher
        secondary_info: state
        grid_options:
          columns: 12
          rows: 1
        card_mod:
          style: ha-card {
  --card-mod-icon-color: var(--blue-color);
}

        visibility:
          -
            condition: state
            entity: binary_sensor.dishwasher_active
            state: on
      -
        type: custom:mushroom-template-card
        primary: Washing Machine Running
        secondary: {{ states('sensor.washing_machine_plug_power') }} W
        icon: mdi:washing-machine
        entity: sensor.washing_machine_status
        icon_color: blue
        layout: horizontal
        grid_options:
          columns: 12
          rows: 1
        visibility:
          -
            condition: state
            entity: sensor.washing_machine_status
            state_not: Stopped
      -
        type: custom:mushroom-entity-card
        entity: sensor.aqara_w500_bathroom_heating_hvac
        grid_options:
          columns: 12
          rows: 1
        visibility:
          -
            condition: state
            entity: sensor.aqara_w500_bathroom_heating_hvac
            state: heating
        name: Bathroom Floor Heating
        icon_color: pink
      -
        type: custom:config-template-card
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
              show: True
              borderColor: rgba(255,255,255,0.2)
            stroke:
              dashArray: 4
              curve: smooth
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
              all_series_config:
                show:
                  offset_in_name: True
            legend:
              show: False
              position: bottom
              horizontalAlign: left
              fontSize: 14px
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              enabled: False
              style:
                fontSize: 14px
          header:
            title: Electricity Today
            standard_format: False
            show: False
            show_states: True
            colorize_states: True
          show:
            last_updated: True
          experimental:
            color_threshold: True
          now:
            show: True
          yaxis:
            -
              id: cost
              min: 0
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: 0
                  offsetX: -25
                  offsetY: -90
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~0.5
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
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
            -
              entity: sensor.electricity_prices
              name: Current Price
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                legend_value: False
                extremas: True
                in_header: True
                header_color_threshold: True
              data_generator: return entity.attributes.data.map(entry => {
  return [new Date(entry.start).getTime(), entry.price];
});

              color_threshold:
                -
                  value: -10
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.electricity_daily_average_cents
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
                legend_value: False
                datalabels: False
                extremas: True
                in_header: True
            -
              entity: sensor.home_total_energy_hourly
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
                legend_value: False
                datalabels: False
                extremas: True
                in_header: raw
                header_color_threshold: True
      -
        type: custom:config-template-card
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
              show: True
              borderColor: rgba(255,255,255,0.2)
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
            legend:
              show: False
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              enabled: False
              style:
                fontSize: 14px
          show:
            last_updated: True
          experimental:
            color_threshold: True
          header:
            show_states: True
            colorize_states: True
          now:
            show: True
          yaxis:
            -
              id: cost
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: 0
                  offsetX: -25
                  offsetY: -90
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~2
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
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
            -
              entity: sensor.electricity_prices
              name: Price
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                extremas: True
                in_header: raw
                header_color_threshold: True
              data_generator: const tomorrow = new Date();
tomorrow.setHours(0, 0, 0, 0);
tomorrow.setDate(tomorrow.getDate() + 1);

return entity.attributes.data
  .filter(entry => new Date(entry.start) >= tomorrow)
  .map(entry => [new Date(entry.start).getTime(), entry.price]);

              color_threshold:
                -
                  value: -10
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.home_total_energy_hourly
              name: Energy (kWh)
              color: skyblue
              type: line
              opacity: 1
              yaxis_id: energy
              stroke_width: 2
              float_precision: 1
              extend_to: False
              unit: kWh
              group_by:
                duration: 1hour
                func: max
              show:
                legend_value: False
                datalabels: False
                extremas: True
                in_header: raw
                header_color_threshold: True
        visibility:
          -
            condition: state
            entity: sensor.electricity_tomorrow_valid
            state: True
      -
        type: custom:mushroom-template-card
        entity: sensor.electricity_daily_average_cents
        primary: {{ (states(entity) | float(0)) | round(1) }}
        secondary: c/kWh
Average
        icon: mdi:arrow-up-circle
        badge_icon: 
        badge_color: 
        tap_action:
          action: more-info
        hold_action:
          action: none
        double_tap_action:
          action: none
        color: {% set high = states('sensor.electricity_today_32nd_highest_price') | float(0) %} {% set low = states('sensor.electricity_today_32nd_lowest_price') | float(0) %} {% set price = states(entity) | float(0) %}
{% if price > high %}
  red
{% elif price < low %}
  green
{% else %}
  orange
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        multiline_secondary: True
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: OUTDOOR
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:streamline-card
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
          indicator_1_state: on
          indicator_1_active_color: yellow
          indicator_2_entity: lock.front_door_lock
          indicator_2_icon: mdi:lock-open
          indicator_2_state: unlocked
          indicator_2_active_color: #FF4444
          indicator_2_animation_on: blink 1s ease infinite
          indicator_3_entity: binary_sensor.front_door_lock_door
          indicator_3_icon: mdi:door-open
          indicator_3_state: on
          indicator_3_active_color: #FF4444
          indicator_3_animation_on: blink 1s ease infinite
          indicator_4_entity: sensor.front_door_lock_battery
          indicator_4_icon: mdi:battery-alert
          indicator_4_state: 20
          indicator_4_active_color: orange
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
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
          indicator_1_state: on
          indicator_1_active_color: yellow
          indicator_2_entity: lock.front_door_lock
          indicator_2_icon: mdi:lock-open
          indicator_2_state: unlocked
          indicator_2_active_color: #FF4444
          indicator_2_animation_on: blink 1s ease infinite
          indicator_3_entity: binary_sensor.front_door_lock_door
          indicator_3_icon: mdi:door-open
          indicator_3_state: on
          indicator_3_active_color: #FF4444
          indicator_3_animation_on: blink 1s ease infinite
          indicator_4_entity: sensor.front_door_lock_battery
          indicator_4_icon: mdi:battery-alert
          indicator_4_state: 20
          indicator_4_active_color: orange
          camera_entity: camera.front_porch_frigate
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
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
          indicator_1_state: on
          indicator_1_active_color: yellow
          indicator_2_entity: binary_sensor.backyard_door_sensor_contact
          indicator_2_icon: mdi:door-open
          indicator_2_state: on
          indicator_2_active_color: #FF4444
          indicator_2_animation_on: blink 1s ease infinite
          indicator_3_entity: binary_sensor.backyard_frigate_person_occupancy
          indicator_3_icon: mdi:account-alert
          indicator_3_state: on
          indicator_3_active_color: #088CF8
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
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
          indicator_1_state: on
          indicator_1_active_color: yellow
          indicator_2_entity: binary_sensor.storage_cam_motion
          indicator_2_icon: mdi:motion-sensor
          indicator_2_state: on
          indicator_2_active_color: #088CF8
        grid_options:
          columns: 6
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: 2nd Floor
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: sauna
          area_title: Sauna
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.ruuvitag_8572_temperature
          indicator_1_entity: binary_sensor.sauna_door_contact
          indicator_1_icon: mdi:door
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 1s ease infinite
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: bathroom
          area_title: Bathroom
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_1_entity: sensor.washing_machine_status
          indicator_1_icon: mdi:washing-machine
          indicator_1_state: Running
          indicator_1_active_color: #088CF8
          indicator_1_animation_on: blink 2s ease infinite
          indicator_2_entity: input_select.bathroom_toilet_presence
          indicator_2_icon: mdi:toilet
          indicator_3_icon: mdi:shower-head
          indicator_3_active_color: #088CF8
          indicator_2_active_color: orange
          indicator_3_entity: input_select.shower_presence
          indicator_3_state: presence
          indicator_2_state: presence
          temp_sensor_entity: sensor.aqara_w500_temperature_smoothed
          indicator_6_entity: sensor.aqara_w500_bathroom_heating_hvac
          indicator_6_icon: mdi:heating-coil
          indicator_6_state: heating
          indicator_6_active_color: #FF4444
          indicator_6_animation_on: blink 2s ease infinite
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: office
          area_title: Office
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.bedroom_temperature
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
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
          indicator_3_entity: input_boolean.bed_jukka_occupancy
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_4_entity: input_boolean.bed_piia_occupancy
          indicator_4_icon: mdi:bed
          indicator_4_state: on
          indicator_4_active_color: #FF44C4
          indicator_3_active_color: #088CF8
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: elias
          area_title: E Room
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_3_entity: binary_sensor.elias_bed_fp2_presence_sensor
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_3_active_color: lightgreen
          indicator_4_entity: binary_sensor.elias_desk_fp2_presence_sensor
          indicator_4_icon: mdi:chair-rolling
          indicator_4_state: on
          indicator_4_active_color: #088CF8
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: anton
          area_title: A Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.anton_temperature
          indicator_3_entity: binary_sensor.anton_bed_fp2_presence_sensor
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_3_active_color: lightgreen
          indicator_4_entity: binary_sensor.anton_desk_fp2_presence_sensor
          indicator_4_icon: mdi:chair-rolling
          indicator_4_state: on
          indicator_4_active_color: #088CF8
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: stairs
          area_title: Stairs
          temperature_sensor: sensor.airthings_wave_temperature
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: lobby
          area_title: Lobby
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.bedroom_temperature
        grid_options:
          columns: 6
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: 1st Floor
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: hallway
          area_title: Hallway
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.airthings_wave_temperature
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: kitchen
          area_title: Kitchen
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.kitchen_fridge_door_device_temperature
          indicator_1_entity: binary_sensor.kitchen_fridge_door_contact
          indicator_1_icon: mdi:fridge
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 0.5s ease infinite
          indicator_2_entity: binary_sensor.kitchen_fridge_leak_sensor_water_leak
          indicator_2_icon: mdi:fridge-alert
          indicator_2_state: on
          indicator_2_active_color: #088CF8
          indicator_2_animation_on: blink 0.5s ease infinite
          indicator_3_entity: sensor.coffee_machine_state
          indicator_3_icon: mdi:coffee
          indicator_3_active_color: orange
          indicator_3_state: Running
          indicator_4_entity: switch.schedule_coffee_machine_schedule
          indicator_4_icon: mdi:coffee-to-go-outline
          indicator_4_state: on
          indicator_3_animation_on: blink 2s ease infinite
          indicator_4_active_color: lightgreen
          indicator_5_entity: sensor.dishwasher_current_status
          indicator_5_icon: mdi:dishwasher
          indicator_5_state: running
          indicator_5_active_color: skyblue
          indicator_5_animation_on: blink 2s ease infinite
          indicator_6_entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
          indicator_6_icon: mdi:dishwasher-alert
          indicator_6_state: on
          indicator_6_active_color: #088CF8
          indicator_6_animation_on: blink 0.5s ease infinite
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: alisa
          area_title: Guest Room
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_1_entity: binary_sensor.alisa_bed_fp2_presence_sensor
          indicator_1_icon: mdi:bed-king
          indicator_1_state: on
          indicator_1_active_color: lightgreen
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: living_room
          area_title: Living Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.airthings_wave_temperature
          indicator_1_entity: light.fireplace
          indicator_1_icon: mdi:fireplace
          indicator_1_state: on
          indicator_1_active_color: orange
          indicator_1_animation_on: blink 2s ease infinite
          indicator_2_entity: media_player.70pus9005_12_2
          indicator_2_icon: mdi:television
          indicator_2_state: on
          indicator_2_active_color: lightgreen
          indicator_2_animation_on: blink 2s ease infinite
          indicator_3_entity: input_select.sofa_presence
          indicator_3_icon: mdi:sofa
          indicator_3_state: presence
          indicator_3_active_color: lightgreen
          indicator_5_entity: binary_sensor.inner_back_door_contact
          indicator_5_icon: mdi:door
          indicator_5_state: on
          indicator_6_entity: binary_sensor.backyard_door_sensor_contact
          indicator_6_icon: mdi:door
          indicator_6_state: on
          indicator_6_active_color: #FF4444
          indicator_6_animation_on: blink 0.5s ease infinite
          indicator_5_active_color: #FF4444
          indicator_5_animation_on: blink 0.5s ease infinite
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: toilet
          area_title: Toilet
          temperature_sensor: sensor.airthings_wave_temperature
        grid_options:
          columns: 6
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: mud_room
          area_title: Mud Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.mud_room_motion_sensor_device_temperature
          indicator_1_entity: binary_sensor.front_door_lock_door
          indicator_1_icon: mdi:door
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 0.5s ease infinite
          indicator_2_entity: lock.front_door_lock
          indicator_2_icon: mdi:lock
          indicator_2_state: unlocked
          indicator_2_active_color: #FF4444
          indicator_2_animation_on: blink 0.5s ease infinite
          indicator_6_entity: binary_sensor.mud_room_door_sensor_contact
          indicator_6_icon: mdi:door
          indicator_6_state: on
          indicator_6_active_color: orange
          indicator_6_animation_on: blink 1s ease infinite
        grid_options:
          columns: 6
      -
        type: picture-elements
        image: local/car/Car-BG.png
        elements:
          -
            type: custom:button-card
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
                      -
                        type: horizontal-stack
                        cards:
                          -
                            type: custom:mushroom-template-card
                            entity: sensor.fuel_level
                            primary: Fuel Level
                            secondary: {{ states('sensor.xpb_358_fuel_level') }}% | {{ states('sensor.xpb_358_range_liquid') }} km range
                            icon: mdi:gas-station
                            features_position: bottom
                            color: {% set fuel = states('sensor.xpb_358_fuel_level') | int %} {% if fuel < 20 %}
  darkred
{% elif fuel < 50 %}
  yellow
{% else %}
  darkgreen
{% endif %}

                            card_mod:
                              style: ha-card {
  background: linear-gradient(
    to right,
    orange {{ states('sensor.xpb_358_fuel_level') }}%,
    var(--card-background-color) {{ states('sensor.xpb_358_fuel_level') }}%
  );
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

                          -
                            type: custom:mushroom-template-card
                            entity: sensor.ev_battery_level
                            primary: EV Charge
                            secondary: {{ states('sensor.xpb_358_state_of_charge') }}% | {{ states('sensor.xpb_358_range_electric') }} km range

                            icon: mdi:car-electric
                            tap_action:
                              action: more-info
                            hold_action:
                              action: more-info
                            color: {% set charge = states('sensor.xpb_358_state_of_charge') | int %} {% if charge < 20 %}
  red
{% elif charge < 50 %}
  yellow
{% else %}
  lightgreen
{% endif %}

                            features_position: bottom
                            card_mod:
                              style: ha-card {
  --charge: {{ states('sensor.xpb_358_state_of_charge') }}%;
  background: linear-gradient(
    to right,
    green var(--charge),
    var(--card-background-color) var(--charge)
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

                      -
                        type: custom:scheduler-card
                        include:
                          - switch.xpb_358_pre_entry_climate_control
                        exclude:
                        discover_existing: False
                        title: True
                        show_header_toggle: False
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
                        customize:
                        tags:
                          - Car
                        exclude_tags:
                        card_mod:
                          style: ha-card {
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

                      -
                        type: map
                        entities:
                          -
                            entity: person.car
                        hours_to_show: 48
                        aspect_ratio: 1.5
                        default_zoom: 15
                        theme_mode: auto
            card_mod:
              style: ha-card {
  /* Moves border logic here from original for border display */
  {% if is_state('sensor.xpb_358_ignition_state','4') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('sensor.xpb_358_ignition_state','2') %}
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
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: home
            elements:
              -
                type: image
                image: local/car/GLC-front.png
                style:
                  left: 50%
                  top: 50%
                  width: 80%
                  opacity: 100%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: not_home
            elements:
              -
                type: image
                image: local/car/GLC-back.png
                style:
                  left: 50%
                  top: 50%
                  width: 65%
                  opacity: 100%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: binary_sensor.car_engine
                state: on
            elements:
              -
                type: image
                image: local/car/road.png
                style:
                  left: 50%
                  top: 65%
                  width: 100%
                  opacity: 100%
                  z-index: 2
          -
            type: custom:button-card
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
          -
            type: custom:button-card
            template: area_text_element
            entity: sensor.xpb_358_state_of_charge
            show_name: False
            show_icon: False
            show_state: True
            style:
              top: 0%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: #088CF8
                    -
                      animation: [[[
  if (states['binary_sensor.xpb_358_charging_active'].state == 'on') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: unlocked
                styles:
                  icon:
                    -
                      animation: blink 0.5s linear infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: locked
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 0.5s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: #088CF8
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: rgba(253,89,89,1)
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      animation: rotating 1s linear infinite
                      color: #21ff21
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
        grid_options:
          columns: 6
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: HOME
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:mushroom-entity-card
        entity: input_boolean.home_occupancy
        tap_action:
          action: none
        hold_action:
          action: none
        double_tap_action:
          action: none
        layout: vertical
      -
        type: custom:mushroom-entity-card
        entity: input_select.home_occupancy_state
        tap_action:
          action: none
        hold_action:
          action: none
        double_tap_action:
          action: none
        layout: vertical
      -
        type: custom:mushroom-template-card
        primary: Home Occupancy
        secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  Occupied
{% else %}
  Unoccupied
{% endif %}
        icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:home-account
{% else %}
  mdi:home-outline
{% endif %}
        icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  orange
{% endif %}
        entity: input_boolean.home_occupancy
        layout: vertical
      -
        type: custom:mushroom-template-card
        primary: Home Occupancy State
        secondary: {{ states(entity) }}
        icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:home-account
{% else %}
  mdi:home-outline
{% endif %}
        entity: input_select.home_occupancy_state
        color: {% set status = states(entity) %}
{% if status == 'sleeping' %}
  blue
{% elif status == 'away' %}
  orange
{% elif status == 'home' %}
  green
{% elif status == 'simulated' %}
  purple
{% else %}
  gray
{% endif %}
        vertical: True
        features_position: bottom
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: COTTAGE
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: picture-elements
        entity: camera.cottage_yard_high_resolution_channel
        camera_image: camera.cottage_yard_high_resolution_channel
        camera_view: live
        aspect_ratio: 57%
        elements:
          -
            type: custom:button-card
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
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
                -
                  font-size: 5cqw
              name:
                -
                  font-family: arial
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: left
                -
                  padding-left: 15px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 5px rgb(0,0,0,1)
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  height: 100%
  container-type: inline-size
  {% if is_state('select.backyard_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.backyard_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

        layout_options:
          grid_columns: 2
      -
        type: picture-elements
        entity: camera.cottage_medium_resolution_channel
        camera_image: camera.cottage_medium_resolution_channel
        camera_view: live
        aspect_ratio: 57%
        elements:
          -
            type: custom:button-card
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
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
                -
                  font-size: 5cqw
              name:
                -
                  font-family: arial
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: left
                -
                  padding-left: 15px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 5px rgb(0,0,0,1)
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  height: 100%
  container-type: inline-size
  {% if is_state('select.backyard_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.backyard_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

        layout_options:
          grid_columns: 2
      -
        type: picture-elements
        entity: camera.cottage_driveway_high_resolution_channel
        camera_image: camera.cottage_driveway_high_resolution_channel
        camera_view: live
        aspect_ratio: 57%
        elements:
          -
            type: custom:button-card
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
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
                -
                  font-size: 5cqw
              name:
                -
                  font-family: arial
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: left
                -
                  padding-left: 15px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 5px rgb(0,0,0,1)
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  height: 100%
  container-type: inline-size
  {% if is_state('select.backyard_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.backyard_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

        layout_options:
          grid_columns: 2
max_columns: 4

` 
### View: Office

Path: $(@{theme=Backend-selected; title=Office; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; max_columns=6; sections=System.Object[]; path=office}.path)`n
![View Screenshot](assets/images/view_office.png)

`yaml
theme: Backend-selected
title: Office
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
max_columns: 6
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: office
          area_title: Office
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.bedroom_temperature
        grid_options:
          columns: 12
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: ENVIRONMENT
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:decluttering-card
                template: minigraph_co2
                variables:
                  -
                    sensor: sensor.bedroom_carbon_dioxide
              -
                type: custom:decluttering-card
                template: minigraph_temperature
                variables:
                  -
                    sensor: sensor.bedroom_temperature
              -
                type: custom:decluttering-card
                template: minigraph_humidity
                variables:
                  -
                    sensor: sensor.bedroom_humidity
            columns: 3
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-light-card
                entity: light.wled_2
                layout: vertical
                show_color_control: False
                show_brightness_control: True
                name: Desk
                use_light_color: True
              -
                type: custom:mushroom-light-card
                entity: light.server_cabinet_light
                layout: vertical
                show_brightness_control: True
                name: Rack
                use_light_color: True
                show_color_temp_control: False
                show_color_control: False
                collapsible_controls: False
                fill_container: True
              -
                type: custom:mushroom-light-card
                entity: light.bedroom_ceiling_light
                name: Ceiling
                layout: vertical
                show_brightness_control: True
                use_light_color: True
              -
                type: custom:mushroom-light-card
                entity: light.office_desk_wall_light
                name: Wall
                layout: vertical
                show_brightness_control: True
                use_light_color: True
            columns: 4
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-select-card
                entity: select.wled_preset_2
                name: Office Desk Presets
            columns: 1
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: WINDOW
            alignment: center
          -
            square: False
            columns: 2
            type: grid
            cards:
              -
                type: custom:mushroom-cover-card
                entity: cover.bedroom_window_blinds
                show_position_control: True
                show_buttons_control: False
                tap_action:
                  action: none
                name: Blinds
                layout: vertical
              -
                type: custom:mushroom-cover-card
                entity: cover.bedroom_window_roller_cover
                fill_container: False
                show_position_control: False
                show_buttons_control: True
                tap_action:
                  action: none
                name: Roller Blind
                layout: vertical
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: PC
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-template-card
                primary: Audio Device
                secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  Speakers
{% else %}
  Headset
{% endif %}
                icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:speaker-multiple
{% else %}
  mdi:headphones
{% endif %}
                layout: vertical
                entity: switch.officepc_audio_device
                tap_action:
                  action: toggle
                icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  orange
{% endif %}
              -
                type: custom:mushroom-entity-card
                entity: button.officepc_mediaplaypause
                name: Play | Pause
                icon: mdi:play-pause
                icon_color: blue
                layout: vertical
                secondary_info: last-changed
                fill_container: True
                tap_action:
                  action: call-service
                  service: button.press
                  target:
                    entity_id: button.officepc_mediaplaypause
                  data:
              -
                type: custom:mushroom-template-card
                primary: Audio Mute
                secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  Muted
{% else %}
 Volume {{ states('sensor.officepc_audio_default_device_volume') }}
{% endif %}
                icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:volume-mute
{% else %}
  mdi:volume-high
{% endif %}
                layout: vertical
                entity: switch.officepc_audio_mute
                tap_action:
                  action: toggle
                icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  red
{% else %}
  green
{% endif %}
      -
        type: custom:mushroom-entity-card
        entity: switch.office_pc_power
        layout: vertical
        fill_container: True
        icon_color: green
        tap_action:
          action: none
        hold_action:
          action: toggle
        name: PC Power
      -
        type: custom:mushroom-template-card
        primary: Displays
        secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  On
{% else %}
 Off
{% endif %}
        icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:monitor
{% else %}
  mdi:monitor-off
{% endif %}
        layout: vertical
        entity: switch.officepc_displays
        tap_action:
          action: toggle
        icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  red
{% endif %}
        fill_container: True
      -
        type: history-graph
        entities:
          -
            entity: switch.office_pc_power
            name:  
      -
        type: custom:apexcharts-card
        graph_span: 12h
        show:
          loading: False
        apex_config:
          chart:
            height: 120px
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          legend:
            show: False
        header:
          show: True
          show_states: True
          colorize_states: True
          standard_format: False
        all_series_config:
          stroke_width: 2
        yaxis:
          -
            min: 0
            max: 100
            decimals: 0
            apex_config:
              tickAmount: 4
        series:
          -
            entity: sensor.officepc_memoryusage
            type: area
            opacity: 0.3
            name: Memory
            color: skyblue
            float_precision: 0
            fill_raw: zero
            group_by:
              func: max
            show:
              legend_value: False
          -
            entity: sensor.officepc_cpuload
            type: area
            opacity: 0.3
            name: CPU
            color: orange
            float_precision: 0
            fill_raw: zero
            group_by:
              func: max
            show:
              legend_value: False
        card_mod:
          style: ha-card {
  padding-top: 12px;
}

      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: POWER OUTLETS
            alignment: center
          -
            type: grid
            cards:
              -
                type: custom:mini-graph-card
                name: Desk
                entities:
                  -
                    entity: sensor.office_desk_outlet_power
                    name: Power
                icon: mdi:flash
                font_size_header: 12
                font_size: 75
                line_width: 8
                hours_to_show: 24
              -
                type: custom:mini-graph-card
                name: Modem
                entities:
                  -
                    entity: sensor.shellyplusplugs_b0b21c1991a8_switch_0_power
                    name: Power
                icon: mdi:flash
                font_size_header: 12
                font_size: 75
                line_width: 8
                hours_to_show: 24
              -
                type: custom:mini-graph-card
                name: Rack
                entities:
                  -
                    entity: sensor.rack_power_plug_power
                    name: Power
                icon: mdi:flash
                font_size_header: 12
                font_size: 75
                line_width: 8
                hours_to_show: 24
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: PROXMOX VE
            subtitle: 
            alignment: center
          -
            type: custom:uptime-card
            entity: binary_sensor.node_halo_status
            icon: mdi:heart-pulse
            title_template: UPTIME
            hours_to_show: 168
            alignment:
              status: spaced
              header: center
              icon_first: False
            alias:
              ok: Running
              ko: Unvailable
              half: Unvailable
            color:
              ko: red
              ok: lightgreen
              half: red
              icon: orange
            bar:
              spacing: 4
              height: 20
              round: 5
          -
            square: False
            type: grid
            cards:
              -
                type: custom:apexcharts-card
                graph_span: 48h
                show:
                  loading: False
                header:
                  show: True
                  title: MEMORY
                  standard_format: False
                  show_states: True
                  colorize_states: True
                color_list:
                  - green
                  - rgba(253,80,80,1)
                  - skyblue
                all_series_config:
                  stroke_width: 2
                  opacity: 1
                chart_type: donut
                series:
                  -
                    entity: sensor.node_halo_memory_free
                    name: Free MEM
                    unit: GB
                    show:
                      in_header: False
                  -
                    entity: sensor.node_halo_memory_used
                    name: Used MEM
                    show:
                      in_header: False
                  -
                    entity: sensor.node_halo_memory_total_2
                    name: Total
                    show:
                      in_chart: False
                card_mod:
                  style: ha-card {
  padding-bottom: 20px;
}

              -
                type: custom:apexcharts-card
                graph_span: 48h
                show:
                  loading: False
                header:
                  show: True
                  title: SSD10
                  standard_format: False
                  show_states: True
                  colorize_states: True
                color_list:
                  - green
                  - rgba(253,80,80,1)
                  - skyblue
                all_series_config:
                  stroke_width: 2
                  opacity: 1
                chart_type: donut
                series:
                  -
                    entity: sensor.storage_ssd10_disk_free
                    name: Free
                    unit: GB
                    show:
                      in_header: False
                  -
                    entity: sensor.storage_ssd10_disk_used
                    name: Used
                    show:
                      in_header: False
                  -
                    entity: sensor.storage_ssd10_disk_total
                    name: Total
                    show:
                      in_chart: False
                card_mod:
                  style: ha-card {
  padding-bottom: 20px;
}

            columns: 2
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: PROXMOX VE
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-entity-card
                entity: binary_sensor.qemu_vm_homeassistantos_150_status
                layout: vertical
                fill_container: True
                name: HAOS
              -
                type: custom:mini-graph-card
                title: Home Assistant
                font_size_header: 12
                font_size: 70
                decimals: 0
                height: 200
                entities:
                  -
                    entity: sensor.qemu_vm_homeassistantos_150_cpu_used
                    name: CPU
                    color: orange
                    show_state: True
                  -
                    entity: sensor.qemu_vm_homeassistantos_150_memory_used_percentage
                    name: MEM
                    color: lightgreen
                    show_state: True
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-entity-card
                    entity: sensor.qemu_vm_homeassistantos_150_uptime
                    layout: horizontal
                    fill_container: True
                    name: Uptime
                  -
                    type: custom:mushroom-entity-card
                    entity: binary_sensor.qemu_vm_homeassistantos_150_health
                    layout: horizontal
                    fill_container: True
                    name: Health
                  -
                    type: custom:mushroom-entity-card
                    entity: sensor.qemu_vm_homeassistantos_150_node
                    layout: horizontal
                    fill_container: False
                    name: Node
                columns: 1
            columns: 3
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: OCCUPANCY SETTINGS
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: office
          -
            area_name: Office
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.office_automation_mode
          - light.office_desk_wall_light
          - light.office_lights
        exclude:
        discover_existing: False
        tags:
          - living-room
        time_step: 1
        show_header_toggle: False
        title: False
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: AUTOMATION MODE SCHEDULES
        alignment: center
      -
        type: markdown
        content: Automation Mode Changes, based on time or sun.
      -
        type: custom:scheduler-card
        include:
          - input_select.office_automation_mode
        exclude:
        discover_existing: False
        tags:
          - office-mode-control
        time_step: 1
        show_header_toggle: False
        title: False
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            alignment: center
            subtitle: Battery Levels
          -
            type: custom:auto-entities
            card:
              type: entities
            filter:
              include:
                -
                  entity_id: sensor.office*battery*
              exclude:
      -
        type: markdown
        content: **Automation Modes**

_Presence Control:_ Lights are automatically controlled by the occupancy state of the room.

_Absence Detection:_ When room is no longer occupied, lights will be turned off after a the absence delay time.

_Schedule Mode:_ Light schedules are working as set in the Scheduler. (schedule-mode condition)
      -
        type: custom:scheduler-card
        include:
          - input_select.living_room_automation_mode
          - light.floor_light
          - light.living_room_ceiling_light
          - light.living_room_lights
        exclude:
        discover_existing: False
        tags:
          - living-room
        time_step: 1
        show_header_toggle: False
        title: True
  -
    type: grid
    cards:
path: office

` 
### View: Bedroom

Path: $(@{theme=Backend-selected; title=Bedroom; path=bedroom; subview=True; type=sections; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_bedroom.png)

`yaml
theme: Backend-selected
title: Bedroom
path: bedroom
subview: True
type: sections
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
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
          indicator_3_entity: input_boolean.bed_jukka_occupancy
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_4_entity: input_boolean.bed_piia_occupancy
          indicator_4_icon: mdi:bed
          indicator_4_state: on
          indicator_4_active_color: #FF44C4
          indicator_3_active_color: #088CF8
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: ENVIRONMENT
        alignment: center
      -
        type: vertical-stack
        cards:
          -
            square: False
            type: grid
            cards:
              -
                type: custom:decluttering-card
                template: minigraph_co2
                variables:
                  -
                    sensor: sensor.bedroom_carbon_dioxide
              -
                type: custom:decluttering-card
                template: minigraph_temperature
                variables:
                  -
                    sensor: sensor.bedroom_temperature
              -
                type: custom:decluttering-card
                template: minigraph_humidity
                variables:
                  -
                    sensor: sensor.bedroom_humidity
            columns: 3
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.bedroom_ceiling_light
        name: Ceiling
        layout: vertical
        show_brightness_control: True
        use_light_color: True
        grid_options:
          columns: 6
          rows: 3
      -
        type: custom:mushroom-light-card
        entity: light.bedroom_bed_light
        layout: vertical
        show_color_control: False
        show_brightness_control: True
        name: Bed
        use_light_color: True
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: WINDOW COVERS
        alignment: center
      -
        type: custom:mushroom-cover-card
        entity: cover.bedroom_window_blinds
        show_position_control: True
        show_buttons_control: False
        tap_action:
          action: none
        name: Blinds
        layout: vertical
      -
        type: custom:mushroom-cover-card
        entity: cover.bedroom_window_roller_cover
        fill_container: False
        show_position_control: False
        show_buttons_control: True
        tap_action:
          action: none
        name: Roller Blind
        layout: vertical
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:scheduler-card
                tags:
                  - Bedroom
                title: False
                discover_existing: False
                show_header_toggle: False
                display_options:
                  primary_info: default
                  secondary_info:
                    - relative-time
                    - additional-tasks
                  icon: action
                include:
                  - cover
                  - light
                exclude:
            columns: 1
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: Sensors
            alignment: center
          -
            type: entities
            entities:
              -
                entity: sensor.bedroom_noise
                name: Bedroom Noise
              -
                entity: sensor.bedroom_temperature
                name: Bedroom Temperature
              -
                entity: sensor.bedroom_carbon_dioxide
                name: Bedroom CO2
              -
                entity: sensor.bedroom_humidity
                name: Bedroom Humidity
            show_header_toggle: False
            state_color: True
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            alignment: center
            subtitle: Battery Levels
          -
            type: custom:auto-entities
            card:
              type: entities
            filter:
              include:
                -
                  entity_id: sensor.bedroom*battery*
              exclude:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        subtitle: Occupancy Settings
        alignment: center
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: bedroom
          -
            area_name: Bedroom
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: Bed Occupancy
            alignment: center
          -
            type: custom:mushroom-template-card
            primary: Bed {% set status = states(entity) %}
{% if status == 'on' %}
  Occupied
{% else %}
  Unoccupied
{% endif %}
            secondary: 
            icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:bed-king
{% else %}
  mdi:bed-king-outline
{% endif %}
            layout: vertical
            entity: input_boolean.bedroom_bed_occupancy
            icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
 green
{% else %}
  white
{% endif %}
            fill_container: True
            tap_action:
              action: none
            hold_action:
              action: more-info
            double_tap_action:
              action: none
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-template-card
                primary: Jukka {% set status = states(entity) %}
{% if status == 'on' %}
  in Bed
{% else %}
  not in Bed
{% endif %}
                secondary: 
                icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:bed
{% else %}
  mdi:bed-empty
{% endif %}
                layout: vertical
                entity: binary_sensor.master_bed_sensor_master_bed_occupancy_left
                icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  blue
{% else %}
  white
{% endif %}
                fill_container: True
                tap_action:
                  action: none
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
              -
                type: custom:mushroom-template-card
                primary: Piia {% set status = states(entity) %}
{% if status == 'on' %}
  in Bed
{% else %}
  not in Bed
{% endif %}
                secondary: 
                icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:bed
{% else %}
  mdi:bed-empty
{% endif %}
                layout: vertical
                entity: binary_sensor.master_bed_sensor_master_bed_occupancy_right
                icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  red
{% else %}
  white
{% endif %}
                fill_container: True
                tap_action:
                  action: none
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
              -
                type: entities
                entities:
                  -
                    entity: binary_sensor.bedroom_bed_1_pressure_sensor
                    name: Pressure
                    icon: mdi:bed-outline
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_bed_jukka_fp2_occupancy
                    name: Bed FP2
                    icon: mdi:bed
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_bedside_jukka_fp2_sensor
                    name: Bedside
                    icon: mdi:walk
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_office_fp2_occupancy
                    name: Office FP2
                    icon: mdi:desk
                    state_color: True
                  -
                    entity: sensor.master_bed_sensor_master_bed_occupancy_left_value
              -
                type: entities
                entities:
                  -
                    entity: binary_sensor.bedroom_bed_2_pressure_sensor
                    name: Pressure
                    icon: mdi:bed-outline
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_bed_piia_fp2_occupancy
                    name: Bed FP2
                    icon: mdi:bed
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_bedside_piia_fp2_sensor
                    name: Bedside
                    icon: mdi:walk
                    state_color: True
                  -
                    entity: binary_sensor.bedroom_office_fp2_occupancy
                    name: Office FP2
                    icon: mdi:desk
                    state_color: True
                  -
                    entity: sensor.master_bed_sensor_master_bed_occupancy_right_value
            columns: 2
max_columns: 4

` 
### View: Elias

Path: $(@{theme=Backend-selected; title=Elias; path=elias; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_elias.png)

`yaml
theme: Backend-selected
title: Elias
path: elias
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: elias
          area_title: E Room
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_3_entity: binary_sensor.elias_bed_fp2_presence_sensor
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_3_active_color: lightgreen
          indicator_4_entity: binary_sensor.elias_desk_fp2_presence_sensor
          indicator_4_icon: mdi:chair-rolling
          indicator_4_state: on
          indicator_4_active_color: #088CF8
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            type: custom:mushroom-light-card
            entity: light.elias_ceiling_light
            use_light_color: False
            show_brightness_control: True
            show_color_temp_control: True
            collapsible_controls: False
            layout: horizontal
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: POWER
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mini-graph-card
                entities:
                  -
                    entity: sensor.elias_window_outlet_power
                    name: Energy
            columns: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        subtitle: Occupancy Settings
        alignment: center
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: elias
          -
            area_name: Elias
max_columns: 4

` 
### View: Anton

Path: $(@{theme=Backend-selected; title=Anton; path=anton; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_anton.png)

`yaml
theme: Backend-selected
title: Anton
path: anton
type: sections
layout:
  max_cols: 4
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: anton
          area_title: A Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.anton_temperature
          indicator_3_entity: binary_sensor.anton_bed_fp2_presence_sensor
          indicator_3_icon: mdi:bed
          indicator_3_state: on
          indicator_3_active_color: lightgreen
          indicator_4_entity: binary_sensor.anton_desk_fp2_presence_sensor
          indicator_4_icon: mdi:chair-rolling
          indicator_4_state: on
          indicator_4_active_color: #088CF8
      -
        type: vertical-stack
        cards:
          -
            square: False
            type: grid
            cards:
              -
                type: custom:decluttering-card
                template: minigraph_co2
                variables:
                  -
                    sensor: sensor.anton_carbon_dioxide
              -
                type: custom:decluttering-card
                template: minigraph_temperature
                variables:
                  -
                    sensor: sensor.anton_temperature
              -
                type: custom:decluttering-card
                template: minigraph_humidity
                variables:
                  -
                    sensor: sensor.anton_humidity
            columns: 3
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            square: False
            columns: 2
            type: grid
            cards:
              -
                type: custom:mushroom-light-card
                entity: light.anton_ceiling_light
                show_brightness_control: True
                show_color_temp_control: False
              -
                type: custom:mushroom-light-card
                entity: light.anton_window_light
                fill_container: True
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        subtitle: Occupancy Settings
        alignment: center
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: anton
          -
            area_name: Anton
max_columns: 4

` 
### View: Alisa

Path: $(@{theme=Backend-selected; title=Alisa; path=alisa; type=sections; layout=max_cols:5; subview=True; badges=System.Object[]; cards=System.Object[]; max_columns=5; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_alisa.png)

`yaml
theme: Backend-selected
title: Alisa
path: alisa
type: sections
layout: max_cols:5
subview: True
badges:
cards:
max_columns: 5
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: alisa
          area_title: Guest Room
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_1_entity: binary_sensor.alisa_bed_fp2_presence_sensor
          indicator_1_icon: mdi:bed-king
          indicator_1_state: on
          indicator_1_active_color: lightgreen
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.alisa_ceiling_light
        use_light_color: False
        show_brightness_control: True
        show_color_temp_control: True
        collapsible_controls: False
        layout: vertical
        fill_container: True
        grid_options:
          columns: 12
          rows: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: OCCUPANCY SETTINGS
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: alisa
          -
            area_name: Alisa
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.alisa_automation_mode
          - light.alisa_ceiling_light
          - light.alisa_lights
        exclude:
        discover_existing: False
        tags:
          - alisa
        time_step: 1
        show_header_toggle: False
        title: False

` 
### View: Living Room

Path: $(@{theme=Backend-selected; title=Living Room; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4; path=living_room}.path)`n
![View Screenshot](assets/images/view_living_room.png)

`yaml
theme: Backend-selected
title: Living Room
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: living_room
          area_title: Living Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.airthings_wave_temperature
          indicator_1_entity: light.fireplace
          indicator_1_icon: mdi:fireplace
          indicator_1_state: on
          indicator_1_active_color: orange
          indicator_1_animation_on: blink 2s ease infinite
          indicator_2_entity: media_player.70pus9005_12_2
          indicator_2_icon: mdi:television
          indicator_2_state: on
          indicator_2_active_color: lightgreen
          indicator_2_animation_on: blink 2s ease infinite
          indicator_3_entity: input_select.sofa_presence
          indicator_3_icon: mdi:sofa
          indicator_3_state: presence
          indicator_3_active_color: lightgreen
          indicator_5_entity: binary_sensor.inner_back_door_contact
          indicator_5_icon: mdi:door
          indicator_5_state: on
          indicator_6_entity: binary_sensor.backyard_door_sensor_contact
          indicator_6_icon: mdi:door
          indicator_6_state: on
          indicator_6_active_color: #FF4444
          indicator_6_animation_on: blink 0.5s ease infinite
          indicator_5_active_color: #FF4444
          indicator_5_animation_on: blink 0.5s ease infinite
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: ENVIRONMENT
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:decluttering-card
                template: minigraph_co2
                variables:
                  -
                    sensor: sensor.airthings_wave_living_room_co2
              -
                type: custom:decluttering-card
                template: minigraph_temperature
                variables:
                  -
                    sensor: sensor.airthings_wave_temperature
              -
                type: custom:decluttering-card
                template: minigraph_humidity
                variables:
                  -
                    sensor: sensor.airthings_wave_humidity
              -
                type: custom:mini-graph-card
                entities:
                  -
                    entity: sensor.airthings_wave_living_room_voc
                    name: VOC
                font_size_header: 12
                font_size: 75
                line_width: 8
                height: 200
                animate: True
                hours_to_show: 24
                show:
                  points: False
                color_thresholds:
                  -
                    value: 250
                    color: #5FE787
                  -
                    value: 500
                    color: #FF9800
                  -
                    value: 2000
                    color: #FF535B
                card_mod:
                  style: .header.flex .icon {
{% set sensor = states('sensor.airthings_wave_living_room_voc')|float %}
  {% if sensor > 2000 %}
    color: red;
  {% elif sensor > 500  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 2000 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 500  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

              -
                type: custom:mini-graph-card
                entities:
                  -
                    entity: sensor.airthings_wave_living_room_radon_1_day_average
                    name: Radon Short
                font_size_header: 12
                font_size: 75
                line_width: 8
                height: 200
                animate: True
                hours_to_show: 24
                show:
                  points: False
                color_thresholds:
                  -
                    value: 100
                    color: #5FE787
                  -
                    value: 150
                    color: #FF9800
                  -
                    value: 200
                    color: #FF535B
                card_mod:
                  style: .header.flex .icon {
  {% set sensor =
states('sensor.airthings_wave_living_room_radon_1_day_average')|float %}
  {% if sensor > 150 %}
    color: red;
  {% elif sensor > 100  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} 
} ha-card {
  {% if sensor > 200 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 150  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

              -
                type: custom:mini-graph-card
                entities:
                  -
                    entity: sensor.airthings_wave_living_room_radon_longterm_average
                    name: Radon Long
                font_size_header: 12
                font_size: 75
                line_width: 8
                height: 200
                animate: True
                hours_to_show: 24
                show:
                  points: False
                color_thresholds:
                  -
                    value: 100
                    color: #5FE787
                  -
                    value: 150
                    color: #FF9800
                  -
                    value: 200
                    color: #FF535B
                card_mod:
                  style: .header.flex .icon {
  {% set sensor =
  states('sensor.airthings_wave_living_room_radon_longterm_average')|float %}
  {% if sensor > 150 %}
    color: red;
  {% elif sensor > 100  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %}
} ha-card {
  {% if sensor > 200 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 150  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            square: False
            columns: 2
            type: grid
            cards:
              -
                type: custom:mushroom-light-card
                entity: light.living_room_ceiling_light
                fill_container: False
                use_light_color: False
                show_brightness_control: True
                show_color_control: False
                show_color_temp_control: False
                collapsible_controls: False
                name: Ceiling
                icon: 
              -
                type: custom:mushroom-light-card
                entity: light.floor_light
                show_brightness_control: True
                show_color_control: False
                show_color_temp_control: False
                use_light_color: False
                icon: mdi:floor-lamp
              -
                type: custom:mushroom-light-card
                entity: light.hallway_ceiling_light
                show_brightness_control: True
              -
                type: custom:mushroom-light-card
                entity: light.stairs_wled
                show_brightness_control: True
      -
        type: custom:mushroom-entity-card
        entity: switch.christmas_tree_plug
        icon: mdi:pine-tree
        layout: vertical
        name: Christmas Tree
        fill_container: True
        icon_color: accent
        visibility:
          -
            condition: state
            entity: switch.christmas_tree_plug
            state_not: unavailable
          -
            condition: state
            entity: switch.christmas_tree_plug
            state_not: unknown
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: AIR PURIFIER
            alignment: center
          -
            square: False
            columns: 1
            type: grid
            cards:
              -
                type: custom:mushroom-fan-card
                entity: fan.philips_air_purifier
                show_percentage_control: True
                layout: horizontal
                tap_action:
                  action: toggle
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
                card_mod:
                  style: ha-card {
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
}

              -
                square: False
                columns: 4
                type: grid
                cards:
                  -
                    type: custom:mushroom-template-card
                    entity: fan.philips_air_purifier
                    primary: Auto
                    secondary: 
                    icon: mdi:fan
                    layout: vertical
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
{% set mode = state_attr(entity,'preset_mode') %}
{% if mode == 'auto' %}
  blue
{% else %}
  disabled
{% endif %}
{% else %}
  disabled
{% endif %}

                    tap_action:
                      action: call-service
                      service: fan.set_preset_mode
                      data:
                        preset_mode: auto
                      target:
                        entity_id: fan.philips_air_purifier
                    card_mod:
                      style:
                        mushroom-shape-icon:
                          $: .shape ha-icon
  {
    {% set status = states(config.entity) %}
    {% if status == 'on' %}
    {% set mode = state_attr(config.entity,'preset_mode') %}
    {% if mode == 'auto' %}
    {% set speed = state_attr(config.entity,'percentage') | int %}
    {% if speed < 60 %}
    --icon-animation: rotation 2s linear infinite;
    {% elif speed < 80 %}
    --icon-animation: rotation 1s linear infinite;
    {% elif speed < 100 %}
    --icon-animation: rotation 0.6s linear infinite;
    {% else %}
    --icon-animation: rotation 0.3s linear infinite;
    {% endif %}
    {% endif %}
    {% endif %}
  }
  @keyframes rotation {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

                          .: ha-card {
  border-radius: 0px;
  box-shadow: 0px 0px;
  background-color: rgba(0,0,0,0);
  border: 5px solid #222;
}
:host {
}

                  -
                    type: custom:mushroom-template-card
                    entity: fan.philips_air_purifier
                    primary: Allergen
                    secondary: 
                    icon: mdi:fan
                    layout: vertical
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
{% set mode = state_attr(entity,'preset_mode') %}
{% if mode == 'allergen' %}
  blue
{% else %}
  disabled
{% endif %}
{% else %}
  disabled
{% endif %}

                    tap_action:
                      action: call-service
                      service: fan.set_preset_mode
                      data:
                        preset_mode: allergen
                      target:
                        entity_id: fan.philips_air_purifier
                    card_mod:
                      style:
                        mushroom-shape-icon:
                          $: .shape ha-icon
  {
    {% set status = states(config.entity) %}
    {% if status == 'on' %}
    {% set mode = state_attr(config.entity,'preset_mode') %}
    {% if mode == 'allergen' %}
    {% set speed = state_attr(config.entity,'percentage') | int %}
    {% if speed < 60 %}
    --icon-animation: rotation 2s linear infinite;
    {% elif speed < 80 %}
    --icon-animation: rotation 1s linear infinite;
    {% elif speed < 100 %}
    --icon-animation: rotation 0.6s linear infinite;
    {% else %}
    --icon-animation: rotation 0.3s linear infinite;
    {% endif %}
    {% endif %}
    {% endif %}
  }
  @keyframes rotation {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

                          .: ha-card {
  border-radius: 0px;
  box-shadow: 0px 0px;
  background-color: rgba(0,0,0,0);
  border: 5px solid #222;
}
:host {
}

                  -
                    type: custom:mushroom-template-card
                    entity: fan.philips_air_purifier
                    primary: Night
                    secondary: 
                    icon: mdi:fan
                    layout: vertical
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
{% set mode = state_attr(entity,'preset_mode') %}
{% if mode == 'night' %}
  blue
{% else %}
  disabled
{% endif %}
{% else %}
  disabled
{% endif %}

                    tap_action:
                      action: call-service
                      service: fan.set_preset_mode
                      data:
                        preset_mode: night
                      target:
                        entity_id: fan.philips_air_purifier
                    card_mod:
                      style:
                        mushroom-shape-icon:
                          $: .shape ha-icon
  {
    {% set status = states(config.entity) %}
    {% if status == 'on' %}
    {% set mode = state_attr(config.entity,'preset_mode') %}
    {% if mode == 'night' %}
    {% set speed = state_attr(config.entity,'percentage') | int %}
    {% if speed < 60 %}
    --icon-animation: rotation 2s linear infinite;
    {% elif speed < 80 %}
    --icon-animation: rotation 1s linear infinite;
    {% elif speed < 100 %}
    --icon-animation: rotation 0.6s linear infinite;
    {% else %}
    --icon-animation: rotation 0.3s linear infinite;
    {% endif %}
    {% endif %}
    {% endif %}
  }
  @keyframes rotation {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

                          .: ha-card {
  border-radius: 0px;
  box-shadow: 0px 0px;
  background-color: rgba(0,0,0,0);
  border: 5px solid #222;
}
:host {
}

                  -
                    type: custom:mushroom-template-card
                    entity: fan.philips_air_purifier
                    primary: Manual
                    secondary: 
                    icon: mdi:fan
                    layout: vertical
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
{% set mode = state_attr(entity,'preset_mode') %}
{% if mode == 'manual' %}
  blue
{% else %}
  disabled
{% endif %}
{% else %}
  disabled
{% endif %}

                    tap_action:
                      action: call-service
                      service: fan.set_preset_mode
                      data:
                        preset_mode: manual
                      target:
                        entity_id: fan.philips_air_purifier
                    card_mod:
                      style:
                        mushroom-shape-icon:
                          $: .shape ha-icon
  {
    {% set status = states(config.entity) %}
    {% if status == 'on' %}
    {% set mode = state_attr(config.entity,'preset_mode') %}
    {% if mode == 'manual' %}
    {% set speed = state_attr(config.entity,'percentage') | int %}
    {% if speed < 60 %}
    --icon-animation: rotation 2s linear infinite;
    {% elif speed < 80 %}
    --icon-animation: rotation 1s linear infinite;
    {% elif speed < 100 %}
    --icon-animation: rotation 0.6s linear infinite;
    {% else %}
    --icon-animation: rotation 0.3s linear infinite;
    {% endif %}
    {% endif %}
    {% endif %}
  }
  @keyframes rotation {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

                          .: ha-card {
  border-radius: 0px;
  box-shadow: 0px 0px;
  background-color: rgba(0,0,0,0);
  border: 5px solid #222;
}
:host {
}

              -
                square: False
                columns: 3
                type: grid
                cards:
                  -
                    type: custom:mushroom-template-card
                    entity: sensor.philips_air_purifier_pre_filter
                    primary: Pre-filter
                    secondary: {{ states(entity) }} hours
                    icon: mdi:air-filter
                    icon_color: {% set value = states(entity) | int
%}
{% if value < 2 %}
  red
{% elif value < 168 %}
  orange
{% else %}
  green
{% endif %}

                    tap_action:
                      action: none
                    hold_action:
                      action: more-info
                    double_tap_action:
                      action: none
                    card_mod:
                      style: :host { display:
  {% set filter = states(config.entity) | int
%}
  {% if filter > 168 %}
    inline;
  {% else %}
    inline;
  {% endif %}
}
@keyframes blink {
  50% { opacity: 0; }
}
ha-card {
  --mush-chip-border-radius: 0px;
  {% set filter = states(config.entity) |
  int %}
  {% if filter == 0 %}
  animation: blinks 1s ease infinite;
  {% endif %}
  border-radius: 0px;
}

                  -
                    type: custom:mushroom-template-card
                    entity: sensor.philips_air_purifier_hepa_filter
                    primary: Hepa
                    secondary: {{ states(entity) }} hours
                    icon: mdi:air-filter
                    icon_color: {% set value = states(entity) | int
%}
{% if value < 2 %}
  red
{% elif value < 168 %}
  orange
{% else %}
  green
{% endif %}

                    tap_action:
                      action: none
                    hold_action:
                      action: more-info
                    double_tap_action:
                      action: none
                    card_mod:
                      style: :host { display:
  {% set filter = states(config.entity) | int
%}
  {% if filter < 168 %}
    inline;
  {% else %}
    inline;
  {% endif %}
}
@keyframes blink {
  50% { opacity: 0; }
}
ha-card {
  --mush-chip-border-radius: 0px;
  {% set filter = states(config.entity) |
  int %}
  {% if filter == 0 %}
  animation: blinks 1s ease infinite;
  {% endif %}
  border-radius: 0px;
}

                  -
                    type: custom:mushroom-template-card
                    entity: sensor.philips_air_purifier_carbon_filter
                    primary: Carbon
                    secondary: {{ states(entity) }} hours
                    icon: mdi:air-filter
                    icon_color: {% set value = states(entity) | int
%}
{% if value < 2 %}
  red
{% elif value < 168 %}
  orange
{% else %}
  green
{% endif %}

                    tap_action:
                      action: none
                    hold_action:
                      action: more-info
                    double_tap_action:
                      action: none
                    card_mod:
                      style: :host { display:
  {% set filter = states(config.entity) | int
%}
  {% if filter < 168 %}
    inline;
  {% else %}
    inline;
  {% endif %}
}
@keyframes blink {
  50% { opacity: 0; }
}
ha-card {
  --mush-chip-border-radius: 0px;
  {% set filter = states(config.entity) |
  int %}
  {% if filter == 0 %}
  animation: blinks 1s ease infinite;
  {% endif %}
  border-radius: 0px;
}

              -
                square: False
                columns: 1
                type: grid
                cards:
                  -
                    type: custom:mushroom-template-card
                    primary: 
                    secondary: AC1214/10
                    icon: 
                    entity: fan.philips_air_purifier
                    card_mod:
                      style: ha-card {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}

      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            alignment: center
            subtitle: FIREPLACE
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-light-card
                entity: light.fireplace
                fill_container: True
                layout: vertical
                name: Fireplace
              -
                type: custom:mushroom-select-card
                entity: select.fireplace_preset
                name: Fireplace Preset
            columns: 2
          -
            type: custom:mushroom-entity-card
            entity: number.fireplace_fade_timeout
            icon: mdi:camera-timer
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            alignment: center
            subtitle: REMOTE CONTROLS
          -
            square: False
            columns: 3
            type: grid
            cards:
              -
                type: custom:mushroom-entity-card
                entity: input_button.tv_remote_button
                icon: mdi:remote-tv
                name: TV
                secondary_info: none
                icon_color: orange
                fill_container: True
                layout: vertical
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-popups/tv-remote
              -
                type: custom:mushroom-entity-card
                entity: input_button.tv_remote_button
                icon: mdi:remote
                name: SOUNDBAR
                secondary_info: none
                icon_color: orange
                fill_container: True
                layout: vertical
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-popups/soundbar-remote
              -
                type: custom:mushroom-entity-card
                entity: switch.remote_fix
                icon: mdi:auto-fix
                layout: vertical
                fill_container: True
                icon_color: primary
                secondary_info: none
                tap_action:
                  action: none
                hold_action:
                  action: call-service
                  service: automation.trigger
                  target:
                    entity_id: automation.fix_tv_remote
                  data:
                    skip_condition: True
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: WALL OUTLETS
            alignment: center
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-entity-card
                entity: sensor.living_room_media_outlet_power
                layout: vertical
                name: Media Wall Outlet
                fill_container: True
                icon_color: accent
              -
                type: custom:mushroom-entity-card
                entity: switch.living_room_media_outlet
                layout: vertical
                name: Media Wall Outlet
                tap_action:
                  action: none
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
                fill_container: True
                icon_color: green
              -
                type: custom:mushroom-entity-card
                entity: sensor.living_room_desk_outlet_channel_1_power
                layout: vertical
                fill_container: True
                name: Desk Wall Outlet
                icon_color: accent
              -
                type: custom:mushroom-entity-card
                entity: switch.air_purifier_plug
                layout: vertical
                name: Air Purifier Plug
                tap_action:
                  action: none
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
                fill_container: True
                icon_color: green
            columns: 2
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SOFA OUTLETS
            alignment: center
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: BATTERY LEVELS
            alignment: center
          -
            type: custom:auto-entities
            card:
              type: entities
            filter:
              include:
                -
                  entity_id: sensor.*living_room*battery*
                -
                  entity_id: sensor.*back_door*battery*
              exclude:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: DEVICES
          -
            type: horizontal-stack
            cards:
              -
                type: entities
                entities:
                  -
                    entity: sensor.airthings_wave_living_room_co2
                  -
                    entity: sensor.airthings_wave_living_room_humidity
                  -
                    entity: sensor.airthings_wave_living_room_pressure
                  -
                    entity: sensor.airthings_wave_living_room_radon_1_day_average
                  -
                    entity: sensor.airthings_wave_living_room_radon_longterm_average
                  -
                    entity: sensor.airthings_wave_living_room_temperature
                  -
                    entity: sensor.airthings_wave_living_room_voc
                  -
                    entity: sensor.airthings_wave_living_room_illuminance
                  -
                    entity: sensor.airthings_wave_living_room_battery
                  -
                    type: section
                    label: Sensors
                  -
                    entity: sensor.philips_air_purifier_pm25
                  -
                    entity: sensor.philips_air_purifier_allergen_index
                  -
                    type: section
                    label: Air Purifier
                  -
                    entity: fan.philips_air_purifier
                  -
                    entity: switch.air_purifier_plug
                    name: Air Purifier Power Plug
                  -
                    entity: sensor.philips_air_purifier_pre_filter
                  -
                    entity: sensor.philips_air_purifier_carbon_filter
                  -
                    entity: sensor.philips_air_purifier_hepa_filter
                  -
                    type: section
                    label: Presense
                show_header_toggle: False
                state_color: True
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: OCCUPANCY SETTINGS
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: living_room
          -
            area_name: Living Room
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: history-graph
        entities:
          -
            entity: binary_sensor.living_room_fp2_sensor
            name: Presence
          -
            entity: input_select.sofa_presence
            name: Sofa
        hours_to_show: 12
max_columns: 4
path: living_room

` 
### View: Kitchen

Path: $(@{title=Kitchen; path=kitchen; type=sections; sections=System.Object[]; max_columns=4; subview=True; cards=System.Object[]}.path)`n
![View Screenshot](assets/images/view_kitchen.png)

`yaml
title: Kitchen
path: kitchen
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: kitchen
          area_title: Kitchen
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.kitchen_fridge_door_device_temperature
          indicator_1_entity: binary_sensor.kitchen_fridge_door_contact
          indicator_1_icon: mdi:fridge
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 0.5s ease infinite
          indicator_2_entity: binary_sensor.kitchen_fridge_leak_sensor_water_leak
          indicator_2_icon: mdi:fridge-alert
          indicator_2_state: on
          indicator_2_active_color: #088CF8
          indicator_2_animation_on: blink 0.5s ease infinite
          indicator_3_entity: sensor.coffee_machine_state
          indicator_3_icon: mdi:coffee
          indicator_3_active_color: orange
          indicator_3_state: Running
          indicator_4_entity: switch.schedule_coffee_machine_schedule
          indicator_4_icon: mdi:coffee-to-go-outline
          indicator_4_state: on
          indicator_3_animation_on: blink 2s ease infinite
          indicator_4_active_color: lightgreen
          indicator_5_entity: sensor.dishwasher_current_status
          indicator_5_icon: mdi:dishwasher
          indicator_5_state: running
          indicator_5_active_color: skyblue
          indicator_5_animation_on: blink 2s ease infinite
          indicator_6_entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
          indicator_6_icon: mdi:dishwasher-alert
          indicator_6_state: on
          indicator_6_active_color: #088CF8
          indicator_6_animation_on: blink 0.5s ease infinite
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.kitchen_ceiling_light
        show_brightness_control: True
        show_color_control: False
        show_color_temp_control: False
        fill_container: False
        tap_action:
          action: toggle
      -
        type: custom:mushroom-light-card
        entity: light.kitchen_sink_light
        show_color_temp_control: False
        show_brightness_control: True
        tap_action:
          action: toggle
      -
        type: custom:mushroom-entity-card
        entity: switch.kitchen_wall_box_switch_left
        name: Ceiling Light Switch
        icon: mdi:light-switch
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: DISHWASHER
        alignment: center
      -
        type: custom:mushroom-entity-card
        entity: sensor.dishwasher_state
        layout: vertical
        name: Dishwasher
        icon: mdi:dishwasher
        fill_container: True
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
        name: Leak Sensor
        layout: vertical
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.dishwasher_door
        layout: vertical
        name: Dishwasher Door
        icon: mdi:dishwasher
        fill_container: True
      -
        type: custom:mushroom-entity-card
        entity: sensor.dishwasher_current_status
        layout: vertical
        name: Dishwasher Status
        icon: mdi:dishwasher
        fill_container: True
      -
        type: custom:mushroom-entity-card
        entity: sensor.dishwasher_remaining_time
        layout: vertical
        name: Dishwasher Remaining Time
        icon: mdi:dishwasher
        fill_container: True
      -
        type: custom:mushroom-entity-card
        entity: sensor.dishwasher_total_time
        layout: vertical
        name: Dishwasher Run Time
        icon: mdi:dishwasher
        fill_container: True
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: APPLIANCES
        alignment: center
      -
        type: custom:mushroom-template-card
        primary: Fridge Door
        secondary: {% set status = states(entity) %}
{% if status == 'off' %}
  Closed
{% else %}
  Open
{% endif %}
        icon: mdi:fridge
        entity: binary_sensor.kitchen_fridge_door_contact
        fill_container: True
        layout: vertical
        icon_color: {% set status = states(entity) %}
{% if status == 'off' %}
  green
{% else %}
  red
{% endif %}
      -
        type: custom:mushroom-template-card
        primary: Coffee Machine
        secondary_info: last-changed
        secondary: {% set status = states(entity) %}
{% if status == 'Running' %}
  Running
{% else %}
  {{ (as_timestamp(now()) - as_timestamp(states.sensor.coffee_machine_state.last_changed | default(0)) | int ) | timestamp_custom("%Hh %Mm", false) }} ago
{% endif %}
        icon: mdi:coffee
        entity: sensor.coffee_machine_state
        fill_container: True
        layout: vertical
        icon_color: {% set status = states(entity) %}
{% if status == 'Running' %}
  red
{% else %}
  green
{% endif %}
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: POWER
        alignment: center
      -
        type: custom:mushroom-entity-card
        entity: sensor.kitchen_coffee_machine_outlet_power
        layout: vertical
        name: Coffee Machine Power
        icon_color: accent
        tap_action:
          action: none
        double_tap_action:
          action: none
        hold_action:
          action: more-info
        fill_container: True
      -
        type: custom:mushroom-entity-card
        entity: switch.kitchen_coffee_machine_outlet
        layout: vertical
        name: Coffee Machine Outlet
        icon_color: green
        tap_action:
          action: none
        double_tap_action:
          action: none
        hold_action:
          action: more-info
        fill_container: True
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHT SETTINGS
        alignment: center
      -
        type: entities
        entities:
          -
            entity: light.kitchen_sink_light
          -
            entity: light.kitchen_ceiling_light
          -
            type: section
            label: Ceiling Bulbs
          -
            type: buttons
            entities:
              -
                entity: light.kitchen_ceiling_light_1
                name: Ceiling Light 1
              -
                entity: light.kitchen_ceiling_light_2
                name: Ceiling Light 2
              -
                entity: light.kitchen_ceiling_light_3
                name: Ceiling Light 3
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: BATTERY LEVELS
        alignment: center
      -
        type: custom:auto-entities
        card:
          type: entities
        filter:
          include:
            -
              entity_id: sensor.kitchen*battery*
            -
              entity_id: sensor.dishwasher*battery
          exclude:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: COFFEE MACHINE AUTOMATION
        alignment: center
      -
        type: entities
        entities:
          -
            entity: switch.kitchen_coffee_machine_outlet
            secondary_info: last-changed
            icon: mdi:coffee
      -
        type: custom:scheduler-card
        include:
          - switch.kitchen_coffee_machine_outlet
        exclude:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: markdown
        content: <li>{{ expand('light.kitchen_ceiling_light')|map(attribute='name')|list|join('<li>') }}
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:mushroom-title-card
            title: SETTINGS
            alignment: center
            subtitle: OCCUPANCY SETTINGS
      -
        type: history-graph
        entities:
          -
            entity: input_boolean.kitchen_occupancy
            name: Presence
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_6
            name: Entrance
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_4
            name: Table
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_3
            name: Cooking
        hours_to_show: 12
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: kitchen
          -
            area_name: Kitchen
      -
        type: entities
        entities:
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_1
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_6
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_5
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_4
          -
            entity: binary_sensor.kitchen_sensor_fp2_a94f_presence_sensor_3
max_columns: 4
subview: True
cards:

` 
### View: Hallway

Path: $(@{theme=Backend-selected; title=Hallway; path=hallway; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_hallway.png)

`yaml
theme: Backend-selected
title: Hallway
path: hallway
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: hallway
          area_title: Hallway
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.airthings_wave_temperature
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            type: vertical-stack
            cards:
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-light-card
                    entity: light.hallway_ceiling_light
                    show_brightness_control: True
                    name: Ceiling
                    collapsible_controls: False
                    layout: vertical
                    show_color_temp_control: True
                  -
                    type: custom:mushroom-light-card
                    entity: light.stairs_lights
                    show_brightness_control: True
                    show_color_control: True
                    show_color_temp_control: True
                    layout: vertical
                columns: 2
  -
    type: grid
    cards:
      -
        type: entities
        entities:
          -
            entity: binary_sensor.hallway_fp2_presence_sensor
          -
            entity: binary_sensor.downstairs_hallway_fp2_presence_sensor
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: hallway
          -
            area_name: Hallway
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
max_columns: 4

` 
### View: Bathroom

Path: $(@{theme=Backend-selected; title=Bathroom; path=bathroom; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_bathroom.png)

`yaml
theme: Backend-selected
title: Bathroom
path: bathroom
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: bathroom
          area_title: Bathroom
          temperature_sensor: sensor.airthings_wave_temperature
          indicator_1_entity: sensor.washing_machine_status
          indicator_1_icon: mdi:washing-machine
          indicator_1_state: Running
          indicator_1_active_color: #088CF8
          indicator_1_animation_on: blink 2s ease infinite
          indicator_2_entity: input_select.bathroom_toilet_presence
          indicator_2_icon: mdi:toilet
          indicator_3_icon: mdi:shower-head
          indicator_3_active_color: #088CF8
          indicator_2_active_color: orange
          indicator_3_entity: input_select.shower_presence
          indicator_3_state: presence
          indicator_2_state: presence
          temp_sensor_entity: sensor.aqara_w500_temperature_smoothed
          indicator_6_entity: sensor.aqara_w500_bathroom_heating_hvac
          indicator_6_icon: mdi:heating-coil
          indicator_6_state: heating
          indicator_6_active_color: #FF4444
          indicator_6_animation_on: blink 2s ease infinite
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.bathroom_wall_box_switch_right
        name: Sauna
        layout: vertical
        grid_options:
          columns: 4
          rows: 2
      -
        type: custom:mushroom-light-card
        entity: light.bathroom_lightstrip
        layout: vertical
        name: Table
        grid_options:
          columns: 4
          rows: 2
      -
        type: custom:mushroom-light-card
        name: Ceiling
        layout: vertical
        grid_options:
          columns: 4
          rows: 2
        entity: light.bathroom_wall_box_switch_right
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: APPLIANCES
        alignment: center
      -
        type: custom:mushroom-entity-card
        entity: sensor.washing_machine_status
        grid_options:
          columns: 12
          rows: 1
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: HEATING
        alignment: center
      -
        type: thermostat
        entity: climate.aqara_w500
        name: Bathroom Floor
        show_current_as_primary: False
        features:
          -
            type: climate-hvac-modes
      -
        type: history-graph
        show_names: True
        entities:
          -
            entity: sensor.aqara_w500_state
            name:  
          -
            entity: climate.aqara_w500
          -
            entity: sensor.aqara_w500_temperature_smoothed
        hours_to_show: 12
        logarithmic_scale: False
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: OCCUPANCY
        alignment: center
      -
        type: custom:mushroom-entity-card
        entity: input_select.bathroom_presence
        layout: vertical
        grid_options:
          columns: 4
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: input_select.shower_presence
        layout: vertical
        grid_options:
          columns: 4
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: input_select.bathroom_toilet_presence
        layout: vertical
        grid_options:
          columns: 4
          rows: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: bathroom
          -
            area_name: Bathroom
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: heading
        heading: Floor Heating Automations
        heading_style: title
      -
        type: custom:scheduler-card
        title: Floor Heating
        discover_existing: False
        time_step: 5
        tags:
          - Bathroom
        include:
          - climate.aqara_w500
          - sensor.nord_pool_fi_current_price
        display_options:
          secondary_info:
            - relative-time
        default_editor: single
        sort_by:
          - state
          - relative-time
        show_header_toggle: False
      -
        type: markdown
        content: *Default Temperature* is the heating base temperature.

If the thermostate is turned higher than the default, the *Heating Timer* will keep this new temperature until the timer runs out.

The *Heating Timer* tells how long the heating will still run
      -
        type: custom:timer-bar-card
        entity: timer.bathroom_floor_heating_timer
      -
        type: custom:mushroom-number-card
        entity: input_number.bathroom_floor_heat_default_temperature
        name: Default Temperature
        grid_options:
          columns: 6
          rows: 2
        icon_color: accent
      -
        type: custom:mushroom-number-card
        entity: input_number.bathroom_floor_heat_target_temperature
        name: Target Temperature
        grid_options:
          columns: 6
          rows: 2
        icon_color: red
      -
        type: custom:mushroom-number-card
        entity: input_number.bathroom_floor_heat_override_duration
        name: Heating Timer
        grid_options:
          columns: 12
          rows: 2
        icon_color: teal
  -
    type: grid
    cards:
max_columns: 4

` 
### View: Sauna

Path: $(@{theme=Backend-selected; title=Sauna; type=sections; subview=True; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4; path=sauna}.path)`n
![View Screenshot](assets/images/view_sauna.png)

`yaml
theme: Backend-selected
title: Sauna
type: sections
subview: True
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: sauna
          area_title: Sauna
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.ruuvitag_8572_temperature
          indicator_1_entity: binary_sensor.sauna_door_contact
          indicator_1_icon: mdi:door
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 1s ease infinite
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.bathroom_wall_box_switch_left
        name: Sauna
        layout: vertical
        grid_options:
          columns: full
          rows: 2
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: ENVIRONMENT
        alignment: center
      -
        type: vertical-stack
        cards:
          -
            square: False
            type: grid
            cards:
              -
                type: custom:decluttering-card
                template: minigraph_temperature
                variables:
                  -
                    sensor: sensor.ruuvitag_8572_temperature
              -
                type: custom:decluttering-card
                template: minigraph_humidity
                variables:
                  -
                    sensor: sensor.ruuvitag_8572_humidity
            columns: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: sauna
          -
            area_name: Sauna
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
max_columns: 4
path: sauna

` 
### View: Mud Room

Path: $(@{theme=Backend-selected; title=Mud Room; path=mud_room; type=sections; layout=; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_mud_room.png)

`yaml
theme: Backend-selected
title: Mud Room
path: mud_room
type: sections
layout:
  max_cols: 5
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: mud_room
          area_title: Mud Room
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.mud_room_motion_sensor_device_temperature
          indicator_1_entity: binary_sensor.front_door_lock_door
          indicator_1_icon: mdi:door
          indicator_1_state: on
          indicator_1_active_color: #FF4444
          indicator_1_animation_on: blink 0.5s ease infinite
          indicator_2_entity: lock.front_door_lock
          indicator_2_icon: mdi:lock
          indicator_2_state: unlocked
          indicator_2_active_color: #FF4444
          indicator_2_animation_on: blink 0.5s ease infinite
          indicator_6_entity: binary_sensor.mud_room_door_sensor_contact
          indicator_6_icon: mdi:door
          indicator_6_state: on
          indicator_6_active_color: orange
          indicator_6_animation_on: blink 1s ease infinite
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHT
            alignment: center
          -
            type: vertical-stack
            cards:
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-light-card
                    entity: light.mud_room_ceiling_light
                    layout: vertical
                    fill_container: True
                    use_light_color: True
                columns: 1
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.mud_room_motion_sensor_occupancy
        layout: vertical
        name: Mudroom Occupancy
        icon: mdi:account
        grid_options:
          columns: 12
          rows: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: mud_room
          -
            area_name: Mud Room
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: SCHEDULES
        alignment: center
      -
        type: markdown
        content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.mud_room_automation_mode
          - light.mud_room_ceiling_light
          - light.mud_room_lights
        exclude:
        discover_existing: False
        tags:
          - mud-room
        title: False
        display_options:
          primary_info: default
          secondary_info:
            - relative-time
            - time
            - additional-tasks
          icon: action
        sort_by:
          - state
          - relative-time
        time_step: 5
        show_header_toggle: False
max_columns: 4

` 
### View: Toilet

Path: $(@{theme=Backend-selected; title=Toilet; path=toilet; type=sections; subview=True; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_toilet.png)

`yaml
theme: Backend-selected
title: Toilet
path: toilet
type: sections
subview: True
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: toilet
          area_title: Toilet
          temperature_sensor: sensor.airthings_wave_temperature
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: LIGHTS
            alignment: center
          -
            type: custom:mushroom-light-card
            entity: light.toilet_wall_box_switch
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: backyard
          -
            area_name: Backyard
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SENSOR SETTINGS
            alignment: center
      -
        type: entities
        entities:
          -
            entity: binary_sensor.toilet_mmwave
          -
            entity: binary_sensor.toilet_pir
          -
            entity: number.toilet_distance
          -
            entity: number.toilet_latency
max_columns: 4

` 
### View: Lobby

Path: $(@{theme=Backend-selected; title=Lobby; path=lobby; type=sections; subview=True; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_lobby.png)

`yaml
theme: Backend-selected
title: Lobby
path: lobby
type: sections
subview: True
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: lobby
          area_title: Lobby
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.bedroom_temperature
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mushroom-light-card
            entity: light.lobby_ceiling_light
            fill_container: True
            layout: vertical
            show_brightness_control: True
            use_light_color: True
        columns: 1
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        subtitle: OCCUPANCY SETTINGS
        alignment: center
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: lobby
          -
            area_name: Lobby
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: SCHEDULES
        alignment: center
      -
        type: markdown
        content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.office_automation_mode
          - light.lobby_light
          - light.lobby_lights
          - sensor.presence_sensor_fp2_65ab_light_sensor_light_level
        exclude:
        discover_existing: False
        tags:
          - Lobby
        time_step: 1
        show_header_toggle: False
        title: False
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: AUTOMATION MODE SCHEDULES
        alignment: center
      -
        type: markdown
        content: Automation Mode Changes, based on time or sun.
      -
        type: custom:scheduler-card
        include:
          - input_select.lobby_automation_mode
        exclude:
        discover_existing: False
        tags:
          - lobby-mode-control
          - office-mode-control
        time_step: 1
        show_header_toggle: False
        title: False
max_columns: 4

` 
### View: Stairs

Path: $(@{title=Stairs; path=stairs; type=sections; max_columns=5; subview=True; sections=System.Object[]; cards=System.Object[]}.path)`n
![View Screenshot](assets/images/view_stairs.png)

`yaml
title: Stairs
path: stairs
type: sections
max_columns: 5
subview: True
sections:
  -
    type: grid
    cards:
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: stairs
          area_title: Stairs
          temperature_sensor: sensor.airthings_wave_temperature
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: LIGHTS
        alignment: center
      -
        type: custom:mushroom-light-card
        entity: light.stairs_wled
        layout: vertical
        icon: mdi:led-strip-variant
        fill_container: True
        show_brightness_control: True
        show_color_control: False
        use_light_color: True
        grid_options:
          columns: 6
          rows: 3
      -
        type: custom:mushroom-select-card
        entity: select.stairs_wled_preset
        name: Stairs Preset
        fill_container: True
        layout: vertical
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        subtitle: OCCUPANCY SETTINGS
        alignment: center
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: stairs
          -
            area_name: Stairs
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.stairs_automation_mode
          - light.stairs_lights
          - light.stairs_wled
        exclude:
        discover_existing: False
        tags:
          - stairs
        time_step: 1
        show_header_toggle: False
        title: False
cards:

` 
### View: Front Door

Path: $(@{title=Front Door; path=front-door; type=sections; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_front-door.png)

`yaml
title: Front Door
path: front-door
type: sections
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: vertical-stack
        cards:
          -
            type: custom:frigate-card
            cameras:
              -
                camera_entity: camera.g4_doorbell_pro_poe_high_resolution_channel
            view:
              default: live
              interaction_seconds: 1200
            live:
              preload: True
              controls:
                builtin: True
              lazy_load: True
              show_image_during_load: False
            performance:
              style:
                box_shadow: True
                border_radius: True
            image:
              zoomable: True
            menu:
              position: bottom
              button_size: 48
              buttons:
                cameras:
                  enabled: False
                snapshots:
                  enabled: False
                clips:
                  enabled: True
                  priority: 30
                substreams:
                  enabled: False
                timeline:
                  enabled: False
                microphone:
                  enabled: False
                frigate:
                  enabled: False
                download:
                  priority: 35
                screenshot:
                  enabled: True
              style: outside
              alignment: left
            media_gallery:
              controls:
                thumbnails:
                  show_details: False
            timeline:
              show_recordings: True
          -
            type: custom:frigate-card
            cameras:
              -
                camera_entity: camera.front_porch_frigate
            view:
              default: live
              timeout_seconds: 1200
            live:
              preload: True
              controls:
                builtin: True
              lazy_load: True
              show_image_during_load: False
            performance:
              style:
                box_shadow: True
                border_radius: True
            image:
              zoomable: True
            menu:
              position: bottom
              button_size: 48
              buttons:
                cameras:
                  enabled: False
                snapshots:
                  enabled: False
                clips:
                  enabled: True
                  priority: 30
                substreams:
                  enabled: False
                timeline:
                  enabled: False
                microphone:
                  enabled: False
                frigate:
                  enabled: False
                download:
                  priority: 35
                screenshot:
                  enabled: True
              style: outside
              alignment: left
            media_gallery:
              controls:
                thumbnails:
                  show_details: False
            timeline:
              show_recordings: True
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-light-card
                entity: light.front_door_rail_light
                icon: mdi:string-lights
                layout: vertical
                name: Front Door Light
                tap_action:
                  action: more-info
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
                use_light_color: False
              -
                type: custom:mushroom-light-card
                entity: light.mud_room_ceiling_light
                icon: 
                layout: vertical
                name: Mud Room Light
                tap_action:
                  action: more-info
                hold_action:
                  action: more-info
                double_tap_action:
                  action: none
                use_light_color: False
            columns: 2
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-lock-card
                entity: lock.front_door_lock
                layout: vertical
                name: Lock
              -
                type: custom:mushroom-entity-card
                entity: binary_sensor.front_porch_frigate_person_occupancy
                layout: vertical
                name: Persons
                icon: mdi:account
                fill_container: True
              -
                type: custom:mushroom-entity-card
                entity: binary_sensor.front_door_lock_door
                icon: mdi:door
                layout: vertical
                name: Lock Contact
                fill_container: True
              -
                type: custom:mushroom-entity-card
                entity: binary_sensor.front_door_lock_door
                icon: mdi:door
                layout: vertical
                name: Contact
                fill_container: True
            columns: 4
          -
            square: False
            type: grid
            cards:
              -
                type: custom:mushroom-entity-card
                entity: input_select.home_front_door_occupancy_state
                name: Front State
                fill_container: True
                layout: vertical
              -
                type: custom:mushroom-alarm-control-panel-card
                entity: alarm_control_panel.front_door
                states:
                  - armed_home
                  - armed_away
                  - armed_night
                  - armed_custom_bypass
                fill_container: True
                layout: vertical
            columns: 2
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: EVENTS
            alignment: center
          -
            type: custom:frigate-card
            cameras:
              -
                camera_entity: camera.frontdoor_doorbell
            view:
              default: clips
              update_cycle_camera: False
              dark_mode: on
              timeout_seconds: 1200
              update_seconds: 120
            menu:
              buttons:
                frigate:
                  enabled: True
                  alignment: matching
                  icon: mdi:view-grid
                live:
                  enabled: False
                camera_ui:
                  enabled: True
                cameras:
                  enabled: False
                clips:
                  enabled: False
                timeline:
                  enabled: False
                snapshots:
                  enabled: False
                screenshot:
                  enabled: True
              style: outside
              position: bottom
              alignment: left
            timeline:
              media: all
              controls:
                thumbnails:
                  size: 100
            media_gallery:
              controls:
                thumbnails:
                  size: 125
                  show_details: False
            dimensions:
              aspect_ratio: 4:3
          -
            type: custom:frigate-card
            cameras:
              -
                camera_entity: camera.front_porch_frigate
            view:
              default: clips
              update_cycle_camera: False
              dark_mode: on
              timeout_seconds: 1200
              update_seconds: 120
            menu:
              buttons:
                frigate:
                  enabled: True
                  alignment: matching
                  icon: mdi:view-grid
                live:
                  enabled: False
                camera_ui:
                  enabled: True
                cameras:
                  enabled: False
                clips:
                  enabled: False
                timeline:
                  enabled: False
                snapshots:
                  enabled: False
                screenshot:
                  enabled: True
              style: outside
              position: bottom
              alignment: left
            timeline:
              media: all
              controls:
                thumbnails:
                  size: 100
            media_gallery:
              controls:
                thumbnails:
                  size: 125
                  show_details: False
            dimensions:
              aspect_ratio: 4:3
          -
            type: custom:auto-entities
            card:
              type: entities
            filter:
              include:
                -
                  entity_id: *front_door_battery*
                -
                  entity_id: *keypad_battery*
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: front_door
          -
            area_name: Front Door
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: SCHEDULES
        alignment: center
      -
        type: markdown
        content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.front_door_automation_mode
          - light.front_door_light
          - light.front_door_rail_light
        exclude:
        discover_existing: False
        title: 
        time_step: 5
        display_options:
          primary_info: default
          secondary_info:
            - relative-time
            - time
            - additional-tasks
          icon: action
        tags:
          - Front Door
max_columns: 4

` 
### View: Backyard

Path: $(@{title=Backyard; type=sections; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=4; subview=False; path=backyard}.path)`n
![View Screenshot](assets/images/view_backyard.png)

`yaml
title: Backyard
type: sections
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: BACKYARD
        alignment: center
        title_tap_action:
          action: navigate
          navigation_path: /lovelace
        subtitle: CONTROLS
      -
        type: custom:frigate-card
        cameras:
          -
            camera_entity: camera.backyard_frigate
        menu:
          style: outside
          position: bottom
          buttons:
            cameras:
              enabled: False
            frigate:
              enabled: False
            live:
              enabled: True
            recordings:
              enabled: False
              priority: 50
            expand:
              enabled: False
            play:
              enabled: True
            screenshot:
              enabled: True
            snapshots:
              enabled: False
            clips:
              priority: 30
              enabled: True
            timeline:
              priority: 40
              enabled: False
            mute:
              enabled: False
            microphone:
              enabled: False
            download:
              priority: 35
          alignment: left
          button_size: 48
        view:
          default: live
          timeout_seconds: 1200
        live:
          preload: True
          lazy_load: True
          zoomable: True
          draggable: False
          show_image_during_load: False
        media_gallery:
          controls:
            thumbnails:
      -
        type: custom:mushroom-light-card
        entity: light.backyard_plug
        icon: mdi:string-lights
        layout: vertical
        name: Backyard Light
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.inner_back_door_contact
        fill_container: True
        layout: vertical
        tap_action:
          action: none
        hold_action:
          action: none
        double_tap_action:
          action: none
        icon: mdi:door
        name: Inner Door
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.backyard_door_sensor_contact
        fill_container: True
        layout: vertical
        tap_action:
          action: none
        hold_action:
          action: none
        double_tap_action:
          action: none
        icon: mdi:door
        name: Backyard Door
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: binary_sensor.backyard_frigate_person_occupancy
        layout: vertical
        icon: mdi:account
        grid_options:
          columns: 3
          rows: 2
        name: Person(s)
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: ENVIRONMENT
        alignment: center
      -
        type: custom:mini-graph-card
        hours_to_show: 24
        name: Temperature
        entities:
          - sensor.backyard_temperature
        color_thresholds:
          -
            value: 0
            color: skyblue
          -
            value: 3
            color: white
          -
            value: 10
            color: yellow
          -
            value: 20
            color: orange
          -
            value: 25
            color: red
        layout_options:
          grid_columns: 2
      -
        type: custom:mini-graph-card
        name: Humidity
        entities:
          - sensor.backyard_humidity
        hours_to_show: 24
        color_thresholds:
          -
            value: 20
            color: #FF535B
          -
            value: 30
            color: #5FE787
          -
            value: 60
            color: #03A9F4
        layout_options:
          grid_columns: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:mushroom-entity-card
        entity: input_select.backyard_presence
        layout: vertical
      -
        type: custom:mushroom-entity-card
        entity: input_boolean.backyard_occupancy
        layout: vertical
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: backyard
          -
            area_name: Backyard
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
      -
        type: custom:scheduler-card
        include:
          - input_select.backyard_automation_mode
          - light.backyard_plug
        exclude:
        discover_existing: False
        tags:
          - Backyard
        title: False
        display_options:
          primary_info: default
          secondary_info:
            - relative-time
            - time
            - additional-tasks
          icon: action
        sort_by:
          - state
          - relative-time
        time_step: 5
        show_header_toggle: False
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: CAMERA SETTINGS
        alignment: center
      -
        type: entities
        entities:
          -
            entity: binary_sensor.backyard_cam_motion
          -
            entity: select.backyard_cam_infrared_mode
          -
            entity: binary_sensor.backyard_cam_is_dark
          -
            entity: switch.backyard_cam_privacy_mode
          -
            entity: switch.backyard_cam_detections_motion
          -
            entity: number.backyard_cam_microphone_level
          -
            entity: select.backyard_cam_hdr_mode
          -
            entity: switch.backyard_cam_hdr_mode
          -
            entity: switch.backyard_cam_overlay_show_date
          -
            entity: switch.backyard_cam_overlay_show_name
          -
            entity: switch.backyard_cam_overlay_show_nerd_mode
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: FRIGATE SETTINGS
        alignment: center
      -
        type: picture
        image_entity: image.backyard_frigate_person
        grid_options:
          columns: 3
          rows: auto
      -
        type: entities
        entities:
          -
            entity: sensor.backyard_frigate_all_count
          -
            entity: switch.backyard_frigate_detect
          -
            entity: switch.backyard_frigate_motion
          -
            entity: binary_sensor.backyard_frigate_motion
          -
            entity: sensor.backyard_frigate_person_count
          -
            entity: binary_sensor.backyard_frigate_person_occupancy
          -
            entity: switch.backyard_frigate_recordings
          -
            entity: switch.backyard_frigate_snapshots
    visibility:
      -
        condition: user
        users:
          - 5f4dd0e939344fd6b58ed4299cdafcd6
max_columns: 4
subview: False
path: backyard

` 
### View: Storage

Path: $(@{title=Storage; type=sections; layout=; badges=System.Object[]; cards=System.Object[]; sections=System.Object[]; max_columns=5; path=storage}.path)`n
![View Screenshot](assets/images/view_storage.png)

`yaml
title: Storage
type: sections
layout:
  max_cols: 5
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: STORAGE
        alignment: center
        title_tap_action:
          action: navigate
          navigation_path: /lovelace
        subtitle: CONTROLS
      -
        type: custom:frigate-card
        cameras:
          -
            camera_entity: camera.storage_cam_high
        live:
          preload: True
        view:
          default: live
          timeout_seconds: 1200
        menu:
          style: outside
          position: bottom
          buttons:
            frigate:
              enabled: False
            substreams:
              enabled: False
            cameras:
              enabled: False
            snapshots:
              enabled: False
            recordings:
              enabled: False
              priority: 10
            clips:
              priority: 10
            timeline:
              enabled: False
            screenshot:
              enabled: True
          button_size: 48
        performance:
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mushroom-light-card
            entity: light.storage_light
            icon: 
            layout: vertical
            name: Storage Light
            tap_action:
              action: toggle
            hold_action:
              action: more-info
            double_tap_action:
              action: none
        columns: 1
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: EVENTS
        alignment: center
      -
        type: custom:frigate-card
        cameras:
          -
            camera_entity: camera.storage_frigate
        live:
          preload: True
        view:
          default: clips
          timeout_seconds: 1200
        menu:
          style: outside
          position: bottom
          buttons:
            frigate:
              enabled: False
            substreams:
              enabled: False
            cameras:
              enabled: False
            snapshots:
              enabled: False
            recordings:
              enabled: False
              priority: 10
            clips:
              priority: 10
            timeline:
              enabled: False
            screenshot:
              enabled: True
          button_size: 48
        performance:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: CAMERA SETTINGS
        alignment: center
      -
        type: entities
        entities:
          -
            entity: binary_sensor.storage_cam_motion
          -
            entity: select.storage_cam_infrared_mode
          -
            entity: binary_sensor.storage_cam_is_dark
          -
            entity: switch.storage_cam_privacy_mode
          -
            entity: switch.storage_cam_detections_motion
          -
            entity: number.storage_cam_microphone_level
          -
            entity: select.storage_cam_hdr_mode
          -
            entity: switch.storage_cam_hdr_mode
          -
            entity: switch.storage_cam_overlay_show_date
          -
            entity: switch.storage_cam_overlay_show_name
          -
            entity: switch.storage_cam_overlay_show_nerd_mode
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: FRIGATE SETTINGS
        alignment: center
      -
        type: entities
        entities:
          -
            entity: sensor.storage_frigate_all_count
          -
            entity: switch.storage_frigate_detect
          -
            entity: switch.storage_frigate_motion
          -
            entity: binary_sensor.storage_frigate_motion
          -
            entity: sensor.storage_frigate_person_count
          -
            entity: binary_sensor.storage_frigate_person_occupancy
          -
            entity: switch.storage_frigate_recordings
          -
            entity: switch.storage_frigate_snapshots
    visibility:
      -
        condition: user
        users:
          - 5f4dd0e939344fd6b58ed4299cdafcd6
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SETTINGS
        alignment: center
        subtitle: Occupancy
      -
        type: custom:decluttering-card
        template: area_occupancy_settings
        variables:
          -
            area: storage
          -
            area_name: Storage
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: SCHEDULES
            alignment: center
          -
            type: markdown
            content: These schedules work when they are set on and _Presence Automation Mode_ is set to _Schedule Mode_
max_columns: 5
path: storage

` 
### View: Settings

Path: $(@{title=Settings; path=settings; cards=System.Object[]; type=sections; sections=System.Object[]; max_columns=7}.path)`n
![View Screenshot](assets/images/view_settings.png)

`yaml
title: Settings
path: settings
cards:
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: kitchen
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: hallway
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: stairs
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: lobby
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: living_room
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: toilet
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: bedroom
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: office
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: mud_room
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: storage
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: bathroom
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: backyard
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: front_door
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: elias
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: anton
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: alisa
      -
        type: custom:decluttering-card
        template: presence_settings
        variables:
          -
            area: sauna
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: place_presence_settings
        variables:
          -
            area: shower
      -
        type: custom:decluttering-card
        template: place_presence_settings
        variables:
          -
            area: bathroom_toilet
      -
        type: custom:decluttering-card
        template: place_presence_settings
        variables:
          -
            area: sofa
max_columns: 7

` 
### View: Electricity

Path: $(@{type=sections; max_columns=4; title=Electricity; path=electricity; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_electricity.png)

`yaml
type: sections
max_columns: 4
title: Electricity
path: electricity
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: Today's Energy Prices Per Hour
        heading_style: subtitle
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:config-template-card
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
                stroke:
                  dashArray: 4
                chart:
                  height: 280px
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
                  show: True
                  borderColor: rgba(255,255,255,0.2)
                xaxis:
                  position: bottom
                  labels:
                    format: H
                    hideOverlappingLabels: True
                    offsetX: 0
                  axisTicks:
                    offsetX: 0
                  all_series_config:
                    show:
                      offset_in_name: True
                legend:
                  show: True
                  position: bottom
                  horizontalAlign: left
                  fontSize: 14px
                  itemMargin:
                    vertical: 10
                    horizontal: 10
                tooltip:
                  enabled: False
                  style:
                    fontSize: 14px
              header:
                title: Electricity Today
                standard_format: False
                show: False
                show_states: True
                colorize_states: True
              show:
                last_updated: True
              experimental:
                color_threshold: True
              now:
                show: True
              yaxis:
                -
                  id: cost
                  opposite: True
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
                    title:
                      text: c/kWh
                      rotate: 0
                      offsetX: -25
                      offsetY: -90
                      style:
                        fontSize: 10px
                        fontFamily: verdana
                        color: orange
                -
                  id: energy
                  max: ~2
                  min: 0
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
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
                -
                  entity: sensor.electricity_prices
                  name: Price
                  yaxis_id: cost
                  type: column
                  opacity: 0.8
                  stroke_width: 0
                  show:
                    legend_value: False
                    extremas: True
                    in_header: True
                    header_color_threshold: True
                  data_generator: return entity.attributes.data.map(entry => {
  return [new Date(entry.start).getTime(), entry.price];
});

                  color_threshold:
                    -
                      value: -10
                      color: lightgreen
                    -
                      value: ${PRICELOW * 1}
                      color: orange
                    -
                      value: ${PRICEHIGH * 1}
                      color: darkred
                -
                  entity: sensor.electricity_daily_average_cents
                  name: Avg Price
                  yaxis_id: cost
                  type: line
                  color: yellow
                  stroke_width: 1
                  opacity: 0.8
                  group_by:
                    func: last
                    duration: 24h
                  show:
                    legend_value: False
                    datalabels: False
                    extremas: True
                    in_header: True
                -
                  entity: sensor.home_total_energy_hourly
                  name: Energy (kWh)
                  color: skyblue
                  type: line
                  opacity: 1
                  yaxis_id: energy
                  stroke_width: 2
                  float_precision: 1
                  unit: kWh
                  group_by:
                    duration: 1h
                    func: delta
                  show:
                    legend_value: False
                    datalabels: False
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
      -
        type: heading
        heading: Tomorrow's Energy Prices Per 15 minutes
        heading_style: subtitle
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:config-template-card
            variables:
              PRICEHIGH: states['sensor.nordpool_today_32nd_highest_price'].state
              PRICELOW: states['sensor.nordpool_today_32nd_lowest_price'].state
            entities:
              - sensor.nordpool_kwh_fi_eur
            card:
              type: custom:apexcharts-card
              graph_span: 1d
              span:
                start: day
              apex_config:
                stroke:
                  dashArray: 2
                chart:
                  height: 180px
                  width: 115%
                  offsetX: -30
                title:
                  text: Energy Price Today
                  align: center
                  offsetY: 10
                  style:
                    fontSize: 13px
                    fontFamily: Verdana
                    fontWeight: normal
                grid:
                  show: True
                  borderColor: rgba(255,255,255,0.2)
                xaxis:
                  position: bottom
                  labels:
                    format: H
                    hideOverlappingLabels: True
                    offsetX: 0
                  axisTicks:
                    offsetX: 0
                legend:
                  show: False
                  itemMargin:
                    vertical: 10
                    horizontal: 10
                tooltip:
                  enabled: False
                  style:
                    fontSize: 14px
              show:
                last_updated: True
              experimental:
                color_threshold: True
              header:
                show_states: True
                colorize_states: True
              now:
                show: True
              yaxis:
                -
                  id: cost
                  opposite: True
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
                    title:
                      text: c/kWh
                      rotate: 0
                      offsetX: -25
                      offsetY: -70
                      style:
                        fontSize: 10px
                        fontFamily: verdana
                        color: orange
                -
                  id: energy
                  max: ~2
                  min: 0
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
                    title:
                      text: kWh
                      rotate: 0
                      offsetX: 25
                      offsetY: -70
                      style:
                        color: skyblue
                        fontSize: 10px
                        fontFamily: verdana
              series:
                -
                  entity: sensor.nordpool_kwh_fi_eur
                  name: Price
                  yaxis_id: cost
                  type: column
                  opacity: 0.8
                  stroke_width: 0
                  show:
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
                  data_generator: return entity.attributes.raw_today.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
});

                  color_threshold:
                    -
                      value: -10
                      color: lightgreen
                    -
                      value: ${PRICELOW*1}
                      color: orange
                    -
                      value: ${PRICEHIGH * 1}
                      color: darkred
                -
                  entity: sensor.home_total_energy_hourly
                  name: Energy (kWh)
                  color: skyblue
                  type: line
                  opacity: 1
                  yaxis_id: energy
                  stroke_width: 2
                  float_precision: 1
                  extend_to: False
                  unit: kWh
                  group_by:
                    duration: 15min
                    func: diff
                  show:
                    legend_value: False
                    datalabels: False
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
      -
        type: custom:config-template-card
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
              height: 180px
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
              show: True
              borderColor: rgba(255,255,255,0.2)
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
            legend:
              show: False
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              enabled: False
              style:
                fontSize: 14px
          show:
            last_updated: True
          experimental:
            color_threshold: True
          header:
            show_states: True
            colorize_states: True
          now:
            show: True
          yaxis:
            -
              id: cost
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: 0
                  offsetX: -25
                  offsetY: -70
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~2
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: kWh
                  rotate: 0
                  offsetX: 25
                  offsetY: -70
                  style:
                    color: skyblue
                    fontSize: 10px
                    fontFamily: verdana
          series:
            -
              entity: sensor.electricity_prices
              name: Price
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                extremas: True
                in_header: raw
                header_color_threshold: True
              data_generator: const tomorrow = new Date();
tomorrow.setHours(0, 0, 0, 0);
tomorrow.setDate(tomorrow.getDate() + 1);

return entity.attributes.data
  .filter(entry => new Date(entry.start) >= tomorrow)
  .map(entry => [new Date(entry.start).getTime(), entry.price]);

              color_threshold:
                -
                  value: -10
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.home_total_energy_hourly
              name: Energy (kWh)
              color: skyblue
              type: line
              opacity: 1
              yaxis_id: energy
              stroke_width: 2
              float_precision: 1
              extend_to: False
              unit: kWh
              group_by:
                duration: 1hour
                func: max
              show:
                legend_value: False
                datalabels: False
                extremas: True
                in_header: raw
                header_color_threshold: True
        visibility:
          -
            condition: state
            entity: sensor.electricity_tomorrow_valid
            state: True
  -
    type: grid
    cards:
      -
        type: heading
        heading: Energy Usage
        heading_style: subtitle
      -
        type: custom:apexcharts-card
        graph_span: 7d
        update_interval: 15min
        apex_config:
          fill:
            opacity: 0.5
          markers:
            size: 3
          xaxis:
            showDuplicates: True
            position: bottom
            labels:
              format: ddd
              hideOverlappingLabels: False
          chart:
            height: 180px
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          legend:
            show: True
            itemMargin:
              vertical: 10
              horizontal: 10
          dataLabels:
            enabled: True
            position: top
            offsetY: -8
            background:
              enabled: False
          tooltip:
            style:
              fontSize: 14px
          stroke:
            dashArray: 0
          title:
            text: Energy Daily
            align: center
            offsetY: 10
            style:
              fontSize: 13px
              fontFamily: Verdana
              fontWeight: normal
        header:
          show: False
        yaxis:
          -
            id: cost
            max: ~100
            min: 0
            decimals: 0
            apex_config:
              tickAmount: 4
              labels:
                show: True
          -
            id: power
            opposite: True
            max: ~35
            min: 0
            decimals: 0
            apex_config:
              tickAmount: 7
              labels:
                show: True
              title:
                text: kWh
                rotate: 0
                offsetX: -25
                offsetY: -70
                style:
                  fontSize: 10px
                  fontFamily: verdana
                  color: orange
        series:
          -
            entity: sensor.home_total_energy_daily
            name: Energy (kWh)
            color: skyblue
            type: column
            yaxis_id: power
            stroke_width: 1
            float_precision: 1
            unit: kWh
            statistics:
              type: state
            group_by:
              duration: 1day
              func: max
            show:
              legend_value: False
              datalabels: True
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:config-template-card
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
                stroke:
                  dashArray: 4
                chart:
                  height: 180px
                  width: 115%
                  offsetX: -30
                title:
                  text: Energy Price Today
                  align: center
                  offsetY: 10
                  style:
                    fontSize: 13px
                    fontFamily: Verdana
                    fontWeight: normal
                grid:
                  show: True
                  borderColor: rgba(255,255,255,0.2)
                xaxis:
                  position: bottom
                  labels:
                    format: H
                    hideOverlappingLabels: True
                    offsetX: 0
                  axisTicks:
                    offsetX: 0
                legend:
                  show: False
                  itemMargin:
                    vertical: 10
                    horizontal: 10
                tooltip:
                  enabled: True
                  style:
                    fontSize: 14px
              show:
                last_updated: True
              experimental:
                color_threshold: True
              header:
                show_states: True
                colorize_states: True
              now:
                show: True
              yaxis:
                -
                  id: cost
                  opposite: True
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
                    title:
                      text: c/kWh
                      rotate: 0
                      offsetX: -25
                      offsetY: -70
                      style:
                        fontSize: 10px
                        fontFamily: verdana
                        color: orange
                -
                  id: energy
                  max: ~2
                  min: 0
                  decimals: 1
                  apex_config:
                    tickAmount: 4
                    labels:
                      show: True
                    title:
                      text: kWh
                      rotate: 0
                      offsetX: 25
                      offsetY: -70
                      style:
                        color: skyblue
                        fontSize: 10px
                        fontFamily: verdana
              series:
                -
                  entity: sensor.electricity_prices
                  name: Price
                  yaxis_id: cost
                  type: column
                  opacity: 0.8
                  stroke_width: 0
                  show:
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
                  data_generator: return entity.attributes.data.map(entry => {
  return [new Date(entry.start).getTime(), entry.price];
});

                  color_threshold:
                    -
                      value: -10
                      color: lightgreen
                    -
                      value: ${PRICELOW * 1}
                      color: orange
                    -
                      value: ${PRICEHIGH * 1}
                      color: darkred
                -
                  entity: sensor.home_total_energy_hourly
                  name: Energy (kWh)
                  color: skyblue
                  type: line
                  opacity: 1
                  yaxis_id: energy
                  stroke_width: 2
                  float_precision: 1
                  extend_to: False
                  unit: kWh
                  group_by:
                    duration: 1hour
                    func: max
                  show:
                    legend_value: False
                    datalabels: False
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
      -
        type: custom:config-template-card
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
              height: 180px
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
              show: True
              borderColor: rgba(255,255,255,0.2)
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
            legend:
              show: False
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              shared: False
              enabled: True
              followCursor: False
              style:
                fontSize: 11px
              x:
                show: False
          show:
            last_updated: True
          experimental:
            color_threshold: True
          header:
            show_states: True
            colorize_states: True
          now:
            show: True
          yaxis:
            -
              id: cost
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: 0
                  offsetX: -25
                  offsetY: -70
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~2
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: kWh
                  rotate: 0
                  offsetX: 25
                  offsetY: -70
                  style:
                    color: skyblue
                    fontSize: 10px
                    fontFamily: verdana
          series:
            -
              entity: sensor.electricity_prices
              name: Price
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                extremas: True
                in_header: raw
                header_color_threshold: True
              data_generator: const tomorrow = new Date();
tomorrow.setHours(0, 0, 0, 0);
tomorrow.setDate(tomorrow.getDate() + 1);

return entity.attributes.data
  .filter(entry => new Date(entry.start) >= tomorrow)
  .map(entry => [new Date(entry.start).getTime(), entry.price]);

              color_threshold:
                -
                  value: -10
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.home_total_energy_hourly
              name: Energy (kWh)
              color: skyblue
              type: line
              opacity: 1
              yaxis_id: energy
              stroke_width: 2
              float_precision: 1
              extend_to: False
              unit: kWh
              group_by:
                duration: 1hour
                func: max
              show:
                legend_value: False
                datalabels: False
                extremas: True
                in_header: raw
                header_color_threshold: True
      -
        type: custom:apexcharts-card
        graph_span: 1d
        span:
          start: day
        header:
          show: False
          show_states: True
          colorize_states: True
        apex_config:
          stroke:
            dashArray: 0
          chart:
            height: 200px
            width: 115%
            offsetX: -30
          title:
            text: Energy Price Today
            align: center
            offsetY: 10
            style:
              fontSize: 13px
              fontFamily: Verdana
              fontWeight: normal
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          xaxis:
            position: bottom
            labels:
              format: HH
            hideOverlappingLabels: True
          tooltip:
            enabled: False
            style:
              fontSize: 14px
        now:
          show: True
        experimental:
          color_threshold: True
        yaxis:
          -
            id: price
            opposite: True
            decimals: 1
            apex_config:
              tickAmount: 4
              labels:
                show: True
              title:
                text: c/kWh
                rotate: 0
                offsetX: -25
                offsetY: -70
                style:
                  fontSize: 10px
                  fontFamily: verdana
                  color: orange
          -
            id: energy
            max: ~1
            min: 0
            decimals: 1
            apex_config:
              tickAmount: 4
              labels:
                show: True
              title:
                text: kWh
                rotate: 0
                offsetX: 25
                offsetY: -70
                style:
                  color: skyblue
                  fontSize: 10px
                  fontFamily: verdana
        series:
          -
            entity: sensor.electricity_prices
            name: Price
            yaxis_id: price
            type: column
            opacity: 0.6
            show:
              extremas: True
              in_header: raw
              header_color_threshold: True
            data_generator: if (!entity.attributes.data) return [];
const today = new Date();
today.setHours(0, 0, 0, 0);
const tomorrow = new Date(today);
tomorrow.setDate(today.getDate() + 1);

return entity.attributes.data
  .filter(entry => {
    const start = new Date(entry.start);
    return start >= today && start < tomorrow;
  })
  .map(entry => [new Date(entry.start).getTime(), entry.price]);

            color_threshold:
              -
                value: -10
                color: lightgreen
              -
                value: 15
                color: orange
              -
                value: 20
                color: red
          -
            entity: sensor.home_total_energy
            name: Energy
            yaxis_id: energy
            type: line
            group_by:
              duration: 15min
              func: diff
            color: skyblue
            opacity: 1
            stroke_width: 2
            show:
              extremas: True
              in_header: raw
              header_color_threshold: True
      -
        type: custom:apexcharts-card
        header:
          title: Shelly 3M - Energy Usage Today
        graph_span: 1d
        span:
          start: day
        update_interval: 5min
        apex_config:
          title:
            text: Energy Usage Today
            align: center
            offsetY: 10
            style:
              fontSize: 13px
              fontFamily: Verdana
              fontWeight: normal
          chart:
            height: 180px
          stroke:
            dashArray: 4
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          xaxis:
            position: bottom
            labels:
              format: HH
          tooltip:
            enabled: False
            style:
              fontSize: 14px
        yaxis:
          -
            decimals: 2
            min: 0
        series:
          -
            entity: sensor.home_total_3em_energy
            name: Energy Usage
            type: column
            group_by:
              duration: 15min
              func: diff
            color: skyblue
            opacity: 0.8
            stroke_width: 0
            show:
              extremas: True
              in_header: raw
              header_color_threshold: True
      -
        type: custom:apexcharts-card
        graph_span: 1d
        span:
          start: day
        header:
          show: False
          show_states: True
          colorize_states: True
        apex_config:
          stroke:
            dashArray: 2
          chart:
            height: 200px
            width: 115%
            offsetX: -30
          title:
            text: Energy Price Today
            align: center
            offsetY: 10
            style:
              fontSize: 13px
              fontFamily: Verdana
              fontWeight: normal
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          xaxis:
            position: bottom
            labels:
              format: HH
            hideOverlappingLabels: True
          tooltip:
            enabled: False
            style:
              fontSize: 14px
        now:
          show: True
        experimental:
          color_threshold: True
        yaxis:
          -
            id: price
            opposite: True
            decimals: 1
            apex_config:
              tickAmount: 4
              labels:
                show: True
              title:
                text: c/kWh
                rotate: 0
                offsetX: -25
                offsetY: -70
                style:
                  fontSize: 10px
                  fontFamily: verdana
                  color: orange
          -
            id: energy
            max: ~1
            min: 0
            decimals: 1
            apex_config:
              tickAmount: 4
              labels:
                show: True
              title:
                text: kWh
                rotate: 0
                offsetX: 25
                offsetY: -70
                style:
                  color: skyblue
                  fontSize: 10px
                  fontFamily: verdana
        series:
          -
            entity: sensor.electricity_prices
            name: Price
            yaxis_id: price
            type: line
            opacity: 0.8
            stroke_width: 2
            show:
              extremas: True
              in_header: raw
              header_color_threshold: True
            data_generator: if (!entity.attributes.data) return [];
const today = new Date();
today.setHours(0, 0, 0, 0);
const tomorrow = new Date(today);
tomorrow.setDate(today.getDate() + 1);

return entity.attributes.data
  .filter(entry => {
    const start = new Date(entry.start);
    return start >= today && start < tomorrow;
  })
  .map(entry => [new Date(entry.start).getTime(), entry.price]);

            color_threshold:
              -
                value: 10
                color: lightgreen
              -
                value: 17
                color: orange
              -
                value: 25
                color: red
          -
            entity: sensor.home_total_energy
            name: Energy
            yaxis_id: energy
            type: column
            group_by:
              duration: 15min
              func: diff
            color_threshold:
              -
                value: 0.25
                color: skyblue
              -
                value: 1
                color: lightblue
            opacity: 0.5
            stroke_width: 0
            show:
              extremas: True
              in_header: raw
              header_color_threshold: True
      -
        type: custom:apexcharts-card
        graph_span: 24h
        span:
          start: day
        header:
          title: 15-Minute Energy Cost
          show: True
        apex_config:
          stroke:
            dashArray: 2
          chart:
            height: 200px
          title:
            text: Energy Expenses
            align: center
            offsetY: 10
            style:
              fontSize: 13px
              fontFamily: Verdana
              fontWeight: normal
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
          xaxis:
            position: bottom
            labels:
              format: HH
            hideOverlappingLabels: True
          tooltip:
            enabled: False
            style:
              fontSize: 14px
        yaxis:
          -
            id: cost
            opposite: True
            decimals: 3
            max: 1
            min: 0
            apex_config:
              tickAmount: 4
              labels:
                show: True
              title:
                text: â‚¬
                rotate: 0
                offsetX: -30
                offsetY: -90
                style:
                  fontSize: 14px
                  fontFamily: verdana
                  color: orange
        series:
          -
            entity: sensor.15_minute_energy_cost_block
            name: Cost
            type: column
            group_by:
              duration: 15min
              func: max
            yaxis_id: cost
            show:
              extremas: True
              in_header: raw
  -
    type: grid
    cards:
      -
        type: heading
        heading_style: subtitle
        heading: Settings
      -
        type: custom:mushroom-entity-card
        entity: input_number.electricity_high_price_threshold
        grid_options:
          columns: 12
          rows: 1
      -
        type: markdown
        content: Price Threshold controls devices and appliances that have high impact on energy usage. These devices will be turned off or can't be used when the Electoricity price is above this treshold.
      -
        type: entities
        entities:
          -
            entity: input_number.energy_tax_c_kwh
          -
            entity: input_number.energy_transfer_fee
          -
            entity: input_number.energy_vat
          -
            entity: input_number.energy_transfer_base_fee
          -
            entity: input_number.energy_monthly_base_fee
      -
        type: custom:apexcharts-card
        graph_span: 24h
        update_interval: 5min
        header:
          title: Energy & Cost per 15min
          show: True
        apex_config:
          stroke:
            dashArray: 2
          chart:
            height: 200
          tooltip:
            shared: True
          grid:
            show: True
            borderColor: rgba(255,255,255,0.2)
        yaxis:
          -
            id: energy
            show: True
            opposite: False
            decimals: 2
          -
            id: cost
            show: True
            opposite: True
            decimals: 2
        series:
          -
            entity: sensor.shelly_home_energy_15min
            name: Energy
            type: column
            opacity: 0.8
            yaxis_id: energy
            unit: kWh
            group_by:
              duration: 15min
              func: max
            color: #1E90FF
          -
            entity: sensor.energy_cost_15min_c
            name: Cost
            type: line
            stroke_width: 2
            yaxis_id: cost
            unit: c
            group_by:
              duration: 15min
              func: max
            color: #FF6347

` 
### View: Electricity Dev

Path: $(@{type=panel; path=electricity-dev; title=Electricity Dev; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_electricity-dev.png)

`yaml
type: panel
path: electricity-dev
title: Electricity Dev
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:config-template-card
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
            stroke:
              dashArray: 4
            chart:
              height: 250%
              width: 100%
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
              show: True
              borderColor: rgba(255,255,255,0.2)
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
              all_series_config:
                show:
                  offset_in_name: True
            legend:
              show: True
              position: bottom
              horizontalAlign: left
              fontSize: 14px
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              enabled: True
              style:
                fontSize: 14px
          header:
            title: Electricity Today
            standard_format: False
            show: False
            show_states: True
            colorize_states: True
          show:
            last_updated: True
          experimental:
            color_threshold: True
          now:
            show: True
          yaxis:
            -
              id: cost
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: -90
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~2
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: kWh
                  rotate: -90
                  style:
                    color: skyblue
                    fontSize: 10px
                    fontFamily: verdana
          series:
            -
              entity: sensor.electricity_prices
              name: Price (snt/kWh)
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                legend_value: False
                extremas: True
                in_header: True
                header_color_threshold: True
              data_generator: return entity.attributes.data.map(entry => {
  return [new Date(entry.start).getTime(), entry.price];
});

              color_threshold:
                -
                  value: -10
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.electricity_daily_average_cents
              name: Avg Price
              yaxis_id: cost
              type: line
              color: yellow
              stroke_width: 1
              opacity: 0.8
              group_by:
                func: last
                duration: 24h
              show:
                legend_value: False
                datalabels: False
                extremas: True
                in_header: True
            -
              entity: sensor.home_total_energy_hourly
              name: Energy (kWh)
              color: skyblue
              type: line
              opacity: 1
              yaxis_id: energy
              stroke_width: 2
              float_precision: 1
              unit: kWh
              group_by:
                duration: 1h
                func: delta
              show:
                legend_value: False
                datalabels: False
                extremas: True
                in_header: raw
                header_color_threshold: True
      -
        type: horizontal-stack
        cards:
          -
            type: custom:apexcharts-card
            graph_span: 7d
            update_interval: 15min
            apex_config:
              fill:
                opacity: 0.5
              markers:
                size: 3
              xaxis:
                showDuplicates: True
                position: bottom
                labels:
                  format: ddd
                  hideOverlappingLabels: False
              chart:
                height: 200vh
              grid:
                show: True
                borderColor: rgba(255,255,255,0.2)
              legend:
                show: True
                itemMargin:
                  vertical: 10
                  horizontal: 10
              dataLabels:
                enabled: True
                position: top
                offsetY: -9
                background:
                  enabled: False
              tooltip:
                style:
                  fontSize: 14px
              stroke:
                dashArray: 0
              title:
                text: Energy Daily
                align: center
                offsetY: 8
                style:
                  fontSize: 13px
                  fontFamily: Verdana
                  fontWeight: normal
            header:
              show: False
            yaxis:
              -
                id: cost
                max: ~100
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 4
                  labels:
                    show: True
              -
                id: power
                opposite: True
                max: ~35
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 7
                  labels:
                    show: True
                  title:
                    text: kWh
                    rotate: 0
                    offsetX: 0
                    offsetY: 0
                    style:
                      fontSize: 10px
                      fontFamily: verdana
                      color: orange
            series:
              -
                entity: sensor.home_total_energy_daily
                name: Energy (kWh)
                color: skyblue
                type: column
                yaxis_id: power
                stroke_width: 0
                float_precision: 1
                unit: kWh
                statistics:
                  type: state
                group_by:
                  duration: 1day
                  func: max
                show:
                  legend_value: False
                  datalabels: True
          -
            type: custom:apexcharts-card
            header:
              title: Shelly 3M - Energy Usage Today
            graph_span: 1d
            span:
              start: day
            update_interval: 5min
            apex_config:
              title:
                text: Energy Usage Today
                align: center
                offsetY: 10
                style:
                  fontSize: 13px
                  fontFamily: Verdana
                  fontWeight: normal
              stroke:
                dashArray: 4
              chart:
                height: 200vh
              grid:
                show: True
                borderColor: rgba(255,255,255,0.2)
              xaxis:
                position: bottom
                labels:
                  format: HH
              tooltip:
                enabled: False
                style:
                  fontSize: 14px
            yaxis:
              -
                decimals: 2
                min: 0
            series:
              -
                entity: sensor.home_total_3em_energy
                name: Energy Usage
                type: column
                group_by:
                  duration: 15min
                  func: diff
                color: skyblue
                opacity: 0.8
                stroke_width: 0
                show:
                  extremas: True
                  in_header: raw
                  header_color_threshold: True

` 

## XDEV

**ID**: $Id | **URL**: /dashboard-dev | **File**: $F`n
### View: Floor Plan

**Card Types**: picture-elements

![View Screenshot](assets/images/view_.png)

`yaml
theme: Backend-selected
title: Floor Plan
type: custom:horizontal-layout
badges:
cards:
  -
    type: picture-elements
    title: 2nd Floor
    elements:
      -
        type: custom:mushroom-chips-card
        chips:
          -
            type: entity
            entity: sensor.anton_temperature
            use_entity_picture: False
        style:
          top: 6%
          left: 61%
      -
        type: custom:mushroom-chips-card
        chips:
          -
            type: entity
            entity: sensor.anton_co2
            use_entity_picture: False
        style:
          top: 13%
          left: 61.6%
    image: local/floorplan/HA_floorplan_2nd_floor.png
  -
    type: picture-elements
    title: 1st Floor
    elements:
      -
        type: state-badge
        entity: binary_sensor.node_red_running
        style:
          top: 32%
          left: 40%
    image: local/floorplan/HA_floorplan_1st_floor_only.png
  -
    type: picture-elements
    title: Backyard
    elements:
      -
        type: custom:mushroom-chips-card
        chips:
          -
            type: entity
            entity: sensor.backyard_humidity
            use_entity_picture: False
        style:
          top: 6%
          left: 15%
      -
        type: custom:mushroom-chips-card
        chips:
          -
            type: entity
            entity: sensor.backyard_temperature
            use_entity_picture: False
        style:
          top: 13%
          left: 15%
    image: local/floorplan/HA_floorplan_backyard.png

` 
### View: Rooms

Path: $(@{title=Rooms; path=rooms; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: grid, picture-elements, custom:hourly-weather, custom:mushroom-entity-card

![View Screenshot](assets/images/view_rooms.png)

`yaml
title: Rooms
path: rooms
badges:
cards:
  -
    square: False
    type: grid
    cards:
      -
        type: area
        area: alisa
        navigation_path: /lovelace/alisa
      -
        camera_view: auto
        type: picture-glance
        title: Kitchen
        image: https://demo.home-assistant.io/stub_config/kitchen.png
        entities:
        entity: light.kitchen_lights
      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Mercedes-Benz-GLC-BG.png
        state_filter:
          home: brightness(100%)
          away: brightness(25%)
        elements:
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-small3.png
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            style:
              name: GLC
              left: 50%
              top: 50%
              width: 100%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                entity: sensor.xpb_358_charging_power
                image: local/car/charging_cable_only.png
                style:
                  name: Charging Cable
                  left: 35px
                  top: 52%
                  width: 30%
                  animation: {% set value = states(entity) | float %} 
{% if value < 10 %}
pulse 1s ease infinite
{% endif %}

                filter: brightness(80%)
              -
                type: state-label
                entity: sensor.xpb_358_charging_power
                style:
                  name: Charging Power
                  top: 10%
                  left: 45%
                  color: orange
                  font-size: 70%
                  font-weight: bold
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-green.png
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-persons/car
                style:
                  left: 50%
                  top: 50%
                  width: 100%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: custom:bar-card
            entities:
              -
                entity: sensor.xpb_358_state_of_charge
            entity_row: True
            direction: up
            stack: horizontal
            height: 40px
            animation:
              state: on
              speed: 1
            severity:
              -
                color: Red
                from: 0
                to: 25
              -
                color: Orange
                from: 26
                to: 50
              -
                color: #21ff21
                from: 51
                to: 100
            positions:
              icon: off
              indicator: off
              title: off
              name: off
              value: off
              minmax: off
            style:
              name: Battery Status
              top: 48%
              left: 25px
              width: 15px
              --ha-card-border-width: 0px
          -
            type: image
            image: local/car/charging_station_blocks.png
            style:
              name: Charging Station
              left: 40px
              top: 50%
              width: 90px
            filter: brightness(80%)
          -
            type: state-label
            entity: sensor.xpb_358_state_of_charge
            style:
              name: Battery Status
              top: 14%
              left: 26px
              color: #21ff21
              font-size: 80%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_range_electric
            style:
              name: Range Electric
              top: 86%
              left: 26px
              color: orange
              font-size: 70%
              font-weight: bold
          -
            type: custom:bar-card
            entities:
              -
                entity: sensor.xpb_358_fuel_level
            entity_row: True
            direction: up
            stack: horizontal
            height: 40px
            animation:
              state: on
              speed: 1
            color: #ad6e00
            positions:
              icon: off
              indicator: off
              title: off
              name: off
              value: off
              minmax: off
            style:
              name: Fuel Status
              top: 48%
              right: 15px
              width: 15px
              --ha-card-border-width: 0px
          -
            type: image
            image: local/car/charging_station_blocks.png
            style:
              name: GAS Station
              right: -75px
              top: 50%
              width: 90px
            filter: brightness(80%)
          -
            type: state-label
            entity: sensor.xpb_358_range_liquid
            style:
              name: Range
              top: 86%
              right: -22px
              color: orange
              font-size: 70%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_fuel_level
            style:
              name: Fuel Level
              top: 14%
              right: -12px
              color: #21ff21
              font-size: 80%
              font-weight: bold
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}

      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Mercedes-Benz-GLC-BG.png
        state_filter:
          home: brightness(100%)
          away: brightness(25%)
        elements:
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-small3.png
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            style:
              name: GLC
              left: 50%
              top: 50%
              width: 100%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-green.png
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-persons/car
                style:
                  left: 50%
                  top: 50%
                  width: 100%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: state-label
            entity: sensor.xpb_358_range_liquid
            style:
              name: Range
              top: 86%
              right: -5px
              color: orange
              font-size: 70%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_fuel_level
            style:
              name: Fuel Level
              top: 14%
              right: 5px
              color: #21ff21
              font-size: 80%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_state_of_charge
            style:
              name: Battery Status
              top: 14%
              left: 40px
              color: #21ff21
              font-size: 80%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_range_electric
            style:
              name: Range Electric
              top: 86%
              left: 38px
              color: orange
              font-size: 70%
              font-weight: bold
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}

    columns: 2
  -
    type: picture-elements
    entity: device_tracker.xpb_358_device_tracker
    image: local/car/Mercedes-Benz-GLC-BG.png
    state_filter:
      home: brightness(100%)
      away: brightness(25%)
    elements:
      -
        type: state-label
        entity: sensor.xpb_358_range_liquid
        style:
          name: Range
          top: 86%
          right: -5px
          color: orange
          font-size: 70%
          font-weight: bold
      -
        type: state-label
        entity: sensor.xpb_358_fuel_level
        style:
          name: Fuel Level
          top: 14%
          right: 5px
          color: #21ff21
          font-size: 80%
          font-weight: bold
      -
        type: image
        image: local/car/Mercedes-Benz-GLC-small3.png
        tap_action:
          action: navigate
          navigation_path: /dashboard-persons/car
        style:
          name: GLC
          left: 50%
          top: 50%
          width: 100%
      -
        type: conditional
        conditions:
          -
            entity: sensor.car_charge_plug
            state: on
        elements:
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-green.png
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            style:
              left: 50%
              top: 50%
              width: 100%
              animation: blink 1s ease infinite
              opacity: 100%
      -
        type: state-label
        entity: sensor.xpb_358_state_of_charge
        style:
          name: Battery Status
          top: 14%
          left: 40px
          color: #21ff21
          font-size: 80%
          font-weight: bold
      -
        type: state-label
        entity: sensor.xpb_358_range_electric
        style:
          name: Range Electric
          top: 86%
          left: 38px
          color: orange
          font-size: 70%
          font-weight: bold
    card_mod:
      style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}

  -
    type: custom:hourly-weather
    entity: weather.openweathermap
  -
    type: custom:mushroom-entity-card
    entity: person.evishomelab
    tap_action:
      action: navigate
      navigation_path: test/#test
    hold_action:
      action: none
    double_tap_action:
      action: none

` 
### View: test

Path: $(@{title=test; path=test; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_test.png)

`yaml
title: test
path: test
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:bubble-card
        card_type: pop-up
        hash: #test
        icon: mdi:car
      -
        show_name: True
        show_icon: True
        type: button
        tap_action:
          action: toggle
        entity: light.lobby_light
      -
        type: entities
        entities:
          - sensor.nordpool_current_price
          - sensor.car_charge_plug
          - sensor.car_charging

` 
### View: declutter

Path: $(@{title=declutter; path=declutter; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: grid, custom:mushroom-entity-card

![View Screenshot](assets/images/view_declutter.png)

`yaml
title: declutter
path: declutter
badges:
cards:
  -
    square: False
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: area_card
        variables:
          -
            entity_name: office
          -
            display_name: OFFICE
          -
            temperature_sensor: sensor.bedroom_temperature
          -
            double_tap_entity: light.bedroom_bed_light
          -
            sensor_1: sensor.bedroom_temperature
          -
            sensor_1_state: 25
          -
            sensor_1_logic: >
          -
            sensor_1_icon: mdi:fridge
          -
            sensor_1_color: red
          -
            sensor_1_animation: blink
          -
            sensor_2: sensor.anton_co2
          -
            sensor_2_state: 1000
          -
            sensor_2_logic: >
          -
            sensor_2_icon: mdi:molecule-co2
          -
            sensor_2_color: blue
          -
            sensor_2_animation: blink
          -
            sensor_3: sensor.bedroom_temperature
          -
            sensor_3_state: 24
          -
            sensor_3_logic: >
          -
            sensor_3_icon: mdi:temperature-celsius
          -
            sensor_3_color: green
          -
            sensor_3_animation: none
          -
            sensor_4: sensor.bedroom_temperature
          -
            sensor_4_state: 24
          -
            sensor_4_logic: >
          -
            sensor_4_icon: mdi:water-alert
          -
            sensor_4_color: orange
          -
            sensor_4_animation: blink
          -
            device_1: switch.office_pc_power
          -
            device_1_color: green
          -
            device_1_icon: mdi:desktop-classic
          -
            device_1_state: on
          -
            device_1_animation: none
          -
            device_2: switch.office_pc_power
          -
            device_2_icon: mdi:server
          -
            device_2_state: on
          -
            device_2_animation: none
          -
            device_3: switch.office_pc_power
          -
            device_3_icon: mdi:nas
          -
            device_3_state: on
          -
            device_3_animation: blink
          -
            device_4: switch.office_pc_power
          -
            device_4_color: blue
          -
            device_4_icon: mdi:speaker
          -
            device_4_state: on
          -
            device_4_animation: blink
          -
            device_5: switch.office_pc_power
          -
            device_5_color: blue
          -
            device_5_icon: mdi:speaker
          -
            device_5_state: on
          -
            device_5_animation: none
          -
            device_6: switch.office_pc_power
          -
            device_6_color: orange
          -
            device_6_icon: mdi:printer-3d
          -
            device_6_state: on
          -
            device_6_animation: none
      -
        square: False
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: office
              -
                display_name: OFFICE
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                sensor_1: sensor.bedroom_temperature
              -
                sensor_1_state: 24
              -
                sensor_1_logic: >
              -
                sensor_1_icon: mdi:fridge
              -
                sensor_1_color: red
              -
                sensor_1_animation: blink
              -
                sensor_2: sensor.bedroom_temperature
              -
                sensor_2_state: 24
              -
                sensor_2_logic: >
              -
                sensor_2_icon: mdi:water-alert
              -
                sensor_2_color: blue
              -
                sensor_2_animation: blink
              -
                sensor_3: sensor.bedroom_temperature
              -
                sensor_3_state: 24
              -
                sensor_3_logic: >
              -
                sensor_3_icon: mdi:water-alert
              -
                sensor_3_color: none
              -
                sensor_3_animation: none
              -
                sensor_4: sensor.bedroom_temperature
              -
                sensor_4_state: 24
              -
                sensor_4_logic: >
              -
                sensor_4_icon: mdi:water-alert
              -
                sensor_4_color: none
              -
                sensor_4_animation: none
              -
                device_1: switch.office_pc_power
              -
                device_1_color: green
              -
                device_1_icon: mdi:desktop-classic
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: switch.office_pc_power
              -
                device_2_icon: mdi:server
              -
                device_2_state: on
              -
                device_2_animation: none
              -
                device_3: switch.office_pc_power
              -
                device_3_icon: mdi:nas
              -
                device_3_state: on
              -
                device_4: switch.office_pc_power
              -
                device_4_color: blue
              -
                device_4_icon: mdi:speaker
              -
                device_4_state: on
              -
                device_4_animation: none
              -
                device_5: switch.office_pc_power
              -
                device_5_color: blue
              -
                device_5_icon: mdi:speaker
              -
                device_5_state: on
              -
                device_5_animation: none
              -
                device_6: switch.office_pc_power
              -
                device_6_color: orange
              -
                device_6_icon: mdi:printer-3d
              -
                device_6_state: on
              -
                device_6_animation: none
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: sauna
              -
                display_name: SAUNA
              -
                co2_sensor: sensor.bedroom_co2
              -
                humidity_sensor: sensor.bedroom_humidity
              -
                device_1: switch.office_pc_power
              -
                icon_1: mdi:desktop-classic
              -
                state_1: on
              -
                animation_1: none
              -
                device_2: switch.unraid_power_toggle
              -
                icon_2: mdi:server
              -
                state_2: on
              -
                device_3: switch.td_ds1_2
              -
                icon_3: mdi:nas
              -
                state_3: on
              -
                device_4: media_player.bedroom_echo
              -
                icon_4: mdi:speaker
              -
                state_4: playing
              -
                animation_4: blink
              -
                device_5: media_player.bedroom_display_2
              -
                icon_5: mdi:speaker
              -
                state_5: playing
              -
                animation_5: blink
              -
                device_6: sensor.ender_5_pro_current_state
              -
                icon_6: mdi:printer-3d
              -
                state_6: Printing
              -
                animation_6: blink
        columns: 2
      -
        square: True
        type: grid
        cards:
          -
            type: vertical-stack
            cards:
              -
                type: custom:bubble-card
                card_type: pop-up
                hash: #office
                icon: mdi:floor-plan
                width_desktop: 540px
              -
                type: custom:decluttering-card
                template: area_card
                variables:
                  -
                    entity_name: office
                  -
                    display_name: OFFICE
                  -
                    temperature_sensor: sensor.bedroom_temperature
                  -
                    co2_sensor: sensor.bedroom_co2
                  -
                    humidity_sensor: sensor.bedroom_humidity
                  -
                    device_1: switch.office_pc_power
                  -
                    icon_1: mdi:desktop-classic
                  -
                    state_1: on
                  -
                    animation_1: none
                  -
                    device_2: switch.unraid_power_toggle
                  -
                    icon_2: mdi:server
                  -
                    state_2: on
                  -
                    device_3: switch.td_ds1_2
                  -
                    icon_3: mdi:nas
                  -
                    state_3: on
                  -
                    device_4: media_player.bedroom_echo
                  -
                    icon_4: mdi:speaker
                  -
                    state_4: playing
                  -
                    animation_4: blink
                  -
                    device_5: media_player.bedroom_display_2
                  -
                    icon_5: mdi:speaker
                  -
                    state_5: playing
                  -
                    animation_5: blink
                  -
                    device_6: sensor.ender_5_pro_current_state
                  -
                    icon_6: mdi:printer-3d
                  -
                    state_6: Printing
                  -
                    animation_6: blink
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-entity-card
                    entity: switch.office_pc_power
                    layout: vertical
                    fill_container: True
                    icon_color: green
                    tap_action:
                      action: none
                    hold_action:
                      action: toggle
                    name: PC
                    icon: mdi:desktop-classic
                  -
                    type: custom:mushroom-template-card
                    primary: Displays
                    fill_container: True
                    secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  On
{% else %}
 Off
{% endif %}
                    icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:monitor
{% else %}
  mdi:monitor-off
{% endif %}
                    layout: vertical
                    entity: switch.officepc_displays
                    tap_action:
                      action: toggle
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  red
{% endif %}
                  -
                    type: custom:mushroom-template-card
                    primary: Output
                    fill_container: True
                    secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  Speakers
{% else %}
  Headset
{% endif %}
                    icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:speaker-multiple
{% else %}
  mdi:headphones
{% endif %}
                    layout: vertical
                    entity: switch.officepc_audio_device
                    tap_action:
                      action: toggle
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  orange
{% endif %}
                  -
                    type: custom:mushroom-entity-card
                    entity: button.officepc_mediaplaypause
                    name: Media
                    icon: mdi:play-pause
                    icon_color: blue
                    layout: vertical
                    secondary_info: none
                    fill_container: True
                    tap_action:
                      action: call-service
                      service: button.press
                      target:
                        entity_id: button.officepc_mediaplaypause
                      data:
                  -
                    type: custom:mushroom-template-card
                    primary: Volume
                    fill_container: True
                    secondary: {% set status = states(entity) %}
{% if status == 'on' %}
  Muted
{% else %}
 Volume {{ states('sensor.officepc_audio_default_device_volume') }}
{% endif %}
                    icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:volume-mute
{% else %}
  mdi:volume-high
{% endif %}
                    layout: vertical
                    entity: switch.officepc_audio_mute
                    tap_action:
                      action: toggle
                    icon_color: {% set status = states(entity) %}
{% if status == 'on' %}
  red
{% else %}
  green
{% endif %}
                columns: 5
        columns: 2
    columns: 1
  -
    type: custom:mushroom-entity-card
    entity: person.evishomelab
    double_tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id: light.bedroom_bed_light

` 
### View: door

Path: $(@{title=door; path=f; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: entities

![View Screenshot](assets/images/view_f.png)

`yaml
title: door
path: f
badges:
cards:
  -
    type: entities
    entities:
      -
        entity: binary_sensor.front_door_lock_door
      -
        entity: lock.front_door_lock
    title: Ble
  -
    type: entities
    entities:
      - lock.front_door
      - binary_sensor.front_door_door
    title: Cloud

` 
### View: CAR

Path: $(@{title=CAR; path=car; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: custom:scheduler-card

![View Screenshot](assets/images/view_car.png)

`yaml
title: CAR
path: car
badges:
cards:
  -
    type: custom:scheduler-card
    include:
      - switch.car_pre_entry_ac
    exclude:
    title: Schedules
    discover_existing: False
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
    show_header_toggle: False

` 
### View: graphs

Path: $(@{title=graphs; path=graphs; badges=System.Object[]; cards=System.Object[]}.path)`n
![View Screenshot](assets/images/view_graphs.png)

`yaml
title: graphs
path: graphs
badges:
cards:

` 

## Persons

**ID**: $Id | **URL**: /dashboard-persons | **File**: $F`n
### View: Map All

Path: $(@{theme=Backend-selected; title=Map All; path=map-all; type=panel; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-all.png)

`yaml
theme: Backend-selected
title: Map All
path: map-all
type: panel
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.anton
      -
        entity: person.elias
      -
        entity: person.jukka
      -
        entity: person.piia
      -
        entity: person.alisa
      -
        entity: person.car
    hours_to_show: 2

` 
### View: Piia

Path: $(@{theme=Backend-selected; title=Piia; path=piia; badges=System.Object[]; cards=System.Object[]; type=sections; sections=System.Object[]; max_columns=4}.path)`n
![View Screenshot](assets/images/view_piia.png)

`yaml
theme: Backend-selected
title: Piia
path: piia
badges:
cards:
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: custom:decluttering-card
        template: family_member_card
        variables:
          -
            person: piia
          -
            device: SM_S721B_piia
          -
            background: background_3
          -
            color: #ddd
      -
        type: custom:auto-entities
        card:
          type: entities
          title: My Notification Settings
          show_header_toggle: False
          icon: mdi:bell-cog
        filter:
          template: {% set user_slug = 'piia' %} {# <--- CHANGE THIS to the person's slug #}
{% set ns = namespace(switches=[]) %}

{% for state in states.switch %}
  {# Find switches ending with _notification_[user_slug] #}
  {% if state.entity_id.endswith('_notification_' ~ user_slug) %}
    {# Extract category (e.g. switch.info_notification_jukka -> info) #}
    {% set category = state.object_id.split('_notification_')[0] | capitalize %}
    
    {% set ns.switches = ns.switches + [{
        'entity': state.entity_id,
        'name': category ~ " Notification", 
        'secondary_info': 'last-updated'
    }] %}
  {% endif %}
{% endfor %}

{{ ns.switches | to_json }}

        sort:
          method: name
max_columns: 4

` 
### View: Jukka

![View Screenshot](assets/images/view_.png)

`yaml
theme: Backend-selected
title: Jukka
badges:
cards:
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:decluttering-card
        template: family_member_card
        variables:
          -
            person: jukka
          -
            device: sm_f966b
          -
            background: background_2
          -
            color: #dddddd
      -
        type: custom:auto-entities
        card:
          type: entities
          title: My Notification Settings
          show_header_toggle: False
          icon: mdi:bell-cog
        filter:
          template: {% set user_slug = 'jukka' %} {# <--- CHANGE THIS to the person's slug #}
{% set ns = namespace(switches=[]) %}

{% for state in states.switch %}
  {# Find switches ending with _notification_[user_slug] #}
  {% if state.entity_id.endswith('_notification_' ~ user_slug) %}
    {# Extract category (e.g. switch.info_notification_jukka -> info) #}
    {% set category = state.object_id.split('_notification_')[0] | capitalize %}
    
    {% set ns.switches = ns.switches + [{
        'entity': state.entity_id,
        'name': category ~ " Notification", 
        'secondary_info': 'last-updated'
    }] %}
  {% endif %}
{% endfor %}

{{ ns.switches | to_json }}

        sort:
          method: name

` 
### View: Anton

Path: $(@{theme=Backend-selected; title=Anton; path=anton; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_anton.png)

`yaml
theme: Backend-selected
title: Anton
path: anton
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:decluttering-card
        template: family_member_card
        variables:
          -
            person: anton
          -
            device: sm_a426b_anton
          -
            background: background_3
          -
            color: #dddddd
      -
        type: custom:decluttering-card
        template: family_member_notifications
        variables:
          -
            person: anton

` 
### View: Alisa

Path: $(@{theme=Backend-selected; title=Alisa; path=alisa; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_alisa.png)

`yaml
theme: Backend-selected
title: Alisa
path: alisa
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:decluttering-card
        template: family_member_card
        variables:
          -
            person: alisa
          -
            device: alisa_mobile
          -
            background: background_3
          -
            color: #dddddd
      -
        type: custom:decluttering-card
        template: family_member_notifications
        variables:
          -
            person: elias

` 
### View: Elias

Path: $(@{theme=Backend-selected; title=Elias; path=elias; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_elias.png)

`yaml
theme: Backend-selected
title: Elias
path: elias
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:decluttering-card
        template: family_member_card
        variables:
          -
            person: elias
          -
            device: mobile_elias
          -
            background: background_3
          -
            color: #dddddd
      -
        type: custom:decluttering-card
        template: family_member_notifications
        variables:
          -
            person: elias

` 
### View: Map Jukka

Path: $(@{theme=Backend-selected; subview=True; title=Map Jukka; path=map-jukka; type=panel; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-jukka.png)

`yaml
theme: Backend-selected
subview: True
title: Map Jukka
path: map-jukka
type: panel
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.jukka
    dark_mode: False
    hours_to_show: 48

` 
### View: Map Piia

Path: $(@{theme=Backend-selected; title=Map Piia; path=map-piia; type=panel; subview=True; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-piia.png)

`yaml
theme: Backend-selected
title: Map Piia
path: map-piia
type: panel
subview: True
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.piia
    hours_to_show: 48
    dark_mode: False

` 
### View: Map Anton

Path: $(@{theme=Backend-selected; title=Map Anton; path=map-anton; type=panel; subview=True; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-anton.png)

`yaml
theme: Backend-selected
title: Map Anton
path: map-anton
type: panel
subview: True
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.anton
    hours_to_show: 48
    dark_mode: False

` 
### View: Map Elias

Path: $(@{theme=Backend-selected; title=Map Elias; path=map-elias; type=panel; subview=True; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-elias.png)

`yaml
theme: Backend-selected
title: Map Elias
path: map-elias
type: panel
subview: True
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.elias
    hours_to_show: 48

` 
### View: Map Alisa

Path: $(@{theme=Backend-selected; title=Map Alisa; path=map-alisa; type=panel; subview=True; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: map

![View Screenshot](assets/images/view_map-alisa.png)

`yaml
theme: Backend-selected
title: Map Alisa
path: map-alisa
type: panel
subview: True
badges:
cards:
  -
    type: map
    entities:
      -
        entity: person.alisa
    hours_to_show: 48

` 
### View: CAR

Path: $(@{title=CAR; badges=System.Object[]; cards=System.Object[]; type=sections; sections=System.Object[]; max_columns=4; path=car; subview=True}.path)`n
![View Screenshot](assets/images/view_car.png)

`yaml
title: CAR
badges:
cards:
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: picture-elements
        image: local/car/Car-BG.png
        elements:
          -
            type: custom:button-card
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
                      -
                        type: horizontal-stack
                        cards:
                          -
                            type: custom:mushroom-template-card
                            entity: sensor.fuel_level
                            primary: Fuel Level
                            secondary: {{ states('sensor.xpb_358_fuel_level') }}% | {{ states('sensor.xpb_358_range_liquid') }} km range
                            icon: mdi:gas-station
                            features_position: bottom
                            color: {% set fuel = states('sensor.xpb_358_fuel_level') | int %} {% if fuel < 20 %}
  darkred
{% elif fuel < 50 %}
  yellow
{% else %}
  darkgreen
{% endif %}

                            card_mod:
                              style: ha-card {
  background: linear-gradient(
    to right,
    orange {{ states('sensor.xpb_358_fuel_level') }}%,
    var(--card-background-color) {{ states('sensor.xpb_358_fuel_level') }}%
  );
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

                          -
                            type: custom:mushroom-template-card
                            entity: sensor.ev_battery_level
                            primary: EV Charge
                            secondary: {{ states('sensor.xpb_358_state_of_charge') }}% | {{ states('sensor.xpb_358_range_electric') }} km range

                            icon: mdi:car-electric
                            tap_action:
                              action: more-info
                            hold_action:
                              action: more-info
                            color: {% set charge = states('sensor.xpb_358_state_of_charge') | int %} {% if charge < 20 %}
  red
{% elif charge < 50 %}
  yellow
{% else %}
  lightgreen
{% endif %}

                            features_position: bottom
                            card_mod:
                              style: ha-card {
  --charge: {{ states('sensor.xpb_358_state_of_charge') }}%;
  background: linear-gradient(
    to right,
    green var(--charge),
    var(--card-background-color) var(--charge)
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

                      -
                        type: custom:scheduler-card
                        include:
                          - switch.xpb_358_pre_entry_climate_control
                        exclude:
                        discover_existing: False
                        title: True
                        show_header_toggle: False
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
                        customize:
                        tags:
                          - Car
                        exclude_tags:
                        card_mod:
                          style: ha-card {
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

                      -
                        type: map
                        entities:
                          -
                            entity: person.car
                        hours_to_show: 48
                        aspect_ratio: 1.5
                        default_zoom: 15
                        theme_mode: auto
            card_mod:
              style: ha-card {
  /* Moves border logic here from original for border display */
  {% if is_state('sensor.xpb_358_ignition_state','4') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('sensor.xpb_358_ignition_state','2') %}
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
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: home
            elements:
              -
                type: image
                image: local/car/GLC-home.png
                style:
                  left: 50%
                  top: 30%
                  width: 80%
                  opacity: 100%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: not_home
            elements:
              -
                type: image
                image: local/car/GLC-back.png
                style:
                  left: 50%
                  top: 50%
                  width: 65%
                  opacity: 100%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: binary_sensor.car_engine
                state: on
            elements:
              -
                type: image
                image: local/car/road.png
                style:
                  left: 50%
                  top: 65%
                  width: 100%
                  opacity: 100%
                  z-index: 2
          -
            type: custom:button-card
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
          -
            type: custom:button-card
            template: area_text_element
            entity: sensor.xpb_358_state_of_charge
            show_name: False
            show_icon: False
            show_state: True
            style:
              top: 0%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: #088CF8
                    -
                      animation: [[[
  if (states['binary_sensor.xpb_358_charging_active'].state == 'on') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: unlocked
                styles:
                  icon:
                    -
                      animation: blink 0.5s linear infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: locked
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 0.5s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: #088CF8
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: rgba(253,89,89,1)
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      animation: rotating 1s linear infinite
                      color: #21ff21
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
      -
        type: custom:mushroom-template-card
        entity: sensor.fuel_level
        primary: Fuel Level
        secondary: {{ states('sensor.xpb_358_fuel_level') }}% | {{ states('sensor.xpb_358_range_liquid') }} km range
        icon: mdi:gas-station
        features_position: bottom
        color: {% set fuel = states('sensor.xpb_358_fuel_level') | int %} {% if fuel < 20 %}
  darkred
{% elif fuel < 50 %}
  yellow
{% else %}
  darkgreen
{% endif %}

        card_mod:
          style: ha-card {
  background: linear-gradient(
    to right,
    orange {{ states('sensor.xpb_358_fuel_level') }}%,
    var(--card-background-color) {{ states('sensor.xpb_358_fuel_level') }}%
  );
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

      -
        type: custom:mushroom-template-card
        entity: sensor.ev_battery_level
        primary: EV Charge
        secondary: {{ states('sensor.xpb_358_state_of_charge') }}% | {{ states('sensor.xpb_358_range_electric') }} km range

        icon: mdi:car-electric
        tap_action:
          action: more-info
        hold_action:
          action: more-info
        color: {% set charge = states('sensor.xpb_358_state_of_charge') | int %} {% if charge < 20 %}
  red
{% elif charge < 50 %}
  yellow
{% else %}
  lightgreen
{% endif %}

        features_position: bottom
        card_mod:
          style: ha-card {
  --charge: {{ states('sensor.xpb_358_state_of_charge') }}%;
  background: linear-gradient(
    to right,
    green var(--charge),
    var(--card-background-color) var(--charge)
  );
  background-size: 100% 100%;
  background-repeat: no-repeat;
  border-radius: 12px;
}

      -
        type: custom:mushroom-template-card
        primary: Doors
        secondary: {% set status = states(entity) %}
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
        entity: sensor.car_doors
        badge_color: {% set status = states('switch.car_doors') %}
{% if status == 'off' %}
  red
{% else %}
  green
{% endif %}
        badge_icon: {% set status = states('switch.car_doors') %}
{% if status == 'off' %}
  mdi:lock-off-outline
{% else %}
  mdi:lock
{% endif %}
        color: {% set status = states(entity) %}
{% if status == 'open' %}
  red
{% else %}
  disabled
{% endif %}
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        vertical: True
      -
        type: custom:mushroom-template-card
        primary: Windows
        secondary: {% set status = states(entity) %}
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
        badge_icon: 
        badge_color: 
        hold_action:
          action: more-info
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  red
{% else %}
  disabled
{% endif %}
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        vertical: True
        icon_tap_action:
          action: more-info
      -
        type: custom:mushroom-template-card
        entity: switch.xpb_358_pre_entry_climate_control
        primary: Pre AC
        secondary: {% set status = states(entity) %}
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
        badge_icon: 
        badge_color: 
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  green
{% endif %}
        features_position: bottom
        grid_options:
          columns: 4
          rows: 2
        vertical: True
        icon_tap_action:
          action: more-info
      -
        include:
          - switch.xpb_358_pre_entry_climate_control
        exclude:
        discover_existing: False
        title: True
        show_header_toggle: False
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
        customize:
        tags:
          - Car
        exclude_tags:
        type: custom:scheduler-card
        card_mod:
          style: ha-card {
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

      -
        type: map
        entities:
          -
            entity: person.car
        hours_to_show: 48
        aspect_ratio: 1.5
        default_zoom: 15
        theme_mode: auto
  -
    type: grid
    cards:
      -
        type: picture-elements
        image: local/car/Car-BG.png
        aspect_ratio: 1:1
        elements:
          -
            type: custom:button-card
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
                      -
                        type: custom:scheduler-card
                        include:
                          - switch.car_pre_entry_ac
                        exclude:
                        title: Schedules
                        discover_existing: False
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
                        show_header_toggle: False
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 4
          -
            type: image
            image: local/car/GLC-top.png
            style:
              left: 50.5%
              top: 54%
              width: 140%
              opacity: 100%
              z-index: 2
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: >
                value: 0
                styles:
                  icon:
                    -
                      color: orange
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: 0
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: orange
                      animation: blink 1s ease infinite
              -
                operator: ==
                value: off
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: 2
                styles:
                  icon:
                    -
                      color: lightgreen
              -
                operator: !=
                value: 2
                icon: mdi:lock-open-variant
                styles:
                  icon:
                    -
                      color: orange
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_tire_pressure_front_right
            icon: mdi:tire
            show_state: True
            layout: vertical
            style:
              top: 25%
              left: 80%
              width: 12%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: >
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: lightgreen
              -
                operator: <=
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: orange
                      animate: blink 1s ease infinite
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_tire_pressure_rear_right
            icon: mdi:tire
            show_state: True
            layout: vertical
            style:
              top: 75%
              left: 80%
              width: 12%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: >
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: lightgreen
              -
                operator: <=
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: orange
                      animate: blink 1s ease infinite
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_tire_pressure_front_left
            icon: mdi:tire
            show_state: True
            layout: vertical
            style:
              top: 25%
              left: 20%
              width: 12%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: >
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: lightgreen
              -
                operator: <=
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: orange
                      animate: blink 1s ease infinite
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_tire_pressure_rear_left
            icon: mdi:tire
            show_state: True
            layout: vertical
            style:
              top: 75%
              left: 20%
              width: 12%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: >
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: lightgreen
              -
                operator: <=
                value: 2
                styles:
                  card:
                    -
                      font-size: 24cqw
                  icon:
                    -
                      color: orange
                      animate: blink 1s ease infinite
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: orange
                    -
                      transform: scaleX(1) rotate(90deg)
                    -
                      animation: [[[
  if (states['binary_sensor.car_glc_door_front_right'].state == 'off') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: orange
                    -
                      transform: scaleX(-1) rotate(-90deg)
                    -
                      animation: [[[
  if (states['binary_sensor.car_glc_door_rear_left'].state == 'off') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: orange
                    -
                      transform: scaleX(-1) rotate(90deg)
                    -
                      animation: [[[
  if (states['binary_sensor.car_glc_door_front_left'].state == 'off') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: orange
                    -
                      transform: scaleX(1) rotate(-90deg)
                    -
                      animation: [[[
  if (states['binary_sensor.car_glc_door_rear_right'].state == 'off') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
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
              -
                operator: ==
                value: on
                styles:
                  icon:
                    -
                      color: #088CF8
                    -
                      animation: [[[
  if (states['binary_sensor.xpb_358_charging_active'].state == 'on') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: off
                icon: mdi:ev-plug-type2
                styles:
                  icon:
                    -
                      display: none
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_charging_power
            show_icon: False
            show_state: True
            layout: vertical
            style:
              top: 89%
              left: 62%
              width: 25%
              z-index: 2
              container-type: inline-size
            styles:
              state:
                -
                  font-size: 13cqw
                  color: #088CF8
              card:
                -
                  display: [[[
  // Get the state of the power sensor
  var power = states['sensor.xpb_358_charging_power'].state;

  // Hide if power is 0 OR if the main entity is 0
  if (parseFloat(power) == 0 || entity.state == '0') {
    return 'none';
  } else {
    return 'block'; // Show the card
  }
]]]

          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_charging_power
            show_icon: False
            show_name: True
            show_state: False
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
                -
                  font-size: 13cqw
                  color: #088CF8
              card:
                -
                  display: [[[
  // Get the state of the power sensor
  var power = states['sensor.xpb_358_charging_power'].state;

  // Hide if power is 0 OR if the main entity is 0
  if (parseFloat(power) == 0 || entity.state == '0') {
    return 'none';
  } else {
    return 'block'; // Show the card
  }
]]]

          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.car_charge_ready
            show_icon: False
            show_state: True
            layout: vertical
            style:
              top: 95%
              left: 75%
              width: 25%
              z-index: 2
              container-type: inline-size
            styles:
              state:
                -
                  font-size: 13cqw
                  color: #088CF8
              card:
                -
                  display: [[[
  // Get the state of the power sensor
  var power = states['sensor.xpb_358_charging_power'].state;

  // Hide if power is 0 OR if the main entity is 0
  if (parseFloat(power) == 0 || entity.state == '0') {
    return 'none';
  } else {
    return 'block'; // Show the card
  }
]]]

          -
            type: custom:button-card
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
              -
                operator: ==
                value: off
                icon: [[[
  var soc = states['sensor.xpb_358_state_of_charge'].state;
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
                    -
                      color: [[[
  var soc = states['sensor.xpb_358_state_of_charge'].state;
  if (soc > 75) {
    return 'lightgreen';
  } else if (soc > 25) {
    return 'orange';
  } else {
    return 'red';
  }
]]]

                    -
                      animation: [[[
  if (states['binary_sensor.xpb_358_charging_active'].state == 'on') {
    return 'blink 1s ease infinite';
  } else {
    return 'none';
  }
]]]

              -
                operator: ==
                value: on
                styles:
                  card:
                    -
                      display: none
          -
            type: custom:button-card
            template: area_status_indicator
            entity: sensor.xpb_358_state_of_charge
            show_icon: False
            show_state: True
            layout: vertical
            style:
              top: 92%
              left: 38%
              width: 25%
              z-index: 2
              container-type: inline-size
            styles:
              card:
                -
                  font-size: 18cqw
            state:
              -
                operator: >
                value: 75
                styles:
                  card:
                    -
                      color: lightgreen
              -
                operator: >
                value: 25
                styles:
                  card:
                    -
                      color: orange
              -
                operator: default
                styles:
                  card:
                    -
                      color: red
      -
        type: entities
        entities:
          -
            entity: sensor.xpb_358_odometer
            name: Odometer
            secondary_info: none
          -
            entity: sensor.xpb_358_electric_consumption_reset
            name: Fuel Consumption
          -
            entity: sensor.xpb_358_liquid_consumption_reset
            name: Electric Consumption
max_columns: 4
path: car
subview: True

` 

## System

**ID**: $Id | **URL**: /dashboard-system | **File**: $F`n
### View: Network

Path: $(@{title=Network; path=network; cards=System.Object[]; type=sections; max_columns=6; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_network.png)

`yaml
title: Network
path: network
cards:
type: sections
max_columns: 6
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: WAN
        alignment: center
      -
        square: True
        type: grid
        cards:
          -
            type: custom:mini-graph-card
            icon: mdi:web
            height: 190
            hours_to_show: 24
            points_per_hour: 5
            line_width: 8
            font_size_header: 12
            font_size: 75
            decimals: 0
            show:
              fill: fade
              extrema: False
              name: True
              icon: True
              points: False
            entities:
              -
                entity: sensor.unifi_udmpro_latency_ms
                name: WAN Latency
                label: test
                show_state: True
                unit: ms
            color_thresholds:
              -
                value: 10
                color: #5FE787
              -
                value: 15
                color: #FF9800
              -
                value: 20
                color: #FF535B
            card_mod:
              style: .header.flex .icon { {% set sensor = states('sensor.unifi_udmpro_latency_ms')|float %}
  {% if sensor > 65 %}
    color: red;
  {% elif sensor > 55  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 20 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 15  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mini-graph-card
            icon: mdi:clock-fast
            name: DNS Processing
            height: 200
            hours_to_show: 24
            points_per_hour: 5
            line_width: 8
            font_size_header: 12
            font_size: 75
            decimals: 0
            show:
              fill: fade
              extrema: False
              name: True
              icon: False
              points: False
            entities:
              -
                entity: sensor.adguard_home_average_processing_speed_2
                show_state: True
                unit: ms
            color_thresholds:
              -
                value: 25
                color: #5FE787
              -
                value: 35
                color: #FF9800
              -
                value: 45
                color: #FF535B
            card_mod:
              style: .header.flex .icon { {% set sensor = states('sensor.adguard_home_average_processing_speed')|float %}
  {% if sensor > 45 %}
    color: red;
  {% elif sensor > 35  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 45 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 35  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mini-graph-card
            icon: mdi:web-cancel
            name: DNS Blocked
            height: 200
            hours_to_show: 24
            points_per_hour: 5
            line_width: 8
            font_size_header: 12
            font_size: 75
            decimals: 0
            show:
              fill: fade
              extrema: False
              name: True
              icon: False
              points: False
            entities:
              -
                entity: sensor.adguard_home_dns_queries_blocked_ratio_2
                show_state: True
                unit: %
            card_mod:
              style: .header.flex .icon {
  color: red;
} ha-card {
  --ha-card-background: rgba(255, 83, 91,0.05);
}

        columns: 3
      -
        type: entities
        entities:
          -
            entity: sensor.unifi_gateway_wan
            name: ISP Name
            type: attribute
            attribute: isp_name
            icon: mdi:web
            card_mod:
              style: :host {
  --card-mod-icon-color: skyblue;
}

          -
            entity: sensor.unifi_dream_machine_wan_status
            name: WAN
            icon: mdi:wan
            card_mod:
              style: :host {
  --card-mod-icon-color:yellow; 
}

          -
            entity: sensor.unifi_dream_machine_external_ip
            name: External IP
            icon: mdi:ip-network
            card_mod:
              style: :host {
  --card-mod-icon-color:yellow; 
}

          -
            entity: sensor.unifi_gateway_wan
            name: DNS Servers
            type: attribute
            attribute: nameservers
            icon: mdi:shield-check
            card_mod:
              style: :host {
  --card-mod-icon-color: skyblue;
}

          -
            type: section
            label: PRIMARY WAN
          -
            entity: sensor.primary_wan_availability
            name: Availability
            icon: mdi:web
            card_mod:
              style: :host {
  --card-mod-icon-color: lightgreen;
}

          -
            type: conditional
            conditions:
              -
                entity: sensor.primary_wan_availability
                state_not: unavailable
            row:
              entity: sensor.primary_wan_latency_avg
              name: Latency Average
              icon: mdi:pulse
            card_mod:
              style: :host {
  --card-mod-icon-color: lightgreen;
}

          -
            type: conditional
            conditions:
              -
                entity: sensor.primary_wan_availability
                state_not: unavailable
            row:
              entity: sensor.primary_wan_uptime
              name: Uptime
              icon: mdi:timelapse
          -
            type: conditional
            conditions:
              -
                entity: sensor.primary_wan_availability
                state: unavailable
            row:
              entity: sensor.primary_wan_downtime
              name: Downtime
              icon: mdi:timelapse
          -
            type: section
            label: FAILOVER WAN
          -
            entity: sensor.failover_wan_availability
            name: Availability
            icon: mdi:web
            card_mod:
              style: :host {
  --card-mod-icon-color: lightgreen;
}

          -
            type: conditional
            conditions:
              -
                entity: sensor.failover_wan_availability
                state_not: unavailable
            row:
              entity: sensor.failover_wan_latency_avg
              name: Latency Average
              icon: mdi:pulse
          -
            type: conditional
            conditions:
              -
                entity: sensor.failover_wan_availability
                state_not: unavailable
            row:
              entity: sensor.failover_wan_uptime
              name: Uptime
              icon: mdi:timelapse
          -
            type: conditional
            conditions:
              -
                entity: sensor.failover_wan_availability
                state: Unknown
            row:
              entity: sensor.failover_wan_downtime
              name: Downtime
              icon: mdi:timelapse
        state_color: True
      -
        type: entities
        entities:
          -
            entity: switch.shellyplusplugs_b0b21c1991a8_switch_0
            name: Cable Mode Power PLug
            icon: mdi:web
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: Dream Machine Pro
        alignment: center
      -
        type: picture
        image: local/network/UDM-Pro-front2.png
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.unifi_dream_machine_pro_cpu_temperature
                name: Temp
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            hours_to_show: 24
            show:
              points: False
            color_thresholds:
              -
                value: 45
                color: #5FE787
              -
                value: 55
                color: #FF9800
              -
                value: 65
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.unifi_dream_machine_pro_cpu_temperature')|float %}
  {% if sensor > 65 %}
    color: red;
  {% elif sensor > 55  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 65 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 55  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.unifi_dream_machine_pro_memory_utilization
                name: MEM
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            hours_to_show: 24
            decimals: 0
            show:
              points: False
            color_thresholds:
              -
                value: 70
                color: #5FE787
              -
                value: 80
                color: #FF9800
              -
                value: 90
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.unifi_dream_machine_pro_memory_utilization')|float %}
  {% if sensor > 90 %}
    color: red;
  {% elif sensor > 75  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 90 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 75  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.unifi_dream_machine_pro_cpu_utilization
                name: CPU
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            hours_to_show: 24
            decimals: 0
            show:
              points: False
            color_thresholds:
              -
                value: 25
                color: #5FE787
              -
                value: 50
                color: #FF9800
              -
                value: 75
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.unifi_dream_machine_pro_cpu_utilization')|float %}
  {% if sensor > 75 %}
    color: red;
  {% elif sensor > 50  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 75 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 50  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

        columns: 3
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: PORT FORWARDING
        alignment: center
      -
        type: custom:auto-entities
        card:
          type: grid
          columns: 2
          square: False
        card_param: cards
        sort:
          method: name
        filter:
          include:
            -
              entity_id: switch.unifi_network_*
              options:
                type: custom:mushroom-template-card
                primary: {% set name = state_attr(config.entity, "friendly_name") %}
{% set name = name | replace("UniFi Network ", "") %}
{{ name }}
                secondary: 
                icon: mdi:download-network
                layout: vertical
                fill_container: True
                icon_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
                tap_action:
                  action: more-info
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: NETWORKS
        alignment: center
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mushroom-template-card
            entity: switch.3visiot
            layout: vertical
            primary: {{ state_attr(config.entity, "friendly_name") }}
            secondary: {% set sensor_id = config.entity.replace("switch.", "sensor.") %}
{% set sensor_state = states(sensor_id) %}
{% set state = states(config.entity) %}
{% if state == "on" %}
  {{ sensor_state}} clients
{% else %}
  No Clients
{% endif %}
            icon: mdi:qrcode
            icon_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            badge_icon: mdi:wifi
            badge_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            double_tap_action:
              action: none
            hold_action:
              action: none
            tap_action:
              action: fire-dom-event
              browser_mod:
                service: browser_mod.popup
                data:
                  title: 3visIoT
                  content:
                    type: vertical-stack
                    cards:
                      -
                        type: conditional
                        conditions:
                          -
                            condition: state
                            entity: image.3visiot_qr_code
                            state_not: unavailable
                        card:
                          type: custom:more-info-card
                          entity: image.3visiot_qr_code
                          title:  
                      -
                        type: entities
                        entities:
                          -
                            entity: switch.3visiot
                            name: 3visIoT Network
                          -
                            entity: sensor.3visiot
                            name: 3visIoT Clients
                            icon: mdi:devices
          -
            type: custom:mushroom-template-card
            entity: switch.evisguest
            layout: vertical
            primary: {{ state_attr(config.entity, "friendly_name") }}
            secondary: {% set sensor_id = config.entity.replace("switch.", "sensor.") %}
{% set sensor_state = states(sensor_id) %}
{% set state = states(config.entity) %}
{% if state == "on" %}
  {{ sensor_state}} clients
{% else %}
  No Clients
{% endif %}
            icon: mdi:qrcode
            icon_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            badge_icon: mdi:wifi
            badge_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            tap_action:
              action: fire-dom-event
              browser_mod:
                service: browser_mod.popup
                data:
                  title: EvisGuest
                  content:
                    type: vertical-stack
                    cards:
                      -
                        type: conditional
                        conditions:
                          -
                            condition: state
                            entity: image.evisguest_qr_code
                            state_not: unavailable
                        card:
                          type: custom:more-info-card
                          entity: image.evisguest_qr_code
                          title:  
                      -
                        type: entities
                        entities:
                          -
                            entity: switch.evisguest
                            name: EvisGuest Network
                          -
                            entity: sensor.evisguest
                            name: EvisGuest Clients
                            icon: mdi:devices
          -
            type: custom:mushroom-template-card
            entity: switch.eviswifi
            layout: vertical
            primary: {{ state_attr(config.entity, "friendly_name") }}
            secondary: {% set sensor_id = config.entity.replace("switch.", "sensor.") %}
{% set sensor_state = states(sensor_id) %}
{% set state = states(config.entity) %}
{% if state == "on" %}
  {{ sensor_state}} clients
{% else %}
  No Clients
{% endif %}
            icon: mdi:qrcode
            icon_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            badge_icon: mdi:wifi
            badge_color: {% set state = states(config.entity) %}
{% if state == "on" %}
  green
{% else %}
  red
{% endif %}
            tap_action:
              action: fire-dom-event
              browser_mod:
                service: browser_mod.popup
                data:
                  title: EvisWifi
                  content:
                    type: vertical-stack
                    cards:
                      -
                        type: conditional
                        conditions:
                          -
                            condition: state
                            entity: image.eviswifi_qr_code
                            state_not: unavailable
                        card:
                          type: custom:more-info-card
                          entity: image.eviswifi_qr_code
                          title:  
                      -
                        type: entities
                        entities:
                          -
                            entity: switch.eviswifi
                            name: EvisWifi Network
                          -
                            entity: sensor.eviswifi
                            name: EvisWifi Clients
                            icon: mdi:devices
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: USW Enterprise 24 PoE
        alignment: center
      -
        type: picture
        image: local/network/USW-Enterprise-24-PoE-2.png
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.unifi_switch_enterprise_temperature
                name: Temp
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            hours_to_show: 24
            show:
              points: False
            color_thresholds:
              -
                value: 50
                color: #5FE787
              -
                value: 55
                color: #FF9800
              -
                value: 60
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.unifi_switch_enterprise_temperature')|float %}
  {% if sensor > 2000 %}
    color: red;
  {% elif sensor > 500  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 2000 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 500  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mushroom-update-card
            entity: update.unifi_switch_enterprise
            fill_container: True
            layout: vertical
            name: Updates
          -
            type: custom:mushroom-entity-card
            entity: sensor.unifi_switch_enterprise_uptime
            layout: vertical
            fill_container: True
            name: Uptime
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: PoE PORTS
        alignment: center
      -
        type: custom:auto-entities
        card:
          type: grid
          columns: 6
          square: False
        card_param: cards
        sort:
          method: name
        filter:
          include:
            -
              entity_id: sensor.unifi_switch_enterprise*poe*
              options:
                type: custom:mushroom-template-card
                primary: {% set name = state_attr(config.entity, "friendly_name") %}
{% set name = name | replace("UniFi Switch Enterprise ", "") %}
{% set port = name[:2] %}
{{ port }}
                secondary: {% set name = state_attr(config.entity, "friendly_name") %}
{% set name = name | replace("UniFi Switch Enterprise ", "") %}
{% set name = name | replace("PoE", "") %}
{% set name = name | replace("Power", "") %}
{% set name = name[5:100] %}
{% if name != "" %}
  {{ name }}
{% else %}
  Port
{% endif %}
                icon: mdi:ethernet
                icon_color: {% set poe_id = config.entity.replace("sensor.", "switch.") %}
{% set poe_id = poe_id | replace("_power", "") %}
{% set poe = states(poe_id) %}
{% if poe == "on" %}
  green
{% else %}
  red
{% endif %}
                layout: vertical
                multiline_secondary: False
                fill_container: True
                card_mod:
                  style: ha-card {
  {% set power = states(config.entity)|float(0) %}
  {% if power > 10 %}
    background-color: rgba(153, 255, 102, 0.3);
  {% elif power > 5 %}
    background-color: rgba(153, 255, 102, 0.2);
  {% elif power > 0 %}
    background-color: rgba(153, 255, 102, 0.1);
  {% endif %}

                tap_action:
                  action: fire-dom-event
                  browser_mod:
                    service: browser_mod.popup
                    data:
                      title: Port
                      content:
                        type: vertical-stack
                        cards:
                          -
                            type: history-graph
                            entities:
                              -
                                entity: this.entity_id
                          -
                            type: entities
                            entities:
                              -
                                entity: this.entity_id
                                name: Current Power Usage
                          -
                            type: custom:button-card
                            entity: [[[
  var new_id = 'this.entity_id'.replace("sensor.", "switch.");
  new_id = new_id.replace("_power", "")
  return new_id
]]]

                            name: Port PoE Switch
                            layout: icon_name
                            show_state: True
                            tap_action:
                              action: toggle
                              confirmation:
                                text: Switching Port PoE Power will take a short time to take an effect
                            state:
                              -
                                value: on
                                styles:
                                  icon:
                                    -
                                      color: lightgreen
                              -
                                value: off
                                styles:
                                  icon:
                                    -
                                      color: red
                            styles:
                              name:
                                -
                                  position: absolute
                                -
                                  left: 74px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  font-size: 14px
                              state:
                                -
                                  position: absolute
                                -
                                  right: 20px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  font-size: 14px
                              icon:
                                -
                                  position: absolute
                                -
                                  left: 15px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  width: 40px
                                -
                                  height: 25px
                              card:
                                -
                                  height: 60px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: custom:auto-entities
        card:
          type: grid
          columns: 4
          square: False
        card_param: cards
        sort:
          method: name
        filter:
          include:
            -
              entity_id: sensor.unifi_switch_enterprise*poe*
              options:
                type: custom:mushroom-template-card
                primary: {% set name = state_attr(config.entity, "friendly_name") %}
{% set name = name | replace("UniFi Switch Enterprise ", "") %}
{% set port = name[:2] %}
{{ port }}
                secondary: {% set name = state_attr(config.entity, "friendly_name") %}
{% set name = name | replace("UniFi Switch Enterprise ", "") %}
{% set name = name | replace("PoE", "") %}
{% set name = name | replace("Power", "") %}
{% set name = name[5:100] %}
{% if name != "" %}
  {{ name }}
{% else %}
  Port
{% endif %}
                icon: mdi:ethernet
                icon_color: {% set poe_id = config.entity.replace("sensor.", "switch.") %}
{% set poe_id = poe_id | replace("_power", "") %}
{% set poe = states(poe_id) %}
{% if poe == "on" %}
  green
{% else %}
  red
{% endif %}
                layout: vertical
                multiline_secondary: False
                fill_container: True
                card_mod:
                  style: ha-card {
  {% set power = states(config.entity)|float(0) %}
  {% if power > 10 %}
    background-color: rgba(153, 255, 102, 0.3);
  {% elif power > 5 %}
    background-color: rgba(153, 255, 102, 0.2);
  {% elif power > 0 %}
    background-color: rgba(153, 255, 102, 0.1);
  {% endif %}

                tap_action:
                  action: fire-dom-event
                  browser_mod:
                    service: browser_mod.popup
                    data:
                      title: Port
                      content:
                        type: vertical-stack
                        cards:
                          -
                            type: history-graph
                            entities:
                              -
                                entity: this.entity_id
                          -
                            type: entities
                            entities:
                              -
                                entity: this.entity_id
                                name: Current Power Usage
                          -
                            type: custom:button-card
                            entity: [[[
  var new_id = 'this.entity_id'.replace("sensor.", "switch.");
  new_id = new_id.replace("_power", "")
  return new_id
]]]

                            name: Port PoE Switch
                            layout: icon_name
                            show_state: True
                            tap_action:
                              action: toggle
                              confirmation:
                                text: Switching Port PoE Power will take a short time to take an effect
                            state:
                              -
                                value: on
                                styles:
                                  icon:
                                    -
                                      color: lightgreen
                              -
                                value: off
                                styles:
                                  icon:
                                    -
                                      color: red
                            styles:
                              name:
                                -
                                  position: absolute
                                -
                                  left: 74px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  font-size: 14px
                              state:
                                -
                                  position: absolute
                                -
                                  right: 20px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  font-size: 14px
                              icon:
                                -
                                  position: absolute
                                -
                                  left: 15px
                                -
                                  margin: 0px
                                -
                                  padding: 0px
                                -
                                  width: 40px
                                -
                                  height: 25px
                              card:
                                -
                                  height: 60px
                                -
                                  margin: 0px
                                -
                                  padding: 0px

` 
### View: Proxmox

Path: $(@{theme=Backend-selected; title=Proxmox; path=proxmox; icon=; type=custom:vertical-layout; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack, custom:layout-break

![View Screenshot](assets/images/view_proxmox.png)

`yaml
theme: Backend-selected
title: Proxmox
path: proxmox
icon: 
type: custom:vertical-layout
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:mushroom-title-card
        title: PROXMOX VE
        subtitle: HALO | ENVIRONMENT
        alignment: center
      -
        type: custom:uptime-card
        entity: binary_sensor.node_halo_status
        icon: mdi:heart-pulse
        title_template: UPTIME
        hours_to_show: 168
        alignment:
          status: spaced
          header: center
          icon_first: False
        alias:
          ok: Running
          ko: Unvailable
          half: Unvailable
        color:
          ko: red
          ok: lightgreen
          half: red
          icon: orange
        bar:
          spacing: 4
          height: 20
          round: 5
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.node_halo_memory_used_percentage
                name: MEM
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            hours_to_show: 24
            decimals: 0
            show:
              points: False
            color_thresholds:
              -
                value: 70
                color: #5FE787
              -
                value: 80
                color: #FF9800
              -
                value: 90
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.node_halo_memory_used_percentage')|float %}
  {% if sensor > 90 %}
    color: red;
  {% elif sensor > 75  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 90 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 75  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

          -
            type: custom:mini-graph-card
            entities:
              -
                entity: sensor.node_halo_cpu_used
                name: CPU
            font_size_header: 12
            font_size: 75
            line_width: 8
            height: 200
            animate: True
            decimals: 0
            hours_to_show: 24
            show:
              points: False
            color_thresholds:
              -
                value: 25
                color: #5FE787
              -
                value: 50
                color: #FF9800
              -
                value: 75
                color: #FF535B
            card_mod:
              style: .header.flex .icon {
{% set sensor = states('sensor.node_halo_cpu_used')|float %}
  {% if sensor > 75 %}
    color: red;
  {% elif sensor > 50  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 75 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 50  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

        columns: 2
  -
    type: vertical-stack
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: HALO | CONTROLS
        alignment: center
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            entity: button.node_halo_reboot
            layout: vertical
            name: Reboot
            secondary_info: none
            tap_action:
              action: none
          -
            type: custom:mushroom-entity-card
            entity: button.node_halo_shutdown
            secondary_info: none
            layout: vertical
            name: Shutdown
            tap_action:
              action: none
          -
            type: custom:mushroom-entity-card
            entity: button.node_halo_stop_all
            layout: vertical
            secondary_info: none
            name: Stop All
            tap_action:
              action: none
          -
            type: custom:mushroom-entity-card
            entity: button.node_halo_start_all
            layout: vertical
            secondary_info: none
            name: Start All
            tap_action:
              action: none
        columns: 4
  -
    type: vertical-stack
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: HALO | STORAGE
        alignment: center
      -
        type: vertical-stack
        cards:
          -
            type: custom:bar-card
            severity:
              -
                from: 0
                to: 50
              -
                color: Orange
                from: 51
                to: 75
              -
                color: red
                from: 76
                to: 100
            entities:
              -
                entity: sensor.node_halo_disk_used_2
                name: SSD10
                decimal: 0
                icon: mdi:harddisk
                positions:
                  icon: inside
              -
                entity: sensor.node_halo_disk_used_percentage
                name: Local NVMe
                decimal: 0
                positions:
                  icon: inside
  -
    type: custom:layout-break
  -
    type: vertical-stack
    cards:
      -
        type: custom:mushroom-title-card
        title: VIRTUAL MACHINES
        alignment: center
        subtitle: NODE | HALO
      -
        type: custom:auto-entities
        card:
          type: grid
          columns: 1
          square: False
        card_param: cards
        sort:
          method: name
        filter:
          include:
            -
              entity_id: sensor.*qemu*cpu*
              options:
                type: custom:button-card
                layout: icon_name_state2nd
                show_name: True
                show_state: False
                show_icon: False
                show_label: False
                card_mod:
                  style: ha-card {
  overflow: visible;
  border-top: 1px solid #333333;
}

                name: [[[
  var name = states['this.entity_id'].attributes.friendly_name;
  name = name.replace("QEMU ", "");
  name = name.replace(" CPU used", "");
  return name
]]]

                styles:
                  name:
                    -
                      position: absolute
                    -
                      top: 15px
                    -
                      left: 65px
                    -
                      color: white
                    -
                      font-size: 15px
                    -
                      text-transform: uppercase
                  state:
                    -
                      position: absolute
                    -
                      top: 37px
                    -
                      left: 65px
                    -
                      font-size: 12px
                  card:
                    -
                      border-radius: 8px
                    -
                      height: 210px
                    -
                      overflow: unset
                    -
                      margin-bottom: 13px
                    -
                      padding: 0px
                  custom_fields:
                    cpugraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 35%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    memgraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 67.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    netgraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 67.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    icon:
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        position: absolute
                      -
                        left: -12px
                      -
                        top: 12px
                    power:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 2.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        height: 124px
                      -
                        display: block
                    ip:
                      -
                        position: absolute
                      -
                        top: 28px
                      -
                        left: 64px
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        display: block
                    uptime:
                      -
                        position: absolute
                      -
                        top: 10px
                      -
                        left: 50px
                      -
                        width: 85%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        display: block
                    navoverlay:
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        position: absolute
                      -
                        width: 100%
                      -
                        height: 100%
                      -
                        right: 0px
                      -
                        top: 0px
                      -
                        z-index: 90
                custom_fields:
                  icon:
                    card:
                      type: custom:button-card
                      entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_status");
]]]
                      name: Icon
                      icon: mdi:vector-combine
                      show_name: False
                      show_state: False
                      card_mod:
                        style: ha-card {
  box-shadow: none;
  border: 0px;
}

                      styles:
                        card:
                          -
                            width: 90px
                          -
                            background-color: rgba(0,0,0,0)
                          -
                            border: 0px
                        icon:
                          -
                            color: red
                          -
                            filter: drop-shadow(0px 0px 2px rgba(0,0,0,0)
                      state:
                        -
                          value: running
                          styles:
                            icon:
                              -
                                color: rgba(95, 231, 135, 1)
                  cpugraph:
                    card:
                      type: custom:mini-graph-card
                      entities:
                        -
                          entity: this.entity_id
                          name: CPU
                      font_size_header: 12
                      font_size: 75
                      line_width: 8
                      height: 75
                      animate: True
                      hours_to_show: 24
                      decimals: 0
                      show:
                        points: False
                      color_thresholds:
                        -
                          value: 0
                          color: rgba(0, 0, 0, 0)
                        -
                          value: 1
                          color: #5FE787
                        -
                          value: 70
                          color: #5FE787
                        -
                          value: 80
                          color: #FF9800
                        -
                          value: 90
                          color: #FF535B
                      card_mod:
                        style: .header.flex .icon {
  {% set sensor = states('this.entity_id')|float(0) %}
  {% if sensor > 90 %}
    color: red;
  {% elif sensor > 75  %}
    color: orange;
  {% elif sensor > 1 %}
    color: lightgreen;
  {% else  %}
    color: gray;
  {% endif %} }
ha-card {
  {% if sensor > 90 %}
    --ha-card-background: rgba(255, 83, 91, 0.05);
  {% elif sensor > 75  %}
    --ha-card-background: rgba(255, 152, 0, 0.05);
  {% elif sensor > 1  %}
    --ha-card-background: rgba(95, 231, 135, 0.05);
  {% else  %}
    --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif %} }
}

                  memgraph:
                    card:
                      type: custom:mini-graph-card
                      entities:
                        -
                          entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage");
]]]
                          name: MEM
                      font_size_header: 12
                      font_size: 75
                      line_width: 8
                      height: 75
                      animate: True
                      decimals: 0
                      hours_to_show: 24
                      show:
                        points: False
                      color_thresholds:
                        -
                          value: 0
                          color: rgba(0, 0, 0, 0)
                        -
                          value: 1
                          color: #5FE787
                        -
                          value: 50
                          color: #5FE787
                        -
                          value: 60
                          color: #FF9800
                        -
                          value: 80
                          color: #FF535B
                      card_mod:
                        style: .header.flex .icon {
  {% set mem_id = 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage") %}
  {% set mem_sensor = states(mem_id)|float(0) %}
  {% if mem_sensor > 80 %}
    color: red;
  {% elif mem_sensor > 60  %}
    color: orange;
  {% elif mem_sensor > 1 %}
    color: lightgreen;
  {% else  %}
    color: grey;
  {% endif %}
}
ha-card {
  {% if mem_sensor > 80 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif mem_sensor > 60  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% elif mem_sensor > 1  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% else %}
    --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif %} }
}

                  power:
                    card:
                      type: custom:mushroom-template-card
                      primary: 
                      secondary: CONTROLS
                      icon: mdi:power
                      entity: [[[
  var uptime_id = 'this.entity_id'.replace("_cpu_used", "_status");
  return uptime_id;
]]]
                      icon_color: {% set power_id = 'this.entity_id'.replace("_cpu_used", "_status") %}
{% set power_state = states(power_id) %}
{% if power_state == "running" %}
  orange
{% else %}
  orange
{%endif %}
                      layout: vertical
                      fill_container: True
                      card_mod:
                        style: ha-card {
  width: 100%;
  {% set power_id = 'this.entity_id'.replace("_cpu_used", "_status") %}
  {% set power_state = states(power_id) %}
  {% if power_state == "running" %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% else  %}
     --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif  %}
}

                      tap_action:
                        action: fire-dom-event
                        browser_mod:
                          service: browser_mod.popup
                          data:
                            title: VM
                            content:
                              type: vertical-stack
                              cards:
                                -
                                  type: custom:mushroom-title-card
                                  title: [[[
  var name = states['this.entity_id'].attributes.friendly_name;
  name = name.replace("QEMU ", "");
  name = name.replace(" CPU used", "");
  return name
]]]

                                  alignment: center
                                -
                                  type: history-graph
                                  entities:
                                    -
                                      entity: this.entity_id
                                      name: CPU Usage
                                    -
                                      entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage");
]]]
                                      name: Memory Usage
                                -
                                  type: custom:mushroom-entity-card
                                  entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_status");
]]]
                                  layout: vertical
                                  primary_info: state
                                  secondary_info: none
                                  icon: mdi:server
                                -
                                  type: grid
                                  square: False
                                  cards:
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_start");
  return button_id
]]]
                                      layout: vertical
                                      name: START
                                      icon: mdi:power
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_resume");
  return button_id
]]]
                                      layout: vertical
                                      name: RESUME
                                      icon: mdi:play
                                      secondary_info: none
                                      tap_action:
                                        action: call-service
                                        service: button.press
                                        target:
                                          entity_id: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_resume");
  return button_id
]]]
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: HIBERNATE
                                      icon: mdi:arrow-collapse-down
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: PAUSE
                                      icon: mdi:pause
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: SHUTDOWN
                                      icon: mdi:power-off
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: REBOOT
                                      icon: mdi:refresh
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: RESET
                                      icon: mdi:power-plug
                                      secondary_info: none
                                      icon_color: red
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_start
                                      layout: vertical
                                      name: STOP
                                      icon: mdi:power-plug-off
                                      secondary_info: none
                                      icon_color: red
                                  columns: 4
                  uptime:
                    card:
                      type: custom:uptime-card
                      entity: [[[
  var uptime_id = 'this.entity_id'.replace("_cpu_used", "_status");
  uptime_id = uptime_id.replace("sensor.", "binary_sensor.");
  return uptime_id;
]]]
                      title_template: UPTIME
                      hours_to_show: 168
                      alignment:
                        status: spaced
                        header: center
                        icon_first: False
                      alias:
                        ok: Running
                        ko: Unvailable
                        none:
                          - unknown
                          - unavailable
                      color:
                        ko: red
                        ok: lightgreen
                        half: red
                        icon: orange
                        none: black
                      bar:
                        spacing: 8
                        height: 8
                        round: 2
                      show:
                        header: False
                        status: False
                        footer: True
                        average: False
                      card_mod:
                        style: :host {
  border-style: none;
}
ha-card {
  border: 0px;
  box-shadow: none;
  border-style: none;
  background-color: rgba(0,0,0,0);
  font-size: 12px
}

                      hold_Action:
                        action: more-info
                      tap_action:
                        action: more-info
  -
    type: custom:layout-break

` 
### View: Energy

![View Screenshot](assets/images/view_.png)

`yaml
theme: Backend-selected
title: Energy
type: sections
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section

` 
### View: Feed

Path: $(@{title=Feed; path=Feed; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: custom:home-feed-card, history-graph

![View Screenshot](assets/images/view_Feed.png)

`yaml
title: Feed
path: Feed
badges:
cards:
  -
    type: custom:home-feed-card
    title: Home Feed
    card_id: main_feed
    show_empty: False
    calendars:
      - calendar.family_calendar
    id_filter: ^home_feed_.*
    more_info_on_tap: True
    state_color: True
    compact_mode: True
    entities:
      -
        entity: binary_sensor.backyard_door_sensor_contact
        name: Backyard Door
      -
        entity: binary_sensor.front_door_door
        name: Front Door
  -
    type: history-graph
    entities:
      -
        entity: binary_sensor.backyard_door_sensor_contact
        name: Back Door
      -
        entity: binary_sensor.etuovi_contact
        name: Front Door
      -
        entity: lock.etuovi
        name: Front Lock
    hours_to_show: 24

` 
### View: Proxmox

![View Screenshot](assets/images/view_.png)

`yaml
theme: Backend-selected
title: Proxmox
icon: 
type: sections
badges:
cards:
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: PROXMOX VE
        subtitle: HALO | ENVIRONMENT
        alignment: center
        grid_options:
          columns: 12
          rows: 2
      -
        type: custom:uptime-card
        entity: binary_sensor.node_halo_status
        icon: mdi:heart-pulse
        title_template: UPTIME
        hours_to_show: 168
        alignment:
          status: spaced
          header: center
          icon_first: False
        alias:
          ok: Running
          ko: Unvailable
          half: Unvailable
        color:
          ko: red
          ok: lightgreen
          half: red
          icon: orange
        bar:
          spacing: 4
          height: 20
          round: 5
        grid_options:
          columns: 12
          rows: 2.15
      -
        type: custom:mini-graph-card
        entities:
          -
            entity: sensor.node_halo_memory_used_percentage
            name: MEM
        font_size_header: 12
        font_size: 75
        line_width: 8
        height: 80
        animate: True
        hours_to_show: 24
        decimals: 0
        show:
          points: False
        color_thresholds:
          -
            value: 70
            color: #5FE787
          -
            value: 80
            color: #FF9800
          -
            value: 90
            color: #FF535B
        card_mod:
          style: .header.flex .icon {
{% set sensor = states('sensor.node_halo_memory_used_percentage')|float %}
  {% if sensor > 90 %}
    color: red;
  {% elif sensor > 75  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 90 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 75  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

        grid_options:
          columns: 3
      -
        type: custom:mini-graph-card
        entities:
          -
            entity: sensor.node_halo_cpu_used
            name: CPU
        font_size_header: 12
        font_size: 75
        line_width: 8
        height: 80
        animate: True
        decimals: 0
        hours_to_show: 24
        show:
          points: False
        color_thresholds:
          -
            value: 25
            color: #5FE787
          -
            value: 50
            color: #FF9800
          -
            value: 75
            color: #FF535B
        card_mod:
          style: .header.flex .icon {
{% set sensor = states('sensor.node_halo_cpu_used')|float %}
  {% if sensor > 75 %}
    color: red;
  {% elif sensor > 50  %}
    color: orange;
  {% else  %}
    color: lightgreen;
  {% endif %} }
ha-card {
  {% if sensor > 75 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif sensor > 50  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% else  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% endif %} }
}

        grid_options:
          columns: 3
      -
        type: vertical-stack
        cards:
          -
            type: custom:bar-card
            severity:
              -
                from: 0
                to: 50
              -
                color: Orange
                from: 51
                to: 75
              -
                color: red
                from: 76
                to: 100
            entities:
              -
                entity: sensor.node_halo_disk_used_2
                name: SSD10
                decimal: 0
                icon: mdi:harddisk
                positions:
                  icon: inside
              -
                entity: sensor.node_halo_disk_used_percentage
                name: Local NVMe
                decimal: 0
                positions:
                  icon: inside
        grid_options:
          columns: 6
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: HALO | CONTROLS
        alignment: center
      -
        type: custom:mushroom-entity-card
        entity: button.node_halo_reboot
        layout: vertical
        name: Reboot
        secondary_info: none
        tap_action:
          action: none
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: button.node_halo_shutdown
        secondary_info: none
        layout: vertical
        name: Shutdown
        tap_action:
          action: none
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: button.node_halo_stop_all
        layout: vertical
        secondary_info: none
        name: Stop All
        tap_action:
          action: none
        grid_options:
          columns: 3
          rows: 2
      -
        type: custom:mushroom-entity-card
        entity: button.node_halo_start_all
        layout: vertical
        secondary_info: none
        name: Start All
        tap_action:
          action: none
        grid_options:
          columns: 3
          rows: 2
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: VIRTUAL MACHINES
        alignment: center
        subtitle: NODE | HALO
      -
        type: custom:auto-entities
        card:
          type: grid
          columns: 1
          square: False
        card_param: cards
        sort:
          method: name
        filter:
          include:
            -
              entity_id: sensor.*qemu*cpu*
              options:
                type: custom:button-card
                layout: icon_name_state2nd
                show_name: True
                show_state: False
                show_icon: False
                show_label: False
                card_mod:
                  style: ha-card {
  overflow: visible;
  border-top: 1px solid #333333;
}

                name: [[[
  var name = states['this.entity_id'].attributes.friendly_name;
  name = name.replace("QEMU ", "");
  name = name.replace(" CPU used", "");
  return name
]]]

                styles:
                  name:
                    -
                      position: absolute
                    -
                      top: 15px
                    -
                      left: 65px
                    -
                      color: white
                    -
                      font-size: 15px
                    -
                      text-transform: uppercase
                  state:
                    -
                      position: absolute
                    -
                      top: 37px
                    -
                      left: 65px
                    -
                      font-size: 12px
                  card:
                    -
                      border-radius: 8px
                    -
                      height: 210px
                    -
                      overflow: unset
                    -
                      margin-bottom: 13px
                    -
                      padding: 0px
                  custom_fields:
                    cpugraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 35%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    memgraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 67.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    netgraph:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 67.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        display: block
                    icon:
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        position: absolute
                      -
                        left: -12px
                      -
                        top: 12px
                    power:
                      -
                        position: absolute
                      -
                        top: 70px
                      -
                        left: 2.5%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        margin-bottom: 10px
                      -
                        width: 30%
                      -
                        height: 124px
                      -
                        display: block
                    ip:
                      -
                        position: absolute
                      -
                        top: 28px
                      -
                        left: 64px
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        display: block
                    uptime:
                      -
                        position: absolute
                      -
                        top: 10px
                      -
                        left: 50px
                      -
                        width: 85%
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        display: block
                    navoverlay:
                      -
                        margin: 0px
                      -
                        padding: 0px
                      -
                        position: absolute
                      -
                        width: 100%
                      -
                        height: 100%
                      -
                        right: 0px
                      -
                        top: 0px
                      -
                        z-index: 90
                custom_fields:
                  icon:
                    card:
                      type: custom:button-card
                      entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_status");
]]]
                      name: Icon
                      icon: mdi:vector-combine
                      show_name: False
                      show_state: False
                      card_mod:
                        style: ha-card {
  box-shadow: none;
  border: 0px;
}

                      styles:
                        card:
                          -
                            width: 90px
                          -
                            background-color: rgba(0,0,0,0)
                          -
                            border: 0px
                        icon:
                          -
                            color: red
                          -
                            filter: drop-shadow(0px 0px 2px rgba(0,0,0,0)
                      state:
                        -
                          value: running
                          styles:
                            icon:
                              -
                                color: rgba(95, 231, 135, 1)
                  cpugraph:
                    card:
                      type: custom:mini-graph-card
                      entities:
                        -
                          entity: this.entity_id
                          name: CPU
                      font_size_header: 12
                      font_size: 75
                      line_width: 8
                      height: 75
                      animate: True
                      hours_to_show: 24
                      decimals: 0
                      show:
                        points: False
                      color_thresholds:
                        -
                          value: 0
                          color: rgba(0, 0, 0, 0)
                        -
                          value: 1
                          color: #5FE787
                        -
                          value: 70
                          color: #5FE787
                        -
                          value: 80
                          color: #FF9800
                        -
                          value: 90
                          color: #FF535B
                      card_mod:
                        style: .header.flex .icon {
  {% set sensor = states('this.entity_id')|float(0) %}
  {% if sensor > 90 %}
    color: red;
  {% elif sensor > 75  %}
    color: orange;
  {% elif sensor > 1 %}
    color: lightgreen;
  {% else  %}
    color: gray;
  {% endif %} }
ha-card {
  {% if sensor > 90 %}
    --ha-card-background: rgba(255, 83, 91, 0.05);
  {% elif sensor > 75  %}
    --ha-card-background: rgba(255, 152, 0, 0.05);
  {% elif sensor > 1  %}
    --ha-card-background: rgba(95, 231, 135, 0.05);
  {% else  %}
    --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif %} }
}

                  memgraph:
                    card:
                      type: custom:mini-graph-card
                      entities:
                        -
                          entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage");
]]]
                          name: MEM
                      font_size_header: 12
                      font_size: 75
                      line_width: 8
                      height: 75
                      animate: True
                      decimals: 0
                      hours_to_show: 24
                      show:
                        points: False
                      color_thresholds:
                        -
                          value: 0
                          color: rgba(0, 0, 0, 0)
                        -
                          value: 1
                          color: #5FE787
                        -
                          value: 50
                          color: #5FE787
                        -
                          value: 60
                          color: #FF9800
                        -
                          value: 80
                          color: #FF535B
                      card_mod:
                        style: .header.flex .icon {
  {% set mem_id = 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage") %}
  {% set mem_sensor = states(mem_id)|float(0) %}
  {% if mem_sensor > 80 %}
    color: red;
  {% elif mem_sensor > 60  %}
    color: orange;
  {% elif mem_sensor > 1 %}
    color: lightgreen;
  {% else  %}
    color: grey;
  {% endif %}
}
ha-card {
  {% if mem_sensor > 80 %}
    --ha-card-background: rgba(255, 83, 91,0.05);
  {% elif mem_sensor > 60  %}
    --ha-card-background: rgba(255, 152, 0,0.05);
  {% elif mem_sensor > 1  %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% else %}
    --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif %} }
}

                  power:
                    card:
                      type: custom:mushroom-template-card
                      primary: 
                      secondary: CONTROLS
                      icon: mdi:power
                      entity: [[[
  var uptime_id = 'this.entity_id'.replace("_cpu_used", "_status");
  return uptime_id;
]]]
                      icon_color: {% set power_id = 'this.entity_id'.replace("_cpu_used", "_status") %}
{% set power_state = states(power_id) %}
{% if power_state == "running" %}
  orange
{% else %}
  orange
{%endif %}
                      layout: vertical
                      fill_container: True
                      card_mod:
                        style: ha-card {
  width: 100%;
  {% set power_id = 'this.entity_id'.replace("_cpu_used", "_status") %}
  {% set power_state = states(power_id) %}
  {% if power_state == "running" %}
    --ha-card-background: rgba(95, 231, 135,0.05);
  {% else  %}
     --ha-card-background: rgba(0, 0, 0, 0.25);
  {% endif  %}
}

                      tap_action:
                        action: fire-dom-event
                        browser_mod:
                          service: browser_mod.popup
                          data:
                            title: VM
                            content:
                              type: vertical-stack
                              cards:
                                -
                                  type: custom:mushroom-title-card
                                  title: [[[
  var name = states['this.entity_id'].attributes.friendly_name;
  name = name.replace("QEMU ", "");
  name = name.replace(" CPU used", "");
  return name
]]]

                                  alignment: center
                                -
                                  type: history-graph
                                  entities:
                                    -
                                      entity: this.entity_id
                                      name: CPU Usage
                                    -
                                      entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_memory_used_percentage");
]]]
                                      name: Memory Usage
                                -
                                  type: custom:mushroom-entity-card
                                  entity: [[[
  return 'this.entity_id'.replace("_cpu_used", "_status");
]]]
                                  layout: vertical
                                  primary_info: state
                                  secondary_info: none
                                  icon: mdi:server
                                -
                                  type: grid
                                  square: False
                                  cards:
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_start");
  return button_id
]]]
                                      layout: vertical
                                      name: START
                                      icon: mdi:power
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_resume");
  return button_id
]]]
                                      layout: vertical
                                      name: RESUME
                                      icon: mdi:play
                                      secondary_info: none
                                      tap_action:
                                        action: call-service
                                        service: button.press
                                        target:
                                          entity_id: [[[
  var button_id = 'this.entity_id'.replace("sensor.", "button.");
  button_id = button_id.replace("_cpu_used", "_resume");
  return button_id
]]]
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: HIBERNATE
                                      icon: mdi:arrow-collapse-down
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: PAUSE
                                      icon: mdi:pause
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: SHUTDOWN
                                      icon: mdi:power-off
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: REBOOT
                                      icon: mdi:refresh
                                      secondary_info: none
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_suspend
                                      layout: vertical
                                      name: RESET
                                      icon: mdi:power-plug
                                      secondary_info: none
                                      icon_color: red
                                    -
                                      type: custom:mushroom-entity-card
                                      entity: button.qemu_vm_windows_11_pro_110_start
                                      layout: vertical
                                      name: STOP
                                      icon: mdi:power-plug-off
                                      secondary_info: none
                                      icon_color: red
                                  columns: 4
                  uptime:
                    card:
                      type: custom:uptime-card
                      entity: [[[
  var uptime_id = 'this.entity_id'.replace("_cpu_used", "_status");
  uptime_id = uptime_id.replace("sensor.", "binary_sensor.");
  return uptime_id;
]]]
                      title_template: UPTIME
                      hours_to_show: 168
                      alignment:
                        status: spaced
                        header: center
                        icon_first: False
                      alias:
                        ok: Running
                        ko: Unvailable
                        none:
                          - unknown
                          - unavailable
                      color:
                        ko: red
                        ok: lightgreen
                        half: red
                        icon: orange
                        none: black
                      bar:
                        spacing: 8
                        height: 8
                        round: 2
                      show:
                        header: False
                        status: False
                        footer: True
                        average: False
                      card_mod:
                        style: :host {
  border-style: none;
}
ha-card {
  border: 0px;
  box-shadow: none;
  border-style: none;
  background-color: rgba(0,0,0,0);
  font-size: 12px
}

                      hold_Action:
                        action: more-info
                      tap_action:
                        action: more-info

` 

## Remotes

**ID**: $Id | **URL**: /dashboard-popups | **File**: $F`n
### View: tv-remote

Path: $(@{theme=Backend-selected; title=tv-remote; subview=True; path=tv-remote; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: grid

![View Screenshot](assets/images/view_tv-remote.png)

`yaml
theme: Backend-selected
title: tv-remote
subview: True
path: tv-remote
badges:
cards:
  -
    square: False
    columns: 1
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: PHILIPS TV
        alignment: center
        subtitle: 
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:mushroom-entity-card
        tap_action:
          action: call-service
          service: script.turn_on
          data:
          target:
            entity_id: script.philips_tv_power
        entity: input_button.tv_remote_button
        fill_container: True
        primary_info: none
        secondary_info: none
        layout: horizontal
        icon: mdi:power
        icon_color: red
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: Navigation
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_menu
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MENU
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_up
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-up-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_source
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: SOURCES
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_left
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-left-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_ok
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:circle
            icon_color: light-green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_right
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-right-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_back
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: BACK
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-down-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:home
            icon_color: white
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: TV Controls
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_vol_up
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:volume-plus
            icon_color: orange
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_guide
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:volume-plus
            icon_color: orange
            name: GUIDE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_channel_up
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:playlist-plus
            icon_color: yellow
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_vol_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:volume-minus
            icon_color: orange
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_mute
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:volume-mute
            icon_color: orange
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_channel_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:playlist-minus
            icon_color: yellow
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: Media Control
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_rewind
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:rewind
            icon_color: light-blue
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_play
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:play
            icon_color: light-blue
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_forward
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:fast-forward
            icon_color: light-blue
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_stop
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:stop
            icon_color: light-blue
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_pause
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:pause
            icon_color: light-blue
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_record
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:record
            icon_color: red
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: Color Buttons
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        columns: 4
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_red
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:square-rounded
            icon_color: red
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_green
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:square-rounded
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_yellow
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:square-rounded
            icon_color: yellow
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_blue
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:square-rounded
            icon_color: blue
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: Numbers
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_1
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-1
            icon_color: white
            name: 1
            icon_type: icon
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_2
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-2
            icon_color: white
            name: 2
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_3
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-3
            icon_color: white
            name: 3
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_4
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-4
            icon_color: white
            name: 4
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_5
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-5
            icon_color: white
            name: 5
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_6
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-6
            icon_color: white
            name: 6
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_7
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-7
            icon_color: white
            name: 7
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_8
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-8
            icon_color: white
            name: 8
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_9
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-9
            icon_color: white
            name: 9
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_text
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-4-box-outline
            icon_color: white
            name: TEXT
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_0
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-0
            icon_color: white
            name: 0
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.philips_tv_list
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:numeric-4-box-outline
            icon_color: white
            name: LIST
            icon_type: none

` 
### View: Soundbar-Remote

Path: $(@{theme=Backend-selected; title=Soundbar-Remote; path=soundbar-remote; subview=True; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: grid

![View Screenshot](assets/images/view_soundbar-remote.png)

`yaml
theme: Backend-selected
title: Soundbar-Remote
path: soundbar-remote
subview: True
badges:
cards:
  -
    square: False
    columns: 1
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: SOUND BAR
        alignment: center
        subtitle: 
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:mushroom-entity-card
        tap_action:
          action: call-service
          service: script.toggle
          data:
          target:
            entity_id: script.soundbar_power_toggle
        entity: input_button.tv_remote_button
        fill_container: True
        primary_info: none
        secondary_info: none
        layout: horizontal
        icon: mdi:power
        icon_color: red
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_source
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: SOURCE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_up
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-up-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_mute
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MUTE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_left
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-left-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_ok
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:circle
            icon_color: light-green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_right
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-right-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_menu
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MENU
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-down-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_menu
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: BACK
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_mode
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MODE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_dolby_atmos
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:dolby
            icon_color: light-blue
            name: DOLBY ATMOS
            icon_type: icon
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_sound
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: SOUND
            icon_type: none

` 
### View: DNA-Remote

Path: $(@{theme=Backend-selected; title=DNA-Remote; path=dna-remote; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: grid

![View Screenshot](assets/images/view_dna-remote.png)

`yaml
theme: Backend-selected
title: DNA-Remote
path: dna-remote
badges:
cards:
  -
    square: False
    columns: 1
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: DNA TV HUB
        alignment: center
        subtitle: 
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: custom:mushroom-entity-card
        tap_action:
          action: call-service
          service: script.toggle
          data:
          target:
            entity_id: script.soundbar_power_toggle
        entity: input_button.tv_remote_button
        fill_container: True
        primary_info: none
        secondary_info: none
        layout: horizontal
        icon: mdi:power
        icon_color: red
      -
        square: False
        columns: 3
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_source
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: SOURCE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_up
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-up-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_mute
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MUTE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_left
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-left-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_ok
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:circle
            icon_color: light-green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_right
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-right-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_menu
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MENU
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_down
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: none
            secondary_info: none
            layout: horizontal
            icon: mdi:arrow-down-bold
            icon_color: green
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_menu
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: BACK
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_mode
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: MODE
            icon_type: none
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_dolby_atmos
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:dolby
            icon_color: light-blue
            name: DOLBY ATMOS
            icon_type: icon
          -
            type: custom:mushroom-entity-card
            tap_action:
              action: call-service
              service: script.turn_on
              data:
              target:
                entity_id: script.soundbar_sound
            entity: input_button.tv_remote_button
            fill_container: True
            primary_info: name
            secondary_info: none
            layout: vertical
            icon: mdi:circle
            icon_color: green
            name: SOUND
            icon_type: none

` 

## Room-PopUps

**ID**: $Id | **URL**: /room-popups | **File**: $F`n
### View: Home

![View Screenshot](assets/images/view_.png)

`yaml
title: Home
cards:

` 
### View: car

Path: $(@{title=car; path=car; badges=System.Object[]; cards=System.Object[]}.path)`n
**Card Types**: vertical-stack

![View Screenshot](assets/images/view_car.png)

`yaml
title: car
path: car
badges:
cards:
  -
    type: vertical-stack
    cards:
      -
        type: custom:bubble-card
        card_type: pop-up
        hash: #car
      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Car-BG-vertical.png
        state_filter:
          home: brightness(100%) contrast(85%)
          away: brightness(25%)
        elements:
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            show_name: False
            show_icon: False
            tap_action:
              action: navigate
              navigation_path: /room-popups/car/#car
            hold_action:
              action: toggle
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 9
            styles:
              card:
                -
                  border-radius: 0px
                -
                  height: 100%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px
          -
            type: custom:button-card
            name: CAR
            style:
              top: 0%
              left: 50%
              width: 102%
              height: 0px
              z-index: 7
            styles:
              name:
                -
                  font-family: verdana
                -
                  font-size: 11px
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: center
                -
                  padding-left: 0px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 4px rgb(0,0,0,5)
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0.3)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:mushroom-chips-card
            chips:
              -
                type: template
                entity: device_tracker.xpb_358_device_tracker
                content: 
                icon: {% if is_state(config.entity,'home') %}
  mdi:home
{% else %}
  mdi:home-export-outline
{% endif %}

                icon_color: {% if is_state(config.entity,'home') %}
  green
{% else %}
  gray
{% endif %}

                card_mod:
                  style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index:8
}

            alignment: left
            style:
              top: 46%
              left: 50%
              width: 100%
              height: 100%
              border: 0px
              z-index: 8
            card_mod:
              style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

          -
            type: image
            image: local/car/Mercedes-Benz-GLC-BG-960x444.png
            style:
              name: GLC
              left: 50%
              top: 45%
              width: 90%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: custom:button-card
            name: Electric
            show_name: True
            icon: mdi:flash
            show_icon: False
            style:
              top: 22%
              left: 13.3%
              width: 25%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 75%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_state_of_charge
            name: Battery Status
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              left: 10.5%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_electric
            name: Range Electric
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              left: 11%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            name: Fuel
            show_name: True
            icon: mdi:gas-station
            show_icon: False
            style:
              top: 22%
              right: -19%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 70%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_fuel_level
            name: Fuel Level
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              right: -9%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_liquid
            name: Fuel Range
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              right: -6%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: lock.xpb_358_lock
            name: Doors
            show_name: False
            icon: mdi:lock
            style:
              bottom: 35px
              left: 13%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: unlocked
                icon: mdi:lock-open-outline
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
                    -
                      animation: blink 1s ease infinite
              -
                value: locked
                icon: mdi:lock
                styles:
                  icon:
                    -
                      color: #21ff21
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_low_wash_water_warning
            name: Wash Water
            show_name: False
            icon: mdi:wiper-wash
            style:
              bottom: 35px
              left: 32%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            name: AC
            show_name: False
            icon: mdi:air-conditioner
            style:
              bottom: 35px
              left: 50%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_park_brake_status
            name: Engine
            show_name: False
            icon: mdi:car-brake-parking
            style:
              bottom: 35px
              right: 12%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: red
          -
            type: custom:button-card
            entity: sensor.car_engine
            name: Engine
            show_name: False
            icon: mdi:engine
            style:
              bottom: 35px
              right: -5%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
}

      -
        type: custom:scheduler-card
        include:
          - switch.car_pre_entry_ac
        exclude:
        title: Schedules
        discover_existing: False
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
        show_header_toggle: False
      -
        type: map
        entities:
          -
            entity: person.car
        hours_to_show: 48
        aspect_ratio: 1.5
        default_zoom: 15
      -
        square: False
        type: grid
        cards:
          -
            type: custom:mushroom-entity-card
            entity: sensor.xpb_358_odometer
            name: Odometer
            tap_action:
              action: more-info
            hold_action:
              action: none
            double_tap_action:
              action: none
            layout: vertical
          -
            type: custom:mushroom-entity-card
            entity: sensor.xpb_358_distance_reset
            layout: vertical
            fill_container: False
            name: Distance
          -
            type: custom:mushroom-entity-card
            entity: sensor.xpb_358_distance_zero_emission_reset
            layout: vertical
            name: Zero-emission
            icon_color: green

` 

## Demo

**ID**: $Id | **URL**: /dashboard-demo | **File**: $F`n
### View: Home

![View Screenshot](assets/images/view_.png)

`yaml
title: Home
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        subtitle: AREAS
        alignment: center
      -
        square: False
        type: grid
        cards:
          -
            type: picture-elements
            entity: camera.g4_doorbell_pro_poe_high_resolution_channel
            camera_image: camera.g4_doorbell_pro_poe_high_resolution_channel
            camera_view: live
            aspect_ratio: 75%
            elements:
              -
                type: custom:button-card
                entity: binary_sensor.frontdoor_ceiling_frigate_person_occupancy
                icon: mdi:account-circle
                show_name: False
                show_icon: True
                tap_action:
                  action: none
                hold_action:
                  action: none
                style:
                  top: 50%
                  left: 50%
                  width: 140%
                  height: 115%
                  z-index: 8
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
                  icon:
                    -
                      display: none
                    -
                      height: 12%
                    -
                      top: 2.5%
                    -
                      left: 0%
                state:
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: lightgreen
                        -
                          display: box
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: gray
                        -
                          display: box
              -
                type: custom:button-card
                entity: sensor.backyard_temperature
                name: Backyard Temp
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 8
                  container-type: inline-size
                  position: absolute
                styles:
                  card:
                    -
                      position: absolute
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                  state:
                    -
                      position: absolute
                    -
                      top: 9px
                    -
                      right: 3%
                    -
                      color: #ffffff
                    -
                      font-weight: bold
                    -
                      font-size: 5cqw
              -
                type: custom:button-card
                entity: light.front_door_rail_light
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/front-door
                hold_action:
                  action: toggle
                double_tap_action:
                  action: call-service
                  service: lock.unlock
                  data:
                    entity_id: lock.front_door_lock
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Front Door
                style:
                  top: 0%
                  left: 50%
                  width: 102%
                  height: 0px
                  z-index: 7
                  container-type: inline-size
                styles:
                  name:
                    -
                      font-family: verdana
                    -
                      font-size: 6cqw
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: center
                    -
                      padding-left: 0px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 4px rgb(0,0,0,5)
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0.3)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: lock.front_door
                icon: mdi:lock
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: locked
                    styles:
                      icon:
                        -
                          width: 20px
                          color: #21ff21
                  -
                    operator: ==
                    value: unlocked
                    styles:
                      icon:
                        -
                          width: 20px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 35px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_battery
                icon: mdi:lock
                tap_action:
                  action: more-info
                show_icon: False
                show_name: False
                show_state: True
                show_label: False
                layout: vertical
                state:
                  -
                    operator: >
                    value: 25
                    styles:
                      state:
                        -
                          color: #21ff21
                          display: none
                  -
                    operator: >=
                    value: 0
                    styles:
                      state:
                        -
                          animation: blink 1s ease infinite
                          font-weight: bold
                style:
                  bottom: 34px
                  height: 0px
                  left: 60px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_keypad_battery
                icon: mdi:dialpad
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: >
                    value: 50
                    styles:
                      icon:
                        -
                          width: 20px
                          color: rgba(253,89,89,0)
                  -
                    operator: >
                    value: 35
                    styles:
                      icon:
                        -
                          width: 20px
                          color: orange
                  -
                    operator: >=
                    value: 0
                    styles:
                      icon:
                        -
                          width: 20px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 64px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_keypad_battery
                icon: mdi:dialpad
                tap_action:
                  action: more-info
                show_icon: False
                show_name: False
                show_state: True
                show_label: False
                layout: default
                state:
                  -
                    operator: >
                    value: 50
                    styles:
                      state:
                        -
                          color: #21ff21
                          display: none
                  -
                    operator: >=
                    value: 0
                    styles:
                      state:
                        -
                          animation: blink 1s ease infinite
                          font-weight: bold
                style:
                  bottom: 64px
                  height: 0px
                  left: 55px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 50px
                    -
                      color: rgba(255,255,255,1)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 80px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: light.front_door_rail_light
                icon: mdi:lightbulb
                tap_action:
                  action: none
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 20px
                          color: yellow
                style:
                  bottom: 35px
                  height: 0px
                  left: 50%
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: binary_sensor.front_door_sensor_contact
                icon: mdi:door
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 22px
                          color: #21ff21
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 22px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 35px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 22px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
}

          -
            type: picture-elements
            entity: device_tracker.xpb_358_device_tracker
            image: local/car/Car-BG-vertical.png
            state_filter:
              home: brightness(100%) contrast(85%)
              away: brightness(25%)
            elements:
              -
                type: custom:button-card
                entity: switch.car_pre_entry_ac
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-persons/car
                double_tap_action:
                  action: fire-dom-event
                  browser_mod:
                    service: browser_mod.popup
                    data:
                      title: CAR
                      content:
                        type: vertical-stack
                        cards:
                          -
                            type: custom:scheduler-card
                            include:
                              - switch.car_pre_entry_ac
                            exclude:
                            title: Schedules
                            discover_existing: False
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
                            show_header_toggle: False
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: CAR
                style:
                  top: 0%
                  left: 50%
                  width: 102%
                  height: 0px
                  z-index: 2
                  container-type: inline-size
                styles:
                  name:
                    -
                      font-family: verdana
                    -
                      font-size: 6cqw
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: center
                    -
                      padding-left: 0px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 4px rgb(0,0,0,5)
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0.3)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: device_tracker.xpb_358_device_tracker
                    content: 
                    icon: {% if is_state(config.entity,'home') %}
  mdi:home
{% else %}
  mdi:home-export-outline
{% endif %}

                    icon_color: {% if is_state(config.entity,'home') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 2;
}

                alignment: left
                style:
                  top: 46%
                  left: 50%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: switch.schedule_898e47
                    content: 
                    icon: {% if is_state(config.entity,'on') %}
  mdi:clock-check
{% else %}
  mdi:clock-remove-outline
{% endif %}

                    icon_color: {% if is_state(config.entity,'on') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
  background: rgba(0,0,0,0);
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 8;
}

                alignment: left
                style:
                  top: 46%
                  left: 130%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
  background: rgba(0,0,0,0);
}

              -
                type: image
                image: local/car/Mercedes-Benz-GLC-BG-960x444.png
                style:
                  name: GLC
                  left: 50%
                  top: 45%
                  width: 90%
              -
                type: conditional
                conditions:
                  -
                    entity: sensor.car_charge_plug
                    state: on
                elements:
                  -
                    type: image
                    image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                    style:
                      left: 50%
                      top: 45%
                      width: 90%
                      animation: blink 1s ease infinite
                      opacity: 100%
              -
                type: custom:button-card
                name: Electric
                show_name: True
                icon: mdi:flash
                show_icon: False
                style:
                  top: 22%
                  left: 13.3%
                  width: 25%
                  height: 0px
                  z-index: 7
                styles:
                  card:
                    -
                      font-size: 75%
                    -
                      font-weight: bold
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_state_of_charge
                name: Battery Status
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 32%
                  left: 10.5%
                  width: 30%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: #21ff21
                    -
                      font-weight: bold
                    -
                      font-size: 60%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_range_electric
                name: Range Electric
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 42%
                  left: 11%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: orange
                    -
                      font-weight: bold
                    -
                      font-size: 55%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                name: Fuel
                show_name: True
                icon: mdi:gas-station
                show_icon: False
                style:
                  top: 22%
                  right: -19%
                  width: 30%
                  height: 0px
                  z-index: 7
                styles:
                  card:
                    -
                      font-size: 70%
                    -
                      font-weight: bold
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_fuel_level
                name: Fuel Level
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 32%
                  right: -9%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: #21ff21
                    -
                      font-weight: bold
                    -
                      font-size: 60%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_range_liquid
                name: Fuel Range
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 42%
                  right: -6%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: orange
                    -
                      font-weight: bold
                    -
                      font-size: 55%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: lock.xpb_358_lock
                name: Doors
                show_name: False
                icon: mdi:lock
                style:
                  bottom: 35px
                  left: 13%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: unlocked
                    icon: mdi:lock-open-outline
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                        -
                          animation: blink 1s ease infinite
                  -
                    value: locked
                    icon: mdi:lock
                    styles:
                      icon:
                        -
                          color: #21ff21
              -
                type: custom:button-card
                entity: binary_sensor.xpb_358_low_wash_water_warning
                name: Wash Water
                show_name: False
                icon: mdi:wiper-wash
                style:
                  bottom: 35px
                  left: 32%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
              -
                type: custom:button-card
                entity: switch.car_pre_entry_ac
                name: AC
                show_name: False
                icon: mdi:air-conditioner
                style:
                  bottom: 35px
                  left: 50%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
              -
                type: custom:button-card
                entity: binary_sensor.xpb_358_park_brake_status
                name: Engine
                show_name: False
                icon: mdi:car-brake-parking
                style:
                  bottom: 35px
                  right: 12%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: red
              -
                type: custom:button-card
                entity: sensor.car_engine
                name: Engine
                show_name: False
                icon: mdi:engine
                style:
                  bottom: 35px
                  right: -5%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgba(0,0,0,0);
  z-index: 0;
  border: 0px;
}

        columns: 2
      -
        square: False
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: area_card_new
            variables:
              -
                entity_name: bedroom
              -
                display_name: BEDROOM
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                device_1: cover.bedroom_window_blinds
              -
                device_1_icon: mdi:window-shutter
              -
                device_1_state: open
              -
                device_1_color: green
              -
                device_1_animation: none
              -
                device_2: cover.bedroom_window_roller_cover
              -
                device_2_icon: mdi:blinds-open
              -
                device_2_state: open
              -
                device_2_color: green
              -
                device_2_animation: none
              -
                device_3: input_boolean.bed_jukka_occupancy
              -
                device_3_icon: mdi:bed
              -
                device_3_state: on
              -
                device_3_color: blue
              -
                device_3_animation: none
              -
                device_4: input_boolean.bed_piia_occupancy
              -
                device_4_icon: mdi:bed
              -
                device_4_state: on
              -
                device_4_color: pink
              -
                device_4_animation: none
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: office
              -
                display_name: OFFICE
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                device_1: switch.office_pc_power
              -
                device_1_icon: mdi:desktop-classic
              -
                device_1_color: green
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: switch.unraid_power_toggle
              -
                device_6: sensor.ender_5_pro_current_state
              -
                device_6_icon: mdi:printer-3d
              -
                device_6_state: Printing
              -
                device_6_color: orange
              -
                device_6_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: elias
              -
                display_name: Study
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: anton
              -
                display_name: Guest Room
              -
                temperature_sensor: sensor.anton_temperature
              -
                device_1: media_player.anton_spot
              -
                device_1_icon: speaker
              -
                device_1_state: playing
              -
                device_1_color: green
              -
                device_1_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: alisa
              -
                display_name: Guest Room
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: living_room
              -
                display_name: Living Room
              -
                temperature_sensor: sensor.airthings_wave_temperature
              -
                device_1: media_player.70pus9005_12_2
              -
                device_1_icon: mdi:television
              -
                device_1_color: green
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: binary_sensor.backyard_door_sensor_contact
              -
                device_2_icon: mdi:door
              -
                device_2_color: red
              -
                device_2_state: on
              -
                device_2_animation: blink
              -
                device_3: fan.philips_air_purifier
              -
                device_3_icon: mdi:air-filter
              -
                device_3_state: on
              -
                device_3_color: green
              -
                device_3_animation: none
              -
                device_6: light.fireplace
              -
                device_6_icon: mdi:fireplace
              -
                device_6_state: on
              -
                device_6_color: orange
              -
                device_6_animation: none
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: kitchen
              -
                display_name: Kitchen
              -
                temperature_sensor: sensor.airthings_wave_temperature
              -
                device_1: binary_sensor.kitchen_fridge_door_contact
              -
                device_1_icon: mdi:fridge
              -
                device_1_state: on
              -
                device_1_color: red
              -
                device_1_animation: blink
              -
                device_2: sensor.coffee_machine_state
              -
                device_2_icon: mdi:coffee
              -
                device_2_state: Running
              -
                device_2_color: orange
              -
                device_2_animation: none
              -
                device_3: sensor.dishwasher_state
              -
                device_3_icon: mdi:dishwasher
              -
                device_3_state: Running
              -
                device_3_color: blue
              -
                device_3_animation: none
              -
                device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
              -
                device_4_icon: mdi:dishwasher-alert
              -
                device_4_state: on
              -
                device_4_color: red
              -
                device_4_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: hallway
              -
                display_name: Hallway
              -
                temperature_sensor: sensor.airthings_wave_temperature
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: bathroom
              -
                display_name: Bathroom
              -
                device_1: sensor.washing_machine_status
              -
                device_1_icon: mdi:washing-machine
              -
                device_1_state: Running
              -
                device_1_color: blue
              -
                device_1_animation: none
              -
                device_2: input_boolean.bathroom_toilet_occupancy
              -
                device_2_icon: mdi:toilet
              -
                device_2_state: on
              -
                device_2_color: orange
              -
                device_2_animation: blink
              -
                device_3: input_boolean.bathroom_shower_occupancy
              -
                device_3_icon: mdi:shower-head
              -
                device_3_state: on
              -
                device_3_color: blue
              -
                device_3_animation: blink
              -
                device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
              -
                device_4_icon: mdi:dishwasher-alert
              -
                device_4_state: on
              -
                device_4_color: red
              -
                device_4_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: sauna
              -
                display_name: Sauna
              -
                temperature_sensor: sensor.ruuvitag_8572_temperature
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: mud_room
              -
                display_name: Mud Room
              -
                temperature_sensor: sensor.mud_room_motion_sensor_temperature
              -
                device_1: binary_sensor.front_door_sensor_contact
              -
                device_1_icon: mdi:door
              -
                device_1_state: on
              -
                device_1_color: red
              -
                device_1_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: toilet
              -
                display_name: Toilet
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: stairs
              -
                display_name: Stairs
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: lobby
              -
                display_name: Lobby
        columns: 2
      -
        square: False
        type: grid
        cards:
          -
            type: picture-elements
            entity: camera.backyard_frigate
            camera_image: camera.backyard_frigate
            camera_view: live
            aspect_ratio: 57%
            elements:
              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: binary_sensor.backyard_frigate_person_occupancy
                    content: 
                    icon: mdi:account-circle
                    icon_color: {% if is_state(config.entity,'on') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index:8
}

                alignment: left
                style:
                  top: 46%
                  left: 50%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                  container-type: inline-size
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

              -
                type: custom:button-card
                entity: sensor.backyard_temperature
                name: Backyard Temp
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 8
                  container-type: inline-size
                  position: absolute
                styles:
                  card:
                    -
                      position: absolute
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                  state:
                    -
                      position: absolute
                    -
                      top: 9px
                    -
                      right: 3%
                    -
                      color: #ffffff
                    -
                      font-weight: bold
                    -
                      font-size: 5cqw
              -
                type: custom:button-card
                entity: light.backyard_plug
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/backyard
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                  container-type: inline-size
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Backyard
                style:
                  top: 0%
                  left: 50%
                  width: 102%
                  height: 0px
                  z-index: 7
                  container-type: inline-size
                styles:
                  name:
                    -
                      font-family: verdana
                    -
                      font-size: 6cqw
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: center
                    -
                      padding-left: 0px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 4px rgb(0,0,0,5)
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0.3)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: binary_sensor.backyard_door_sensor_contact
                icon: mdi:door
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 24px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 24px
                          color: #21ff21
                style:
                  bottom: 35px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 24px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1))
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: binary_sensor.backyard_door_sensor_moving
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 26px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 26px
                          color: rgba(155,245,66,0)
                style:
                  bottom: 43px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 26px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1))
                  card:
                    -
                      width: 40px
                    -
                      height: 48px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: light.backyard_plug
                icon: mdi:lightbulb
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 20px
                          color: yellow
                  -
                    operator: ==
                    value: off
                    icon: mdi:lightbulb-outline
                    styles:
                      icon:
                        -
                          width: 20px
                          color: rgba(255,255,255,1)
                style:
                  bottom: 35px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  height: 100%
  container-type: inline-size
}

          -
            type: picture-elements
            entity: camera.storage_frigate
            camera_image: camera.storage_frigate
            camera_view: live
            aspect_ratio: 56%
            elements:
              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: binary_sensor.storage_frigate_person_occupancy
                    content: 
                    icon: mdi:account-circle
                    icon_color: {% if is_state(config.entity,'on') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index:8
}

                alignment: left
                style:
                  top: 46%
                  left: 50%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

              -
                type: custom:button-card
                entity: light.backyard_plug
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/storage
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Storage
                style:
                  top: 0%
                  left: 50%
                  width: 102%
                  height: 0px
                  z-index: 7
                  container-type: inline-size
                styles:
                  name:
                    -
                      font-family: verdana
                    -
                      font-size: 6cqw
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: center
                    -
                      padding-left: 0px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 4px rgb(0,0,0,5)
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0.3)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
}

        columns: 2
  -
    type: grid
    cards:
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: WEATHER
            alignment: center
          -
            show_current: True
            show_forecast: True
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
                      -
                        type: weather-forecast
                        entity: weather.openweathermap
                        show_current: True
                        show_forecast: True
                        forecast_type: hourly
                      -
                        type: entities
                        entities:
                          -
                            entity: sensor.openweathermap_feels_like_temperature
                            name: Feels Like
                          -
                            entity: sensor.openweathermap_wind_speed
                            name: Wind
                          -
                            entity: sensor.backyard_humidity
                            name: Backyard Humidity
                          -
                            entity: sensor.backyard_temperature
                            name: Backyard Temperature
                      -
                        type: weather-forecast
                        show_current: False
                        show_forecast: True
                        entity: weather.forecast_home
                        forecast_type: daily
                        name: Forecast
                      -
                        type: custom:horizon-card
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: ENERGY
            alignment: center
          -
            square: False
            columns: 1
            type: grid
            cards:
              -
                type: custom:config-template-card
                variables:
                  PRICEAVERAGE: states['sensor.nordpool_kwh_fi_eur_3_10_024'].attributes['average']
                  PRICEMEAN: states['sensor.nordpool_kwh_fi_eur_3_10_024'].attributes['mean']
                  PRICEHIGH: states['sensor.nordpool_today_mean_hi_limit'].state
                  PRICELOW: states['sensor.nordpool_today_mean_lo_limit'].state
                entities:
                  - sensor.nordpool_kwh_eur_without_tax
                card:
                  type: custom:apexcharts-card
                  graph_span: 1d
                  span:
                    start: day
                  apex_config:
                    stroke:
                      dashArray: 4
                    chart:
                      height: 180px
                      width: 115%
                      offsetX: -30
                    title:
                      text: Energy Price Today
                      align: center
                      offsetY: 10
                      style:
                        fontSize: 13px
                        fontFamily: Verdana
                        fontWeight: normal
                    grid:
                      show: True
                      borderColor: rgba(255,255,255,0.2)
                    xaxis:
                      position: bottom
                      labels:
                        format: H
                        hideOverlappingLabels: True
                        offsetX: 0
                      axisTicks:
                        offsetX: 0
                    legend:
                      show: False
                      itemMargin:
                        vertical: 10
                        horizontal: 10
                    tooltip:
                      enabled: False
                      style:
                        fontSize: 14px
                  show:
                    last_updated: True
                  experimental:
                    color_threshold: True
                  header:
                    show_states: True
                    colorize_states: True
                  now:
                    show: True
                  yaxis:
                    -
                      id: cost
                      opposite: True
                      decimals: 1
                      apex_config:
                        tickAmount: 4
                        labels:
                          show: True
                        title:
                          text: c/kWh
                          rotate: 0
                          offsetX: -25
                          offsetY: -70
                          style:
                            fontSize: 10px
                            fontFamily: verdana
                            color: orange
                    -
                      id: energy
                      max: ~2
                      min: 0
                      decimals: 1
                      apex_config:
                        tickAmount: 4
                        labels:
                          show: True
                        title:
                          text: kWh
                          rotate: 0
                          offsetX: 25
                          offsetY: -70
                          style:
                            color: skyblue
                            fontSize: 10px
                            fontFamily: verdana
                  series:
                    -
                      entity: sensor.nordpool_kwh_fi_eur_3_10_024
                      name: Price
                      yaxis_id: cost
                      type: column
                      opacity: 0.8
                      stroke_width: 0
                      show:
                        extremas: True
                        in_header: raw
                        header_color_threshold: True
                      data_generator: return entity.attributes.raw_today.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
});

                      color_threshold:
                        -
                          value: 1
                          color: lightgreen
                        -
                          value: ${PRICELOW * 1}
                          color: orange
                        -
                          value: ${PRICEHIGH * 1}
                          color: darkred
                    -
                      entity: sensor.home_total_energy_hourly
                      name: Energy (kWh)
                      color: skyblue
                      type: line
                      opacity: 1
                      yaxis_id: energy
                      stroke_width: 2
                      float_precision: 1
                      extend_to: False
                      unit: kWh
                      group_by:
                        duration: 1hour
                        func: max
                      show:
                        legend_value: False
                        datalabels: False
          -
            square: False
            type: grid
            cards:
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-template-card
                    primary: {{ states(entity) | float(0) | round(2) }}
                    secondary: c/kWh
                    icon: mdi:currency-eur
                    icon_color: {% set mean_hi = states('sensor.nordpool_today_mean_hi_limit') | float(0) %}
{% set mean_lo = states('sensor.nordpool_today_mean_lo_limit') | float(0) %}
{% set price = state_attr(config.entity, 'current_price') | float(0) %}
{% if price > mean_hi %}
  red
{% elif price < mean_lo %}
  green
{% else %}
  orange
{% endif %}
                    badge_icon: 
                    badge_color: 

                    entity: sensor.nordpool_kwh_fi_eur_3_10_024
                    layout: vertical
                    fill_container: True
                    tap_action:
                      action: more-info
                    hold_action:
                      action: none
                    double_tap_action:
                      action: none
                  -
                    type: custom:mushroom-template-card
                    primary: {{ states(entity) | float(0) | round(0) }}
                    secondary: W
                    icon: mdi:flash
                    icon_color: blue
                    entity: sensor.home_total_power
                    layout: vertical
                    badge_color: 
                    fill_container: True
                    tap_action:
                      action: more-info
                    hold_action:
                      action: none
                    double_tap_action:
                      action: none
                columns: 2
            columns: 2
          -
            type: conditional
            conditions:
              -
                entity: sensor.nordpool_tomorrow
                state: True
            card:
              type: custom:apexcharts-card
              graph_span: 1d
              span:
                start: day
                offset: +1d
              apex_config:
                chart:
                  height: 180px
                title:
                  text: Price Tomorrow (c/kWh)
                  align: center
                  offsetY: 10
                  style:
                    fontSize: 13px
                    fontFamily: Verdana
                    fontWeight: normal
                grid:
                  show: True
                  borderColor: rgba(255,255,255,0.2)
                xaxis:
                  position: bottom
                  labels:
                    format: H
                    hideOverlappingLabels: True
                    offsetX: 0
                  axisTicks:
                    offsetX: 0
                legend:
                  show: False
                  itemMargin:
                    vertical: 10
                    horizontal: 10
                tooltip:
                  enabled: False
                  style:
                    fontSize: 14px
              show:
                last_updated: True
              experimental:
                color_threshold: True
              header:
                show_states: True
                colorize_states: True
              now:
                show: True
              yaxis:
                -
                  id: cost
                  opposite: True
                  decimals: 1
                  apex_config:
                    tickAmount: 3
                    labels:
                      show: True
              series:
                -
                  entity: sensor.nordpool_kwh_fi_eur_3_10_024
                  name: Price
                  yaxis_id: cost
                  type: column
                  opacity: 0.9
                  stroke_width: 0
                  show:
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
                  data_generator: return entity.attributes.raw_tomorrow.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_tomorrow[index]["value"]];
});

          -
            type: custom:apexcharts-card
            graph_span: 7d
            update_interval: 15min
            apex_config:
              fill:
                opacity: 0.5
              markers:
                size: 3
              xaxis:
                showDuplicates: True
                position: bottom
                labels:
                  format: ddd
                  hideOverlappingLabels: False
              chart:
                height: 180px
              grid:
                show: True
                borderColor: rgba(255,255,255,0.2)
              legend:
                show: True
                itemMargin:
                  vertical: 10
                  horizontal: 10
              dataLabels:
                enabled: True
                position: top
                offsetY: -8
                background:
                  enabled: False
              tooltip:
                style:
                  fontSize: 14px
              stroke:
                dashArray: 0
              title:
                text: Energy Daily
                align: center
                offsetY: 10
                style:
                  fontSize: 13px
                  fontFamily: Verdana
                  fontWeight: normal
            header:
              show: False
            yaxis:
              -
                id: cost
                max: ~100
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 4
                  labels:
                    show: True
              -
                id: power
                opposite: True
                max: ~35
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 7
                  labels:
                    show: True
            series:
              -
                entity: sensor.home_total_energy_daily
                name: Energy (kWh)
                color: skyblue
                type: column
                yaxis_id: power
                stroke_width: 1
                float_precision: 1
                unit: kWh
                statistics:
                  type: state
                group_by:
                  duration: 1day
                  func: max
                show:
                  legend_value: False
                  datalabels: True
      -
        type: custom:config-template-card
        variables:
          PRICEAVERAGE: states['sensor.nordpool_kwh_fi_eur'].attributes['average']
          PRICEMEAN: states['sensor.nordpool_kwh_fi_eur'].attributes['mean']
          PRICEHIGH: states['sensor.nordpool_today_mean_hi_limit'].state
          PRICELOW: states['sensor.nordpool_today_mean_lo_limit'].state
        entities:
          - sensor.nordpool_kwh_fi_eur
        card:
          type: custom:apexcharts-card
          graph_span: 1d
          span:
            start: day
          apex_config:
            stroke:
              dashArray: 4
            chart:
              height: 180px
              width: 115%
              offsetX: -30
            title:
              text: Energy Price Today
              align: center
              offsetY: 10
              style:
                fontSize: 13px
                fontFamily: Verdana
                fontWeight: normal
            grid:
              show: True
              borderColor: rgba(255,255,255,0.2)
            xaxis:
              position: bottom
              labels:
                format: H
                hideOverlappingLabels: True
                offsetX: 0
              axisTicks:
                offsetX: 0
            legend:
              show: False
              itemMargin:
                vertical: 10
                horizontal: 10
            tooltip:
              enabled: False
              style:
                fontSize: 14px
          show:
            last_updated: True
          experimental:
            color_threshold: True
          header:
            show_states: True
            colorize_states: True
          now:
            show: True
          yaxis:
            -
              id: cost
              opposite: True
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: c/kWh
                  rotate: 0
                  offsetX: -25
                  offsetY: -70
                  style:
                    fontSize: 10px
                    fontFamily: verdana
                    color: orange
            -
              id: energy
              max: ~2
              min: 0
              decimals: 1
              apex_config:
                tickAmount: 4
                labels:
                  show: True
                title:
                  text: kWh
                  rotate: 0
                  offsetX: 25
                  offsetY: -70
                  style:
                    color: skyblue
                    fontSize: 10px
                    fontFamily: verdana
          series:
            -
              entity: sensor.nordpool_kwh_fi_eur
              name: Price
              yaxis_id: cost
              type: column
              opacity: 0.8
              stroke_width: 0
              show:
                extremas: True
                in_header: raw
                header_color_threshold: True
              data_generator: return entity.attributes.raw_today.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
});

              color_threshold:
                -
                  value: 1
                  color: lightgreen
                -
                  value: ${PRICELOW * 1}
                  color: orange
                -
                  value: ${PRICEHIGH * 1}
                  color: darkred
            -
              entity: sensor.home_total_energy_hourly
              name: Energy (kWh)
              color: skyblue
              type: line
              opacity: 1
              yaxis_id: energy
              stroke_width: 2
              float_precision: 1
              extend_to: False
              unit: kWh
              group_by:
                duration: 1hour
                func: max
              show:
                legend_value: False
                datalabels: False
      -
        type: custom:apexcharts-card
        graph_span: 24h
        header:
          title: Energy price today (snt/kWh)
          show: True
        span:
          start: day
        now:
          show: True
          label: Now
        series:
          -
            entity: sensor.nordpool_kwh_fi_eur
            type: column
            data_generator: return entity.attributes.raw_today.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
});

  -
    type: grid
    cards:
      -
        type: custom:weather-chart-card
        entity: weather.forecast_home
        show_main: True
        show_temperature: True
        show_current_condition: True
        show_attributes: True
        show_time: False
        show_time_seconds: False
        show_day: False
        show_date: False
        show_humidity: True
        show_pressure: True
        show_wind_direction: True
        show_wind_speed: True
        show_sun: True
        show_feels_like: False
        show_dew_point: False
        show_wind_gust_speed: False
        show_visibility: False
        show_last_changed: False
        use_12hour_format: False
        icons_size: 40
        animated_icons: True
        icon_style: style1
        autoscroll: False
        forecast:
          precipitation_type: rainfall
          show_probability: False
          labels_font_size: 11
          precip_bar_size: 100
          style: style2
          show_wind_forecast: True
          condition_icons: True
          round_temp: False
          type: hourly
          number_of_forecasts: 0
          disable_animation: False
          chart_height: 150
        units:
          speed: m/s
      -
        type: custom:weather-chart-card
        entity: weather.openweathermap
        show_main: False
        show_temperature: True
        show_current_condition: True
        show_attributes: False
        show_time: False
        show_time_seconds: False
        show_day: False
        show_date: False
        show_humidity: True
        show_pressure: False
        show_wind_direction: False
        show_wind_speed: True
        show_sun: True
        show_feels_like: True
        show_dew_point: False
        show_wind_gust_speed: False
        show_visibility: False
        show_last_changed: False
        use_12hour_format: False
        icons_size: 40
        animated_icons: True
        icon_style: style1
        autoscroll: False
        forecast:
          precipitation_type: rainfall
          show_probability: True
          labels_font_size: 11
          precip_bar_size: 50
          style: style2
          show_wind_forecast: True
          condition_icons: True
          round_temp: True
          type: daily
          number_of_forecasts: 0
          disable_animation: False
          chart_height: 150
        units:
          speed: m/s
        locale: 
        current_temp_size: 24
    column_span: 1
cards:

` 
### View: Security

Path: $(@{type=sections; max_columns=5; path=security; title=Security; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_security.png)

`yaml
type: sections
max_columns: 5
path: security
title: Security
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: Front Porch
        heading_style: title
      -
        type: custom:frigate-card
        cameras:
          -
            camera_entity: camera.front_porch_frigate
        live:
          preload: True
        status_bar:
        menu:
          style: outside
          position: bottom
          alignment: left
          buttons:
            frigate:
              enabled: False
            live:
              enabled: True
            snapshots:
              permanent: False
            recordings:
              enabled: True
            image:
              enabled: False
  -
    type: grid
    cards:
      -
        type: heading
        heading: Backyard
        heading_style: title
      -
        type: custom:frigate-card
        cameras:
          -
            camera_entity: camera.g5_turret_ultra_high_resolution_channel

` 

## Map

**ID**: $Id | **URL**: /map | **File**: $F`n

## DEV

**ID**: $Id | **URL**: /dashboard-dev2 | **File**: $F`n
### View: Home

![View Screenshot](assets/images/view_.png)

`yaml
title: Home
type: sections
max_columns: 4
icon: mdi:home
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: HOME
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: True
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: jukka
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: piia
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: anton
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: elias
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: alisa
        layout_options:
          grid_columns: full
          grid_rows: auto
        columns: 5
      -
        type: custom:mushroom-title-card
        title: 
        alignment: center
        subtitle: AREAS
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        square: False
        type: grid
        cards:
          -
            type: picture-elements
            entity: camera.frontdoor_ceiling_frigate
            camera_image: camera.frontdoor_ceiling_frigate
            camera_view: live
            aspect_ratio: 75%
            elements:
              -
                type: custom:button-card
                entity: sensor.backyard_temperature
                name: Backyard Temp
                show_name: False
                icon: mdi:thermometer
                show_icon: False
                show_state: True
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 2
                  container-type: inline-size
                  position: absolute
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 18%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                    -
                      font-size: 5cqw
                  state:
                    -
                      font-size: 5cqw
                    -
                      font-weight: bold
                    -
                      justify-self: right
                    -
                      padding-right: 15px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 5px rgb(0,0,0,1)
              -
                type: custom:button-card
                entity: light.front_door_rail_light
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/front-door
                hold_action:
                  action: toggle
                double_tap_action:
                  action: call-service
                  service: lock.unlock
                  data:
                    entity_id: lock.front_door_lock
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Front Door
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 2
                  container-type: inline-size
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 18%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                    -
                      font-size: 5cqw
                  name:
                    -
                      font-family: arial
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: left
                    -
                      padding-left: 15px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 5px rgb(0,0,0,1)
              -
                type: custom:button-card
                entity: lock.front_door_lock
                icon: mdi:lock
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: locked
                    styles:
                      icon:
                        -
                          width: 20px
                          color: #21ff21
                  -
                    operator: ==
                    value: unlocked
                    styles:
                      icon:
                        -
                          width: 20px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 35px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_lock_battery
                icon: mdi:lock
                tap_action:
                  action: more-info
                show_icon: False
                show_name: False
                show_state: True
                show_label: False
                layout: vertical
                state:
                  -
                    operator: >
                    value: 25
                    styles:
                      state:
                        -
                          color: #21ff21
                          display: none
                  -
                    operator: >=
                    value: 0
                    styles:
                      state:
                        -
                          animation: blink 1s ease infinite
                          font-weight: bold
                style:
                  bottom: 34px
                  height: 0px
                  left: 60px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_lock_keypad_battery
                icon: mdi:dialpad
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: >
                    value: 50
                    styles:
                      icon:
                        -
                          width: 20px
                          color: rgba(253,89,89,0)
                  -
                    operator: >
                    value: 35
                    styles:
                      icon:
                        -
                          width: 20px
                          color: orange
                  -
                    operator: >=
                    value: 0
                    styles:
                      icon:
                        -
                          width: 20px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 64px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.front_door_lock_keypad_battery
                icon: mdi:dialpad
                tap_action:
                  action: more-info
                show_icon: False
                show_name: False
                show_state: True
                show_label: False
                layout: default
                state:
                  -
                    operator: >
                    value: 50
                    styles:
                      state:
                        -
                          color: #21ff21
                          display: none
                  -
                    operator: >=
                    value: 0
                    styles:
                      state:
                        -
                          animation: blink 1s ease infinite
                          font-weight: bold
                style:
                  bottom: 64px
                  height: 0px
                  left: 55px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 50px
                    -
                      color: rgba(255,255,255,1)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 80px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: light.front_door_rail_light
                icon: mdi:lightbulb
                tap_action:
                  action: none
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 20px
                          color: yellow
                style:
                  bottom: 35px
                  height: 0px
                  left: 50%
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: binary_sensor.front_door_lock_door
                icon: mdi:door
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 22px
                          color: #21ff21
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 22px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                style:
                  bottom: 35px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 22px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  {% if is_state('select.front_door_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.front_door_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

          -
            type: picture-elements
            entity: device_tracker.xpb_358_device_tracker
            image: local/car/Car-BG-vertical.png
            state_filter:
              home: brightness(100%) contrast(85%)
              away: brightness(25%)
            elements:
              -
                type: custom:button-card
                entity: switch.car_pre_entry_ac
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /dashboard-persons/car
                double_tap_action:
                  action: fire-dom-event
                  browser_mod:
                    service: browser_mod.popup
                    data:
                      title: CAR
                      content:
                        type: vertical-stack
                        cards:
                          -
                            type: custom:scheduler-card
                            include:
                              - switch.car_pre_entry_ac
                            exclude:
                            title: Schedules
                            discover_existing: False
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
                            show_header_toggle: False
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 9
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: CAR
                style:
                  top: 0%
                  left: 50%
                  width: 102%
                  height: 0px
                  z-index: 2
                  container-type: inline-size
                styles:
                  name:
                    -
                      font-family: verdana
                    -
                      font-size: 6cqw
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: center
                    -
                      padding-left: 0px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 4px rgb(0,0,0,5)
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0.3)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: device_tracker.xpb_358_device_tracker
                    content: 
                    icon: {% if is_state(config.entity,'home') %}
  mdi:home
{% else %}
  mdi:home-export-outline
{% endif %}

                    icon_color: {% if is_state(config.entity,'home') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 2;
}

                alignment: left
                style:
                  top: 46%
                  left: 50%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

              -
                type: custom:mushroom-chips-card
                chips:
                  -
                    type: template
                    entity: switch.schedule_898e47
                    content: 
                    icon: {% if is_state(config.entity,'on') %}
  mdi:clock-check
{% else %}
  mdi:clock-remove-outline
{% endif %}

                    icon_color: {% if is_state(config.entity,'on') %}
  green
{% else %}
  gray
{% endif %}

                    card_mod:
                      style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
  background: rgba(0,0,0,0);
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 8;
}

                alignment: left
                style:
                  top: 46%
                  left: 130%
                  width: 100%
                  height: 100%
                  border: 0px
                  z-index: 8
                card_mod:
                  style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
  background: rgba(0,0,0,0);
}

              -
                type: image
                image: local/car/Mercedes-Benz-GLC-BG-960x444.png
                style:
                  name: GLC
                  left: 50%
                  top: 45%
                  width: 90%
              -
                type: conditional
                conditions:
                  -
                    entity: sensor.car_charge_plug
                    state: on
                elements:
                  -
                    type: image
                    image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                    style:
                      left: 50%
                      top: 45%
                      width: 90%
                      animation: blink 1s ease infinite
                      opacity: 100%
              -
                type: custom:button-card
                name: Electric
                show_name: True
                icon: mdi:flash
                show_icon: False
                style:
                  top: 22%
                  left: 13.3%
                  width: 25%
                  height: 0px
                  z-index: 7
                styles:
                  card:
                    -
                      font-size: 75%
                    -
                      font-weight: bold
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_state_of_charge
                name: Battery Status
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 32%
                  left: 10.5%
                  width: 30%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: #21ff21
                    -
                      font-weight: bold
                    -
                      font-size: 60%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_range_electric
                name: Range Electric
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 42%
                  left: 11%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: orange
                    -
                      font-weight: bold
                    -
                      font-size: 55%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                name: Fuel
                show_name: True
                icon: mdi:gas-station
                show_icon: False
                style:
                  top: 22%
                  right: -19%
                  width: 30%
                  height: 0px
                  z-index: 7
                styles:
                  card:
                    -
                      font-size: 70%
                    -
                      font-weight: bold
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_fuel_level
                name: Fuel Level
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 32%
                  right: -9%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: #21ff21
                    -
                      font-weight: bold
                    -
                      font-size: 60%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: sensor.xpb_358_range_liquid
                name: Fuel Range
                show_name: False
                icon: mdi:flash
                show_icon: False
                show_state: True
                style:
                  top: 42%
                  right: -6%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  state:
                    -
                      color: orange
                    -
                      font-weight: bold
                    -
                      font-size: 55%
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: lock.xpb_358_lock
                name: Doors
                show_name: False
                icon: mdi:lock
                style:
                  bottom: 35px
                  left: 13%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: unlocked
                    icon: mdi:lock-open-outline
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                        -
                          animation: blink 1s ease infinite
                  -
                    value: locked
                    icon: mdi:lock
                    styles:
                      icon:
                        -
                          color: #21ff21
              -
                type: custom:button-card
                entity: binary_sensor.xpb_358_low_wash_water_warning
                name: Wash Water
                show_name: False
                icon: mdi:wiper-wash
                style:
                  bottom: 35px
                  left: 32%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
              -
                type: custom:button-card
                entity: switch.car_pre_entry_ac
                name: AC
                show_name: False
                icon: mdi:air-conditioner
                style:
                  bottom: 35px
                  left: 50%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
              -
                type: custom:button-card
                entity: binary_sensor.xpb_358_park_brake_status
                name: Engine
                show_name: False
                icon: mdi:car-brake-parking
                style:
                  bottom: 35px
                  right: 12%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: red
              -
                type: custom:button-card
                entity: sensor.car_engine
                name: Engine
                show_name: False
                icon: mdi:engine
                style:
                  bottom: 35px
                  right: -5%
                  width: 20%
                  height: 0px
                  z-index: 7
                styles:
                  icon:
                    -
                      width: 20px
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                state:
                  -
                    value: off
                    styles:
                      icon:
                        -
                          color: rgb(60,60,60,1)
                  -
                    value: on
                    styles:
                      icon:
                        -
                          color: #21ff21
                        -
                          animation: blink 1s ease infinite
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgba(0,0,0,0);
  z-index: 0;
  border: 0px;
}

        columns: 2
      -
        square: False
        type: grid
        cards:
          -
            type: picture-elements
            entity: camera.backyard_frigate
            camera_image: camera.backyard_frigate
            camera_view: live
            aspect_ratio: 57%
            elements:
              -
                type: custom:button-card
                entity: sensor.backyard_temperature
                name: Backyard Temp
                show_name: False
                icon: mdi:thermometer
                show_icon: False
                show_state: True
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 2
                  container-type: inline-size
                  position: absolute
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                    -
                      font-size: 5cqw
                  state:
                    -
                      font-size: 5cqw
                    -
                      font-weight: bold
                    -
                      justify-self: right
                    -
                      padding-right: 15px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 5px rgb(0,0,0,1)
              -
                type: custom:button-card
                entity: light.backyard_plug
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/backyard
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 4
                  container-type: inline-size
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Backyard
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 2
                  container-type: inline-size
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                    -
                      font-size: 5cqw
                  name:
                    -
                      font-family: arial
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: left
                    -
                      padding-left: 15px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 5px rgb(0,0,0,1)
              -
                type: custom:button-card
                entity: binary_sensor.backyard_door_sensor_contact
                icon: mdi:door
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 24px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 24px
                          color: #21ff21
                style:
                  bottom: 35px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 24px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1))
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: binary_sensor.backyard_door_sensor_moving
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 26px
                          animation: blink 1s ease infinite
                          color: rgba(253,89,89,1)
                  -
                    operator: ==
                    value: off
                    styles:
                      icon:
                        -
                          width: 26px
                          color: rgba(155,245,66,0)
                style:
                  bottom: 43px
                  height: 0px
                  right: -10px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 26px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1))
                  card:
                    -
                      width: 40px
                    -
                      height: 48px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
              -
                type: custom:button-card
                entity: light.backyard_plug
                icon: mdi:lightbulb
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 20px
                          color: yellow
                  -
                    operator: ==
                    value: off
                    icon: mdi:lightbulb-outline
                    styles:
                      icon:
                        -
                          width: 20px
                          color: rgba(255,255,255,1)
                style:
                  bottom: 35px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  height: 100%
  container-type: inline-size
  {% if is_state('select.backyard_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.backyard_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

          -
            type: picture-elements
            entity: camera.storage_frigate
            camera_image: camera.storage_frigate
            camera_view: live
            aspect_ratio: 56%
            elements:
              -
                type: custom:button-card
                entity: light.storage_light
                show_name: False
                show_icon: False
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/storage
                hold_action:
                  action: toggle
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 4
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      height: 100%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px
              -
                type: custom:button-card
                name: Storage
                style:
                  top: 50%
                  left: 50%
                  width: 100%
                  height: 100%
                  z-index: 2
                  container-type: inline-size
                styles:
                  card:
                    -
                      border-radius: 0px
                    -
                      border: 0px
                    -
                      height: 30%
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
                    -
                      font-size: 5cqw
                  name:
                    -
                      font-family: arial
                    -
                      font-weight: bold
                    -
                      text-transform: uppercase
                    -
                      justify-self: left
                    -
                      padding-left: 15px
                    -
                      color: rgb(255, 255, 255, 1)
                    -
                      text-shadow: 0px 0px 5px rgb(0,0,0,1)
              -
                type: custom:button-card
                entity: light.storage_light
                icon: mdi:lightbulb
                tap_action:
                  action: more-info
                show_name: False
                show_state: False
                show_label: False
                layout: vertical
                state:
                  -
                    operator: ==
                    value: on
                    styles:
                      icon:
                        -
                          width: 20px
                          color: yellow
                  -
                    operator: ==
                    value: off
                    icon: mdi:lightbulb-outline
                    styles:
                      icon:
                        -
                          width: 20px
                          color: rgba(255,255,255,1)
                style:
                  bottom: 35px
                  height: 0px
                  left: 30px
                  z-index: 5
                styles:
                  icon:
                    -
                      width: 20px
                    -
                      color: rgba(255,255,255,0.3)
                    -
                      filter: drop-shadow(0px 0px 2px rgba(0,0,0,1)
                  card:
                    -
                      width: 40px
                    -
                      height: 30px
                    -
                      border: 0px
                    -
                      background-color: rgb(0,0,0,0)
                    -
                      box-shadow: 0px 0px 2px rgb(255,255,255,0)
            card_mod:
              style: @keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgb(0,0,0);
  z-index:0;
  {% if is_state('select.storage_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('select.storage_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

        columns: 2
      -
        square: False
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: mud_room
              -
                display_name: Mud Room
              -
                temperature_sensor: sensor.mud_room_motion_sensor_temperature
              -
                device_1: binary_sensor.front_door_sensor_contact
              -
                device_1_icon: mdi:door
              -
                device_1_state: on
              -
                device_1_color: red
              -
                device_1_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: toilet
              -
                display_name: Toilet
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: kitchen
              -
                display_name: Kitchen
              -
                temperature_sensor: sensor.airthings_wave_temperature
              -
                device_1: binary_sensor.kitchen_fridge_door_contact
              -
                device_1_icon: mdi:fridge
              -
                device_1_state: on
              -
                device_1_color: red
              -
                device_1_animation: blink
              -
                device_2: sensor.coffee_machine_state
              -
                device_2_icon: mdi:coffee
              -
                device_2_state: Running
              -
                device_2_color: orange
              -
                device_2_animation: none
              -
                device_3: sensor.dishwasher_state
              -
                device_3_icon: mdi:dishwasher
              -
                device_3_state: Running
              -
                device_3_color: blue
              -
                device_3_animation: none
              -
                device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
              -
                device_4_icon: mdi:dishwasher-alert
              -
                device_4_state: on
              -
                device_4_color: red
              -
                device_4_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: hallway
              -
                display_name: Hallway
              -
                temperature_sensor: sensor.airthings_wave_temperature
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: living_room
              -
                display_name: Living Room
              -
                temperature_sensor: sensor.airthings_wave_temperature
              -
                device_1: media_player.70pus9005_12_2
              -
                device_1_icon: mdi:television
              -
                device_1_color: green
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: binary_sensor.backyard_door_sensor_contact
              -
                device_2_icon: mdi:door
              -
                device_2_color: red
              -
                device_2_state: on
              -
                device_2_animation: blink
              -
                device_3: fan.philips_air_purifier
              -
                device_3_icon: mdi:air-filter
              -
                device_3_state: on
              -
                device_3_color: green
              -
                device_3_animation: none
              -
                device_6: light.fireplace
              -
                device_6_icon: mdi:fireplace
              -
                device_6_state: on
              -
                device_6_color: orange
              -
                device_6_animation: none
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: stairs
              -
                display_name: Stairs
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: alisa
              -
                display_name: Alisa
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: lobby
              -
                display_name: Lobby
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: bedroom
              -
                display_name: BEDROOM
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                device_1: cover.bedroom_window_blinds
              -
                device_1_icon: mdi:window-shutter
              -
                device_1_state: open
              -
                device_1_color: green
              -
                device_1_animation: none
              -
                device_2: cover.bedroom_window_roller_cover
              -
                device_2_icon: mdi:blinds-open
              -
                device_2_state: open
              -
                device_2_color: green
              -
                device_2_animation: none
              -
                device_3: input_boolean.bed_jukka_occupancy
              -
                device_3_icon: mdi:bed
              -
                device_3_state: on
              -
                device_3_color: blue
              -
                device_3_animation: none
              -
                device_4: input_boolean.bed_piia_occupancy
              -
                device_4_icon: mdi:bed
              -
                device_4_state: on
              -
                device_4_color: pink
              -
                device_4_animation: none
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: office
              -
                display_name: OFFICE
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                device_1: switch.office_pc_power
              -
                device_1_icon: mdi:desktop-classic
              -
                device_1_color: green
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: switch.unraid_power_toggle
              -
                device_6: sensor.ender_5_pro_current_state
              -
                device_6_icon: mdi:printer-3d
              -
                device_6_state: Printing
              -
                device_6_color: orange
              -
                device_6_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: bathroom
              -
                display_name: Bathroom
              -
                device_1: sensor.washing_machine_status
              -
                device_1_icon: mdi:washing-machine
              -
                device_1_state: Running
              -
                device_1_color: blue
              -
                device_1_animation: none
              -
                device_2: input_boolean.bathroom_toilet_occupancy
              -
                device_2_icon: mdi:toilet
              -
                device_2_state: on
              -
                device_2_color: orange
              -
                device_2_animation: blink
              -
                device_3: input_boolean.bathroom_shower_occupancy
              -
                device_3_icon: mdi:shower-head
              -
                device_3_state: on
              -
                device_3_color: blue
              -
                device_3_animation: blink
              -
                device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
              -
                device_4_icon: mdi:dishwasher-alert
              -
                device_4_state: on
              -
                device_4_color: red
              -
                device_4_animation: blink
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: elias
              -
                display_name: Elias
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: sauna
              -
                display_name: Sauna
              -
                temperature_sensor: sensor.ruuvitag_8572_temperature
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: anton
              -
                display_name: ANTON
              -
                temperature_sensor: sensor.anton_temperature
              -
                device_1: media_player.anton_spot
              -
                device_1_icon: speaker
              -
                device_1_state: playing
              -
                device_1_color: green
              -
                device_1_animation: blink
        columns: 2
  -
    type: grid
    cards:
      -
        square: False
        columns: 1
        type: grid
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: WEATHER
            alignment: center
            card_mod:
              style: ha-card {
  margin-top: -0px;
  margin-bottom: -10px;
}

          -
            show_current: True
            show_forecast: True
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
                      -
                        type: weather-forecast
                        entity: weather.openweathermap
                        show_current: True
                        show_forecast: True
                        forecast_type: hourly
                      -
                        type: entities
                        entities:
                          -
                            entity: sensor.openweathermap_feels_like_temperature
                            name: Feels Like
                          -
                            entity: sensor.openweathermap_wind_speed
                            name: Wind
                          -
                            entity: sensor.backyard_humidity
                            name: Backyard Humidity
                          -
                            entity: sensor.backyard_temperature
                            name: Backyard Temperature
                      -
                        type: weather-forecast
                        show_current: False
                        show_forecast: True
                        entity: weather.forecast_home
                        forecast_type: daily
                        name: Forecast
                      -
                        type: custom:horizon-card
      -
        type: vertical-stack
        cards:
          -
            type: custom:mushroom-title-card
            title: 
            subtitle: ENERGY
            alignment: center
            card_mod:
              style: ha-card {
  margin-top: -0px;
  margin-bottom: -10px;
}

          -
            square: False
            columns: 1
            type: grid
            cards:
              -
                type: custom:config-template-card
                variables:
                  PRICEAVERAGE: states['sensor.nordpool_kwh_fi_eur'].attributes['average']
                  PRICEMEAN: states['sensor.nordpool_kwh_fi_eur'].attributes['mean']
                  PRICEHIGH: states['sensor.nordpool_today_mean_hi_limit'].state
                  PRICELOW: states['sensor.nordpool_today_mean_lo_limit'].state
                entities:
                  - sensor.nordpool_kwh_eur_without_tax
                card:
                  type: custom:apexcharts-card
                  graph_span: 1d
                  span:
                    start: day
                  apex_config:
                    stroke:
                      dashArray: 4
                    chart:
                      height: 180px
                      width: 115%
                      offsetX: -30
                    title:
                      text: Energy Price Today
                      align: center
                      offsetY: 10
                      style:
                        fontSize: 13px
                        fontFamily: Verdana
                        fontWeight: normal
                    grid:
                      show: True
                      borderColor: rgba(255,255,255,0.2)
                    xaxis:
                      position: bottom
                      labels:
                        format: H
                        hideOverlappingLabels: True
                        offsetX: 0
                      axisTicks:
                        offsetX: 0
                    legend:
                      show: False
                      itemMargin:
                        vertical: 10
                        horizontal: 10
                    tooltip:
                      enabled: False
                      style:
                        fontSize: 14px
                  show:
                    last_updated: True
                  experimental:
                    color_threshold: True
                  header:
                    show_states: True
                    colorize_states: True
                  now:
                    show: True
                  yaxis:
                    -
                      id: cost
                      opposite: True
                      decimals: 1
                      apex_config:
                        tickAmount: 4
                        labels:
                          show: True
                        title:
                          text: c/kWh
                          rotate: 0
                          offsetX: -25
                          offsetY: -70
                          style:
                            fontSize: 10px
                            fontFamily: verdana
                            color: orange
                    -
                      id: energy
                      max: ~2
                      min: 0
                      decimals: 1
                      apex_config:
                        tickAmount: 4
                        labels:
                          show: True
                        title:
                          text: kWh
                          rotate: 0
                          offsetX: 25
                          offsetY: -70
                          style:
                            color: skyblue
                            fontSize: 10px
                            fontFamily: verdana
                  series:
                    -
                      entity: sensor.nordpool_kwh_fi_eur
                      name: Price
                      yaxis_id: cost
                      type: column
                      opacity: 0.8
                      stroke_width: 0
                      show:
                        extremas: True
                        in_header: raw
                        header_color_threshold: True
                      data_generator: return entity.attributes.raw_today.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
});

                      color_threshold:
                        -
                          value: 1
                          color: lightgreen
                        -
                          value: ${PRICELOW * 1}
                          color: orange
                        -
                          value: ${PRICEHIGH * 1}
                          color: darkred
                    -
                      entity: sensor.home_total_energy_hourly
                      name: Energy (kWh)
                      color: skyblue
                      type: line
                      opacity: 1
                      yaxis_id: energy
                      stroke_width: 2
                      float_precision: 1
                      extend_to: False
                      unit: kWh
                      group_by:
                        duration: 1hour
                        func: max
                      show:
                        legend_value: False
                        datalabels: False
          -
            square: False
            type: grid
            cards:
              -
                square: False
                type: grid
                cards:
                  -
                    type: custom:mushroom-template-card
                    primary: {{ states(entity) | float(0) | round(2) }}
                    secondary: c/kWh
                    icon: mdi:currency-eur
                    icon_color: {% set mean_hi = states('sensor.nordpool_today_mean_hi_limit') | float(0) %}
{% set mean_lo = states('sensor.nordpool_today_mean_lo_limit') | float(0) %}
{% set price = state_attr(config.entity, 'current_price') | float(0) %}
{% if price > mean_hi %}
  red
{% elif price < mean_lo %}
  green
{% else %}
  orange
{% endif %}
                    badge_icon: 
                    badge_color: 

                    entity: sensor.nordpool_kwh_fi_eur_3_10_024
                    layout: vertical
                    fill_container: True
                    tap_action:
                      action: more-info
                    hold_action:
                      action: none
                    double_tap_action:
                      action: none
                  -
                    type: custom:mushroom-template-card
                    primary: {{ states(entity) | float(0) | round(0) }}
                    secondary: W
                    icon: mdi:flash
                    icon_color: blue
                    entity: sensor.home_total_power
                    layout: vertical
                    badge_color: 
                    fill_container: True
                    tap_action:
                      action: more-info
                    hold_action:
                      action: none
                    double_tap_action:
                      action: none
                columns: 2
            columns: 2
          -
            type: conditional
            conditions:
              -
                entity: sensor.nordpool_tomorrow
                state: True
            card:
              type: custom:apexcharts-card
              graph_span: 1d
              span:
                start: day
                offset: +1d
              apex_config:
                chart:
                  height: 180px
                title:
                  text: Price Tomorrow (c/kWh)
                  align: center
                  offsetY: 10
                  style:
                    fontSize: 13px
                    fontFamily: Verdana
                    fontWeight: normal
                grid:
                  show: True
                  borderColor: rgba(255,255,255,0.2)
                xaxis:
                  position: bottom
                  labels:
                    format: H
                    hideOverlappingLabels: True
                    offsetX: 0
                  axisTicks:
                    offsetX: 0
                legend:
                  show: False
                  itemMargin:
                    vertical: 10
                    horizontal: 10
                tooltip:
                  enabled: False
                  style:
                    fontSize: 14px
              show:
                last_updated: True
              experimental:
                color_threshold: True
              header:
                show_states: True
                colorize_states: True
              now:
                show: True
              yaxis:
                -
                  id: cost
                  opposite: True
                  decimals: 1
                  apex_config:
                    tickAmount: 3
                    labels:
                      show: True
              series:
                -
                  entity: sensor.nordpool_kwh_fi_eur
                  name: Price
                  yaxis_id: cost
                  type: column
                  opacity: 0.9
                  stroke_width: 0
                  show:
                    extremas: True
                    in_header: raw
                    header_color_threshold: True
                  data_generator: return entity.attributes.raw_tomorrow.map((start, index) => {
  return [new Date(start["start"]).getTime(), entity.attributes.raw_tomorrow[index]["value"]];
});

          -
            type: custom:apexcharts-card
            graph_span: 7d
            update_interval: 15min
            apex_config:
              fill:
                opacity: 0.5
              markers:
                size: 3
              xaxis:
                showDuplicates: True
                position: bottom
                labels:
                  format: ddd
                  hideOverlappingLabels: False
              chart:
                height: 180px
              grid:
                show: True
                borderColor: rgba(255,255,255,0.2)
              legend:
                show: True
                itemMargin:
                  vertical: 10
                  horizontal: 10
              dataLabels:
                enabled: True
                position: top
                offsetY: -8
                background:
                  enabled: False
              tooltip:
                style:
                  fontSize: 14px
              stroke:
                dashArray: 0
              title:
                text: Energy Daily
                align: center
                offsetY: 10
                style:
                  fontSize: 13px
                  fontFamily: Verdana
                  fontWeight: normal
            header:
              show: False
            yaxis:
              -
                id: cost
                max: ~100
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 4
                  labels:
                    show: True
              -
                id: power
                opposite: True
                max: ~35
                min: 0
                decimals: 0
                apex_config:
                  tickAmount: 7
                  labels:
                    show: True
                  title:
                    text: kWh
                    rotate: 0
                    offsetX: -25
                    offsetY: -70
                    style:
                      fontSize: 10px
                      fontFamily: verdana
                      color: orange
            series:
              -
                entity: sensor.home_total_energy_daily
                name: Energy (kWh)
                color: skyblue
                type: column
                yaxis_id: power
                stroke_width: 1
                float_precision: 1
                unit: kWh
                statistics:
                  type: state
                group_by:
                  duration: 1day
                  func: max
                show:
                  legend_value: False
                  datalabels: True
      -
        type: custom:decluttering-card
        template: area_card
        variables:
          -
            entity_name: kitchen
          -
            display_name: Kitchen
          -
            temperature_sensor: sensor.kitchen_fridge_door_device_temperature
          -
            device_1: binary_sensor.kitchen_fridge_door_contact
          -
            device_1_icon: mdi:fridge
          -
            device_1_state: off
          -
            device_1_color: red
          -
            device_1_animation: blink
          -
            device_2: sensor.coffee_machine_state
          -
            device_2_icon: mdi:coffee
          -
            device_2_state: Running
          -
            device_2_color: orange
          -
            device_2_animation: none
          -
            device_3: sensor.dishwasher_state
          -
            device_3_icon: mdi:dishwasher
          -
            device_3_state: Running
          -
            device_3_color: blue
          -
            device_3_animation: none
          -
            device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
          -
            device_4_icon: mdi:dishwasher-alert
          -
            device_4_state: on
          -
            device_4_color: red
          -
            device_4_animation: blink
  -
    type: grid
    cards:
      -
        square: False
        type: grid
        cards:
          -
            type: custom:streamline-card
            template: area_card
            variables:
              entity_name: mud_room
              display_name: Mud Room
              temperature_sensor: sensor.mud_room_motion_sensor_temperature
              device_1: binary_sensor.front_door_sensor_contact
              device_1_icon: mdi:door
              device_1_state: on
              device_1_color: red
              device_1_animation: blink
              device_2: 
              device_2_icon: 
              device_2_state: 
              device_2_color: 
              device_2_animation: 
              device_3: 
              device_3_icon: 
              device_3_state: 
              device_3_color: 
              device_3_animation: 
              device_4: 
              device_4_icon: 
              device_4_state: 
              device_4_color: 
              device_4_animation: 
              device_5: 
              device_5_icon: 
              device_5_state: 
              device_5_color: 
              device_5_animation: 
              device_6: 
              device_6_icon: 
              device_6_state: 
              device_6_color: 
              device_6_animation: 
          -
            type: custom:streamline-card
            template: area_card
            variables:
              entity_name: office
              display_name: OFFICE
              temperature_sensor: sensor.bedroom_temperature
              device_1: switch.office_pc_power
              device_1_icon: mdi:desktop-classic
              device_1_color: green
              device_1_state: on
              device_1_animation: none
              device_2: switch.unraid_power_toggle
              device_6: sensor.ender_5_pro_current_state
              device_6_icon: mdi:printer-3d
              device_6_state: Printing
              device_6_color: orange
              device_6_animation: blink
              device_2_icon: 
              device_2_state: 
              device_2_color: 
              device_2_animation: 
              device_3: 
              device_3_icon: 
              device_3_state: 
              device_3_color: 
              device_3_animation: 
              device_4: 
              device_4_icon: 
              device_4_state: 
              device_4_color: 
              device_4_animation: 
              device_5: 
              device_5_icon: 
              device_5_state: 
              device_5_color: 
              device_5_animation: 
          -
            type: custom:streamline-card
            template: area_card
            variables:
              entity_name: toilet
              display_name: Toilet
              temperature_sensor: 
              device_1: 
              device_1_icon: 
              device_1_state: 
              device_1_color: 
              device_1_animation: 
              device_2: 
              device_2_icon: 
              device_2_state: 
              device_2_color: 
              device_2_animation: 
              device_3: 
              device_3_icon: 
              device_3_state: 
              device_3_color: 
              device_3_animation: 
              device_4: 
              device_4_icon: 
              device_4_state: 
              device_4_color: 
              device_4_animation: 
              device_5: 
              device_5_icon: 
              device_5_state: 
              device_5_color: 
              device_5_animation: 
              device_6: 
              device_6_icon: 
              device_6_state: 
              device_6_color: 
              device_6_animation: 
          -
            type: custom:streamline-card
            template: area_card
            variables:
              -
                entity_name: kitchen
              -
                display_name: Kitchen
              -
                temperature_sensor: sensor.airthings_wave_temperature
              -
                device_1: binary_sensor.kitchen_fridge_door_contact
              -
                device_1_icon: mdi:fridge
              -
                device_1_state: on
              -
                device_1_color: red
              -
                device_1_animation: blink
              -
                device_2: sensor.coffee_machine_state
              -
                device_2_icon: mdi:coffee
              -
                device_2_state: Running
              -
                device_2_color: orange
              -
                device_2_animation: none
              -
                device_3: sensor.dishwasher_state
              -
                device_3_icon: mdi:dishwasher
              -
                device_3_state: Running
              -
                device_3_color: blue
              -
                device_3_animation: none
              -
                device_4: binary_sensor.kitchen_dishwasher_leak_sensor_water_leak
              -
                device_4_icon: mdi:dishwasher-alert
              -
                device_4_state: on
              -
                device_4_color: red
              -
                device_4_animation: blink
        columns: 2
      -
        square: True
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: jukka
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: piia
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: anton
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: elias
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: alisa
        layout_options:
          grid_columns: full
          grid_rows: auto
        columns: 5
  -
    type: grid
    cards:
      -
        type: picture-elements
        elements:
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: office
              -
                display_name: OFFICE
              -
                temperature_sensor: sensor.bedroom_temperature
              -
                device_1: switch.office_pc_power
              -
                device_1_icon: mdi:desktop-classic
              -
                device_1_color: green
              -
                device_1_state: on
              -
                device_1_animation: none
              -
                device_2: switch.unraid_power_toggle
              -
                device_6: sensor.ender_5_pro_current_state
              -
                device_6_icon: mdi:printer-3d
              -
                device_6_state: Printing
              -
                device_6_color: orange
              -
                device_6_animation: blink
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
        image: /local/rooms/room_office.jpg
        layout_options:
          grid_columns: 2
      -
        type: heading
        heading: New section
      -
        type: picture-elements
        elements:
          -
            type: custom:decluttering-card
            template: area_card
            variables:
              -
                entity_name: toilet
              -
                display_name: Toilet
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
        image: /local/rooms/transparent10x10.png
        layout_options:
          grid_columns: 2
      -
        type: custom:streamline-card
        template: area_card
        variables:
          entity_name: bedroom
          display_name: BEDROOM
          temperature_sensor: sensor.bedroom_temperature
          device_1: cover.bedroom_window_blinds
          device_1_icon: mdi:window-shutter
          device_1_state: open
          device_1_color: green
          device_1_animation: none
          device_2: cover.bedroom_window_roller_cover
          device_2_icon: mdi:blinds-open
          device_2_state: open
          device_2_color: green
          device_2_animation: none
          device_3: input_boolean.bed_jukka_occupancy
          device_3_icon: mdi:bed
          device_3_state: on
          device_3_color: blue
          device_3_animation: none
          device_4: input_boolean.bed_piia_occupancy
          device_4_icon: mdi:bed
          device_4_state: on
          device_4_color: pink
          device_4_animation: none
          device_5: 
          device_5_icon: 
          device_5_state: 
          device_5_color: 
          device_5_animation: 
          device_6: 
          device_6_icon: 
          device_6_state: 
          device_6_color: 
          device_6_animation: 
        layout_options:
          grid_columns: 2
      -
        type: custom:streamline-card
        template: area_card
        variables:
          entity_name: bedroom
          display_name: BEDROOM
          temperature_sensor: sensor.bedroom_temperature
          device_1: cover.bedroom_window_blinds
          device_1_icon: mdi:window-shutter
          device_1_state: open
          device_1_color: green
          device_1_animation: none
          device_2: cover.bedroom_window_roller_cover
          device_2_icon: mdi:blinds-open
          device_2_state: open
          device_2_color: green
          device_2_animation: none
          device_3: input_boolean.bed_jukka_occupancy
          device_3_icon: mdi:bed
          device_3_state: on
          device_3_color: blue
          device_3_animation: none
          device_4: input_boolean.bed_piia_occupancy
          device_4_icon: mdi:bed
          device_4_state: on
          device_4_color: pink
          device_4_animation: none
          device_5: 
          device_5_icon: 
          device_5_state: 
          device_5_color: 
          device_5_animation: 
          device_6: 
          device_6_icon: 
          device_6_state: 
          device_6_color: 
          device_6_animation: 
        layout_options:
          grid_columns: 2
          grid_rows: 2
      -
        type: custom:decluttering-card
        template: area_card
        variables:
          -
            entity_name: mud_room
          -
            display_name: Mud Room
          -
            temperature_sensor: sensor.mud_room_motion_sensor_temperature
          -
            device_1: binary_sensor.front_door_sensor_contact
          -
            device_1_icon: mdi:door
          -
            device_1_state: on
          -
            device_1_color: red
          -
            device_1_animation: blink
    column_span: 1
dense_section_placement: True
cards:

` 
### View: Devices

Path: $(@{type=sections; max_columns=5; title=Devices; path=devices; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_devices.png)

`yaml
type: sections
max_columns: 5
title: Devices
path: devices
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: custom:auto-entities
        card:
          type: entities
        filter:
          include:
            -
              entity_id: sensor.*battery*
          exclude:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: custom:auto-entities
        card:
          type: entities
        filter:
          include:
            -
              state: unknown
          exclude:

` 
### View: car

Path: $(@{type=sections; max_columns=4; title=car; path=car; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_car.png)

`yaml
type: sections
max_columns: 4
title: car
path: car
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: picture-elements
        elements:
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: not_home
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-BG-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  animation: pulse 1.5s ease infinite
                  opacity: 60%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: device_tracker.xbp_358_device_tracker
                state: home
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-BG-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  opacity: 100%
                  z-index: 2
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  animation: blink 1s ease infinite
                  opacity: 100%
                  z-index: 3
          -
            type: custom:button-card
            entity: switch.xpb_358_pre_entry_climate_control
            show_name: False
            show_icon: False
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            hold_action:
              action: toggle
            double_tap_action:
              action: none
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 3
            styles:
              card:
                -
                  border-radius: 8px
                -
                  height: 100%
                -
                  background-color: rgba(0,0,0,0)
                -
                  box-shadow: 0px 0px
            card_mod:
              style: ha-card {
  {% if is_state('input_select.[[entity_name]]_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('input_select.[[entity_name]]_presence','idle') %}
    border: 3px solid rgba(255, 163, 0, 0.8);
  {% else %}
    border: 0px solid rgba(0, 0, 0, 0);
  {% endif %}
}

          -
            type: custom:button-card
            name: CAR
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
            styles:
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
                -
                  font-size: 5cqw
              name:
                -
                  font-family: arial
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: left
                -
                  padding-left: 15px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 5px rgb(0,0,0,1)
          -
            type: custom:button-card
            entity: device_tracker.xbp_358_device_tracker
            icon: mdi:account-circle
            show_name: False
            show_icon: True
            show_state: True
            tap_action:
              action: none
            hold_action:
              action: none
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
            styles:
              name:
                -
                  display: none
              card:
                -
                  border-radius: 0px
                -
                  height: 100%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px
              icon:
                -
                  display: none
                -
                  height: 30%
              state:
                -
                  position: absolute
                -
                  top: 10%
                -
                  right: 3%
                -
                  font-size: 5cqw
                -
                  font-weight: bold
                -
                  text-shadow: 0px 0px 5px rgb(0,0,0,1)
          -
            type: custom:mushroom-chips-card
            chips:
              -
                type: template
                entity: binary_sensor.xpb_358_park_brake_status
                icon: mdi:car-brake-parking
                icon_color: {% if is_state(entity,'on') %}
  green
{% else %}
  grey
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'on') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: blink 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

              -
                type: template
                entity: sensor.car_engine
                icon: mdi:engine
                icon_color: {% if is_state(entity,'on') %}
  green
{% else %}
 grey
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'on') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: blink 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

              -
                type: template
                entity: switch.car_pre_entry_ac
                icon: mdi:fan
                icon_color: {% if is_state(entity,'on') %}
  green
{% else %}
  grey
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'off') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: blink 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

              -
                type: template
                entity: binary_sensor.xpb_358_low_wash_water_warning
                icon: mdi:wiper-wash
                icon_color: {% if is_state(entity,'on') %}
  red
{% else %}
  grey
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'[[device_4_state]]') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: blink 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

              -
                type: template
                entity: lock.xpb_358_lock
                icon: {% if is_state(entity,'locked') %}
  mdi:lock
{% else %}
  mdi:lock-open-outline
{% endif %}

                icon_color: {% if is_state(entity,'locked') %}
  green
{% else %}
  red
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'locked') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: blink 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

              -
                type: template
                entity: [[device_6]]
                icon: [[device_6_icon]]
                icon_color: {% if is_state(entity,'[[device_6_state]]') %}
  [[device_6_color]]
{% else %}
  gray
{% endif %}

                card_mod:
                  style: @keyframes blink {
  50% { opacity: 0; }
}
:host {
  {% if is_state(config.entity,'[[device_6_state]]') %}
    display: flex;
  {% else %}
    display: none;
  {% endif %}
}
ha-card {
  animation: [[device_6_animation]] 1s ease infinite;
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0.8);
  --chip-border-width: 0;
}

            alignment: center
            style:
              top: 120%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
            card_mod:
              style: ha-card {
  --chip-height: 12cqw;
  --chip-icon-size: 8cqw;
  --chip-border-radius: 5px;
  --chip-spacing: 2px;
  --chip-background: rgba(0,0,0,0);
  --chip-box-shadow: 0px 0px;
  --chip-border-width: 0;
}

        entity: device_tracker.xbp_358_device_tracker
        image: local/car/Car-BG-vertical.png
        state_filter:
          home: brightness(100%) saturate(1.2)
          away: brightness(40%) grayscale(100%) contrast(150%)
        card_mod:
          style: ha-card {
  top: 0%;
  border: 0px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  border-color: rgba(0,0,0,0)
  z-index: 0;
}
@keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}

      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Mercedes-Benz-GLC-BG.png
        state_filter:
          home: brightness(100%)
          away: brightness(25%)
        elements:
          -
            type: custom:bar-card
            entities:
              -
                entity: sensor.xpb_358_fuel_level
            entity_row: True
            direction: up
            stack: horizontal
            height: 64px
            animation:
              state: on
              speed: 1
            color: #ad6e00
            positions:
              icon: off
              indicator: off
              title: off
              name: off
              value: off
              minmax: off
            style:
              name: Battery Status
              top: 48%
              right: 20px
              width: 25px
              --ha-card-border-width: 0px
          -
            type: image
            image: local/car/charging_station_blocks.png
            style:
              name: GAS Station
              right: -118px
              top: 50%
              width: 140px
            filter: brightness(80%)
          -
            type: state-label
            entity: sensor.xpb_358_range_liquid
            style:
              name: Range
              top: 86%
              right: -5px
              color: orange
              font-size: 70%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_fuel_level
            style:
              name: Fuel Level
              top: 14%
              right: 5px
              color: #21ff21
              font-size: 80%
              font-weight: bold
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-small3.png
            style:
              name: GLC
              left: 50%
              top: 50%
              width: 100%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                entity: sensor.xpb_358_charging_power
                image: local/car/charging_cable_only.png
                style:
                  name: Charging Cable
                  left: 60px
                  top: 52%
                  width: 30%
                  animation: {% set value = states(entity) | float %} 
{% if value < 10 %}
pulse 1s ease infinite
{% endif %}

                filter: brightness(80%)
              -
                type: state-label
                entity: sensor.xpb_358_charging_power
                style:
                  name: Charging Power
                  top: 10%
                  left: 40%
                  color: orange
                  font-size: 70%
                  font-weight: bold
              -
                type: conditional
                conditions:
                  -
                    entity: sensor.car_charging
                    state: on
                elements:
                  -
                    type: state-label
                    entity: sensor.car_charge_ready
                    style:
                      name: Charging Ready
                      top: 10%
                      left: 55%
                      color: orange
                      font-size: 70%
                      font-weight: bold
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-small3.png
            style:
              name: GLC
              left: 50%
              top: 50%
              width: 100%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-green.png
                style:
                  left: 50%
                  top: 50%
                  width: 100%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: custom:bar-card
            entities:
              -
                entity: sensor.xpb_358_state_of_charge
            entity_row: True
            direction: up
            stack: horizontal
            height: 64px
            animation:
              state: on
              speed: 1
            severity:
              -
                color: Red
                from: 0
                to: 25
              -
                color: Orange
                from: 26
                to: 50
              -
                color: #21ff21
                from: 51
                to: 100
            positions:
              icon: off
              indicator: off
              title: off
              name: off
              value: off
              minmax: off
            style:
              name: Battery Status
              top: 48%
              left: 40px
              width: 25px
              --ha-card-border-width: 0px
          -
            type: image
            image: local/car/charging_station_blocks.png
            style:
              name: Charging Station
              left: 62px
              top: 50%
              width: 140px
            filter: brightness(80%)
          -
            type: state-label
            entity: sensor.xpb_358_state_of_charge
            style:
              name: Battery Status
              top: 14%
              left: 40px
              color: #21ff21
              font-size: 80%
              font-weight: bold
          -
            type: state-label
            entity: sensor.xpb_358_range_electric
            style:
              name: Range Electric
              top: 86%
              left: 38px
              color: orange
              font-size: 70%
              font-weight: bold
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}

      -
        type: picture-elements
        image: local/car/Mercedes-Benz-GLC-BG.png
        state_filter:
          home: brightness(100%)
          away: brightness(25%)
        elements:
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-small3.png
            style:
              left: 50%
              top: 50%
              transform: translate(-50%, -50%)
              width: 125%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-green.png
                style:
                  left: 50%
                  top: 50%
                  width: 125%
                  transform: translate(-50%, -50%)
                  animation: blink 1s ease infinite
                  opacity: 100%
        card_mod:
          style: @keyframes blink {
  {% if is_state('binary_sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  padding: 15px;
}

      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Car-BG-vertical.png
        state_filter:
          home: brightness(100%) contrast(85%)
          away: brightness(25%)
        elements:
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            show_name: False
            show_icon: False
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            double_tap_action:
              action: fire-dom-event
              browser_mod:
                service: browser_mod.popup
                data:
                  title: CAR
                  content:
                    type: vertical-stack
                    cards:
                      -
                        type: custom:scheduler-card
                        include:
                          - switch.car_pre_entry_ac
                        exclude:
                        title: Schedules
                        discover_existing: False
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
                        show_header_toggle: False
            hold_action:
              action: toggle
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 9
            styles:
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 100%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px
          -
            type: custom:button-card
            name: CAR
            style:
              top: 0%
              left: 50%
              width: 102%
              height: 0px
              z-index: 2
              container-type: inline-size
            styles:
              name:
                -
                  font-family: verdana
                -
                  font-size: 6cqw
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: center
                -
                  padding-left: 0px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 4px rgb(0,0,0,5)
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0.3)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:mushroom-chips-card
            chips:
              -
                type: template
                entity: device_tracker.xpb_358_device_tracker
                content: 
                icon: {% if is_state(config.entity,'home') %}
  mdi:home
{% else %}
  mdi:home-export-outline
{% endif %}

                icon_color: {% if is_state(config.entity,'home') %}
  green
{% else %}
  gray
{% endif %}

                card_mod:
                  style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 2;
}

            alignment: left
            style:
              top: 46%
              left: 50%
              width: 100%
              height: 100%
              border: 0px
              z-index: 8
            card_mod:
              style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
}

          -
            type: custom:mushroom-chips-card
            chips:
              -
                type: template
                entity: switch.schedule_898e47
                content: 
                icon: {% if is_state(config.entity,'on') %}
  mdi:clock-check
{% else %}
  mdi:clock-remove-outline
{% endif %}

                icon_color: {% if is_state(config.entity,'on') %}
  green
{% else %}
  gray
{% endif %}

                card_mod:
                  style: :host {
  {% set value = states(config.entity) %}
  {% if value == 'unknown' or value == 'unavailable' %}
    display: none;
  {% else %}
    display: flex;
  {% endif %}
  background: rgba(0,0,0,0);
}
ha-card {
  --chip-box-shadow: 0px 0px;
  --chip-background: rgba(0,0,0,0);
  --chip-border-width: 0;
  z-index: 8;
}

            alignment: left
            style:
              top: 46%
              left: 130%
              width: 100%
              height: 100%
              border: 0px
              z-index: 8
            card_mod:
              style: ha-card {
  --chip-height: 45px;
  --chip-border-radius: 45px;
  --chip-border-width: 0;
  background: rgba(0,0,0,0);
}

          -
            type: image
            image: local/car/Mercedes-Benz-GLC-BG-960x444.png
            style:
              name: GLC
              left: 50%
              top: 45%
              width: 90%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: custom:button-card
            name: Electric
            show_name: True
            icon: mdi:flash
            show_icon: False
            style:
              top: 22%
              left: 13.3%
              width: 25%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 75%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_state_of_charge
            name: Battery Status
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              left: 10.5%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_electric
            name: Range Electric
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              left: 11%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            name: Fuel
            show_name: True
            icon: mdi:gas-station
            show_icon: False
            style:
              top: 22%
              right: -19%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 70%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_fuel_level
            name: Fuel Level
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              right: -9%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_liquid
            name: Fuel Range
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              right: -6%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: lock.xpb_358_lock
            name: Doors
            show_name: False
            icon: mdi:lock
            style:
              bottom: 35px
              left: 13%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: unlocked
                icon: mdi:lock-open-outline
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
                    -
                      animation: blink 1s ease infinite
              -
                value: locked
                icon: mdi:lock
                styles:
                  icon:
                    -
                      color: #21ff21
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_low_wash_water_warning
            name: Wash Water
            show_name: False
            icon: mdi:wiper-wash
            style:
              bottom: 35px
              left: 32%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            name: AC
            show_name: False
            icon: mdi:air-conditioner
            style:
              bottom: 35px
              left: 50%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_park_brake_status
            name: Engine
            show_name: False
            icon: mdi:car-brake-parking
            style:
              bottom: 35px
              right: 12%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: red
          -
            type: custom:button-card
            entity: sensor.car_engine
            name: Engine
            show_name: False
            icon: mdi:engine
            style:
              bottom: 35px
              right: -5%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgba(0,0,0,0);
  z-index: 0;
  border: 0px;
}

        layout_options:
          grid_columns: 2
      -
        type: picture-elements
        entity: device_tracker.xpb_358_device_tracker
        image: local/car/Car-BG-vertical.png
        state_filter:
          home: brightness(100%) contrast(85%)
          away: brightness(25%)
        elements:
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            show_name: False
            show_icon: False
            tap_action:
              action: navigate
              navigation_path: /dashboard-persons/car
            double_tap_action:
              action: fire-dom-event
              browser_mod:
                service: browser_mod.popup
                data:
                  title: CAR
                  content:
                    type: vertical-stack
                    cards:
                      -
                        type: custom:scheduler-card
                        include:
                          - switch.car_pre_entry_ac
                        exclude:
                        title: Schedules
                        discover_existing: False
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
                        show_header_toggle: False
            hold_action:
              action: toggle
            style:
              top: 50%
              left: 50%
              width: 100%
              height: 100%
              z-index: 9
            styles:
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 100%
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px
          -
            type: custom:button-card
            name: CAR
            style:
              top: 0%
              left: 50%
              width: 102%
              height: 0px
              z-index: 2
              container-type: inline-size
            styles:
              name:
                -
                  font-family: verdana
                -
                  font-size: 6cqw
                -
                  font-weight: bold
                -
                  text-transform: uppercase
                -
                  justify-self: center
                -
                  padding-left: 0px
                -
                  color: rgb(255, 255, 255, 1)
                -
                  text-shadow: 0px 0px 4px rgb(0,0,0,5)
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0.3)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: image
            image: local/car/Mercedes-Benz-GLC-BG-960x444.png
            style:
              name: GLC
              left: 50%
              top: 45%
              width: 90%
          -
            type: conditional
            conditions:
              -
                entity: sensor.car_charge_plug
                state: on
            elements:
              -
                type: image
                image: local/car/Mercedes-Benz-GLC-Green-960x444.png
                style:
                  left: 50%
                  top: 45%
                  width: 90%
                  animation: blink 1s ease infinite
                  opacity: 100%
          -
            type: custom:button-card
            name: Electric
            show_name: True
            icon: mdi:flash
            show_icon: False
            style:
              top: 22%
              left: 13.3%
              width: 25%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 75%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_state_of_charge
            name: Battery Status
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              left: 10.5%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_electric
            name: Range Electric
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              left: 11%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            name: Fuel
            show_name: True
            icon: mdi:gas-station
            show_icon: False
            style:
              top: 22%
              right: -19%
              width: 30%
              height: 0px
              z-index: 7
            styles:
              card:
                -
                  font-size: 70%
                -
                  font-weight: bold
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_fuel_level
            name: Fuel Level
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 32%
              right: -9%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: #21ff21
                -
                  font-weight: bold
                -
                  font-size: 60%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: sensor.xpb_358_range_liquid
            name: Fuel Range
            show_name: False
            icon: mdi:flash
            show_icon: False
            show_state: True
            style:
              top: 42%
              right: -6%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              state:
                -
                  color: orange
                -
                  font-weight: bold
                -
                  font-size: 55%
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
          -
            type: custom:button-card
            entity: lock.xpb_358_lock
            name: Doors
            show_name: False
            icon: mdi:lock
            style:
              bottom: 35px
              left: 13%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: unlocked
                icon: mdi:lock-open-outline
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
                    -
                      animation: blink 1s ease infinite
              -
                value: locked
                icon: mdi:lock
                styles:
                  icon:
                    -
                      color: #21ff21
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_low_wash_water_warning
            name: Wash Water
            show_name: False
            icon: mdi:wiper-wash
            style:
              bottom: 35px
              left: 32%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: switch.car_pre_entry_ac
            name: AC
            show_name: False
            icon: mdi:air-conditioner
            style:
              bottom: 35px
              left: 50%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
          -
            type: custom:button-card
            entity: binary_sensor.xpb_358_park_brake_status
            name: Engine
            show_name: False
            icon: mdi:car-brake-parking
            style:
              bottom: 35px
              right: 12%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: red
          -
            type: custom:button-card
            entity: sensor.car_engine
            name: Engine
            show_name: False
            icon: mdi:engine
            style:
              bottom: 35px
              right: -5%
              width: 20%
              height: 0px
              z-index: 7
            styles:
              icon:
                -
                  width: 20px
              card:
                -
                  border-radius: 0px
                -
                  border: 0px
                -
                  height: 30px
                -
                  background-color: rgb(0,0,0,0)
                -
                  box-shadow: 0px 0px 2px rgb(255,255,255,0)
            state:
              -
                value: off
                styles:
                  icon:
                    -
                      color: rgb(60,60,60,1)
              -
                value: on
                styles:
                  icon:
                    -
                      color: #21ff21
                    -
                      animation: blink 1s ease infinite
        card_mod:
          style: @keyframes blink {
  {% if is_state('sensor.car_charging','on') %}
    50% { opacity: 0; }
  {% else %}
    50% { opacity: 100; }
  {% endif %}
}
@keyframes pulse {
  50% { opacity: 0.33; }
}
ha-card {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background: rgba(0,0,0,0);
  z-index: 0;
  border: 0px;
}

        layout_options:
          grid_columns: 2
      -
        type: conditional
        conditions:
        card:
          type: custom:mushroom-template-card
          entity: binary_sensor.car_charging
          primary: {% if states('sensor.xpb_358_charging_status') == '1' %}
  Plugged in | Charging ended
{% else %}
  Charging in progress
{% endif %}

          secondary: {% if states('sensor.xpb_358_charging_status') == '0' %}
  Charging {{ states('sensor.xpb_358_charging_power') }} kW | {{
  states('sensor.car_charge_ready') }}
{% else %}
  Battery at {{ states('sensor.xpb_358_state_of_charge') }}%
{% endif %}

          icon: mdi:ev-station
          icon_color: lightgreen
          card_mod:
            style: ha-card {
  border-radius: 12px;
  box-shadow: 0 0 0px rgba(30, 144, 255, 0.3);
  background-color: var(--card-background-color);
}

      -
        type: custom:mushroom-template-card
        secondary: 
        icon: mdi:oil-level
        entity: binary_sensor.xpb_358_low_coolant_level_warning
        double_tap_action:
          action: none
        hold_action:
          action: none
        tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  red
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1
      -
        type: custom:mushroom-template-card
        secondary: 
        icon: mdi:car-brake-alert
        entity: binary_sensor.xpb_358_low_brake_fluid_warning
        double_tap_action:
          action: none
        hold_action:
          action: none
        tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  red
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1
      -
        type: custom:mushroom-template-card
        icon: mdi:car-brake-parking
        entity: binary_sensor.xpb_358_park_brake_status
        primary: 
        tap_action:
          action: none
        hold_action:
          action: none
        double_tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  red
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1
      -
        type: custom:mushroom-template-card
        secondary: 
        icon: {% set status = states(entity) %}
{% if status == 'on' %}
  mdi:engine
{% else %}
  mdi:engine-off
{% endif %}
        entity: sensor.car_engine
        badge_icon: {% set lock = states('sensor.xpb_358_ignition_state') | float %}
{% if lock == 0 %}
  mdi:lock
{% else %}
  
{% endif %}
        badge_color: {% set lock = states('sensor.xpb_358_ignition_state') | float %}
{% if lock == 0 %}
  green
{% else %}
  
{% endif %}
        double_tap_action:
          action: none
        hold_action:
          action: none
        tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'on' %}
  green
{% else %}
  disabled
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1
      -
        type: custom:mushroom-template-card
        secondary: 
        icon: mdi:tire
        entity: binary_sensor.xpb_358_tire_warning
        double_tap_action:
          action: none
        hold_action:
          action: none
        tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  red
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1
      -
        type: custom:mushroom-template-card
        secondary: 
        icon: mdi:wiper-wash
        entity: binary_sensor.xpb_358_low_wash_water_warning
        badge_color: 
        double_tap_action:
          action: none
        hold_action:
          action: none
        tap_action:
          action: none
        color: {% set status = states(entity) %}
{% if status == 'off' %}
  disabled
{% else %}
  orange
{% endif %}
        vertical: True
        features_position: bottom
        grid_options:
          columns: 2
          rows: 1

` 
### View: Testing

Path: $(@{type=sections; max_columns=4; title=Testing; path=testing; sections=System.Object[]}.path)`n
![View Screenshot](assets/images/view_testing.png)

`yaml
type: sections
max_columns: 4
title: Testing
path: testing
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: New section
      -
        type: custom:streamline-card
        template: area_card
        variables:
          area_name: office
          area_title: Office
          temperature_sensor: sensor.airthings_wave_temperature
          temp_sensor_entity: sensor.bedroom_temperature
        grid_options:
          columns: 6
      -
        type: picture-elements
        entity: light.kitchen_lights
        image: local/rooms/room_kitchen.jpg
        state_filter:
          on: brightness(100%) saturate(1.2)
          off: brightness(40%) grayscale(100%) contrast(150%)
        elements:
          -
            type: custom:button-card
            template:
              - area_base_overlay
            entity: light.kitchen_lights
            card_mod:
              style: ha-card {
  /* Moves border logic here from original for border display */
  {% if is_state('input_select.kitchen_presence','presence') %}
    border: 3px solid rgba(36, 255, 0, 0.8);
  {% elif is_state('input_select.kitchen_presence','idle') %}
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
              z-index: 3
          -
            type: custom:button-card
            template:
              - area_text_element
            name: KITCHEN
            style:
              top: 0%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
          -
            type: custom:button-card
            template: area_text_element
            entity: sensor.kitchen_fridge_door_device_temperature
            show_name: False
            show_icon: False
            show_state: True
            style:
              top: 0%
              left: 50%
              width: 100%
              height: 100%
              z-index: 2
              container-type: inline-size
          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:fan
            layout: vertical
            style:
              top: 75%
              left: 10%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: rotating 1s linear infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:fan
            layout: vertical
            style:
              top: 75%
              left: 26%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: rotating 1s linear infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:door
            layout: vertical
            style:
              top: 75%
              left: 42%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:door
            layout: vertical
            style:
              top: 75%
              left: 58%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:door
            layout: vertical
            style:
              top: 75%
              left: 74%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:button-card
            template: area_status_indicator
            entity: binary_sensor.backyard_door_sensor_contact
            icon: mdi:door
            layout: vertical
            style:
              top: 75%
              left: 90%
              width: 14%
              z-index: 2
              container-type: inline-size
            state:
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      animation: blink 1s ease infinite
                      color: rgba(253,89,89,1)
              -
                operator: ==
                value: off
                styles:
                  icon:
                    -
                      color: #21ff21
            card_mod:
              style: :host {
  {% if '[[entity]]' == '' %}
    display: none;
  {% endif %}
}

          -
            type: custom:timer-bar-card
            entities:
              - timer.kitchen_lights_off_timer
            invert: True
            sync_issues: ignore
            bar_height: 2px
            bar_foreground: orange
            bar_background: #111
            layout: full_row
            text_width: 0px
            bar_width: 100%
            card_mod:
              style: :host {
  width: 100%;
  margin: 0px;
  padding: 0px;
  border: 0px;
}
ha-card {
  left: 44%;
  width: 113%;
  height: 4px;
  padding: 0px;
  z-index: 3;
  margin: 0px;
  margin-top: -39px;
  border: 0px;
  background-color: rgb(0,0,0,0);
  box-shadow: 0px 0px 2px rgb(255,255,255,0);
}

      -
        square: True
        type: grid
        cards:
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: jukka
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: piia
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: anton
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: elias
          -
            type: custom:decluttering-card
            template: family_member
            variables:
              -
                name: alisa
        layout_options:
          grid_columns: full
          grid_rows: auto
        columns: 5

` 

## Notification Center

**ID**: $Id | **URL**: /notification-center | **File**: $F`n
### View: Management

![View Screenshot](assets/images/view_.png)

`yaml
title: Management
icon: mdi:bell-cog
type: sections
max_columns: 5
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: User Management
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: heading
        heading: Add / Update User
        icon: mdi:account-plus
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--green-color);
  --secondary-text-color: var(--green-color);
  --card-mod-icon-color: var(--green-color);
}

      -
        type: markdown
        content: **How to Add a User:**
1. Select a **Home Assistant Person**.
2. Select their **Mobile App Service**.
3. Click **Add User**.
      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_select.notify_mgmt_person_select
            name: Select Person
          -
            type: call-service
            icon: mdi:refresh
            name: Refresh Lists
            action_name: REFRESH
            service: automation.trigger
            service_data:
              entity_id: automation.system_populate_notify_services
              skip_condition: True
          -
            entity: input_select.notify_mgmt_service
            name: Mobile App Service
          -
            entity: input_select.notify_mgmt_platform
            icon: mdi:cellphone-cog
        card_mod:
          style: ha-card {
  border: none;
  --card-mod-icon-color: var(--green-color);
}

      -
        type: tile
        entity: input_select.notify_mgmt_person_select
        name: Add User
        icon: mdi:account-plus
        color: green
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.create_notify_user
        features_position: bottom
        card_mod:
          style: ha-card {
  border: none;
  background: var(--green-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

        grid_options:
          columns: 9
          rows: 1
      -
        type: heading
        heading: Delete User
        icon: mdi:account-remove
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--red-color);
  --card-mod-icon-color: var(--red-color);
}

      -
        type: markdown
        content: **User Cleanup:**

Select a user below and click Delete to remove their notification settings.

      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_select.notify_mgmt_delete_user_select
            name: Select User to Delete
          -
            type: call-service
            icon: mdi:refresh
            name: Refresh User List
            action_name: REFRESH
            service: automation.trigger
            service_data:
              entity_id: automation.system_populate_notify_services
              skip_condition: True
        card_mod:
          style: ha-card {
  border: none;
  --card-mod-icon-color: var(--red-color);
}

      -
        type: tile
        entity: input_select.notify_mgmt_delete_user_select
        name: Delete User
        icon: mdi:account-remove
        color: red
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.delete_notify_user
        features_position: bottom
        card_mod:
          style: ha-card {
  border: none;
  background: var(--red-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

        grid_options:
          columns: 9
          rows: 1
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: Category Management
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: heading
        heading: Add Category
        icon: mdi:playlist-plus
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--green-color);
  --secondary-text-color: var(--green-color);
  --card-mod-icon-color: var(--green-color);
}

      -
        type: markdown
        content: **Add Category:

** Type a new category name below (e.g. 'Garage') and click Add. 

*This adds a switch to all users automatically.*

      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_text.notify_add_category
            name: New Category Name
            icon: mdi:playlist-plus
        card_mod:
          style: ha-card {
  border: none;
  --card-mod-icon-color: var(--green-color);
}

        grid_options:
          columns: 12
      -
        type: tile
        entity: input_text.notify_add_category
        name: Add Category
        icon: mdi:text-box-plus
        color: green
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.add_notify_category_global
        features_position: bottom
        card_mod:
          style: ha-card {
  border: none;
  background: var(--green-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

        grid_options:
          columns: 9
          rows: 1
      -
        type: heading
        heading: Delete Category
        icon: mdi:playlist-remove
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--red-color);
  --secondary-text-color: var(--red-color);
  --card-mod-icon-color: var(--red-color);
}

      -
        type: markdown
        content: **Category Cleanup:**

To delete a category, type the category name below and click the DELETE button.

*This deletes the category from the users and from the settings.*

      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_select.notify_delete_category
            name: Category to Delete
            icon: mdi:playlist-remove
          -
            type: call-service
            icon: mdi:refresh
            name: Refresh Category List
            action_name: REFRESH
            service: automation.trigger
            service_data:
              entity_id: automation.system_populate_notify_services
              skip_condition: True
        card_mod:
          style: ha-card {
  border: none;
  --card-mod-icon-color: var(--red-color);
}

        grid_options:
          columns: 12
      -
        type: tile
        entity: input_select.notify_delete_category
        name: Delete Category
        icon: mdi:text-box-remove
        color: red
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.delete_notify_category_global
        features_position: bottom
        card_mod:
          style: ha-card {
  border: none;
  background: var(--red-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

        grid_options:
          columns: 9
          rows: 1
      -
        type: entities
        entities:
          -
            entity: input_text.notify_mgmt_categories
            name: Master List (ReadOnly)
            icon: mdi:format-list-text
            secondary_info: last-updated
        card_mod:
          style: ha-card {
  border: none;
  --card-mod-icon-color: var(--orange-color);
}

        grid_options:
          columns: 12
          rows: auto
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
        title: Delivery Settings
      -
        type: heading
        heading: Category Settings
        icon: mdi:playlist-check
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--orange-color);
  --secondary-text-color: var(--orange-color);
  --card-mod-icon-color: var(--orange-color);
}

      -
        type: markdown
        content: **Category Delivery Rules**

If the category toggle is on, notification is only sent to users who are currently at home.

* **ON:** Send if person is at **Home**.
* **OFF:** Send always.

      -
        type: custom:auto-entities
        show_empty: True
        card:
          type: entities
          title: Global Delivery Settings
          show_header_toggle: False
          card_mod:
            style: /* hide the header row completely */
.card-header,
.card-header > .name,
.card-header > .menu,
.header {
  display: none !important;
}
/* remove the extra top padding that can remain */
ha-card > :first-child {
  padding-top: 0 !important;
}

        filter:
          template: {% set ns = namespace(rows=[]) %} {# Find switches matching the global category pattern #} {% set switches = states.switch 
   | selectattr('entity_id', 'search', 'notify_category_.*_local') 
   | sort(attribute='name') 
   | list %}

{% if switches | length > 0 %}
  {# Add a single label for all categories with Orange Style #}
  {% set ns.rows = ns.rows + [{
      'type': 'section', 
      'label': 'Categories',
      'card_mod': {
        'style': ".label { color: orange !important; }"
      }
  }] %}

  {% for sw in switches %}
     {% set is_on = is_state(sw.entity_id, 'on') %}
     
     {# Define Icon and Color logic #}
     {% set icon = 'mdi:home-account' if is_on else 'mdi:earth' %}
     {% set color = 'lightgreen' if is_on else '#2196F3' %} {# Standard HA Blue #}
     
     {% set ns.rows = ns.rows + [{
       'entity': sw.entity_id,
       'secondary_info': 'If ON, requires presence',
       'icon': icon,
       'card_mod': {
         'style': ":host { --card-mod-icon-color: " ~ color ~ "; }"
        }
      }] %}
  {% endfor %}
{% endif %}
{{ ns.rows | to_json }}

        sort:
          method: none
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: Subsription Management
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: heading
        heading: User Subscriptions
        icon: mdi:comment-outline
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--orange-color);
  --secondary-text-color: var(--orange-color);
  --card-mod-icon-color: var(--orange-color);
}

      -
        type: markdown
        content: **User Preferences**

*Toggle a switch **OFF** to unsubscribe a specific user from notifications of that category.*

      -
        type: custom:auto-entities
        show_empty: True
        card:
          type: entities
          title: Notification Subscriptions
          show_header_toggle: False
          card_mod:
            style: /* hide the header row completely */
.card-header,
.card-header > .name,
.card-header > .menu,
.header {
  display: none !important;
}
/* remove the extra top padding that can remain */
ha-card > :first-child {
  padding-top: 0 !important;
}

        filter:
          template: {% set ns = namespace(cards=[]) %} {# 1. Find all switches that belong to the notification system (have user_slug attribute) #} {% set switches = states.switch 
   | selectattr('entity_id', 'search', '_notification_') 
   | selectattr('attributes.user_slug', 'defined') 
   | list %}

{# 2. Extract unique users to create groups #} {% set users = switches | map(attribute='attributes.user_slug') | unique | sort | list %}
{% for user in users %}
  {# Filter switches for this specific user #}
  {% set user_switches = switches | selectattr('attributes.user_slug', 'eq', user) | sort(attribute='name') | list %}
  
  {% if user_switches | length > 0 %}
    {# 3. Add Section Header with Orange Style #}
    {% set ns.cards = ns.cards + [{
      'type': 'section', 
      'label': user | capitalize ~ '\'s Subscriptions',
      'card_mod': {
        'style': ".label { color: orange !important; }"
      }
    }] %}
    
    {# 4. Add Switches #}
    {% for sw in user_switches %}
       {% set is_on = is_state(sw.entity_id, 'on') %}
       {% set icon_color = 'green' if is_on else 'red' %}
       {% set icon = 'mdi:email-check' if is_on else 'mdi:email-remove-outline' %}
       
       {# Clean up the name by removing ' Notification' for a cleaner list #}
       {% set clean_name = sw.name | replace(' Notification', '') %}
       
       {% set ns.cards = ns.cards + [{
         'entity': sw.entity_id,
         'name': clean_name,
         'secondary_info': 'last-changed',
         'icon': icon,
         'card_mod': {
           'style': ":host { --card-mod-icon-color: " ~ icon_color ~ "; }"
          }
        }] %}
    {% endfor %}
  {% endif %}
{% endfor %}
{{ ns.cards | to_json }}

        sort:
          method: none
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: Notifications List
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: heading
        heading: Automation Map
        icon: mdi:sitemap
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--orange-color);
  --secondary-text-color: var(--orange-color);
  --card-mod-icon-color: var(--orange-color);
}

      -
        type: markdown
        content: **Notifications Overview**

Lists all notifcation automations grouped by Category Labels. You can turn the automations on or off.

*Tip: Add labels like 'Notify: Electricity' to your automations to see them here.*

      -
        type: custom:auto-entities
        show_empty: True
        card:
          type: entities
          title: Labeled Automations
          show_header_toggle: False
          card_mod:
            style: /* hide the header row completely */
.card-header,
.card-header > .name,
.card-header > .menu,
.header {
  display: none !important;
}
/* remove the extra top padding that can remain */
ha-card > :first-child {
  padding-top: 0 !important;
}

        filter:
          template: {% set ns = namespace(cards=[]) %} {% set all_labels = labels() %} {% set notify_labels = all_labels | select('search', '^notify_') | sort | list %}
{% for label_id in notify_labels %}
  {% set entities = label_entities(label_id) | select('search', '^automation\.') | list %}
  
  {% if entities | length > 0 %}
    {% set display_name = label_id.replace('notify_', '') | capitalize %}
    
    {# Add Section with Orange Label Style #}
    {% set ns.cards = ns.cards + [{
      'type': 'section', 
      'label': display_name ~ ' Notifications',
      'card_mod': {
        'style': ".label { color: orange !important; }"
      }
    }] %}
    
    {% for ent in entities %}
       {% set icon_color = 'lightgreen' if is_state(ent, 'on') else 'red' %}
       {% set ns.cards = ns.cards + [{
         'entity': ent,
         'secondary_info': 'last-triggered',
         'icon': 'mdi:cellphone-message',
         'card_mod': {
           'style': ":host { --card-mod-icon-color: " ~ icon_color ~ "; }"
          }
        }] %}
    {% endfor %}
  {% endif %}
{% endfor %}
{{ ns.cards | to_json }}

        sort:
          method: none
cards:
header:
  card:
    type: markdown
    text_only: True
    content: # Notification Center
Manage Home Assistant App Notifications

` 

## Room Management

**ID**: $Id | **URL**: /room-management | **File**: $F`n
### View: Settings

![View Screenshot](assets/images/view_.png)

`yaml
title: Settings
icon: mdi:home-cog
type: sections
max_columns: 3
sections:
  -
    type: grid
    cards:
      -
        type: heading
        heading: Add / Update Room
        icon: mdi:home-plus
      -
        type: markdown
        content: **Instructions:**

1. Select a **Native Area** from the list.
2. Click **Initialize** to create helpers for it.

*Uses Home Assistant Areas as the source.*

      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_select.room_mgmt_create_select
            name: Select Area
          -
            type: call-service
            icon: mdi:refresh
            name: Refresh Area List
            action_name: REFRESH
            service: automation.trigger
            service_data:
              entity_id: automation.system_populate_room_list
              skip_condition: True
      -
        type: tile
        entity: input_select.room_mgmt_create_select
        name: Initialize Area
        icon: mdi:content-save
        color: green
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.create_room_settings
        card_mod:
          style: ha-card {
  border: none;
  background: var(--green-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

      -
        type: heading
        heading: Danger Zone
        icon: mdi:alert-circle-outline
      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_select.room_mgmt_delete_select
            name: Select Room to Delete
          -
            type: call-service
            icon: mdi:refresh
            name: Refresh Lists
            action_name: REFRESH
            service: automation.trigger
            service_data:
              entity_id: automation.system_populate_room_list
              skip_condition: True
      -
        type: tile
        entity: input_select.room_mgmt_delete_select
        name: Delete Room Config
        icon: mdi:delete
        color: red
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.delete_room_settings
        card_mod:
          style: ha-card {
  border: none;
  background: var(--red-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black; /* Icon visibility fix */
}

  -
    type: grid
    cards:
      -
        type: heading
        heading: Configured Rooms
        icon: mdi:view-dashboard-outline
      -
        type: custom:auto-entities
        show_empty: True
        card:
          type: entities
          show_header_toggle: False
        filter:
          template: {% set ns = namespace(cards=[]) %}
{# Broader search for any select entity with 'automation_mode' in the ID #}
{% set mode_selectors = states.select | selectattr('entity_id', 'search', 'automation_mode') | list %}

{% for sel in mode_selectors %}
  {# Extract slug. Handles "select.bathroom_automation_mode" or "select.room_bathroom_automation_mode" #}
  {% set raw_id = sel.entity_id.split('.')[1] %}
  {% if raw_id.startswith('room_') %}
     {% set slug = raw_id.replace('room_', '').replace('_automation_mode', '') %}
  {% else %}
     {% set slug = raw_id.replace('_automation_mode', '') %}
  {% endif %}
  
  {# UPDATED: Generate Name purely from Slug (Cleaner) #}
  {% set name = slug.replace('_', ' ') | title %}
  
  {# --- Header --- #}
  {% set ns.cards = ns.cards + [{'type': 'section', 'label': name}] %}
  
  {# --- Controls --- #}
  
  {# Mode Selector #}
  {% set ns.cards = ns.cards + [{'entity': sel.entity_id, 'name': 'Mode'}] %}
  
  {# Room State #}
  {% set state_select = 'select.room_' ~ slug ~ '_state' %}
  {% if states[state_select] is defined %}
    {% set ns.cards = ns.cards + [{'entity': state_select, 'name': 'Current State'}] %}
  {% endif %}

  {# Occupancy #}
  {% set occ_sensor = 'binary_sensor.room_' ~ slug ~ '_occupancy' %}
  {% if states[occ_sensor] is defined %}
    {% set ns.cards = ns.cards + [{'entity': occ_sensor, 'name': 'Occupancy'}] %}
  {% endif %}
  
  {# Idle Time #}
  {% set idle_entity = 'number.' ~ slug ~ '_presence_idle_time' %}
  {% if states[idle_entity] is defined %}
    {% set ns.cards = ns.cards + [{'entity': idle_entity, 'name': 'Idle Time (sec)'}] %}
  {% endif %}
  
  {# Off Delay #}
  {% set delay_entity = 'number.' ~ slug ~ '_lights_presence_delay' %}
  {% if states[delay_entity] is defined %}
    {% set ns.cards = ns.cards + [{'entity': delay_entity, 'name': 'Off Delay (sec)'}] %}
  {% endif %}
  
  {# Lux Sensor #}
  {% set lux_s = 'text.room_' ~ slug ~ '_lux_sensor' %}
  {% if states[lux_s] is defined %}
    {% set ns.cards = ns.cards + [{'entity': lux_s, 'name': 'Lux Sensor ID'}] %}
  {% endif %}
  
  {# Lux Threshold #}
  {% set lux_t = 'number.room_' ~ slug ~ '_lux_threshold' %}
  {% if states[lux_t] is defined %}
     {% set ns.cards = ns.cards + [{'entity': lux_t, 'name': 'Lux Threshold (lx)'}] %}
  {% endif %}
  
  {# Bed Sensor #}
  {% set bed_s = 'text.room_' ~ slug ~ '_bed_sensor' %}
  {% if states[bed_s] is defined %}
    {% set ns.cards = ns.cards + [{'entity': bed_s, 'name': 'Bed Sensor ID'}] %}
  
    {# Only show sleep timers if a bed sensor ID is entered #}
    {% if states(bed_s) not in ['unknown', 'unavailable', '', 'none'] %}
       {% set sleep_entry = 'number.room_' ~ slug ~ '_sleep_entry_delay' %}
       {% if states[sleep_entry] is defined %}
         {% set ns.cards = ns.cards + [{'entity': sleep_entry, 'name': 'Sleep Entry Delay (sec)'}] %}
       {% endif %}
       
       {% set sleep_exit = 'number.room_' ~ slug ~ '_sleep_exit_delay' %}
       {% if states[sleep_exit] is defined %}
         {% set ns.cards = ns.cards + [{'entity': sleep_exit, 'name': 'Sleep Exit Delay (sec)'}] %}
       {% endif %}
    {% endif %}
  {% endif %}
  
{% endfor %}
{{ ns.cards | to_json }}

        sort:
          method: none

` 

## Home Access

**ID**: $Id | **URL**: /home-access | **File**: $F`n
### View: Fingerprints

![View Screenshot](assets/images/view_.png)

`yaml
title: Fingerprints
icon: mdi:fingerprint
type: sections
sections:
  -
    type: grid
    cards:
      -
        type: custom:mushroom-title-card
        title: Access Management
        alignment: center
        title_tap_action:
          action: none
        subtitle_tap_action:
          action: none
      -
        type: heading
        heading: Fingerprint Registry
        icon: mdi:fingerprint
        heading_style: title
        card_mod:
          style: ha-card {
  border: none;
  --primary-text-color: var(--orange-color);
  --secondary-text-color: var(--orange-color);
  --card-mod-icon-color: var(--orange-color);
}

      -
        type: markdown
        content: 
### ðŸ“‹ Instructions:
---

1. All fingerprints must be first scanned in Unifi Protect and assigned to persons.

2. When person scans the fingerprint the first time, it will show up as unknown or unassigned.

3. Only assigned fingerprints allow door lock to be opened by scanning the fingerprint.
      -
        type: custom:auto-entities
        show_empty: True
        card:
          type: entities
          title: Registered Fingerprints
          show_header_toggle: False
        filter:
          template: {% set ns = namespace(cards=[]) %}
{% for state in states.select %}
  {% if state.entity_id.startswith('select.fingerprint_') %}
    {# Get the full ID from attributes #}
    {% set full_id = state.attributes.ulp_id | default('-unassigned-') %}
    
    {# Check if assigned #}
    {% set assigned = state.state %}
    {% if assigned in ['-Unassigned-', '-unassigned-', 'Unknown', 'unknown', 'unavailable'] %}
      {% set icon_color = 'red' %}
      {% set label = 'ðŸ”´ ' ~ full_id %}
    {% else %}
      {% set icon_color = 'green' %}
      
      {# Robust Name Cleaner for Dropdown Label #}
      {% set clean = assigned.replace(' Notifications', '').replace(' Notification', '') %}
      {% set parts = clean.split(' ') %}
      {% if parts | length > 1 and parts[0] == parts[-1] %}
        {% set clean_name = parts[0] %}
      {% else %}
        {% set clean_name = clean %}
      {% endif %}
      
      {% set label = 'ðŸŸ¢ ' ~ full_id %}
    {% endif %}

    {% set ns.cards = ns.cards + [{
        'entity': state.entity_id,
        'name': label,
        'secondary_info': full_id,
        'icon': 'mdi:fingerprint'
    }] %}
  {% endif %}
{% endfor %}
{{ ns.cards | to_json }}


        sort:
          method: state
          reverse: False
      -
        type: tile
        entity: input_text.notify_add_category
        name: Refresh User Lists
        icon: mdi:account-sync
        color: green
        show_entity_picture: False
        vertical: False
        tap_action:
          action: call-service
          service: script.refresh_fingerprint_users
        features_position: bottom
        card_mod:
          style: ha-card {
  border: none;
  background: var(--green-color);
  --primary-text-color: white;
  --secondary-text-color: white;
  --card-mod-icon-color: black;
}

        grid_options:
          columns: 6
          rows: 1
      -
        type: markdown
        content: ## <ha-icon icon="mdi:fingerprint"></ha-icon> Registred Fingerprint IDs



| <font color=orange>Assigned User</font> | <font color=orange>Fingerprint ID</font> |
| :--- | :--- |
{% set fingerprints = states.select | selectattr('entity_id', 'search', '^select\.fingerprint_') | list -%}
{% for state in fingerprints | sort(attribute='state') -%}
{% set assigned = state.state | default('Unknown') -%}
{% if assigned in ['Unknown', 'unknown', 'unavailable'] -%}
| **{{ assigned }}** | `{{ (state.attributes.ulp_id | default('unknown')).strip() }}` |
{% else -%}
{% set clean = assigned.replace(' Notifications', '').replace(' Notification', '') -%}
{% set parts = clean.split(' ') -%}
{% if parts | length > 1 and parts[0] == parts[-1] -%}
{% set display_name = parts[0] -%}
{% else -%}
{% set display_name = clean -%}
{% endif -%}
| **{{ display_name }}** | `{{ (state.attributes.ulp_id | default('unknown')).strip() }}` |
{% endif -%}
{% else -%}
| No fingerprints | found yet |
{% endfor %}

  -
    type: grid
    cards:
      -
        type: heading
        heading: Manual Management
        icon: mdi:tools
      -
        type: entities
        show_header_toggle: False
        entities:
          -
            entity: input_text.fingerprint_mgmt_id
            name: Fingerprint ID (ULP)
      -
        type: button
        name: Add / Update ID
        icon: mdi:plus-box
        tap_action:
          action: call-service
          service: script.add_fingerprint_entity
          service_data:
            ulp_id: {{ states('input_text.fingerprint_mgmt_id') }}
            current_user: Unknown
        card_mod:
          style: ha-card { color: green; --paper-item-icon-color: green; }

      -
        type: button
        name: Delete ID
        icon: mdi:delete
        tap_action:
          action: call-service
          service: script.delete_fingerprint_entity
          service_data:
            ulp_id: {{ states('input_text.fingerprint_mgmt_id') }}
        card_mod:
          style: ha-card { color: red; --paper-item-icon-color: red; }

header:
  card:
    type: markdown
    text_only: True
    content: # Home Access Center

` 

## Zigbee2MQTT

**ID**: $Id | **URL**: /dashboard-zigbee2mqtt | **File**: $F`n

