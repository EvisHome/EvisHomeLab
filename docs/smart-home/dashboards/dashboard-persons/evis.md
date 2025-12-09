---
tags:
  - dashboard
  - view
  - automated
---

# Evis

**Dashboard:** Persons  
**Path:** `evis`

![View Screenshot](../../../assets/images/dashboards/dashboard_dashboard-persons_evis.png)

## Configuration
```yaml
theme: Backend-selected
title: Evis
badges: []
cards: []
type: sections
sections:
- type: grid
  cards:
  - type: custom:decluttering-card
    template: family_member_card
    variables:
    - person: Evis
    - device: sm_f966b
    - background: background_2
    - color: '#dddddd'
  - type: custom:auto-entities
    card:
      type: entities
      title: My Notification Settings
      show_header_toggle: false
      icon: mdi:bell-cog
    filter:
      template: "{% set user_slug = 'Evis' %} {# <--- CHANGE THIS to the person's\
        \ slug #}\n{% set ns = namespace(switches=[]) %}\n\n{% for state in states.switch\
        \ %}\n  {# Find switches ending with _notification_[user_slug] #}\n  {% if\
        \ state.entity_id.endswith('_notification_' ~ user_slug) %}\n    {# Extract\
        \ category (e.g. switch.info_notification_Evis -> info) #}\n    {% set category\
        \ = state.object_id.split('_notification_')[0] | capitalize %}\n    \n   \
        \ {% set ns.switches = ns.switches + [{\n        'entity': state.entity_id,\n\
        \        'name': category ~ \" Notification\", \n        'secondary_info':\
        \ 'last-updated'\n    }] %}\n  {% endif %}\n{% endfor %}\n\n{{ ns.switches\
        \ | to_json }}\n"
    sort:
      method: name

```
