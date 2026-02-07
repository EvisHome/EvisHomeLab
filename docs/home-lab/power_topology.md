---
tags:
  - homelab
  - power
  - manual
---

# Power Topology

Documentation of the power distribution, battery backup tiers, and PoE trees.

## 1. Power Map

The lab uses a **Two-Tier UPS** strategy for the main rack, plus independent power for remote nodes.

```mermaid
graph TD
    %% Nodes
    Grid[<b>Wall Outlet</b><br/>Grid Power]
    EcoFlow[<b>EcoFlow Delta 3</b><br/>Tier 1: Whole Rack Backup]
    PDU[<b>9-Outlet PDU</b><br/>Rack Distribution]
    APC[<b>APC 850 UPS</b><br/>Tier 2: Network Stack]
    
    %% Compute Powers
    subgraph Compute [Compute Cluster (Tier 1 Power)]
        Reach[Server | <b>Reach</b>]
        Halo[Server | <b>Halo</b>]
        Edge[Server | <b>Edge</b>]
    end

    %% Network Powers
    subgraph Network [Network Stack (Tier 1+2 Power)]
        UDM[UDM Pro]
        Agg[USW Aggregation]
        Ent[<b>USW Enterprise 24 PoE</b><br/>PoE Source]
    end

    %% PoE Leaf Devices
    subgraph PoE_Leafs [PoE Powered Devices]
        RPiA[RPi 5 A]
        RPiB[RPi 5 B]
        U7[U7 Pro AP]
        FlexFront[<b>USW Flex</b><br/>Front Porch]
    end

    %% Remote Power
    subgraph Remote [Remote Zones (Independent Power)]
        Injector[PoE Injector]
        Flex25[<b>USW Flex 2.5G</b><br/>Remote Room]
        FlexBack[<b>USW Flex</b><br/>Backyard]
    end

    %% Connections
    Grid --> EcoFlow
    EcoFlow -->|AC| PDU
    
    %% PDU Distribution
    PDU --> Reach
    PDU --> Halo
    PDU --> Edge
    PDU --> APC
    
    %% APC Distribution
    APC --> UDM
    APC --> Agg
    APC --> Ent
    
    %% PoE Tree
    Ent -.->|PoE| RPiA
    Ent -.->|PoE| RPiB
    Ent -.->|PoE+| U7
    Ent -.->|PoE++| FlexFront
    
    %% Remote Logic
    Injector -->|PoE Power| Flex25
    Ent ===|Data Only| Flex25
    Flex25 -.->|PoE| FlexBack
```

## 2. Backup Tiers

| Tier | Source | Runtime (Est) | Protected Scope |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Base)** | **EcoFlow Delta 3** | *High Capacity* | **Entire Rack** (Compute + Network). Filters dirty power. |
| **Tier 2 (Sensitive)** | **APC 850 UPS** | *Medium Capacity* | **Network Gear Only**. Provides double-conversion/clean power for UDM/Switches. |
| **Edge** | **PoE Injector** | *0 mins* | Remote Switch (USW Flex 2.5G) - No backup currently. |

## 3. PDU Layout (Main Rack)

*   **Source:** EcoFlow Delta 3 (AC Output)
*   **Distribution:**
    1.  **APC 850 UPS** (Feeds Network)
    2.  **Server | Halo**
    3.  **Server | Edge**
    4.  **Server | Reach**
    5.  *(Empty)*
    6.  *(Empty)*
    7.  *(Empty)*
    8.  *(Empty)*
    9.  *(Empty)*

## 4. PoE Power Budget (USW Enterprise 24 PoE)

The Main Switch powers a significant tree of downstream devices.

*   **Front Porch Chain:** Switch (PoE++) -> USW Flex -> Cameras (G4 Doorbell, G5 Turret).
*   **Internal Ops:** Raspberry Pi 5 A & B directly powered via PoE.
*   **Wireless:** U7 Pro AP (PoE+).
