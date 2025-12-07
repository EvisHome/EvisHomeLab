# Configuration & Structure

## Directory Structure

An overview of the key directories and files in the Home Assistant root folder.

| Directory / File | Purpose |
| :--- | :--- |
| **`.storage/`** | Internal Home Assistant storage for registries (devices, entities, etc.). **Do not edit manually.** |
| **`blueprints/`** | Stores automation blueprints downloaded or created for reusability. |
| **`button_card_templates/`** | Custom templates for `custom:button-card` Lovelace cards. |
| **`custom_components/`** | Custom integrations installed manually or via HACS. |
| **`custom_templates/`** | Global Jinja2 templates (macros) available throughout Home Assistant. |
| **`deps/`** | Python dependencies installed by Home Assistant or integrations. |
| **`docs_site/`** | This documentation repository and MkDocs site structure. |
| **`esphome/`** | ESPHome configuration YAML files and compilation artifacts (binaries). |
| **`include/`** | Split configuration files referenced from `configuration.yaml` to keep it clean. |
| **`model_cache/`** | Cache for local AI models (Wake words, assist pipelines). |
| **`node-red/`** | Storage for Node-RED flows and settings (if the add-on is used). |
| **`packages/`** | Configuration split into logical "packages" (bundling automations, scripts, configuration by feature). |
| **`pyscript/`** | Python scripts and apps for the `pyscript` integration. |
| **`themes/`** | Frontend themes definition files. |
| **`tts/`** | Text-to-speech cache or configuration. |
| **`www/`** | Publicly accessible folder mapped to `/local/` for hosting custom cards, images, and resources. |
| **`zigbee2mqtt/`** | Zigbee2MQTT data directory containing configuration and database. |
| **`zigbee2mqtt-2/`** | Secondary Zigbee2MQTT instance data directory. |
| **`automations.yaml`** | The main file for storing automations, commonly managed via the UI. |
| **`configuration.yaml`** | The main configuration file for Home Assistant. |
| **`scenes.yaml`** | Configuration file for defining scenes. |
| **`scripts.yaml`** | Configuration file for scripts (sequences of actions). |
| **`secrets.yaml`** | Stores sensitive data (passwords, tokens) referenced via `!secret`. |

---

## Configuration.yaml

Below is the current content of `configuration.yaml` with explanations for each section.

```yaml
# Core Home Assistant configuration
# Defines unit system, time zone, and package loading.
homeassistant:
  unit_system: metric
  time_zone: Europe/Helsinki
  ## Packages ##
  # 'packages' allows us to split configuration by feature 
  # (including automations, scripts, etc. in one file/folder)
  packages: !include_dir_named packages

# Loads the default set of integrations (Map, History, Logbook, etc.). 
# Essential for a standard experience.
default_config:

## NEEDED FOR TRAEFIK
# HTTP configuration triggers the HTTP server integration.
# 'use_x_forwarded_for' and 'trusted_proxies' are required when running 
# behind a reverse proxy (like Traefik) to correctly identify client IPs.
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.16.0.0/12
    - 10.0.0.0/8
    - 127.0.0.1

## THEMES ##
# Configures the Lovelace frontend.
# Currently set to include themes from the 'themes' directory (commented out).
frontend:
  #themes: !include_dir_merge_named themes

## TEXT TO SPEECH ##
# Configures the Text-to-Speech (TTS) integration.
# Using Google Translate platform for voice synthesis.
tts:
  - platform: google_translate

# Recorder handles storing data in the database (home-assistant_v2.db).
# Configured here to potentially exclude specific entities from history.
recorder:
#  exclude:
#    entities:

## HACS - PYSCRIPT ##
# Pyscript integration allows writing automations in Python.
# Configuration is split into 'include/pyscript.yaml'.
pyscript: !include include/pyscript.yaml

## PowerCal
# Powercalc integration estimates power consumption for non-smart devices.
# Configuration is split into 'include/powercalc.yaml'.
powercalc: !include include/powercalc.yaml

## CUSTOM/HACS - PHILIPS AIR PURIFIER ##
# Fan domain configuration.
# Specifically includes options for the Philips Air Purifier custom component.
fan: !include include/philips_air_purifier.yaml

## FILES ##
# Automations and Scripts files.
# These are typically managed by the UI editors.
automation: !include automations.yaml ## UI-managed
script: !include scripts.yaml ## UI-managed
```
