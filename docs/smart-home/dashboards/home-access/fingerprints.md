---
tags:
  - dashboard
  - view
  - automated
---

# Fingerprints

**Dashboard:** Home Access  
**Path:** `fingerprints`

<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_fingerprints.png)

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
```yaml+jinja
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
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--orange-color);
          --secondary-text-color: var(--orange-color);
          --card-mod-icon-color: var(--orange-color);
        }
  - type: markdown
    content: |2-

      ### 📋 Instructions:
      ---

      1. All fingerprints must be first scanned in Unifi Protect and assigned to persons.

      2. When person scans the fingerprint the first time, it will show up as unknown or unassigned.

      3. Only assigned fingerprints allow door lock to be opened by scanning the fingerprint.
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Registered Fingerprints
      show_header_toggle: false
    filter:
      template: |
        {% set ns = namespace(cards=[]) %}
        {% for state in states.select %}
          {% if state.entity_id.startswith('select.fingerprint_') %}
            {# Get the full ID from attributes #}
            {% set full_id = state.attributes.ulp_id | default('-unassigned-') %}

            {# Check if assigned #}
            {% set assigned = state.state %}
            {% if assigned in ['-Unassigned-', '-unassigned-', 'Unknown', 'unknown', 'unavailable'] %}
              {% set icon_color = 'red' %}
              {% set label = '🔴 ' ~ full_id %}
            {% else %}
              {% set icon_color = 'green' %}

              {# Robust Name Cleaner for Dropdown Label #}
              {% set clean = assigned.replace(' Notifications', '').replace(' Notification', '') %}
              {% set parts = clean.split(' ') %}
              {% if parts | length > 1 and parts[0] == parts[-1] %}
                {% set clean_name = parts[0] %}
              {% else %}
                {% set clean_name = clean %}
              {% endif %}

              {% set label = '🟢 ' ~ full_id %}
            {% endif %}

            {% set ns.cards = ns.cards + [{
                'entity': state.entity_id,
                'name': label,
                'secondary_info': full_id,
                'icon': 'mdi:fingerprint'
            }] %}
          {% endif %}
        {% endfor %}
        {{ ns.cards | to_json }}
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
      style: |-
        ha-card {
          border: none;
          background: var(--green-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
    grid_options:
      columns: 6
      rows: 1
  - type: markdown
    content: |-
      ## <ha-icon icon="mdi:fingerprint"></ha-icon> Registred Fingerprint IDs



      | <font color=orange>Assigned User</font> | <font color=orange>Fingerprint ID</font> |
      | :--- | :--- |
      {% set fingerprints = states.select | selectattr('entity_id', 'search', '^select\.fingerprint_') | list -%}
      {% for state in fingerprints | sort(attribute='state') -%}
      {% set assigned = state.state | default('Unknown') -%}
      {% if assigned in ['Unknown', 'unknown', 'unavailable'] -%}
      | **{{ assigned }}** | `{{ (state.attributes.ulp_id | default('unknown')).strip() }}` |
      {% else -%}
      {% set clean = assigned.replace(' Notifications', '').replace(' Notification', '') -%}
      {% set parts = clean.split(' ') -%}
      {% if parts | length > 1 and parts[0] == parts[-1] -%}
      {% set display_name = parts[0] -%}
      {% else -%}
      {% set display_name = clean -%}
      {% endif -%}
      | **{{ display_name }}** | `{{ (state.attributes.ulp_id | default('unknown')).strip() }}` |
      {% endif -%}
      {% else -%}
      | No fingerprints | found yet |
      {% endfor %}
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
      style: 'ha-card { --tile-color: var(--green-color); }'
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
      style: 'ha-card { --tile-color: var(--red-color); }'
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
      style: 'ha-card { --tile-color: var(--red-color); }'
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
- type: grid
  cards:
  - type: heading
    heading: New section
header:
  card:
    type: markdown
    text_only: true
    content: '# Home Access Center'

```
