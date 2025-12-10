---
tags:
  - dashboard
  - view
  - automated
---

# Map Guest-1

**Dashboard:** Persons  
**Path:** `map-Guest-1`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_map-guest-1.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->





## Configuration
```yaml
theme: Backend-selected
title: Map Guest-1
path: map-Guest-1
type: panel
subview: true
badges: []
cards:
- type: map
  entities:
  - entity: person.Guest-1
  hours_to_show: 48
  dark_mode: false

```
