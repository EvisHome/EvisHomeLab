---
tags:
  - automations
  - ui
  - automated
---

# UI Automations

This page documents automations that are managed directly via the Home Assistant UI (`automations.yaml`). 

!!! info "Package Automations"
    Automations that are part of a specific feature bundle (e.g., Car, Heating) are documented in the **[Package Catalog](packages/index.md)**.

## Active UI Automations

| Alias | Description | Trigger Types | Mode |
| :--- | :--- | :--- | :--- |
| Turn off Coffee Machine Outlet, when schedule is turned on | No description. | state | `single` |\n| Fetch Tomorrow Prices | No description. | time | `single` |\n| Fetch Today Prices | No description. | time | `single` |\n| Notify: Energy Price (Today & Tomorrow) | Sends 'Today's Prices' at 07:00 and 'Tomorrow's Prices' when available. | state, time | `single` |\n| G4 Doorbell - Event Stream to Nest Hub | Streams G4 Doorbell video to Bedroom Display only on doorbell press (24/7) or person on porch (daytime). | numeric_state, state | `single` |\n| Notify: Coffee Ready | Send notification when coffee machine finishes running | state | `single` |\n| Notify: Doorbell Actions | Notify phones with snapshot when doorbell rings, allowing unlock or DND message. | state | `restart` |
