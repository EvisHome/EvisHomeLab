---
tags:
  - dashboard
  - view
  - automated
---

# Smart Speakers Manager

**Dashboard:** Smart Speakers  
**Path:** `smart-speakers-manager`

<!-- START_DESCRIPTION -->
No description provided.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_smart_speakers_manager.png)

## Summary
<!-- START_SUMMARY -->
*No summary generated yet.*
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Smart Notifications](../../packages/smart_notifications.md)
* [Smart Speakers](../../packages/smart_speakers.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`


## Configuration
```yaml
title: Smart Speakers Manager
type: sections
max_columns: 4
path: smart-speakers-manager
sections:
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Speaker Manager
    subtitle: Route Notifications to Rooms
    alignment: center
  - type: vertical-stack
    cards:
    - type: heading
      heading: Register New Device
      icon: mdi:speaker-plus
      heading_style: title
      card_mod:
        style: 'ha-card { border: none; --primary-text-color: var(--orange-color);
          --card-mod-icon-color: var(--orange-color); }'
    - type: entities
      show_header_toggle: false
      entities:
      - entity: input_text.speaker_mgmt_name
        name: Friendly Name
      - entity: input_select.speaker_mgmt_entity
        name: Select Media Player
      - type: button
        name: Don't see it?
        icon: mdi:refresh
        action_name: REFRESH LIST
        tap_action:
          action: call-service
          service: script.refresh_speaker_list
      - entity: input_select.speaker_mgmt_area
        name: Primary Coverage Room
        secondary_info: 'Note: You can add more rooms later?'
      - type: button
        name: Register Speaker
        icon: mdi:check-bold
        action_name: REGISTER
        tap_action:
          action: call-service
          service: script.create_smart_speaker
  - type: vertical-stack
    cards:
    - type: heading
      heading: Coverage Management
      icon: mdi:map-marker-path
      heading_style: title
      card_mod:
        style: 'ha-card { border: none; --primary-text-color: var(--blue-color); --card-mod-icon-color:
          var(--blue-color); }'
    - type: entities
      show_header_toggle: false
      entities:
      - entity: input_select.speaker_mgmt_registered_list
        name: Select Speaker
        icon: mdi:speaker-wireless
      - entity: input_select.speaker_mgmt_area
        name: Select Room
        icon: mdi:map-marker
      - type: buttons
        entities:
        - entity: script.speaker_add_area
          name: Add Room to Speaker
          icon: mdi:plus-box
          action_name: ADD
          tap_action:
            action: call-service
            service: script.speaker_add_area
        - entity: script.speaker_remove_area
          name: Remove Room from Speaker
          icon: mdi:minus-box
          action_name: REMOVE
          tap_action:
            action: call-service
            service: script.speaker_remove_area
- type: grid
  cards:
  - type: custom:auto-entities
    show_empty: true
    card_param: cards
    card:
      type: vertical-stack
      title: Active Speakers
    filter:
      template: "{% set ns = namespace(cards=[]) %}\n{# Filter: Switches that define\
        \ 'speaker_slug' attribute #}\n{% set configs = states.switch | selectattr('attributes.speaker_slug',\
        \ 'defined') | list %}\n\n{% if configs | length == 0 %}\n    {% set ns.cards\
        \ = [{\n        'type': 'markdown',\n        'content': '_No smart speakers\
        \ registered yet._'\n    }] %}\n{% else %}\n    {% for cfg in configs %}\n\
        \        {% set slug = cfg.attributes.speaker_slug %}\n        {% set raw_name\
        \ = cfg.attributes.friendly_name | default(cfg.name) %}\n        {% set name\
        \ = raw_name\n            | replace(' Config', '')\n            | replace('\
        \ Quiet Mode', '')\n            | replace('Speaker Speaker', 'Speaker')\n\
        \        %}\n        {% set dnd = cfg.entity_id %}\n        \n        {# Build\
        \ Dynamic Category Switches #}\n        {% set cats = states('input_text.notify_mgmt_categories').split(',')\
        \ | map('trim') | map('lower') | select('ne', '') | list %}\n        \n  \
        \      {# 1. Create the list of switches inside a namespace #}\n        {%\
        \ set inner_ns = namespace(switches=[]) %}\n        \n        {% for c in\
        \ cats %}\n           {% set ent_id = 'switch.speaker_' ~ slug ~ '_notify_'\
        \ ~ c %}\n           {% set is_on = is_state(ent_id, 'on') %}\n          \
        \ {% set icon_color = 'green' if is_on else 'red' %}\n           {% set icon\
        \ = 'mdi:bell-ring' if is_on else 'mdi:bell-off' %}\n           \n       \
        \    {% set inner_ns.switches = inner_ns.switches + [{\n             'entity':\
        \ ent_id, \n             'name': c|title, \n             'icon': icon,\n \
        \            'card_mod': { 'style': \":host { --card-mod-icon-color: \" ~\
        \ icon_color ~ \"; }\" }\n           }] %}\n        {% endfor %}\n\n     \
        \   {# 2. Create the Fold Row Object #}\n        {# This wraps the section\
        \ header and the switch list together #}\n        {% set category_fold = {\n\
        \             'type': 'custom:fold-entity-row',\n             'head': {\n\
        \               'type': 'section',\n               'label': 'Subscription\
        \ Categories',\n               'card_mod': { 'style': \".label { color: orange\
        \ !important; }\" }\n             },\n             'entities': inner_ns.switches\n\
        \        } %}\n\n        {# 3. Build the Main Card #}\n        {% set ns.cards\
        \ = ns.cards + [{\n          'type': 'entities',\n          'title': name,\n\
        \          'show_header_toggle': false,\n          'entities': [\n       \
        \     {\n              'entity': dnd,\n              'name': 'DND / Quiet\
        \ Mode',\n              'icon': 'mdi:volume-off'\n            },\n       \
        \     {\n              'type': 'attribute',\n              'entity': dnd,\n\
        \              'attribute': 'linked_rooms',\n              'name': 'Covered\
        \ Rooms',\n              'icon': 'mdi:map-marker-radius'\n            }\n\
        \          ] + [category_fold] + [\n            { 'type': 'divider' },\n \
        \           {\n              'type': 'call-service',\n              'name':\
        \ 'Delete Speaker',\n              'icon': 'mdi:delete-outline',\n       \
        \       'action_name': 'DELETE',\n              'service': 'script.delete_smart_speaker',\n\
        \              'service_data': { 'speaker_slug': slug }\n            }\n \
        \         ]\n        }] %}\n    {% endfor %}\n{% endif %}\n\n{{ ns.cards }}"

```
