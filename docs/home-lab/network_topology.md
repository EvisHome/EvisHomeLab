---
tags:
  - homelab
  - network
  - manual
---

# Network Topology

This page documents the physical and logical layout of the EvisHomeLab network.

## 1. Physical Topology

The core network is built on Ubiquiti UniFi gear, interconnected via 10Gbps SFP+ DACs and fiber where possible.

### Network Map

> [!INFO]
> **Visualization:** This diagram represents the physical cabling hierarchy.

```mermaid
graph TD
    %% Nodes
    ISP["ISP: DNA Oyj"]
    UDM["UDM Pro\nDream Machine Pro"]
    Agg["USW-Aggregation\n10G Core"]
    Ent["USW-Enterprise-24-PoE\nAccess Switch"]
    
    %% Downstream Switches
    Lite8["USW-Lite-8-PoE\nLiving Room"]
    FlexBack["USW-Flex\nBackyard"]
    FlexFront["USW-Flex\nFront Porch"]
    FlexMini["USW-Flex-Mini\nOffice?"]
    
    %% Access Points
    U7Pro["U7 Pro\nUpstairs"]
    U6Lite["U6-Lite\nBackyard"]

    %% Key Clients
    Halo["Server | HALO\nProxmox Node"]
    Edge["Server | EDGE\nProxmox Node"]
    PiDNS1["RPi | DNS 63\nNTP/DNS"]
    PiDNS2["RPi | DNS 62\nNTP/DNS"]

    %% Connections
    ISP -->|WAN| UDM
    UDM -->|10G SFP+| Agg
    
    Agg -->|10G SFP+| Ent
    Agg -->|10G SFP+| Halo
    Agg -->|10G SFP+| Edge
    
    Ent -->|Link| Lite8
    Ent -->|Link| FlexBack
    Ent -->|Link| FlexFront
    Ent -->|Link| FlexMini
    
    %% Wireless Links
    Ent -->|PoE| U7Pro
    FlexBack -->|PoE| U6Lite
```

### Device Hierachy

| Tier | Device | Role | Connection |
| :--- | :--- | :--- | :--- |
| **Core** | **UDM Pro** | Gateway / Router | WAN (ISP) |
| **Core** | **USW-Aggregation** | Layer 2 Aggregation | 10G SFP+ to UDM |
| **Access** | **USW-Enterprise-24-PoE** | Main Switch | 10G SFP+ to Agg |
| **Edge** | **USW-Lite-8-PoE** | Living Room Media | Uplink to Ent |
| **Edge** | **USW-Flex (Backyard)** | Outdoor PoE | Uplink to Ent |
| **Edge** | **USW-Flex (Front Porch)** | Outdoor PoE | Uplink to Ent |
| **Edge** | **USW-Flex-Mini** | Desktop/Misc | Uplink to Ent |

---

## 2. Logical Topology (VLANs)

*Defined network segments for isolation and security.*

| VLAN ID | Subnet | Name | Purpose |
| :--- | :--- | :--- | :--- |
| **1** | `10.0.1.0/24` | **Management** | Network Gear & Core Infra |
| **TBD** | `TBD` | **IoT** | Untrusted Smart Devices |
| **TBD** | `TBD` | **Servers** | Proxmox, NAS, Docker |
| **TBD** | `TBD` | **Users** | Trusted Phones/Laptops |
| **TBD** | `TBD` | **Guest** | Visitors (Client Isolation) |

> [!WARNING]
> VLAN IDs and Subnets need to be verified against the UDM Pro configuration.

---

## 3. Addressing

### Key Gateways
*   **UDM Pro:** `10.0.1.1` (Default Gateway)
*   **DNS 1 (Pi-hole/AdGuard):** `10.0.x.63`
*   **DNS 2 (Pi-hole/AdGuard):** `10.0.x.62`
