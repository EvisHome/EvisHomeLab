---
tags:
  - dashboard
  - view
  - automated
---

# Settings

**Dashboard:** Main Dashboard  
**Path:** `settings`

![View Screenshot](../../../assets/images/dashboards/dashboard_main_settings.png)

## Configuration
```yaml
title: Settings
path: settings
cards: []
type: sections
sections:
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: kitchen
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: hallway
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: stairs
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: lobby
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: living_room
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: toilet
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: bedroom
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: office
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: mud_room
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: storage
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: bathroom
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: backyard
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: front_door
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: Guest 2
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: Guest 3
- type: grid
  cards:
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: Daughter
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: sauna
- type: grid
  cards:
  - type: custom:decluttering-card
    template: place_presence_settings
    variables:
    - area: shower
  - type: custom:decluttering-card
    template: place_presence_settings
    variables:
    - area: bathroom_toilet
  - type: custom:decluttering-card
    template: place_presence_settings
    variables:
    - area: sofa
max_columns: 7

```
