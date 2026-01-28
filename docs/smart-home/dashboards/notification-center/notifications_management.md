---
tags:
  - dashboard
  - view
  - automated
---

# Notifications Management

**Dashboard:** Notification Center  
**Path:** `notifications-management`

<!-- START_DESCRIPTION -->
Centralized management for notification users, categories, and subscriptions.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_notifications_management.png)

## Summary
<!-- START_SUMMARY -->
The Notification Center dashboard provides a comprehensive interface for managing the smart home's notification system. Administrators can add or remove users for mobile app notifications and define notification categories (e.g., 'Garage', 'Electricity'). The view allows for granular control over subscriptions, enabling individual users to opt-in or out of specific notification types, and includes tools to map and monitor notification-related automations.
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Area Manager](../../packages/area_manager.md)
* [Smart Notifications](../../packages/smart_notifications.md)
* [Smart Speakers](../../packages/smart_speakers.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`


## Configuration
```yaml
title: Notifications Management
icon: mdi:bell-cog
type: sections
max_columns: 5
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
    heading: Add / Update User
    icon: mdi:account-plus
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--green-color);\n\
        \  --secondary-text-color: var(--green-color);\n  --card-mod-icon-color: var(--green-color);\n\
        }\n"
  - type: markdown
    content: '**How to Add a User:**

      1. Select a **Home Assistant Person**.

      2. Select their **Mobile App Service**.

      3. Click **Add User**.'
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_select.notify_mgmt_person_select
      name: Select Person
    - type: call-service
      icon: mdi:refresh
      name: Refresh Lists
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_notify_services
        skip_condition: true
    - entity: input_select.notify_mgmt_service
      name: Mobile App Service
    - entity: input_select.notify_mgmt_platform
      icon: mdi:cellphone-cog
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--green-color);\n\
        }\n"
  - type: tile
    entity: input_select.notify_mgmt_person_select
    name: Add User
    icon: mdi:account-plus
    color: green
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.create_notify_user
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--green-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 9
      rows: 1
  - type: heading
    heading: Delete User
    icon: mdi:account-remove
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--red-color);\n\
        \  --card-mod-icon-color: var(--red-color);\n}\n"
  - type: markdown
    content: '**User Cleanup:**


      Select a user below and click Delete to remove their notification settings.

      '
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_select.notify_mgmt_delete_user_select
      name: Select User to Delete
    - type: call-service
      icon: mdi:refresh
      name: Refresh User List
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_notify_services
        skip_condition: true
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--red-color);\n\
        }\n"
  - type: tile
    entity: input_select.notify_mgmt_delete_user_select
    name: Delete User
    icon: mdi:account-remove
    color: red
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.delete_notify_user
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--red-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 9
      rows: 1
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Category Management
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Add Category
    icon: mdi:playlist-plus
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--green-color);\n\
        \  --secondary-text-color: var(--green-color);\n  --card-mod-icon-color: var(--green-color);\n\
        }\n"
  - type: markdown
    content: "**Add Category:\n\n** Type a new category name below (e.g. 'Garage')\
      \ and click Add. \n\n*This adds a switch to all users automatically.*\n"
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_text.notify_add_category
      name: New Category Name
      icon: mdi:playlist-plus
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--green-color);\n\
        }\n"
    grid_options:
      columns: 12
  - type: tile
    entity: input_text.notify_add_category
    name: Add Category
    icon: mdi:text-box-plus
    color: green
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.add_notify_category_global
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--green-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 9
      rows: 1
  - type: heading
    heading: Delete Category
    icon: mdi:playlist-remove
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--red-color);\n\
        \  --secondary-text-color: var(--red-color);\n  --card-mod-icon-color: var(--red-color);\n\
        }\n"
  - type: markdown
    content: '**Category Cleanup:**


      To delete a category, type the category name below and click the DELETE button.


      *This deletes the category from the users and from the settings.*

      '
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_select.notify_delete_category
      name: Category to Delete
      icon: mdi:playlist-remove
    - type: call-service
      icon: mdi:refresh
      name: Refresh Category List
      action_name: REFRESH
      service: automation.trigger
      service_data:
        entity_id: automation.system_populate_notify_services
        skip_condition: true
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--red-color);\n\
        }\n"
    grid_options:
      columns: 12
  - type: tile
    entity: input_select.notify_delete_category
    name: Delete Category
    icon: mdi:text-box-remove
    color: red
    show_entity_picture: false
    vertical: false
    tap_action:
      action: call-service
      service: script.delete_notify_category_global
    features_position: bottom
    card_mod:
      style: "ha-card {\n  border: none;\n  background: var(--red-color);\n  --primary-text-color:\
        \ white;\n  --secondary-text-color: white;\n  --card-mod-icon-color: black;\n\
        }\n"
    grid_options:
      columns: 9
      rows: 1
  - type: entities
    entities:
    - entity: input_text.notify_mgmt_categories
      name: Master List (ReadOnly)
      icon: mdi:format-list-text
      secondary_info: last-updated
    card_mod:
      style: "ha-card {\n  border: none;\n  --card-mod-icon-color: var(--orange-color);\n\
        }\n"
    grid_options:
      columns: 12
      rows: auto
- type: grid
  cards:
  - type: custom:mushroom-title-card
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
    title: Delivery Settings
  - type: heading
    heading: Category Settings
    icon: mdi:playlist-check
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--orange-color);\n\
        \  --secondary-text-color: var(--orange-color);\n  --card-mod-icon-color:\
        \ var(--orange-color);\n}\n"
  - type: markdown
    content: '**Category Delivery Rules**


      If the category toggle is on, notification is only sent to users who are currently
      at home.


      * **ON:** Send if person is at **Home**.

      * **OFF:** Send always.

      '
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Global Delivery Settings
      show_header_toggle: false
      card_mod:
        style: "/* hide the header row completely */\n.card-header,\n.card-header\
          \ > .name,\n.card-header > .menu,\n.header {\n  display: none !important;\n\
          }\n/* remove the extra top padding that can remain */\nha-card > :first-child\
          \ {\n  padding-top: 0 !important;\n}\n"
    filter:
      template: "{% set ns = namespace(rows=[]) %} \n\n{# Find switches matching the\
        \ global category pattern #} \n{% set switches = states.switch \n   | selectattr('entity_id',\
        \ 'search', 'notify_category_.*_local') \n   | sort(attribute='name') \n \
        \  | list %}\n\n{% if switches | length > 0 %}\n\n  {# 1. Create a sub-namespace\
        \ for the inner list to avoid scoping issues #}\n  {% set sub_ns = namespace(entities=[])\
        \ %}\n\n  {# 2. Build the list of switches #}\n  {% for sw in switches %}\n\
        \     {% set is_on = is_state(sw.entity_id, 'on') %}\n     \n     {# Define\
        \ Icon and Color logic #}\n     {% set icon = 'mdi:home-account' if is_on\
        \ else 'mdi:earth' %}\n     {% set color = 'lightgreen' if is_on else '#2196F3'\
        \ %} {# Standard HA Blue #}\n     \n     {% set sub_ns.entities = sub_ns.entities\
        \ + [{\n       'entity': sw.entity_id,\n       'secondary_info': 'If ON, requires\
        \ presence',\n       'icon': icon,\n       'card_mod': {\n         'style':\
        \ \":host { --card-mod-icon-color: \" ~ color ~ \"; }\"\n        }\n     \
        \ }] %}\n  {% endfor %}\n\n  {# 3. Create the Fold Row #}\n  {% set group\
        \ = {\n    'type': 'custom:fold-entity-row',\n    'head': {\n      'type':\
        \ 'section', \n      'label': 'Categories',\n      'card_mod': {\n       \
        \ 'style': \".label { color: orange !important; }\"\n      }\n    },\n   \
        \ 'entities': sub_ns.entities\n  } %}\n\n  {# 4. Add the Fold Row to the main\
        \ list #}\n  {% set ns.rows = ns.rows + [group] %}\n\n{% endif %}\n\n{{ ns.rows\
        \ | to_json }}"
    sort:
      method: none
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Subsription Management
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: heading
    heading: User Subscriptions
    icon: mdi:comment-outline
    heading_style: title
    card_mod:
      style: "ha-card {\n  border: none;\n  --primary-text-color: var(--orange-color);\n\
        \  --secondary-text-color: var(--orange-color);\n  --card-mod-icon-color:\
        \ var(--orange-color);\n}\n"
  - type: markdown
    content: '**User Preferences**


      *Toggle a switch **OFF** to unsubscribe a specific user from notifications of
      that category.*

      '
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Notification Subscriptions
      show_header_toggle: false
      card_mod:
        style: "/* hide the header row completely */\n.card-header,\n.card-header\
          \ > .name,\n.card-header > .menu,\n.header {\n  display: none !important;\n\
          }\n/* remove the extra top padding that can remain */\nha-card > :first-child\
          \ {\n  padding-top: 0 !important;\n}\n"
    filter:
      template: "{% set ns = namespace(cards=[]) %}\n\n{# 1. Find all switches that\
        \ belong to the notification system #}\n{% set switches = states.switch \n\
        \   | selectattr('entity_id', 'search', '_notification_') \n   | selectattr('attributes.user_slug',\
        \ 'defined') \n   | list %}\n\n{# 2. Extract unique users to create groups\
        \ #}\n{% set users = switches | map(attribute='attributes.user_slug') | unique\
        \ | sort | list %}\n\n{% for user in users %}\n  {# Filter switches for this\
        \ specific user #}\n  {% set user_switches = switches | selectattr('attributes.user_slug',\
        \ 'eq', user) | sort(attribute='name') | list %}\n  \n  {% if user_switches\
        \ | length > 0 %}\n    \n    {# FIX: Use a namespace for the inner entities\
        \ list so it persists inside the loop #}\n    {% set sub_ns = namespace(entities=[])\
        \ %}\n\n    {# 3. Build the Switch Rows #}\n    {% for sw in user_switches\
        \ %}\n       {% set is_on = is_state(sw.entity_id, 'on') %}\n       {% set\
        \ icon_color = 'green' if is_on else 'red' %}\n       {% set icon = 'mdi:email-check'\
        \ if is_on else 'mdi:email-remove-outline' %}\n       \n       {# Clean up\
        \ the name #}\n       {% set clean_name = sw.name | replace(' Notification',\
        \ '') %}\n       \n       {% set sub_ns.entities = sub_ns.entities + [{\n\
        \         'entity': sw.entity_id,\n         'name': clean_name,\n        \
        \ 'secondary_info': 'last-changed',\n         'icon': icon,\n         'card_mod':\
        \ {\n           'style': \":host { --card-mod-icon-color: \" ~ icon_color\
        \ ~ \"; }\"\n         }\n       }] %}\n    {% endfor %}\n\n    {# 4. Create\
        \ the Fold Row using sub_ns.entities #}\n    {% set group = {\n      'type':\
        \ 'custom:fold-entity-row',\n      'head': {\n        'type': 'section', \n\
        \        'label': user | capitalize ~ '\\'s Subscriptions',\n        'card_mod':\
        \ {\n          'style': \".label { color: orange !important; }\"\n       \
        \ }\n      },\n      'entities': sub_ns.entities\n    } %}\n\n    {# 5. Add\
        \ the group to the main card list #}\n    {% set ns.cards = ns.cards + [group]\
        \ %}\n\n  {% endif %}\n{% endfor %}\n\n{{ ns.cards | to_json }}"
    sort:
      method: none
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Notifications List
    alignment: center
        '
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Labeled Automations
      show_header_toggle: false
      card_mod:
        style: "/* hide the header row completely */\n.card-header,\n.card-header\n          \
          > .name,\n.card-header > .menu,\n.header {\n  display: none !important;\n\
          }\n/* remove the extra top padding that can remain */\nha-card > :first-child\n          \
          {\n  padding-top: 0 !important;\n}\n"
    filter:
      template: "{% set ns = namespace(cards=[]) %} {% set all_labels = labels() %}\n        \
        {% set notify_labels = all_labels | select('search', '^notify_') | sort\n        \
        | list %}\n{% for label_id in notify_labels %}\n  {% set entities = label_entities(label_id)\n        \
        | select('search', '^automation\\.') | list %}\n  \n  {% if entities | length\n        \
        > 0 %}\n    {% set display_name = label_id.replace('notify_', '') | capitalize\n        \
        %}\n    \n    {# Add Section with Orange Label Style #}\n    {% set ns.cards\n        \
        = ns.cards + [{\n      'type': 'section', \n      'label': display_name\n        \
        ~ ' Notifications',\n      'card_mod': {\n        'style': \".label { color:\n        \
        orange !important; }\"\n      }\n    }] %}\n    \n    {% for ent in entities\n        \
        %}\n       {% set icon_color = 'lightgreen' if is_state(ent, 'on') else\n        \
        \ 'red' %}\n       {% set ns.cards = ns.cards + [{\n         'entity': ent,\n\
        \         'secondary_info': 'last-triggered',\n         'icon': 'mdi:cellphone-message',\n\
        \         'card_mod': {\n           'style': \":host { --card-mod-icon-color:\n        \
        \ \" ~ icon_color ~ \"; }\"\n          }\n        }] %}\n    {% endfor %}\n\
        \  {% endif %}\n{% endfor %}\n{{ ns.cards | to_json }}\n"
    sort:
      method: none

cards: []
header:
  card:
    type: markdown
    text_only: true
    content: '# Notification Center

      Manage Home Assistant App Notifications'
path: notifications-management

```
