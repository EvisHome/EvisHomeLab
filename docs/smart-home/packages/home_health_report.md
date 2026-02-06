---
tags:
  - package
  - automated
  - notification
version: 1.0.0
---

# Package: Home Health Report

**Version:** 1.0.0
**Description:** A local, privacy-focused daily briefing that summarizes home environment and energy costs.

<!-- START_IMAGE -->
{{ package_image(page.file.name) }}
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
The **Home Health Report** is a daily automation that runs every morning to brief you on the state of your home. Unlike the AI Reporter which focuses on server logs, this report focuses on **health and wallet** metrics. It aggregates data from local sensors (Airthings Wave, Shelly Energy, Nordpool prices) and sends a concise notification to your mobile device, letting you know if the air quality was good overnight and how much energy you used yesterday.
<!-- END_SUMMARY -->

## Process Description
<!-- START_DETAILED -->
1.  **Trigger:** Runs daily at **07:15 AM**.
2.  **Data Collection:**
    *   **Air Quality:** Checks the overnight CO2 average from the Airthings Wave Plus.
    *   **Energy Cost:** tallied for yesterday (using Shelly 3EM + Nordpool data).
    *   **Price Forecast:** Checks today's average electricity price.
3.  **Notifications:** Sends a rich notification to all mobile app targets.
<!-- END_DETAILED -->

## Dependencies
<!-- START_DEPENDENCIES -->
*   **[Nordpool Prices](nordpool_prices.md)**: Required for price data (`sensor.nordpool_fi_daily_average`).
*   **Shelly 3EM** (or equivalent): For total energy usage (`sensor.shelly_home_energy_daily`).
*   **Airthings Wave Plus**: For air quality (`sensor.airthings_wave_plus_co2`).
<!-- END_DEPENDENCIES -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Home Health Report
# Version: 1.0.0
# Description: Daily briefing for Air Quality and Energy
# ------------------------------------------------------------------------------

automation:
  - alias: "Daily Home Health Report"
    id: daily_home_health_report
    trigger:
      - platform: time
        at: "07:15:00"
    action:
      - service: notify.notify # specific targets: notify.mobile_app_jukka_phone
        data:
          title: "Good Morning! ☀️"
          message: >
            {% set price = states('sensor.nordpool_fi_daily_average') | float(0) * 100 %}
            {% set cost_yesterday = states('sensor.energy_cost_yesterday') | default(0) %}
            {% set co2 = states('sensor.airthings_wave_plus_co2') | float(400) %}
            
            💡 **Energy:**
            • Today's Avg: {{ price | round(1) }} c/kWh
            {% if price < 5 %} (🟢 Cheap)
            {% elif price > 15 %} (🔴 Expensive)
            {% else %} (🟡 Normal) {% endif %}
            
            🌬️ **Air Quality (Bedroom):**
            • CO2: {{ co2 | int }} ppm
            {% if co2 < 800 %} (🟢 Excellent)
            {% elif co2 < 1200 %} (🟡 Okay)
            {% else %} (🔴 Poor - Open a window!) {% endif %}

            💰 **Yesterday's Spend:**
            • Total: {{ cost_yesterday }} €
          data:
            notification_icon: "mdi:coffee"
            clickAction: "/lovelace/main"
            group: "daily-brief"
```
