# Dashboards

This configuration uses **Lovelace in Storage Mode**, meaning the dashboard configurations are stored in the `.storage/` directory (JSON format) rather than in `ui-lovelace.yaml`.

## Main Dashboard
**File**: `.storage/lovelace`
The default dashboard (Overview). It is highly customized and appears to serve as the main control center.
- **Views detected**: Home, Weather.
- **Key Cards**: Custom Button Card (heavily used), Timer Bar Card, mini-graph-card.

## Custom Dashboards
The following additional dashboards are registered in `.storage/lovelace_dashboards`:

| Title | URL Path | File (in `.storage/`) | Description/Icon |
| :--- | :--- | :--- | :--- |
| **Persons** | `/dashboard-persons` | `lovelace.dashboard_persons` | `mdi:account-group` - Person management |
| **System** | `/dashboard-system` | `lovelace.dashboard_system` | `mdi:cog-box` - System settings |
| **Notification Center** | `/notification-center` | `lovelace.notification_center` | Notification history/settings |
| **Room Management** | `/room-management` | `lovelace.room_management` | `mdi:floor-plan` - Room automation settings |
| **Home Access** | `/home-access` | `lovelace.home_access` | `mdi:key-chain-variant` - Locks/Doors |
| **Remotes** | `/dashboard-popups` | `lovelace.dashboard_popups` | `mdi:remote` - Popups? |
| **Room-PopUps** | `/room-popups` | `lovelace.room_popups` | `mdi:chart-bubble` |
| **Map** | `/map` | `lovelace.map` | `mdi:map` |
| **Zigbee2MQTT** | `/dashboard-zigbee2mqtt` | `lovelace.dashboard_zigbee2mqtt` | `mdi:zigbee` (Admin only) |
| **XDEV** | `/dashboard-dev` | `lovelace.dashboard_dev` | `mdi:dev-to` - Development |
| **DEV** | `/dashboard-dev2` | `lovelace.dashboard_dev2` | `mdi:dev-to` - Development 2 |
| **Demo** | `/dashboard-demo` | `lovelace.dashboard_demo` | `mdi:home` |

## Key Resources
The dashboards rely heavily on custom cards. Based on the configuration, the following seem to be critical dependencies:
- `custom:button-card`: Used for complex, dynamic buttons (e.g., room indicators).
- `custom:timer-bar-card`: Visual timers.
- `custom:mini-graph-card`: Electricity price graphs.
