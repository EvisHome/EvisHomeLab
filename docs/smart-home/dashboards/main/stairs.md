---
tags:
  - dashboard
  - view
  - automated
---

# Stairs

**Dashboard:** Main Dashboard  
**Path:** `stairs`

## Related Packages
This view contains entities managed by:

* [Scenes](../../packages/scenes.md)


![View Screenshot](../../../assets/images/dashboards/dashboard_main_stairs.png)

## Configuration
```yaml
title: Stairs
path: stairs
type: sections
max_columns: 5
subview: true
sections:
- type: grid
  cards:
  - type: custom:streamline-card
    template: area_card
    variables:
      area_name: stairs
      area_title: Stairs
      temperature_sensor: sensor.airthings_wave_temperature
  - type: custom:mushroom-title-card
    title: ''
    subtitle: LIGHTS
    alignment: center
  - type: custom:mushroom-light-card
    entity: light.stairs_wled
    layout: vertical
    icon: mdi:led-strip-variant
    fill_container: true
    show_brightness_control: true
    show_color_control: false
    use_light_color: true
    grid_options:
      columns: 6
      rows: 3
  - type: custom:mushroom-select-card
    entity: select.stairs_wled_preset
    name: Stairs Preset
    fill_container: true
    layout: vertical
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: SETTINGS
    subtitle: OCCUPANCY SETTINGS
    alignment: center
  - type: custom:decluttering-card
    template: area_occupancy_settings
    variables:
    - area: stairs
    - area_name: Stairs
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
    - input_select.stairs_automation_mode
    - light.stairs_lights
    - light.stairs_wled
    exclude: []
    discover_existing: false
    tags:
    - stairs
    time_step: 1
    show_header_toggle: false
    title: false
cards: []

```
