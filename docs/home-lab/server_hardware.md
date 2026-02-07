---
tags:
  - homelab
  - hardware
  - manual
---

# Server Hardware

Inventory of the physical compute nodes in the Home Lab.

!!! info "Device Separation"
    This page tracks **Compute Hardware** (Servers, Pis). For Smart Home IoT devices (Sensors, Lights), see the [Device Inventory](../inventory/index.md).

## 1. Proxmox Nodes

The core compute cluster consists of two nodes: **HALO** (Primary) and **EDGE** (Secondary).

=== "Server | HALO"

    **Role:** Primary Compute / Stable Workloads  
    **OS:** Proxmox VE 8.x
    
    | Component | Specification | Notes |
    | :--- | :--- | :--- |
    | **Chassis** | *TBD* | 2U/4U Rackmount? |
    | **CPU** | *TBD* | Intel/AMD ? |
    | **RAM** | *TBD* | DDR4/5 ECC? |
    | **Storage (Boot)** | *TBD* | NVMe/SSD? |
    | **Storage (Data)** | *TBD* | ZFS Pool? |
    | **Network** | 10GbE SFP+ | Connected to Aggregation Switch |

=== "Server | REACH"

    **Role:** Compute / Expansion
    **OS:** Proxmox VE 8.x

    | Component | Specification | Notes |
    | :--- | :--- | :--- |
    | **Chassis** | *TBD* | |
    | **CPU** | *TBD* | |
    | **RAM** | *TBD* | |
    | **Storage** | *TBD* | |
    | **Network** | *TBD* | |

=== "Server | EDGE"

    **Role:** Secondary Compute / Docker Host / Testing  
    **OS:** Proxmox VE 8.x

    | Component | Specification | Notes |
    | :--- | :--- | :--- |
    | **Chassis** | *TBD* | |
    | **CPU** | *TBD* | |
    | **RAM** | *TBD* | |
    | **Storage** | *TBD* | |
    | **Network** | 10GbE SFP+ | Connected to Aggregation Switch |

---

## 2. Raspberry Pis

Low-power, independent nodes for critical infrastructure (DNS, NTP) that must survive a main server restart.

*   **DNS 63:** Raspberry Pi 4 (Role: Primary DNS/NTP)
*   **DNS 62:** Raspberry Pi 4 (Role: Secondary DNS/NTP)
*   **RPi 5 A:** Raspberry Pi 5 (Role: *TBD*)
*   **RPi 5 B:** Raspberry Pi 5 (Role: *TBD*)

---

## 3. Storage Infrastructure (NAS)

*(Details about separate NAS hardware if applicable, or reference the Proxmox storage above)*
