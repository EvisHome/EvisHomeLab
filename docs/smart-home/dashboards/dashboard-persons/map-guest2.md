---
tags:
  - dashboard
  - view
  - automated
---

# Map Guest 2

**Dashboard:** Persons  
**Path:** `map-Guest 2`

![View Screenshot](../../../assets/images/dashboards/view_dashboard-persons_map-guest2.png)

## Configuration
```yaml
theme: Backend-selected
title: Map Guest 2
path: map-Guest 2
type: panel
subview: true
badges: []
cards:
- type: map
  entities:
  - entity: person.Guest 2
  hours_to_show: 48

```
