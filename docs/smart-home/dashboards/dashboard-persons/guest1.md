---
tags:
  - dashboard
  - view
  - automated
---

# Guest 1

**Dashboard:** Persons  
**Path:** `Guest 1`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_guest1.png)



## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:decluttering-card`


## Configuration
```yaml+jinja
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
      template: |-
        {% set user_slug = 'Guest 1' %} {# <--- CHANGE THIS to the person's slug #}
        {% set ns = namespace(switches=[]) %}

        {% for state in states.switch %}
          {# Find switches ending with _notification_[user_slug] #}
          {% if state.entity_id.endswith('_notification_' ~ user_slug) %}
            {# Extract category (e.g. switch.info_notification_Evis -> info) #}
            {% set category = state.object_id.split('_notification_')[0] | capitalize %}

            {% set ns.switches = ns.switches + [{
                'entity': state.entity_id,
                'name': category ~ " Notification",
                'secondary_info': 'last-updated'
            }] %}
          {% endif %}
        {% endfor %}

        {{ ns.switches | to_json }}
    sort:
      method: name
max_columns: 4

```
