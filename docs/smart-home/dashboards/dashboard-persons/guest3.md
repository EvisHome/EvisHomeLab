---
tags:
  - dashboard
  - view
  - automated
---

# Guest 3

**Dashboard:** Persons  
**Path:** `Guest 3`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_guest3.png)



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:decluttering-card`


## Configuration
```yaml
theme: Backend-selected
title: Guest 3
path: Guest 3
badges: []
cards:
- type: vertical-stack
  cards:
  - type: custom:decluttering-card
    template: family_member_card
    variables:
    - person: Guest 3
    - device: sm_a426b_Guest 3
    - background: background_3
    - color: '#dddddd'
  - type: custom:decluttering-card
    template: family_member_notifications
    variables:
    - person: Guest 3

```
