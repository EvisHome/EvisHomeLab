---
tags:
- security
- network
- frigate
- infrastructure
- manual
version: 1.0.1
---

# Frigate NVR System Documentation

**Version:** 1.0.1 (Documentation Only)
**Source:** External `config.yml` running on Unraid.
**Description:** Documentation of the external Frigate NVR instance (running on Unraid/Docker) and its connection to Home Assistant for critical notifications.

## Executive Summary

Frigate is the critical component responsible for local object detection and event management for security cameras. It runs externally on the **Unraid VM** within the **HALO Proxmox** server stack.

This package defines template entities (`Frigate System Status`) for HA health checks and documents the external configuration required to maintain service integrity. All detection events are pushed to Home Assistant via **MQTT**, which then triggers the Master Notification Scripts.

## Architecture & Data Flow

This diagram illustrates how the infrastructure layers feed data to Home Assistant. The health check sensor monitors if the final MQTT output is running.

```mermaid
graph TD
    subgraph Infrastructure Stack
        HALO[Host: Proxmox Server] --> UNRAID[VM: Unraid OS]
        UNRAID --> FRIGATE(Docker: Frigate NVR System)
    end
    FRIGATE --> MQTT(MQTT Broker)
    MQTT --> HA(Home Assistant OS)
    HA --> NOTIFY(Master Notifications)

    style FRIGATE fill:#03A9F4,stroke:#333,stroke-width:2px
    style HA fill:#4CAF50,stroke:#333,stroke-width:2px