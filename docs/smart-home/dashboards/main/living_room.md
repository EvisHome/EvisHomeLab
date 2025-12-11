---
tags:
  - dashboard
  - view
  - automated
---

# Living Room

**Dashboard:** Main Dashboard  
**Path:** `living_room`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_living_room.png)

## Related Packages
This view contains entities managed by:

* [Airthings](../../packages/airthings.md)
* [Room Automation](../../packages/room_automation.md)
* [Scenes](../../packages/scenes.md)
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:decluttering-card`
* `custom:mini-graph-card`
* `custom:mushroom-entity-card`
* `custom:mushroom-fan-card`
* `custom:mushroom-light-card`
* `custom:mushroom-select-card`
* `custom:mushroom-template-card`
* `custom:mushroom-title-card`
* `custom:streamline-card`


## Configuration
```yaml+jinja
theme: Backend-selected
title: Living Room
type: sections
layout:
  max_cols: 5
subview: true
badges: []
cards: []
sections:
- type: grid
  cards:
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
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: ENVIRONMENT
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:decluttering-card
        template: minigraph_co2
        variables:
        - sensor: sensor.airthings_wave_living_room_co2
      - type: custom:decluttering-card
        template: minigraph_temperature
        variables:
        - sensor: sensor.airthings_wave_temperature
      - type: custom:decluttering-card
        template: minigraph_humidity
        variables:
        - sensor: sensor.airthings_wave_humidity
      - type: custom:mini-graph-card
        entities:
        - entity: sensor.airthings_wave_living_room_voc
          name: VOC
        font_size_header: 12
        font_size: 75
        line_width: 8
        height: 200
        animate: true
        hours_to_show: 24
        show:
          points: false
        color_thresholds:
        - value: 250
          color: '#5FE787'
        - value: 500
          color: '#FF9800'
        - value: 2000
          color: '#FF535B'
        card_mod:
          style: |-
            .header.flex .icon {
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
      - type: custom:mini-graph-card
        entities:
        - entity: sensor.airthings_wave_living_room_radon_1_day_average
          name: Radon Short
        font_size_header: 12
        font_size: 75
        line_width: 8
        height: 200
        animate: true
        hours_to_show: 24
        show:
          points: false
        color_thresholds:
        - value: 100
          color: '#5FE787'
        - value: 150
          color: '#FF9800'
        - value: 200
          color: '#FF535B'
        card_mod:
          style: |-
            .header.flex .icon {
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
      - type: custom:mini-graph-card
        entities:
        - entity: sensor.airthings_wave_living_room_radon_longterm_average
          name: Radon Long
        font_size_header: 12
        font_size: 75
        line_width: 8
        height: 200
        animate: true
        hours_to_show: 24
        show:
          points: false
        color_thresholds:
        - value: 100
          color: '#5FE787'
        - value: 150
          color: '#FF9800'
        - value: 200
          color: '#FF535B'
        card_mod:
          style: |-
            .header.flex .icon {
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
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - square: false
      columns: 2
      type: grid
      cards:
      - type: custom:mushroom-light-card
        entity: light.living_room_ceiling_light
        fill_container: false
        use_light_color: false
        show_brightness_control: true
        show_color_control: false
        show_color_temp_control: false
        collapsible_controls: false
        name: Ceiling
        icon: ''
      - type: custom:mushroom-light-card
        entity: light.floor_light
        show_brightness_control: true
        show_color_control: false
        show_color_temp_control: false
        use_light_color: false
        icon: mdi:floor-lamp
      - type: custom:mushroom-light-card
        entity: light.hallway_ceiling_light
        show_brightness_control: true
      - type: custom:mushroom-light-card
        entity: light.stairs_wled
        show_brightness_control: true
  - type: custom:mushroom-entity-card
    entity: switch.christmas_tree_plug
    icon: mdi:pine-tree
    layout: vertical
    name: Christmas Tree
    fill_container: true
    icon_color: accent
    visibility:
    - condition: state
      entity: switch.christmas_tree_plug
      state_not: unavailable
    - condition: state
      entity: switch.christmas_tree_plug
      state_not: unknown
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: AIR PURIFIER
      alignment: center
    - square: false
      columns: 1
      type: grid
      cards:
      - type: custom:mushroom-fan-card
        entity: fan.philips_air_purifier
        show_percentage_control: true
        layout: horizontal
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        card_mod:
          style: |-
            ha-card {
              border-bottom-right-radius: 0px;
              border-bottom-left-radius: 0px;
            }
      - square: false
        columns: 4
        type: grid
        cards:
        - type: custom:mushroom-template-card
          entity: fan.philips_air_purifier
          primary: Auto
          secondary: ''
          icon: mdi:fan
          layout: vertical
          icon_color: |-
            {% set status = states(entity) %}
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
                $: |-
                  .shape ha-icon
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
                .: |-
                  ha-card {
                    border-radius: 0px;
                    box-shadow: 0px 0px;
                    background-color: rgba(0,0,0,0);
                    border: 5px solid #222;
                  }
                  :host {
                  }
        - type: custom:mushroom-template-card
          entity: fan.philips_air_purifier
          primary: Allergen
          secondary: ''
          icon: mdi:fan
          layout: vertical
          icon_color: |-
            {% set status = states(entity) %}
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
                $: |-
                  .shape ha-icon
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
                .: |-
                  ha-card {
                    border-radius: 0px;
                    box-shadow: 0px 0px;
                    background-color: rgba(0,0,0,0);
                    border: 5px solid #222;
                  }
                  :host {
                  }
        - type: custom:mushroom-template-card
          entity: fan.philips_air_purifier
          primary: Night
          secondary: ''
          icon: mdi:fan
          layout: vertical
          icon_color: |-
            {% set status = states(entity) %}
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
                $: |-
                  .shape ha-icon
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
                .: |-
                  ha-card {
                    border-radius: 0px;
                    box-shadow: 0px 0px;
                    background-color: rgba(0,0,0,0);
                    border: 5px solid #222;
                  }
                  :host {
                  }
        - type: custom:mushroom-template-card
          entity: fan.philips_air_purifier
          primary: Manual
          secondary: ''
          icon: mdi:fan
          layout: vertical
          icon_color: |-
            {% set status = states(entity) %}
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
                $: |-
                  .shape ha-icon
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
                .: |-
                  ha-card {
                    border-radius: 0px;
                    box-shadow: 0px 0px;
                    background-color: rgba(0,0,0,0);
                    border: 5px solid #222;
                  }
                  :host {
                  }
      - square: false
        columns: 3
        type: grid
        cards:
        - type: custom:mushroom-template-card
          entity: sensor.philips_air_purifier_pre_filter
          primary: Pre-filter
          secondary: '{{ states(entity) }} hours'
          icon: mdi:air-filter
          icon_color: |-
            {% set value = states(entity) | int
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
            style: |-
              :host { display:
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
        - type: custom:mushroom-template-card
          entity: sensor.philips_air_purifier_hepa_filter
          primary: Hepa
          secondary: '{{ states(entity) }} hours'
          icon: mdi:air-filter
          icon_color: |-
            {% set value = states(entity) | int
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
            style: |-
              :host { display:
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
        - type: custom:mushroom-template-card
          entity: sensor.philips_air_purifier_carbon_filter
          primary: Carbon
          secondary: '{{ states(entity) }} hours'
          icon: mdi:air-filter
          icon_color: |-
            {% set value = states(entity) | int
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
            style: |-
              :host { display:
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
      - square: false
        columns: 1
        type: grid
        cards:
        - type: custom:mushroom-template-card
          primary: ''
          secondary: AC1214/10
          icon: ''
          entity: fan.philips_air_purifier
          card_mod:
            style: |-
              ha-card {
                border-top-right-radius: 0px;
                border-top-left-radius: 0px;
              }
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      alignment: center
      subtitle: FIREPLACE
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-light-card
        entity: light.fireplace
        fill_container: true
        layout: vertical
        name: Fireplace
      - type: custom:mushroom-select-card
        entity: select.fireplace_preset
        name: Fireplace Preset
      columns: 2
    - type: custom:mushroom-entity-card
      entity: number.fireplace_fade_timeout
      icon: mdi:camera-timer
  - square: false
    columns: 1
    type: grid
    cards:
    - type: custom:mushroom-title-card
      title: ''
      alignment: center
      subtitle: REMOTE CONTROLS
    - square: false
      columns: 3
      type: grid
      cards:
      - type: custom:mushroom-entity-card
        entity: input_button.tv_remote_button
        icon: mdi:remote-tv
        name: TV
        secondary_info: none
        icon_color: orange
        fill_container: true
        layout: vertical
        tap_action:
          action: navigate
          navigation_path: /dashboard-popups/tv-remote
      - type: custom:mushroom-entity-card
        entity: input_button.tv_remote_button
        icon: mdi:remote
        name: SOUNDBAR
        secondary_info: none
        icon_color: orange
        fill_container: true
        layout: vertical
        tap_action:
          action: navigate
          navigation_path: /dashboard-popups/soundbar-remote
      - type: custom:mushroom-entity-card
        entity: switch.remote_fix
        icon: mdi:auto-fix
        layout: vertical
        fill_container: true
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
            skip_condition: true
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: WALL OUTLETS
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-entity-card
        entity: sensor.living_room_media_outlet_power
        layout: vertical
        name: Media Wall Outlet
        fill_container: true
        icon_color: accent
      - type: custom:mushroom-entity-card
        entity: switch.living_room_media_outlet
        layout: vertical
        name: Media Wall Outlet
        tap_action:
          action: none
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        fill_container: true
        icon_color: green
      - type: custom:mushroom-entity-card
        entity: sensor.living_room_desk_outlet_channel_1_power
        layout: vertical
        fill_container: true
        name: Desk Wall Outlet
        icon_color: accent
      - type: custom:mushroom-entity-card
        entity: switch.air_purifier_plug
        layout: vertical
        name: Air Purifier Plug
        tap_action:
          action: none
        hold_action:
          action: more-info
        double_tap_action:
          action: none
        fill_container: true
        icon_color: green
      columns: 2
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SOFA OUTLETS
      alignment: center
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: BATTERY LEVELS
      alignment: center
    - type: custom:auto-entities
      card:
        type: entities
      filter:
        include:
        - entity_id: sensor.*living_room*battery*
        - entity_id: sensor.*back_door*battery*
        exclude: []
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: DEVICES
    - type: horizontal-stack
      cards:
      - type: entities
        entities:
        - entity: sensor.airthings_wave_living_room_co2
        - entity: sensor.airthings_wave_living_room_humidity
        - entity: sensor.airthings_wave_living_room_pressure
        - entity: sensor.airthings_wave_living_room_radon_1_day_average
        - entity: sensor.airthings_wave_living_room_radon_longterm_average
        - entity: sensor.airthings_wave_living_room_temperature
        - entity: sensor.airthings_wave_living_room_voc
        - entity: sensor.airthings_wave_living_room_illuminance
        - entity: sensor.airthings_wave_living_room_battery
        - type: section
          label: Sensors
        - entity: sensor.philips_air_purifier_pm25
        - entity: sensor.philips_air_purifier_allergen_index
        - type: section
          label: Air Purifier
        - entity: fan.philips_air_purifier
        - entity: switch.air_purifier_plug
          name: Air Purifier Power Plug
        - entity: sensor.philips_air_purifier_pre_filter
        - entity: sensor.philips_air_purifier_carbon_filter
        - entity: sensor.philips_air_purifier_hepa_filter
        - type: section
          label: Presense
        show_header_toggle: false
        state_color: true
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: OCCUPANCY SETTINGS
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: living_room
    - area_name: Living Room
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
  - type: history-graph
    entities:
    - entity: binary_sensor.living_room_fp2_sensor
      name: Presence
    - entity: input_select.sofa_presence
      name: Sofa
    hours_to_show: 12
max_columns: 4
path: living_room

```
