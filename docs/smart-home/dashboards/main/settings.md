---
tags:
  - dashboard
  - view
  - automated
---

# Settings

**Dashboard:** Main Dashboard  
**Path:** `settings`

<!-- START_DESCRIPTION -->
Global system settings for occupancy sensitivity, timeouts, and automation flags across all zones.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_settings.png)

## Summary
<!-- START_SUMMARY -->
This view serves as the global control panel for the home's automation logic. It provides a grid of identical configuration cards for every room (e.g., Kitchen, Hallway, Office) and specific sub-zones (e.g., Shower, Sofa). Each card, based on the `presence_settings` template, allows users to fine-tune occupancy timeouts, sensitivity thresholds, and enable/disable specific automation behaviors for that area.
<!-- END_SUMMARY -->



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`


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
    - area: Guest-2
  - type: custom:decluttering-card
    template: presence_settings
    variables:
    - area: Guest-3
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
