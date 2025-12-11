---
tags:
  - dashboard
  - view
  - automated
---

# Office

**Dashboard:** Main Dashboard  
**Path:** `office`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_office.png)

## Related Packages
This view contains entities managed by:

* [Office. Pc](../../packages/office._pc.md)
* [Scenes](../../packages/scenes.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:apexcharts-card`
* `custom:auto-entities`
* `custom:card-mod`
* `custom:decluttering-card`
* `custom:mini-graph-card`
* `custom:mushroom-cover-card`
* `custom:mushroom-entity-card`
* `custom:mushroom-light-card`
* `custom:mushroom-select-card`
* `custom:mushroom-template-card`
* `custom:mushroom-title-card`
* `custom:scheduler-card`
* `custom:streamline-card`
* `custom:uptime-card`


## Configuration
```yaml+jinja
theme: Backend-selected
title: Office
type: sections
layout:
  max_cols: 5
subview: true
badges: []
cards: []
max_columns: 6
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: office
      area_title: Office
      temperature_sensor: sensor.airthings_wave_temperature
      temp_sensor_entity: sensor.bedroom_temperature
    grid_options:
      columns: 12
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
        - sensor: sensor.bedroom_carbon_dioxide
      - type: custom:decluttering-card
        template: minigraph_temperature
        variables:
        - sensor: sensor.bedroom_temperature
      - type: custom:decluttering-card
        template: minigraph_humidity
        variables:
        - sensor: sensor.bedroom_humidity
      columns: 3
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: LIGHTS
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-light-card
        entity: light.wled_2
        layout: vertical
        show_color_control: false
        show_brightness_control: true
        name: Desk
        use_light_color: true
      - type: custom:mushroom-light-card
        entity: light.server_cabinet_light
        layout: vertical
        show_brightness_control: true
        name: Rack
        use_light_color: true
        show_color_temp_control: false
        show_color_control: false
        collapsible_controls: false
        fill_container: true
      - type: custom:mushroom-light-card
        entity: light.bedroom_ceiling_light
        name: Ceiling
        layout: vertical
        show_brightness_control: true
        use_light_color: true
      - type: custom:mushroom-light-card
        entity: light.office_desk_wall_light
        name: Wall
        layout: vertical
        show_brightness_control: true
        use_light_color: true
      columns: 4
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-select-card
        entity: select.wled_preset_2
        name: Office Desk Presets
      columns: 1
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: WINDOW
      alignment: center
    - square: false
      columns: 2
      type: grid
      cards:
      - type: custom:mushroom-cover-card
        entity: cover.bedroom_window_blinds
        show_position_control: true
        show_buttons_control: false
        tap_action:
          action: none
        name: Blinds
        layout: vertical
      - type: custom:mushroom-cover-card
        entity: cover.bedroom_window_roller_cover
        fill_container: false
        show_position_control: false
        show_buttons_control: true
        tap_action:
          action: none
        name: Roller Blind
        layout: vertical
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: PC
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-template-card
        primary: Audio Device
        secondary: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            Speakers
          {% else %}
            Headset
          {% endif %}
        icon: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            mdi:speaker-multiple
          {% else %}
            mdi:headphones
          {% endif %}
        layout: vertical
        entity: switch.officepc_audio_device
        tap_action:
          action: toggle
        icon_color: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            green
          {% else %}
            orange
          {% endif %}
      - type: custom:mushroom-entity-card
        entity: button.officepc_mediaplaypause
        name: Play | Pause
        icon: mdi:play-pause
        icon_color: blue
        layout: vertical
        secondary_info: last-changed
        fill_container: true
        tap_action:
          action: call-service
          service: button.press
          target:
            entity_id: button.officepc_mediaplaypause
          data: {}
      - type: custom:mushroom-template-card
        primary: Audio Mute
        secondary: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            Muted
          {% else %}
           Volume {{ states('sensor.officepc_audio_default_device_volume') }}
          {% endif %}
        icon: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            mdi:volume-mute
          {% else %}
            mdi:volume-high
          {% endif %}
        layout: vertical
        entity: switch.officepc_audio_mute
        tap_action:
          action: toggle
        icon_color: |-
          {% set status = states(entity) %}
          {% if status == 'on' %}
            red
          {% else %}
            green
          {% endif %}
  - type: custom:mushroom-entity-card
    entity: switch.office_pc_power
    layout: vertical
    fill_container: true
    icon_color: green
    tap_action:
      action: none
    hold_action:
      action: toggle
    name: PC Power
  - type: custom:mushroom-template-card
    primary: Displays
    secondary: |-
      {% set status = states(entity) %}
      {% if status == 'on' %}
        On
      {% else %}
       Off
      {% endif %}
    icon: |-
      {% set status = states(entity) %}
      {% if status == 'on' %}
        mdi:monitor
      {% else %}
        mdi:monitor-off
      {% endif %}
    layout: vertical
    entity: switch.officepc_displays
    tap_action:
      action: toggle
    icon_color: |-
      {% set status = states(entity) %}
      {% if status == 'on' %}
        green
      {% else %}
        red
      {% endif %}
    fill_container: true
  - type: history-graph
    entities:
    - entity: switch.office_pc_power
      name: ''
  - type: custom:apexcharts-card
    graph_span: 12h
    show:
      loading: false
    apex_config:
      chart:
        height: 120px
      grid:
        show: true
        borderColor: rgba(255,255,255,0.2)
      legend:
        show: false
    header:
      show: true
      show_states: true
      colorize_states: true
      standard_format: false
    all_series_config:
      stroke_width: 2
    yaxis:
    - min: 0
      max: 100
      decimals: 0
      apex_config:
        tickAmount: 4
    series:
    - entity: sensor.officepc_memoryusage
      type: area
      opacity: 0.3
      name: Memory
      color: skyblue
      float_precision: 0
      fill_raw: zero
      group_by:
        func: max
      show:
        legend_value: false
    - entity: sensor.officepc_cpuload
      type: area
      opacity: 0.3
      name: CPU
      color: orange
      float_precision: 0
      fill_raw: zero
      group_by:
        func: max
      show:
        legend_value: false
    card_mod:
      style: |-
        ha-card {
          padding-top: 12px;
        }
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: POWER OUTLETS
      alignment: center
    - type: grid
      cards:
      - type: custom:mini-graph-card
        name: Desk
        entities:
        - entity: sensor.office_desk_outlet_power
          name: Power
        icon: mdi:flash
        font_size_header: 12
        font_size: 75
        line_width: 8
        hours_to_show: 24
      - type: custom:mini-graph-card
        name: Modem
        entities:
        - entity: sensor.shellyplusplugs_b0b21c1991a8_switch_0_power
          name: Power
        icon: mdi:flash
        font_size_header: 12
        font_size: 75
        line_width: 8
        hours_to_show: 24
      - type: custom:mini-graph-card
        name: Rack
        entities:
        - entity: sensor.rack_power_plug_power
          name: Power
        icon: mdi:flash
        font_size_header: 12
        font_size: 75
        line_width: 8
        hours_to_show: 24
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: PROXMOX VE
      subtitle: ''
      alignment: center
    - type: custom:uptime-card
      entity: binary_sensor.node_halo_status
      icon: mdi:heart-pulse
      title_template: UPTIME
      hours_to_show: 168
      alignment:
        status: spaced
        header: center
        icon_first: false
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
    - square: false
      type: grid
      cards:
      - type: custom:apexcharts-card
        graph_span: 48h
        show:
          loading: false
        header:
          show: true
          title: MEMORY
          standard_format: false
          show_states: true
          colorize_states: true
        color_list:
        - green
        - rgba(253,80,80,1)
        - skyblue
        all_series_config:
          stroke_width: 2
          opacity: 1
        chart_type: donut
        series:
        - entity: sensor.node_halo_memory_free
          name: Free MEM
          unit: GB
          show:
            in_header: false
        - entity: sensor.node_halo_memory_used
          name: Used MEM
          show:
            in_header: false
        - entity: sensor.node_halo_memory_total_2
          name: Total
          show:
            in_chart: false
        card_mod:
          style: |-
            ha-card {
              padding-bottom: 20px;
            }
      - type: custom:apexcharts-card
        graph_span: 48h
        show:
          loading: false
        header:
          show: true
          title: SSD10
          standard_format: false
          show_states: true
          colorize_states: true
        color_list:
        - green
        - rgba(253,80,80,1)
        - skyblue
        all_series_config:
          stroke_width: 2
          opacity: 1
        chart_type: donut
        series:
        - entity: sensor.storage_ssd10_disk_free
          name: Free
          unit: GB
          show:
            in_header: false
        - entity: sensor.storage_ssd10_disk_used
          name: Used
          show:
            in_header: false
        - entity: sensor.storage_ssd10_disk_total
          name: Total
          show:
            in_chart: false
        card_mod:
          style: |-
            ha-card {
              padding-bottom: 20px;
            }
      columns: 2
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: PROXMOX VE
      alignment: center
    - square: false
      type: grid
      cards:
      - type: custom:mushroom-entity-card
        entity: binary_sensor.qemu_vm_homeassistantos_150_status
        layout: vertical
        fill_container: true
        name: HAOS
      - type: custom:mini-graph-card
        title: Home Assistant
        font_size_header: 12
        font_size: 70
        decimals: 0
        height: 200
        entities:
        - entity: sensor.qemu_vm_homeassistantos_150_cpu_used
          name: CPU
          color: orange
          show_state: true
        - entity: sensor.qemu_vm_homeassistantos_150_memory_used_percentage
          name: MEM
          color: lightgreen
          show_state: true
      - square: false
        type: grid
        cards:
        - type: custom:mushroom-entity-card
          entity: sensor.qemu_vm_homeassistantos_150_uptime
          layout: horizontal
          fill_container: true
          name: Uptime
        - type: custom:mushroom-entity-card
          entity: binary_sensor.qemu_vm_homeassistantos_150_health
          layout: horizontal
          fill_container: true
          name: Health
        - type: custom:mushroom-entity-card
          entity: sensor.qemu_vm_homeassistantos_150_node
          layout: horizontal
          fill_container: false
          name: Node
        columns: 1
      columns: 3
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    alignment: center
    subtitle: OCCUPANCY SETTINGS
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: office
    - area_name: Office
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: ''
      subtitle: SCHEDULES
      alignment: center
    - type: markdown
      content: These schedules work when they are set on and _Presence Automation
        Mode_ is set to _Schedule Mode_
  - type: custom:scheduler-card
    include:
    - input_select.office_automation_mode
    - light.office_desk_wall_light
    - light.office_lights
    exclude: []
    discover_existing: false
    tags:
    - living-room
    time_step: 1
    show_header_toggle: false
    title: false
  - type: custom:mushroom-title-card
    title: ''
    subtitle: AUTOMATION MODE SCHEDULES
    alignment: center
  - type: markdown
    content: Automation Mode Changes, based on time or sun.
  - type: custom:scheduler-card
    include:
    - input_select.office_automation_mode
    exclude: []
    discover_existing: false
    tags:
    - office-mode-control
    time_step: 1
    show_header_toggle: false
    title: false
- type: grid
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-title-card
      title: null
      alignment: center
      subtitle: Battery Levels
    - type: custom:auto-entities
      card:
        type: entities
      filter:
        include:
        - entity_id: sensor.office*battery*
        exclude: []
  - type: markdown
    content: |-
      **Automation Modes**

      _Presence Control:_ Lights are automatically controlled by the occupancy state of the room.

      _Absence Detection:_ When room is no longer occupied, lights will be turned off after a the absence delay time.

      _Schedule Mode:_ Light schedules are working as set in the Scheduler. (schedule-mode condition)
  - type: custom:scheduler-card
    include:
    - input_select.living_room_automation_mode
    - light.floor_light
    - light.living_room_ceiling_light
    - light.living_room_lights
    exclude: []
    discover_existing: false
    tags:
    - living-room
    time_step: 1
    show_header_toggle: false
    title: true
- type: grid
  cards: []
path: office

```
