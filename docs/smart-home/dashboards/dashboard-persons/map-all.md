---
tags:
  - dashboard
  - view
  - automated
---

# Map All

**Dashboard:** Persons  
**Path:** `map-all`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-all.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->





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
  - entity: person.Guest-3
  - entity: person.Guest-2
  - entity: person.Evis
  - entity: person.Guest-1
  - entity: person.Daughter
  - entity: person.car
  hours_to_show: 2
  theme_mode: auto

```
