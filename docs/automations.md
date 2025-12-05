# Automations & Packages

This page documents the automation packages found in the `packages/` directory.

| File | Purpose | Triggers | Key Entities |
| :--- | :--- | :--- | :--- |
| `airthings.yaml` | Air quality sensors template | *(Template)* | `sensor.airthings_wave_*` |
| `aqara_w500.yaml` | HVAC/Temp sensors & filters | *(Template)* | `sensor.aqara_w500_*` |
| `car_glc.yaml` | Car status normalization | *(Template)* | `binary_sensor.car_glc_*` |
| `dishwasher.yaml` | Dishwasher status & timer logic | *(Template)* | `binary_sensor.dishwasher_*`, `input_boolean.dishwasher_*` |
| `dna_tv_hub.yaml` | TV Hub remote switch | *(Template)* | `switch.dna_tv_hub` |
| `fingerprint_management.yaml` | Dynamic Fingerprint MQTT Management | MQTT (`.../user/set`) | `script.add_fingerprint_entity`, `automation.system_fingerprint_mqtt_persistence` |
| `garmin.yaml` | *(Empty)* | - | - |
| `home_time_modes.yaml` | Time-of-Day Logic (Day/Night/Evening) | Time, Sun, Time Pattern | `input_select.house_mode`, `automation.system_manager_home_time_modes` |
| `mercedes_glc.yaml` | Car control & sensors | *(Template)* | `switch.car_*`, `binary_sensor.car_*` |
| `nordpool_prices.yaml` | Electricity prices & 15min cost calculation | Time Pattern, HA Start, State | `sensor.electricity_prices`, `nordpool.get_prices_for_date` |
| `office._pc.yaml` | Office PC Control (WOL, Audio, Display) | *(Template/WOL)* | `switch.office_pc_*` |
| `philips_air_purifier.yaml` | Air Purifier sensors | *(Template)* | `sensor.purifier_*` |
| `room_automation.yaml` | Dynamic Room Settings via MQTT | MQTT (`room/#`), HA Start, Time Pattern | `script.create_room_settings`, `automation.system_populate_room_list` |
| `scenes.yaml` | Lighting Scene Definitions | - | `scene.daylight_scene`, `scene.bedroom_mood`, etc. |
| `shelly_3em.yaml` | Total Power Aggregation | *(Template)* | `sensor.home_total_power`, `sensor.home_energy_15min` |
| `smart_notifications.yaml` | Dynamic Notification Router & User Mgmt | HA Start, Time Pattern, MQTT (`notify/#`) | `script.notify_smart_master`, `automation.system_populate_notify_services` |
