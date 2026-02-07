---
tags:
  - homelab
  - landing
  - manual
---

# Home Lab & Infrastructure

Welcome to the **EvisHomeLab** infrastructure documentation. This section covers the "Metal" and "Wire" layers that power the Smart Home.

<div class="grid cards" markdown>

-   :material-lan: **[Network Topology](network_topology.md)**
    
    Physical cabling maps, VLAN segmentation, and IP addressing schemes for the UniFi network.

-   :material-server-network: **[Service Architecture](services.md)**
    
    The software layer. Proxmox clusters, VM inventory, Docker stacks, and application catalogs.

-   :material-server: **[Server Hardware](server_hardware.md)**
    
    Specifications and component inventory for compute nodes (HALO, EDGE) and Raspberry Pis.

-   :material-flash: **[Power Topology](power_topology.md)**
    
    UPS battery backup systems, PDU layouts, and emergency shutdown procedures.

-   :material-server-rack: **[Rack Elevation](rack_elevation.md)**
    
    Physical layout of the server rack, detailing unit (U) positions and cabling.

</div>

## Quick Specs

*   **Core Network:** 10Gbps SFP+ Backbone
*   **Hypervisor:** Proxmox VE (2-Node Cluster)
*   **Controller:** Home Assistant (VM)
*   **Storage:** *[TBD - e.g. TrueNAS / Synology]*
