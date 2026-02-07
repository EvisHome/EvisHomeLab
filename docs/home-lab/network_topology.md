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
    %% Define Styles
    classDef core fill:#2a2a2a,stroke:#fff,stroke-width:2px;
    classDef edge fill:#1f425f,stroke:#fff,stroke-width:1px;
    classDef client fill:#1a5c20,stroke:#fff,stroke-width:1px;

    %% Nodes grouped by location/logic to force cleaner layout
    ISP["ISP: DNA Oyj"]

    subgraph Core_Net [Core Network]
        direction TB
        UDM["UDM Pro\nDream Machine Pro"]:::core
        Agg["USW-Aggregation\n10G Core"]:::core
        Ent["USW-Enterprise-24-PoE\nAccess Switch"]:::core
    end
    
    subgraph Servers [Compute Clients]
        Halo["Server | HALO\nProxmox Node"]:::client
        Edge["Server | EDGE\nProxmox Node"]:::client
    end
    
    subgraph Downstream [Edge Switches]
        Lite8["USW-Lite-8-PoE\nLiving Room"]:::edge
        FlexBack["USW-Flex\nBackyard"]:::edge
        FlexFront["USW-Flex\nFront Porch"]:::edge
        FlexMini["USW-Flex-Mini\nOffice?"]:::edge
    end
    
    subgraph Wireless [Access Points]
        U7Pro["U7 Pro\nUpstairs"]:::edge
        U6Lite["U6-Lite\nBackyard"]:::edge
    end

    subgraph IoT [IoT Clients]
        PiDNS1["RPi | DNS 63\nNTP/DNS"]:::client
        PiDNS2["RPi | DNS 62\nNTP/DNS"]:::client
    end

    %% Main Backbone Connections
    ISP -->|WAN| UDM
    UDM -->|10G DAC| Agg
    Agg -->|20G LACP| Ent
    
    %% Server Connections (Direct from Aggregation)
    Agg -->|10G DAC| Halo
    Agg -->|10G DAC| Edge
    
    %% Downstream Switch Connections (From Enterprise)
    Ent -->|Eth| Lite8
    Ent -->|Eth| FlexBack
    Ent -->|Eth| FlexFront
    Ent -->|Eth| FlexMini
    Ent -->|Eth| PiDNS1
    Ent -->|Eth| PiDNS2
    
    %% Wireless & PoE Chain
    Ent -->|PoE+| U7Pro
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
