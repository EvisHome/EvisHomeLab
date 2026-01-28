---
tags:
  - article
  - automation
  - python
  - architecture
date: 2026-01-21
status: published
draft: true
highlight: false
---

# Redesigning Area Automation: From YAML to Python

**Date:** January 21, 2026  
**Author:** EvisHomeLab Architect  
**Tags:** `automation`, `python`, `pyscript`

## The Problem with YAML

For years, our "Room Manager" relied on complex YAML packages with heavy use of `trigger_variables`, `choose` blocks, and limited state tracking. It worked, but it was fragile. Adding a simple feature like "Dim lights before turning off" required modifying multiple automation blocks and risking breaking the entire flow.

We faced specific challenges:
1.  **Race Conditions:** If you re-entered a room *exactly* as the lights were turning off, the system often got confused.
2.  **Rigidity:** Adding a "Manual Mode" (don't automate lights, but track presence) was nearly impossible.
3.  **Maintenance:** The YAML file grew to 1000+ lines of repetitive code.

## The Solution: A Decoupled Architecture

We completely rewrote the system using **Pyscript**, fully embracing a "State Machine" design pattern.

### 1. Separation of Concerns
We split the logic into two distinct layers:
*   **Presence Layer (`area_presence.py`):** Determines the "Truth" of the room. Is it Occupied? Idle? Asleep?
*   **Automation Layer (`area_automations.py`):** Reacts to the Truth. "Oh, the room is Occupied? The mode is 'Presence Control'? Okay, I'll turn on the lights."

### 2. The Power of Python
Moving to Python allowed us to implement features that were redundant in YAML:

*   **Smart Off Delay:** When you leave a room, the lights don't just snap off. They enter a "Warning" state (dimming) for 2 minutes. The system intelligently checks *if the lights are actually on* before doing this, preventing ghost lights at night.
*   **Dynamic Timers:** We can now see exactly how many seconds are left before a room goes "Idle" directly on the dashboard.
*   **Time-of-Day Scenes:** The code automatically looks up `select.area_living_room_[period]_scene`. If it's Morning, you get the Morning scene. If it's Night, you get the Night scene. No hardcoding.

## Configuration via MQTT

Everything is configured via MQTT Discovery. This means we can "spawn" a new Area just by running a script. The definitions in `area_manager.yaml` generate:
*   `binary_sensor.area_x_occupancy`
*   `select.area_x_mode` (Presence, Absence, Manual)
*   `number.area_x_idle_time`
*   `switch.area_x_dnd`

## Conclusion

The new system is faster, more robust, and significantly easier to debug. By treating our home automation as a software engineering problem—using State Machines and Event Listeners—we've gained stability and flexibility that YAML simply couldn't provide.
