---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Philips Air Purifier

**Version:** 1.0.0  
**Description:** Normalizes Philips Air Purifier attributes (PM2.5, Filters)

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/philips_air_purifier.png)
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
*No specific entities detected to link.*
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
# Package: Philips Air Purifier
# Version: 1.0.0
# Description: Normalizes Philips Air Purifier attributes (PM2.5, Filters)
# Dependencies: fan.philips_air_purifier
# ------------------------------------------------------------------------------
template:
  - sensor:
      - name: "Purifier PM 2.5"
        unique_id: purifier_pm25
        unit_of_measurement: "μg/m³"
        device_class: pm25
        icon: mdi:blur
        state: >
          {{ state_attr('fan.philips_air_purifier', 'pm25') }}

      - name: "Purifier Allergen Index"
        unique_id: purifier_allergen_index
        unit_of_measurement: ""
        icon: mdi:sprout
        state: >
          {{ state_attr('fan.philips_air_purifier', 'allergen_index') }}

      - name: "Purifier Pre Filter"
        unique_id: purifier_pre_filter
        unit_of_measurement: "hours"
        icon: mdi:air-filter
        state: >
          {{ state_attr('fan.philips_air_purifier', 'pre_filter') }}

      - name: "Purifier Carbon Filter"
        unique_id: purifier_carbon_filter
        unit_of_measurement: "hours"
        icon: mdi:air-filter
        state: >
          {{ state_attr('fan.philips_air_purifier', 'carbon_filter') }}

      - name: "Purifier HEPA Filter"
        unique_id: purifier_hepa_filter
        unit_of_measurement: "hours"
        icon: mdi:air-filter
        state: >
          {{ state_attr('fan.philips_air_purifier', 'hepa_filter') }}

```
