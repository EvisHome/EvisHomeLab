# EvisHomeLab

Welcome to the EvisHomeLab documentation.

![Dashboard Image](../../../assets/images/evishomelab.png)

## Sections
- **[Smart Home Documentation](smart-home/index.md)**: Home Assistant configuration, automations, and dashboards.
- **[Home Lab](home-lab/index.md)**: Server infrastructure, VMs, and containers.
- **[Network](network/index.md)**: Network topology, VLANs, and firewall rules.

!!! info "System Architecture & Maintenance"
    This documentation site is managed via an **Agentic CMDB Workflow**. It is automatically generated from the live Home Assistant configuration using Google Antigravity.

    * **Strategy:** Detached Docs (Private Config → Public Site)
    * **Tools:** Home Assistant OS, Antigravity IDE, Git, MkDocs Material

    [📖 **Read the full System Setup & Maintenance Manual**](system_manual/setup_guide.md)

## High Level Architecture

The system integrates various smart home technologies into a cohesive platform.

### Core System
- **Hub:** Home Assistant OS
- **Zigbee:** 2x Zigbee2MQTT networks (Main & Secondary)
- **Voice:** Home Assistant Assist (Wake Words & Pipelines)
- **Logic:** HACS Pyscript + Node-RED

### Key Integrations
| Domain | Technologies / Brands |
| :--- | :--- |
| **Climate & Air** | Philips Air Purifier, Airthings Wave (BLE), Aqara W500 |
| **Appliances** | LG Dishwasher (ThinQ), Shelly 3EM (Energy) |
| **Automotive** | Mercedes GLC (Mercedes Me), Garmin, Car Sensors |
| **Multimedia** | DNA TV Hub, Office PC (IoT Link) |
| **Logic & Data** | Nordpool Energy Prices, Home Time Modes, Scenes |
| **System** | Smart Notifications (Router), Room Automation (MQTT Dynamic), Fingerprint Mgmt |