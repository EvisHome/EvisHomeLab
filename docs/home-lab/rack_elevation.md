---
tags:
  - homelab
  - rack
  - manual
---

# Rack Elevation

Physical layout of the Server Rack.

**Total Height:** *[e.g. 24U, 42U]*

| Unit (U) | Device | Notes |
| :--- | :--- | :--- |
| **U24** | *Patch Panel?* | |
| **U23** | **UDM Pro** | Dream Machine Pro |
| **U22** | **USW-Aggregation** | 10G Aggregation Switch |
| **U21** | **USW-Enterprise-24-PoE** | Main Switch |
| **U20** | *Cable Management* | |
| **U19** | **Server | HALO** | Proxmox Primary |
| **U18** | **Server | HALO** | *(If 2U)* |
| **U17** | **Server | REACH** | Proxmox Node |
| **U16** | **Server | REACH** | *(If 2U)* |
| **U15** | **Server | EDGE** | Proxmox Secondary |
| **U14** | **Server | EDGE** | *(If 2U)* |
| **...** | | |
| **U05** | *Shelf* | Raspberry Pis, Hue Hub |
| **U01** | **UPS** | Battery Backup |

> [!NOTE]
> This table represents the physical vertical ordering of devices from Top (Highest U) to Bottom (U1).
