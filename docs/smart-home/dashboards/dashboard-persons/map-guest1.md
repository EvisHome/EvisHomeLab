---
tags:
  - dashboard
  - view
  - automated
---

# Map Guest 1

**Dashboard:** Persons  
**Path:** `map-Guest 1`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-guest1.png)





## Configuration
```yaml+jinja
theme: Backend-selected
title: Map Guest 1
path: map-Guest 1
type: panel
subview: true
badges: []
cards:
- type: map
  entities:
  - entity: person.Guest 1
  hours_to_show: 48
  dark_mode: false

```
