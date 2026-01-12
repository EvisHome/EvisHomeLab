---
tags:
  - package
  - automated
version: Unknown
---

# Package: Debug Script

**Version:** Unknown  
**Description:** No description provided.

<!-- START_IMAGE -->
![Package Diagram](assets/debug_script.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Dashboard Connections
<!-- START_DASHBOARD -->
*No specific entities detected to link.*
<!-- END_DASHBOARD -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
script:
  debug_mqtt_create_test:
    alias: "Debug: Create Test Entity"
    sequence:
      - service: mqtt.publish
        data:
          retain: true
          topic: "homeassistant/switch/area_debug_test/config"
          payload: >-
            {
              "name": "Area Debug Switch",
              "unique_id": "area_debug_switch_v1",
              "command_topic": "area/debug/set",
              "state_topic": "area/debug/state",
              "availability_topic": "area/debug/availability",
              "payload_available": "online"
            }
      - service: mqtt.publish
        data:
          retain: true
          topic: "area/debug/availability"
          payload: "online"
      - service: system_log.write
        data:
          message: "Debug Script Ran: Published area_debug_test"
          level: warning

```
