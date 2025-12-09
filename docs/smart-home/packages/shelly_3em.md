---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Shelly 3Em

**Version:** 1.0.0  
**Description:** Power aggregation for Shelly 3EM (Total Power, Energy)

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/shelly_3em.png)
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

## Dashboard Connections
<!-- START_DASHBOARD -->
*No linked dashboard views found (Automatic Scan).*
<!-- END_DASHBOARD -->

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
# Package: Shelly 3EM
# Version: 1.0.0
# Description: Power aggregation for Shelly 3EM (Total Power, Energy)
# Dependencies: sensor.home_energy_shelly_3em_*
# ------------------------------------------------------------------------------
template:
  - sensor:
      - name: "Home Total Power"
        unique_id: home_total_power
        unit_of_measurement: "W"
        device_class: power
        state_class: measurement
        state: >
          {{ states('sensor.home_energy_shelly_3em_channel_a_power') | float(0)
            + states('sensor.home_energy_shelly_3em_channel_b_power') | float(0)
            + states('sensor.home_energy_shelly_3em_channel_c_power') | float(0) }}

      - name: "Home Total 3EM Energy"
        unique_id: home_total_3em_energy
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
        state: >
          {{ states('sensor.home_energy_shelly_3em_channel_a_energy') | float(0)
            + states('sensor.home_energy_shelly_3em_channel_b_energy') | float(0)
            + states('sensor.home_energy_shelly_3em_channel_c_energy') | float(0) }}

      - name: "Home Energy 15min"
        unique_id: home_energy_15min
        unit_of_measurement: "kWh"
        device_class: energy
        state_class: total_increasing
        state: >
          {% set power_a = states('sensor.shelly_3em_channel_a_power') | float(0) %}
          {% set power_b = states('sensor.shelly_3em_channel_b_power') | float(0) %}
          {% set power_c = states('sensor.shelly_3em_channel_c_power') | float(0) %}
          {% set total_power = power_a + power_b + power_c %}
          {{ ((total_power / 1000) * 0.25) | round(4) }}

```
