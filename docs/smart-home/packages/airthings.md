---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Airthings

**Version:** 1.0.0  
**Description:** Normalizes Airthings Wave sensors (Temp, Humidity, CO2)

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/airthings.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Airthings
# Version: 1.0.0
# Description: Normalizes Airthings Wave sensors (Temp, Humidity, CO2)
# Dependencies: sensor.airthings_wave_living_room_temperature
# ------------------------------------------------------------------------------
template:
  - sensor:
      - name: "Airthings Wave Temperature"
        unique_id: airthings_wave_temperature
        unit_of_measurement: "°C"
        device_class: temperature
        state_class: measurement
        state: >
          {% set value = states('sensor.airthings_wave_living_room_temperature') | float(0) %}
          {{ value | round(1) }}

      - name: "Airthings Wave Humidity"
        unique_id: airthings_wave_humidity
        unit_of_measurement: "%"
        device_class: humidity
        state_class: measurement
        state: >
          {% set value = states('sensor.airthings_wave_living_room_humidity') | float(0) %}
          {{ value | round(1) }}

      - name: "Airthings Wave CO2"
        unique_id: airthings_wave_co2
        unit_of_measurement: "ppm"
        device_class: carbon_dioxide
        state_class: measurement
        state: >
          {% set value = states('sensor.airthings_wave_living_room_co2') | float(0) %}
          {{ value | round(1) }}

```

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Living Room](../dashboards/main/living_room.md)** (Uses 3 entities)
<!-- END_DASHBOARD -->
