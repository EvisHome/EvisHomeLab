---
tags:
  - dashboard
  - view
  - automated
---

# Management

**Dashboard:** Notification Center  
**Path:** `management`

<!-- START_SUMMARY -->
This dashboard acts as the administrative backend for the Smart Notification System. It is divided into four key sections: **User Management** for onboarding and offboarding notification recipients; **Category Management** for creating and deleting system-wide notification channels; **Delivery Settings** for defining global rules (e.g., presence-based delivery); and **Subscription Management**, allowing individual users to toggle their subscriptions to specific notification categories. Additionally, it provides an overview of all automations tagged with notification labels.
<!-- END_SUMMARY -->

![View Screenshot](../../../assets/images/dashboards/dashboard_management.png)

## Related Packages
This view contains entities managed by:

* [Room Automation](../../packages/room_automation.md)
* [Smart Notifications](../../packages/smart_notifications.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:auto-entities`
* `custom:card-mod`
* `custom:mushroom-title-card`


## Configuration
```yaml+jinja
title: Management
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
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--green-color);
          --secondary-text-color: var(--green-color);
          --card-mod-icon-color: var(--green-color);
        }
  - type: markdown
    content: |-
      **How to Add a User:**
      1. Select a **Home Assistant Person**.
      2. Select their **Mobile App Service**.
      3. Click **Add User**.
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
      style: |-
        ha-card {
          border: none;
          --card-mod-icon-color: var(--green-color);
        }
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
      style: |-
        ha-card {
          border: none;
          background: var(--green-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
    grid_options:
      columns: 9
      rows: 1
  - type: heading
    heading: Delete User
    icon: mdi:account-remove
    heading_style: title
    card_mod:
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--red-color);
          --card-mod-icon-color: var(--red-color);
        }
  - type: markdown
    content: |-
      **User Cleanup:**

      Select a user below and click Delete to remove their notification settings.
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
      style: |-
        ha-card {
          border: none;
          --card-mod-icon-color: var(--red-color);
        }
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
      style: |-
        ha-card {
          border: none;
          background: var(--red-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
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
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--green-color);
          --secondary-text-color: var(--green-color);
          --card-mod-icon-color: var(--green-color);
        }
  - type: markdown
    content: |-
      **Add Category:

      ** Type a new category name below (e.g. 'Garage') and click Add.

      *This adds a switch to all users automatically.*
  - type: entities
    show_header_toggle: false
    entities:
    - entity: input_text.notify_add_category
      name: New Category Name
      icon: mdi:playlist-plus
    card_mod:
      style: |-
        ha-card {
          border: none;
          --card-mod-icon-color: var(--green-color);
        }
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
      style: |-
        ha-card {
          border: none;
          background: var(--green-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
    grid_options:
      columns: 9
      rows: 1
  - type: heading
    heading: Delete Category
    icon: mdi:playlist-remove
    heading_style: title
    card_mod:
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--red-color);
          --secondary-text-color: var(--red-color);
          --card-mod-icon-color: var(--red-color);
        }
  - type: markdown
    content: |-
      **Category Cleanup:**

      To delete a category, type the category name below and click the DELETE button.

      *This deletes the category from the users and from the settings.*
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
      style: |-
        ha-card {
          border: none;
          --card-mod-icon-color: var(--red-color);
        }
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
      style: |-
        ha-card {
          border: none;
          background: var(--red-color);
          --primary-text-color: white;
          --secondary-text-color: white;
          --card-mod-icon-color: black;
        }
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
      style: |-
        ha-card {
          border: none;
          --card-mod-icon-color: var(--orange-color);
        }
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
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--orange-color);
          --secondary-text-color: var(--orange-color);
          --card-mod-icon-color: var(--orange-color);
        }
  - type: markdown
    content: |-
      **Category Delivery Rules**

      If the category toggle is on, notification is only sent to users who are currently at home.

      * **ON:** Send if person is at **Home**.
      * **OFF:** Send always.
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Global Delivery Settings
      show_header_toggle: false
      card_mod:
        style: |-
          /* hide the header row completely */
          .card-header,
          .card-header > .name,
          .card-header > .menu,
          .header {
            display: none !important;
          }
          /* remove the extra top padding that can remain */
          ha-card > :first-child {
            padding-top: 0 !important;
          }
    filter:
      template: |-
        {% set ns = namespace(rows=[]) %} {# Find switches matching the global category pattern #} {% set switches = states.switch
           | selectattr('entity_id', 'search', 'notify_category_.*_local')
           | sort(attribute='name')
           | list %}

        {% if switches | length > 0 %}
          {# Add a single label for all categories with Orange Style #}
          {% set ns.rows = ns.rows + [{
              'type': 'section',
              'label': 'Categories',
              'card_mod': {
                'style': ".label { color: orange !important; }"
              }
          }] %}

          {% for sw in switches %}
             {% set is_on = is_state(sw.entity_id, 'on') %}

             {# Define Icon and Color logic #}
             {% set icon = 'mdi:home-account' if is_on else 'mdi:earth' %}
             {% set color = 'lightgreen' if is_on else '#2196F3' %} {# Standard HA Blue #}

             {% set ns.rows = ns.rows + [{
               'entity': sw.entity_id,
               'secondary_info': 'If ON, requires presence',
               'icon': icon,
               'card_mod': {
                 'style': ":host { --card-mod-icon-color: " ~ color ~ "; }"
                }
              }] %}
          {% endfor %}
        {% endif %}
        {{ ns.rows | to_json }}
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
      style: |-
        ha-card {
          border: none;
          --primary-text-color: var(--orange-color);
          --secondary-text-color: var(--orange-color);
          --card-mod-icon-color: var(--orange-color);
        }
  - type: markdown
    content: |-
      **User Preferences**

      *Toggle a switch **OFF** to unsubscribe a specific user from notifications of that category.*
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Notification Subscriptions
      show_header_toggle: false
      card_mod:
        style: |-
          /* hide the header row completely */
          .card-header,
          .card-header > .name,
          .card-header > .menu,
          .header {
            display: none !important;
          }
          /* remove the extra top padding that can remain */
          ha-card > :first-child {
            padding-top: 0 !important;
          }
    filter:
      template: |-
        {% set ns = namespace(cards=[]) %} {# 1. Find all switches that belong to the notification system (have user_slug attribute) #} {% set switches = states.switch
           | selectattr('entity_id', 'search', '_notification_')
           | selectattr('attributes.user_slug', 'defined')
           | list %}

        {# 2. Extract unique users to create groups #} {% set users = switches | map(attribute='attributes.user_slug') | unique | sort | list %}
        {% for user in users %}
          {# Filter switches for this specific user #}
          {% set user_switches = switches | selectattr('attributes.user_slug', 'eq', user) | sort(attribute='name') | list %}

          {% if user_switches | length > 0 %}
            {# 3. Add Section Header with Orange Style #}
            {% set ns.cards = ns.cards + [{
              'type': 'section',
              'label': user | capitalize ~ '\'s Subscriptions',
              'card_mod': {
                'style': ".label { color: orange !important; }"
              }
            }] %}

            {# 4. Add Switches #}
            {% for sw in user_switches %}
               {% set is_on = is_state(sw.entity_id, 'on') %}
               {% set icon_color = 'green' if is_on else 'red' %}
               {% set icon = 'mdi:email-check' if is_on else 'mdi:email-remove-outline' %}

               {# Clean up the name by removing ' Notification' for a cleaner list #}
               {% set clean_name = sw.name | replace(' Notification', '') %}

               {% set ns.cards = ns.cards + [{
                 'entity': sw.entity_id,
                 'name': clean_name,
                 'secondary_info': 'last-changed',
                 'icon': icon,
                 'card_mod': {
                   'style': ":host { --card-mod-icon-color: " ~ icon_color ~ "; }"
                  }
                }] %}
            {% endfor %}
          {% endif %}
        {% endfor %}
        {{ ns.cards | to_json }}
    sort:
      method: none
- type: grid
  cards:
  - type: custom:mushroom-title-card
    title: Notifications List
    alignment: center
    title_tap_action:
      action: none
    subtitle_tap_action:
      action: none
  - type: heading
    heading: Automation Map
    icon: mdi:sitemap
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
    content: |-
      **Notifications Overview**

      Lists all notifcation automations grouped by Category Labels. You can turn the automations on or off.

      *Tip: Add labels like 'Notify: Electricity' to your automations to see them here.*
  - type: custom:auto-entities
    show_empty: true
    card:
      type: entities
      title: Labeled Automations
      show_header_toggle: false
      card_mod:
        style: |-
          /* hide the header row completely */
          .card-header,
          .card-header > .name,
          .card-header > .menu,
          .header {
            display: none !important;
          }
          /* remove the extra top padding that can remain */
          ha-card > :first-child {
            padding-top: 0 !important;
          }
    filter:
      template: |-
        {% set ns = namespace(cards=[]) %} {% set all_labels = labels() %} {% set notify_labels = all_labels | select('search', '^notify_') | sort | list %}
        {% for label_id in notify_labels %}
          {% set entities = label_entities(label_id) | select('search', '^automation\.') | list %}

          {% if entities | length > 0 %}
            {% set display_name = label_id.replace('notify_', '') | capitalize %}

            {# Add Section with Orange Label Style #}
            {% set ns.cards = ns.cards + [{
              'type': 'section',
              'label': display_name ~ ' Notifications',
              'card_mod': {
                'style': ".label { color: orange !important; }"
              }
            }] %}

            {% for ent in entities %}
               {% set icon_color = 'lightgreen' if is_state(ent, 'on') else 'red' %}
               {% set ns.cards = ns.cards + [{
                 'entity': ent,
                 'secondary_info': 'last-triggered',
                 'icon': 'mdi:cellphone-message',
                 'card_mod': {
                   'style': ":host { --card-mod-icon-color: " ~ icon_color ~ "; }"
                  }
                }] %}
            {% endfor %}
          {% endif %}
        {% endfor %}
        {{ ns.cards | to_json }}
    sort:
      method: none
cards: []
header:
  card:
    type: markdown
    text_only: true
    content: |-
      # Notification Center
      Manage Home Assistant App Notifications

```
