---
tags:
  - dashboard
  - view
  - automated
---

# Fingerprints

**Dashboard:** Home Access  
**Path:** `fingerprints`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_fingerprints.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Fingerprint Management](../../packages/fingerprint_management.md)
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`


## Configuration
```yaml
title: Fingerprints
icon: mdi:fingerprint
type: sections
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: User Management
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Fingerprint Registry
    icon: mdi:fingerprint
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--orange-color);\n\
        \  --secondary-text-color: var(--orange-color);\n  --card-mod-icon-color:\
        \ var(--orange-color);\n}\n"
  - type: markdown
    content: '

      ### 📋 Instructions:

      ---


      1. All fingerprints must be first scanned in Unifi Protect and assigned to persons.


      2. When person scans the fingerprint the first time, it will show up as unknown
      or unassigned.


      3. Only assigned fingerprints allow door lock to be opened by scanning the fingerprint.'
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Registered Fingerprints
      show_header_toggle: false
    filter:
      template: "{% set ns = namespace(cards=[]) %}\n{% for state in states.select\
        \ %}\n  {% if state.entity_id.startswith('select.fingerprint_') %}\n    {#\
        \ Get the full ID from attributes #}\n    {% set full_id = state.attributes.ulp_id\
        \ | default('-unassigned-') %}\n    \n    {# Check if assigned #}\n    {%\
        \ set assigned = state.state %}\n    {% if assigned in ['-Unassigned-', '-unassigned-',\
        \ 'Unknown', 'unknown', 'unavailable'] %}\n      {% set icon_color = 'red'\
        \ %}\n      {% set label = '\U0001F534 ' ~ full_id %}\n    {% else %}\n  \
        \    {% set icon_color = 'green' %}\n      \n      {# Robust Name Cleaner\
        \ for Dropdown Label #}\n      {% set clean = assigned.replace(' Notifications',\
        \ '').replace(' Notification', '') %}\n      {% set parts = clean.split('\
        \ ') %}\n      {% if parts | length > 1 and parts[0] == parts[-1] %}\n   \
        \     {% set clean_name = parts[0] %}\n      {% else %}\n        {% set clean_name\
        \ = clean %}\n      {% endif %}\n      \n      {% set label = '\U0001F7E2\
        \ ' ~ full_id %}\n    {% endif %}\n\n    {% set ns.cards = ns.cards + [{\n\
        \        'entity': state.entity_id,\n        'name': label,\n        'secondary_info':\
        \ full_id,\n        'icon': 'mdi:fingerprint'\n    }] %}\n  {% endif %}\n\
        {% endfor %}\n{{ ns.cards | to_json }}\n\n"
    sort:
      method: state
      reverse: false
  - type: tile
    entity: input_text.notify_add_category
    name: Refresh User Lists
    icon: mdi:account-sync
    color: green
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.refresh_fingerprint_users
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--green-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 6
      rows: 1
  - type: markdown
    content: '## <ha-icon icon="mdi:fingerprint"></ha-icon> Registred Fingerprint
      IDs




      | <font color=orange>Assigned User</font> | <font color=orange>Fingerprint ID</font>
      |

      | :--- | :--- |

      {% set fingerprints = states.select | selectattr(''entity_id'', ''search'',
      ''^select\.fingerprint_'') | list -%}

      {% for state in fingerprints | sort(attribute=''state'') -%}

      {% set assigned = state.state | default(''Unknown'') -%}

      {% if assigned in [''Unknown'', ''unknown'', ''unavailable''] -%}

      | **{{ assigned }}** | `{{ (state.attributes.ulp_id | default(''unknown'')).strip()
      }}` |

      {% else -%}

      {% set clean = assigned.replace('' Notifications'', '''').replace('' Notification'',
      '''') -%}

      {% set parts = clean.split('' '') -%}

      {% if parts | length > 1 and parts[0] == parts[-1] -%}

      {% set display_name = parts[0] -%}

      {% else -%}

      {% set display_name = clean -%}

      {% endif -%}

      | **{{ display_name }}** | `{{ (state.attributes.ulp_id | default(''unknown'')).strip()
      }}` |

      {% endif -%}

      {% else -%}

      | No fingerprints | found yet |

      {% endfor %}

      '
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Access Management
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Guest Access Schedule
    icon: mdi:tools
    heading_style: title
  - type: tile
    entity: input_datetime.fp_guest_start
    name: Start Time
    icon: mdi:clock-start
    vertical: false
    features_position: bottom
  - type: tile
    entity: input_datetime.fp_guest_end
    name: End Time
    icon: mdi:clock-end
  - type: tile
    entity: input_boolean.fp_guest_mon
    name: Mon
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    card_mod:
      style: 'ha-card { --tile-color: var(--green-color); }

        '
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_tue
    name: Tue
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_wed
    name: Wed
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_thu
    name: Thu
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_fri
    name: Fri
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_sat
    name: Sat
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    card_mod:
      style: 'ha-card { --tile-color: var(--red-color); }

        '
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: input_boolean.fp_guest_sun
    name: Sun
    icon: ''
    hide_state: true
    vertical: true
    features_position: bottom
    card_mod:
      style: 'ha-card { --tile-color: var(--red-color); }

        '
    grid_options:
      columns: 3
      rows: 2
  - type: tile
    entity: script.refresh_fingerprint_users
    name: Force Initialize / Refresh Switches
    icon: mdi:refresh-circle
    color: blue
    tap_action:
      action: toggle
  - type: custom:auto-entities
    show_empty: false
    card:
      type: entities
      title: User Access Control
      show_header_toggle: false
    filter:
      include:
      - entity_id: switch.fp_access_*
        options:
          secondary_info: last-changed
      exclude:
      - state: unavailable
    sort:
      method: name
header:
  card:
    type: markdown
    text_only: true
    content: '# Home Access Center'

```
