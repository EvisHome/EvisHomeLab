---
tags:
  - dashboard
  - view
  - automated
---

# Daughter

**Dashboard:** Persons  
**Path:** `Daughter`



![View Screenshot](../../../assets/images/dashboards/dashboard_dashboard-persons_daughter.png)

## Configuration
```yaml
theme: Backend-selected
title: Daughter
path: Daughter
badges: []
cards:
- type: vertical-stack
  cards:
  - type: custom:decluttering-card
    template: family_member_card
    variables:
    - person: Daughter
    - device: Daughter_mobile
    - background: background_3
    - color: '#dddddd'
  - type: custom:decluttering-card
    template: family_member_notifications
    variables:
    - person: Guest 2

```
