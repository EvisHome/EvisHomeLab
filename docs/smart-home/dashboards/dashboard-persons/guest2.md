---
tags:
  - dashboard
  - view
  - automated
---

# Guest 2

**Dashboard:** Persons  
**Path:** `Guest 2`



![View Screenshot](../../../assets/images/dashboards/dashboard_dashboard-persons_guest2.png)

## Configuration
```yaml
theme: Backend-selected
title: Guest 2
path: Guest 2
badges: []
cards:
- type: vertical-stack
  cards:
  - type: custom:decluttering-card
    template: family_member_card
    variables:
    - person: Guest 2
    - device: mobile_Guest 2
    - background: background_3
    - color: '#dddddd'
  - type: custom:decluttering-card
    template: family_member_notifications
    variables:
    - person: Guest 2

```
