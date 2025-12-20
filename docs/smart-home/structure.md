---
tags:
  - structure
  - configuration
  - automated
---

# Configuration & Structure

## Directory Structure
An overview of the key directories and files in the Home Assistant root folder.

| Directory / File | Purpose |
| :--- | :--- |
| **`.ag_scripts/`** | Python tooling for automated docs generation (Packages, Dashboards, Indexing). |
| **`.storage/`** | Internal Home Assistant storage for registries (devices, entities, etc.). **Do not edit manually.** |
| **`AI_CONTEXT.md`** | System prompt and context file for the creation of this AI Agent. |
| **`ag_v2_agent.py`** |  |
| **`ag_v2_dashboard.py`** |  |
| **`ag_v2_package.py`** |  |
| **`ag_v2_update.py`** |  |
| **`automations.yaml`** | The main file for storing automations, commonly managed via the UI. |
| **`blueprints/`** | Stores automation blueprints downloaded or created for reusability. |
| **`button_card_templates/`** | Custom templates for `custom:button-card` Lovelace cards. |
| **`configuration.yaml`** | The main configuration file for Home Assistant. |
| **`custom_components/`** | Custom integrations installed manually or via HACS. |
| **`custom_templates/`** | Global Jinja2 templates (macros) available throughout Home Assistant. |
| **`debug_regex.py`** |  |
| **`deps/`** | Python dependencies installed by Home Assistant or integrations. |
| **`docs_site/`** | This documentation repository and MkDocs site structure. |
| **`esphome/`** | ESPHome configuration YAML files and compilation artifacts (binaries). |
| **`home-assistant-wakewords-collection-main/`** | Directory. |
| **`home-assistant.log.fault`** |  |
| **`home-assistant_v2.db`** |  |
| **`home-assistant_v2.db-shm`** |  |
| **`home-assistant_v2.db-wal`** |  |
| **`image/`** | Directory. |
| **`include/`** | Split configuration files referenced from `configuration.yaml` to keep it clean. |
| **`model_cache/`** | Cache for local AI models (Wake words, assist pipelines). |
| **`node-red/`** | Storage for Node-RED flows and settings (if the add-on is used). |
| **`packages/`** | Configuration split into logical "packages" (bundling automations, scripts, configuration by feature). |
| **`pyscript/`** | Python scripts and apps for the `pyscript` integration. |
| **`scenes.yaml`** | Configuration file for defining scenes. |
| **`scripts.yaml`** | Configuration file for scripts (sequences of actions). |
| **`secrets.yaml`** | Stores sensitive data (passwords, tokens) referenced via `!secret`. |
| **`themes/`** | Frontend themes definition files. |
| **`tts/`** | Text-to-Speech cache or configuration. |
| **`www/`** | Publicly accessible folder mapped to `/local/` for hosting custom cards, images, and resources. |
| **`zigbee2mqtt/`** | Zigbee2MQTT data directory containing configuration and database. |
| **`zigbee2mqtt-2/`** | Secondary Zigbee2MQTT instance data directory. |

---

## Configuration.yaml
Below is the current content of `configuration.yaml` with explanations for each section.

```yaml
homeassistant:
  unit_system: metric
  time_zone: Europe/Helsinki
  ## Packages ##
  packages: !include_dir_named packages

# Loads default set of integrations. Do not remove.
default_config:

## NEEDED FOR TRAEFIK
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.16.0.0/12
    - 10.0.0.0/8
    - 127.0.0.1

## THEMES ##
frontend:
  #themes: !include_dir_merge_named themes

## TEXT TO SPEECH ##
tts:
  - platform: google_translate

recorder:
#  exclude:
#    entities:

## HACS - PYSCRIPT ##
pyscript: !include include/pyscript.yaml

## PowerCal
powercalc: !include include/powercalc.yaml

## CUSTOM/HACS - PHILIPS AIR PURIFIER ##
fan: !include include/philips_air_purifier.yaml

## FILES ##
automation: !include automations.yaml ## UI-managed
script: !include scripts.yaml ## UI-managed

```
