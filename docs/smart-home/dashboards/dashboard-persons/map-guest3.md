---
tags:
  - dashboard
  - view
  - automated
---

# Map Guest 3

**Dashboard:** Persons  
**Path:** `map-Guest 3`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-guest3.png)





## Configuration
```yaml+jinja
theme: Backend-selected
title: Map Guest 3
path: map-Guest 3
type: panel
subview: true
badges: []
cards:
- type: map
  entities:
  - entity: person.Guest 3
  hours_to_show: 48
  dark_mode: false

```
