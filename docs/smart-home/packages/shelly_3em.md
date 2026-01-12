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
![Package Diagram](assets/shelly_3em.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
The **Shelly 3EM** package is a critical energy monitoring abstraction layer. It aggregates data from the three individual phases of the physical Shelly 3EM device into unified "Whole Home" metrics. It calculates real-time total power (Watts) and cumulative energy consumption (kWh), providing the foundational data for energy dashboards and cost calculations.
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
Your home connects to the grid via three separate power lines (phases). The Shelly 3EM measures each one individually. This package combines them:
1.  **Summing**: It adds Phase A + Phase B + Phase C to give you one simple number: "Total House Power."
2.  **Standardization**: It ensures units are correct so the Energy Dashboard can read them.
3.  **Special calculations**: It creates a "15-minute energy" tracker, useful for seeing short-term consumption spikes.
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
*No linked dashboard views found (Automatic Scan).*
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
The diagram below shows the data aggregation flow. The physical Shelly 3EM device provides three separate data streams (one per phase). The Template Sensors defined in this package subscribe to state changes on all three channels. Whenever a change is detected, the template logic executes, summing the values (A+B+C) and updating the single "Home Total" entity effectively in real-time.
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
```mermaid
graph LR
    subgraph Physical Device
    A[Phase A Power]
    B[Phase B Power]
    C[Phase C Power]
    end
    
    subgraph Template Logic
    Sum((Σ Sum))
    Start[Phase A + B + C]
    end
    
    subgraph Output Entities
    Total[Home Total Power<br>(Watts)]
    Energy[Home Total Energy<br>(kWh)]
    end

    A & B & C --> Start --> Sum
    Sum --> Total
    Sum --> Energy
```
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
