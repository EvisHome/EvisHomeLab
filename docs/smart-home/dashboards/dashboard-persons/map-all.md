---
tags:
  - dashboard
  - view
  - automated
---

# Map All

**Dashboard:** Persons  
**Path:** `map-all`



![View Screenshot](../../../assets/images/dashboards/dashboard_map-all.png)

## Configuration
```yaml
theme: Backend-selected
title: Map All
path: map-all
type: panel
badges: []
cards:
- type: map
  entities:
  - entity: person.Guest 3
  - entity: person.Guest 2
  - entity: person.Evis
  - entity: person.Guest 1
  - entity: person.Daughter
  - entity: person.car
  hours_to_show: 2

```
