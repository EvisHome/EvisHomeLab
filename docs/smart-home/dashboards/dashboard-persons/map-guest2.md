---
tags:
  - dashboard
  - view
  - automated
---

# Map Guest 2

**Dashboard:** Persons  
**Path:** `map-Guest 2`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-guest2.png)





## Configuration
```yaml+jinja
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
