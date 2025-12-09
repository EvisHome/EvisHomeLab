---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Dna Tv Hub

**Version:** 1.0.0  
**Description:** Template switch for DNA TV Hub remote control

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/dna_tv_hub.png)
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
# Package: DNA TV Hub
# Version: 1.0.0
# Description: Template switch for DNA TV Hub remote control
# Dependencies: remote.dna_tv_hub
# ------------------------------------------------------------------------------
template:
  - switch:
      - name: "DNA TV HUB"
        unique_id: dna_tv_hub
        icon: mdi:television
        state: "{{ is_state('remote.dna_tv_hub', 'on') }}"
        turn_on:
          service: remote.turn_on
          target:
            entity_id: remote.dna_tv_hubi
        turn_off:
          service: remote.turn_off
          target:
            entity_id: remote.dna_tv_hubi

```
