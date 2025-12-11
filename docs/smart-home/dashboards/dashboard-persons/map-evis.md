---
tags:
  - dashboard
  - view
  - automated
---

# Map Evis

**Dashboard:** Persons  
**Path:** `map-Evis`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-evis.png)





## Configuration
```yaml+jinja
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
