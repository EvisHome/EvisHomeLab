---
tags:
  - dashboard
  - view
  - automated
---

# Map Evis

**Dashboard:** Persons  
**Path:** `map-Evis`

![View Screenshot](../../../assets/images/dashboards/view_dashboard-persons_map-evis.png)

## Configuration
```yaml
theme: Backend-selected
subview: true
title: Map Evis
path: map-Evis
type: panel
badges: []
cards:
- type: map
  entities:
  - entity: person.Evis
  dark_mode: false
  hours_to_show: 48

```
