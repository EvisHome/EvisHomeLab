---
tags:
  - dashboard
  - view
  - automated
---

# Guest 1

**Dashboard:** Persons  
**Path:** `Guest 1`

![View Screenshot](../../../assets/images/dashboards/view_dashboard-persons_guest1.png)

## Configuration
```yaml
theme: Backend-selected
title: Guest 1
path: Guest 1
badges: []
cards: []
type: sections
sections:
- type: grid
  cards:
  - type: heading
    heading: New section
  - type: custom:decluttering-card
    template: family_member_card
    variables:
    - person: Guest 1
    - device: SM_S721B_Guest 1
    - background: background_3
    - color: '#ddd'
  - type: custom:auto-entities
    card:
      type: entities
      title: My Notification Settings
      show_header_toggle: false
      icon: mdi:bell-cog
    filter:
      template: "{% set user_slug = 'Guest 1' %} {# <--- CHANGE THIS to the person's\
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
max_columns: 4

```
