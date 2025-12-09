---
tags:
  - package
  - automated
version: 1.0.0
---

# Package: Nordpool Prices

**Version:** 1.0.0  
**Description:** Nordpool energy price calculations and logic

<!-- START_IMAGE -->
![Package Diagram](../../../assets/images/packages/nordpool_prices.png)
<!-- END_IMAGE -->

## Executive Summary
<!-- START_SUMMARY -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No executive summary generated yet.*
<!-- END_SUMMARY -->

## Process Description (Non-Technical)
<!-- START_DETAILED -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No detailed non-technical description generated yet.*
<!-- END_DETAILED -->

## Architecture Diagram
<!-- START_MERMAID_DESC -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture explanation generated yet.*
<!-- END_MERMAID_DESC -->

<!-- START_MERMAID -->
> ⚠️ **Update Required:** Analysis for v0.0.0. Code is v1.0.0.

*No architecture diagram generated yet.*
<!-- END_MERMAID -->

## Configuration (Source Code)
```yaml
# ------------------------------------------------------------------------------
# Package: Nordpool Prices
# Version: 1.0.0
# Description: Nordpool energy price calculations and logic
# Dependencies: nordpool.get_prices_for_date, sensor.shelly_home_energy_15min
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 2. INPUT BOOLEANS (Flags & Maintenance)
# ------------------------------------------------------------------------------
input_boolean:
  # Energy Prices: Sent flag
  notify_flag_energy_tomorrow_sent:
    name: "Energy: Tomorrow Prices Sent"
    icon: mdi:checkbox-marked-circle-outline

template:
  - triggers:
      - platform: time_pattern
        minutes: "/1"
      - platform: homeassistant
        event: start

    actions:
      - alias: "Fetch Today's Prices"
        service: nordpool.get_prices_for_date
        data:
          config_entry: 01K72AW80S016AZ3CPD6R2062J
          date: "{{ now().date() }}"
          areas: FI
          currency: EUR
        response_variable: today_price

      - alias: "Fetch Tomorrow's Prices"
        service: nordpool.get_prices_for_date
        data:
          config_entry: 01K72AW80S016AZ3CPD6R2062J
          date: "{{ now().date() + timedelta(days=1) }}"
          areas: FI
          currency: EUR
        response_variable: tomorrow_price

    sensor:
      - name: Electricity prices
        unique_id: electricity_prices
        unit_of_measurement: "c/kWh"
        icon: mdi:cash
        state: >
          {%- set region = (this.attributes.get('region', 'FI') | string) -%}
          {%- set tax = (this.attributes.get('tax', 1.0) | float) -%}
          {%- set additional_cost = (this.attributes.get('additional_cost', 0.0) | float) -%}

          {% if (today_price is mapping) and (tomorrow_price is mapping) %}
            {% set data = namespace(prices=[]) %}
            {% for state in today_price[region] %}
              {% set data.prices = data.prices + [(((state.price/10 | float)  * tax + additional_cost)) | round(3, default=0)] %}
            {% endfor %}
            {% for state in tomorrow_price[region] %}
              {% set data.prices = data.prices + [(((state.price/10 | float) * tax + additional_cost)) | round(3, default=0)] %}
            {% endfor %}
            {{min(data.prices)}}
          {% else %}
            unavailable
          {% endif %}
        attributes:
          tomorrow_valid: >
            {%- set region = (this.attributes.get('region', 'FI') | string) -%}
            {%- if (tomorrow_price is mapping) %}
              {%- if tomorrow_price[region] | list | count > 0 -%}
                {{ true | bool }}
              {%- else %}
                {{ false | bool }}
              {%- endif %}
            {%- else %}
              {{ false | bool }}
            {%- endif %}
          data: >
            {%- set region = (this.attributes.get('region', 'FI') | string) -%}
            {%- set tax = (this.attributes.get('tax', 1.0) | float) -%}
            {%- set additional_cost = (this.attributes.get('additional_cost', 0.0) | float) -%}

            {% if (today_price is mapping) and (tomorrow_price is mapping) %}
            {% set data = namespace(prices=[]) %}
              {% for state in today_price[region] %}
                {% set local_start = as_datetime(state.start).astimezone().strftime('%Y-%m-%d %H:%M:%S') %}
                {% set local_end = as_datetime(state.end).astimezone().strftime('%Y-%m-%d %H:%M:%S') %}
                {% set data.prices = data.prices + [{'start':local_start, 'end':local_end, 'price': (((state.price/10 | float) * tax + additional_cost)) | round(3, default=0)}] %}
              {% endfor %}
              {% for state in tomorrow_price[region] %}
                {% set local_start = as_datetime(state.start).astimezone().strftime('%Y-%m-%d %H:%M:%S') %}
                {% set local_end = as_datetime(state.end).astimezone().strftime('%Y-%m-%d %H:%M:%S') %}
                {% set data.prices = data.prices + [{'start':local_start, 'end':local_end, 'price': (((state.price/10 | float) * tax + additional_cost)) | round(3, default=0)}] %}
              {% endfor %}
              {{data.prices}}
            {% else %}
              []
            {% endif %}
          tax: "1"
          additional_cost: "0"
          region: FI

  - sensor:
      - name: "Electricity Price (cents)"
        unique_id: electricity_price_cents
        unit_of_measurement: "c/kWh"
        state_class: measurement
        state: >
          {{ (states('sensor.electricity_prices') | float(0) * 100) | round(1) }}

  - sensor:
      - name: "Electricity Daily Average (cents)"
        unique_id: electricity_daily_average_cents
        unit_of_measurement: "c/kWh"
        state_class: measurement
        state: >
          {{ (states('sensor.nord_pool_fi_daily_average') | float(0) * 100) | round(1) }}

  - sensor:
      - name: "Electricity Today 32nd Lowest Price"
        unique_id: electricity_today_32nd_lowest
        unit_of_measurement: "c/kWh"
        state: >
          {% set today = now().date().isoformat() %}
          {% set entries = state_attr('sensor.electricity_prices', 'data') %}
          {% if entries %}
            {% set today_prices = entries
              | selectattr('start', 'defined')
              | selectattr('start', 'string')
              | selectattr('start', 'search', today)
              | map(attribute='price')
              | list %}
            {% if today_prices | count >= 32 %}
              {% set sorted = today_prices | sort %}
              {{ sorted[31] | round(2) }}
            {% else %}
              none
            {% endif %}
          {% else %}
            none
          {% endif %}

  - sensor:
      - name: "Electricity Today 32nd Highest Price"
        unique_id: electricity_today_32nd_highest
        unit_of_measurement: "c/kWh"
        state: >
          {% set today = now().date() %}
          {% set entries = state_attr('sensor.electricity_prices', 'data') %}
          {% if entries %}
            {% set today_prices = entries
              | selectattr('start', 'defined')
              | selectattr('start', 'string')
              | selectattr('start', 'search', today.isoformat())
              | map(attribute='price')
              | list %}
            {% if today_prices | count >= 32 %}
              {% set sorted = today_prices | sort(reverse=true) %}
              {{ sorted[31] | round(2) }}
            {% else %}
              none
            {% endif %}
          {% else %}
            none
          {% endif %}

  - sensor:
      - name: "Electricity Tomorrow Valid"
        unique_id: electricity_tomorrow_valid
        state: >
          {{ state_attr('sensor.electricity_prices', 'tomorrow_valid') }}

  - sensor:
      - name: "Electricity Tomorrow 32nd Lowest Price"
        unique_id: electricity_tomorrow_32nd_lowest
        unit_of_measurement: "c/kWh"
        state: >
          {% set tomorrow = (now() + timedelta(days=1)).date().isoformat() %}
          {% set entries = state_attr('sensor.electricity_prices', 'data') %}
          {% if entries %}
            {% set tomorrow_prices = entries
              | selectattr('start', 'defined')
              | selectattr('start', 'string')
              | selectattr('start', 'search', tomorrow)
              | map(attribute='price')
              | list %}
            {% if tomorrow_prices | count >= 32 %}
              {% set sorted = tomorrow_prices | sort %}
              {{ sorted[31] | round(2) }}
            {% else %}
              none
            {% endif %}
          {% else %}
            none
          {% endif %}

  - sensor:
      - name: "Electricity Tomorrow 32nd Highest Price"
        unique_id: electricity_tomorrow_32nd_highest
        unit_of_measurement: "c/kWh"
        state: >
          {% set tomorrow = (now() + timedelta(days=1)).date().isoformat() %}
          {% set entries = state_attr('sensor.electricity_prices', 'data') %}
          {% if entries %}
            {% set tomorrow_prices = entries
              | selectattr('start', 'defined')
              | selectattr('start', 'string')
              | selectattr('start', 'search', tomorrow)
              | map(attribute='price')
              | list %}
            {% if tomorrow_prices | count >= 32 %}
              {% set sorted = tomorrow_prices | sort(reverse=true) %}
              {{ sorted[31] | round(2) }}
            {% else %}
              none
            {% endif %}
          {% else %}
            none
          {% endif %}

  - sensor:
      - name: "Energy Cost 15min"
        unique_id: energy_cost_15min
        unit_of_measurement: "€"
        state_class: measurement
        state: >
          {% set energy_kwh = states('sensor.shelly_home_energy_15min') | float(0) %}
          {% set price_c = states('sensor.nord_pool_fi_current_price') | float(0) * 100 %}
          {% set transfer_c = states('input_number.energy_transfer_fee') | float(0) %}
          {% set tax_c = states('input_number.energy_tax_c_kwh') | float(0) %}
          {% set vat_pct = states('input_number.energy_vat') | float(0) / 100 %}
          {% set subtotal_c = price_c + transfer_c + tax_c %}
          {% set cost_eur = (energy_kwh * subtotal_c / 100) * (1 + vat_pct) %}
          {{ cost_eur | round(3) }}
        attributes:
          energy_kWh: "{{ states('sensor.shelly_home_energy_15min') | float(0) | round(3) }}"
          spot_price_c_per_kWh: "{{ (states('sensor.nord_pool_fi_current_price') | float(0) * 100) | round(2) }}"
          transfer_fee_c_per_kWh: "{{ states('input_number.energy_transfer_fee') | float(0) | round(2) }}"
          energy_tax_c_per_kWh: "{{ states('input_number.energy_tax_c_kwh') | float(0) | round(2) }}"
          vat_pct: "{{ states('input_number.energy_vat') | float(0) | round(2) }}"
          subtotal_c_per_kWh: "{{ ((states('sensor.nord_pool_fi_current_price') | float(0) * 100) + states('input_number.energy_transfer_fee') | float(0) + states('input_number.energy_tax_c_kwh') | float(0)) | round(2) }}"
          cost_eur: "{{ ((states('sensor.shelly_home_energy_15min') | float(0) * ((states('sensor.nord_pool_fi_current_price') | float(0) * 100 + states('input_number.energy_transfer_fee') | float(0) + states('input_number.energy_tax_c_kwh') | float(0)) / 100)) * (1 + states('input_number.energy_vat') | float(0) / 100)) | round(3) }}"

  - sensor:
      - name: "Energy Cost 15min (c)"
        unique_id: energy_cost_15min_c
        unit_of_measurement: "c"
        state_class: measurement
        state: >
          {% set energy_kwh = states('sensor.shelly_home_energy_15min') | float(0) %}
          {% set price_c = states('sensor.nord_pool_fi_current_price') | float(0) * 100 %}
          {% set transfer_c = states('input_number.energy_transfer_fee') | float(0) %}
          {% set tax_c = states('input_number.energy_tax_c_kwh') | float(0) %}
          {% set vat_pct = states('input_number.energy_vat') | float(0) / 100 %}
          {% set subtotal_c = price_c + transfer_c + tax_c %}
          {% set cost_c = energy_kwh * subtotal_c * (1 + vat_pct) %}
          {{ cost_c | round(2) }}
        attributes:
          energy_kWh: "{{ states('sensor.shelly_home_energy_15min') | float(0) | round(3) }}"
          spot_price_c_per_kWh: "{{ (states('sensor.nord_pool_fi_current_price') | float(0) * 100) | round(2) }}"
          transfer_fee_c_per_kWh: "{{ states('input_number.energy_transfer_fee') | float(0) | round(2) }}"
          energy_tax_c_per_kWh: "{{ states('input_number.energy_tax_c_kwh') | float(0) | round(2) }}"
          vat_pct: "{{ states('input_number.energy_vat') | float(0) | round(2) }}"
          subtotal_c_per_kWh: "{{ ((states('sensor.nord_pool_fi_current_price') | float(0) * 100) + states('input_number.energy_transfer_fee') | float(0) + states('input_number.energy_tax_c_kwh') | float(0)) | round(2) }}"
          cost_eur: "{{ ((states('sensor.shelly_home_energy_15min') | float(0) * ((states('sensor.nord_pool_fi_current_price') | float(0) * 100 + states('input_number.energy_transfer_fee') | float(0) + states('input_number.energy_tax_c_kwh') | float(0)) / 100)) * (1 + states('input_number.energy_vat') | float(0) / 100)) | round(3) }}"

  - trigger:
      - platform: state
        entity_id: sensor.shelly_home_energy_15min
        to: "0"
    sensor:
      - name: "Energy Cost Final 15min (c)"
        unique_id: energy_cost_final_15min_c
        unit_of_measurement: "c"
        device_class: monetary
        state_class: measurement
        state: >
          {% set energy_kwh = trigger.from_state.state | float(0) %}
          {% set ts = now() - timedelta(seconds=1) %}
          {% set aligned = ts.replace(minute=(ts.minute // 15) * 15, second=0, microsecond=0) %}
          {% set blocks = state_attr('sensor.electricity_prices', 'data') %}
          {% set block = blocks | selectattr('start', 'equalto', aligned.strftime('%Y-%m-%d %H:%M:%S')) | list | first %}
          {% set price_c = block.price | float(0) * 100 %}
          {% set transfer_c = states('input_number.energy_transfer_fee') | float(0) %}
          {% set tax_c = states('input_number.energy_tax_c_kwh') | float(0) %}
          {% set vat_pct = states('input_number.energy_vat') | float(0) / 100 %}
          {% set subtotal_c = price_c + transfer_c + tax_c %}
          {% set cost_c = energy_kwh * subtotal_c * (1 + vat_pct) %}
          {{ cost_c | round(2) }}
        attributes:
          energy_kWh: "{{ trigger.from_state.state | float(0) | round(3) }}"
          spot_price_c_per_kWh: >
            {% set ts = now() - timedelta(seconds=1) %}
            {% set aligned = ts.replace(minute=(ts.minute // 15) * 15, second=0, microsecond=0) %}
            {% set blocks = state_attr('sensor.electricity_prices', 'data') %}
            {% set block = blocks | selectattr('start', 'equalto', aligned.strftime('%Y-%m-%d %H:%M:%S')) | list | first %}
            {{ block.price | float(0) * 100 | round(2) }}
          transfer_fee_c_per_kWh: "{{ states('input_number.energy_transfer_fee') | float(0) | round(2) }}"
          energy_tax_c_per_kWh: "{{ states('input_number.energy_tax_c_kwh') | float(0) | round(2) }}"
          vat_pct: "{{ states('input_number.energy_vat') | float(0) | round(2) }}"
          subtotal_c_per_kWh: >
            {% set ts = now() - timedelta(seconds=1) %}
            {% set aligned = ts.replace(minute=(ts.minute // 15) * 15, second=0, microsecond=0) %}
            {% set blocks = state_attr('sensor.electricity_prices', 'data') %}
            {% set block = blocks | selectattr('start', 'equalto', aligned.strftime('%Y-%m-%d %H:%M:%S')) | list | first %}
            {% set price_c = block.price | float(0) * 100 %}
            {% set transfer_c = states('input_number.energy_transfer_fee') | float(0) %}
            {% set tax_c = states('input_number.energy_tax_c_kwh') | float(0) %}
            {{ (price_c + transfer_c + tax_c) | round(2) }}
          cost_eur: >
            {% set energy_kwh = trigger.from_state.state | float(0) %}
            {% set ts = now() - timedelta(seconds=1) %}
            {% set aligned = ts.replace(minute=(ts.minute // 15) * 15, second=0, microsecond=0) %}
            {% set blocks = state_attr('sensor.electricity_prices', 'data') %}
            {% set block = blocks | selectattr('start', 'equalto', aligned.strftime('%Y-%m-%d %H:%M:%S')) | list | first %}
            {% set price_c = block.price | float(0) * 100 %}
            {% set transfer_c = states('input_number.energy_transfer_fee') | float(0) %}
            {% set tax_c = states('input_number.energy_tax_c_kwh') | float(0) %}
            {% set vat_pct = states('input_number.energy_vat') | float(0) / 100 %}
            {% set subtotal_c = price_c + transfer_c + tax_c %}
            {% set cost_c = energy_kwh * subtotal_c * (1 + vat_pct) %}
            {{ (cost_c / 100) | round(3) }}

  - sensor: # <-- CORRECTED: Use '- sensor:' inside the 'template:' block
      - name: "Current 15-Minute Electricity Price"
        unique_id: "current_15min_electricity_price"
        unit_of_measurement: "c/kWh"
        device_class: monetary
        state_class: measurement
        state: >
          {# 1. Get the list of prices from the 'data' attribute #}
          {% set price_data = state_attr('sensor.electricity_prices', 'data') %}
          {% set current_time = now() %}

          {# 2. Find the entry where the current time is between 'start' and 'end' #}
          {% set current_price_item = price_data | selectattr('start', 'le', current_time.isoformat()) | selectattr('end', 'gt', current_time.isoformat()) | first %}

          {% if current_price_item is defined %}
            {# 3. Use the price value directly (it is already in cents/kWh) #}
            {{ current_price_item.price | float(0) | round(3) }}
          {% else %}
            {# Fallback: If no block is found, use the main state, also in c/kWh #}
            {{ states('sensor.electricity_prices') | float(0) }}
          {% endif %}

  # The second sensor goes under the same top-level 'template:' key
  - sensor: # <-- CORRECTED: Use '- sensor:' for the second sensor as well
      - name: "15-Minute Energy Cost Block"
        unique_id: "15min_energy_cost_block_total"
        unit_of_measurement: "c"
        device_class: monetary
        state_class: total
        state: >
          {# Get the energy usage from the Utility Meter (Step 1: sensor.15_minute_energy_usage) #}
          {% set usage = states('sensor.15_minute_energy_usage') | float(0) %}
          {# Get the current price from the Template Sensor defined above #}
          {% set price = states('sensor.current_15_minute_electricity_price') | float(0) %}

          {# Calculation: Energy (kWh) * Price (c/kWh) = Total Cost in Cents (c) #}
          {{ (usage * price) | float | round(2) }}

  - sensor:
      - name: "Tomorrow Average Electricity Price"
        # Unique ID for the sensor
        unique_id: tomorrow_average_electricity_price
        # Set the unit of measurement, copied from your existing sensor
        unit_of_measurement: "c/kWh"
        # Set the device class to 'monetary' so it's treated as a price
        device_class: monetary
        # Set the state class for long-term statistics
        state_class: measurement
        # The 'icon' is optional, but this one fits
        icon: "mdi:chart-line"
        # This is where the magic happens
        state: >
          {% set tomorrow_str = (now().date() + timedelta(days=1)).isoformat() %}
          {% set price_data = state_attr('sensor.electricity_prices', 'truedata') %}

          {% if price_data is not none %}
            {% set tomorrow_prices = price_data 
                                     | selectattr('start', 'starts_with', tomorrow_str) 
                                     | map(attribute='price') 
                                     | list %}
            
            {% if tomorrow_prices | count > 0 %}
              {{ tomorrow_prices | average | round(3) }}
            {% else %}
              {# This will happen if tomorrow's data is not yet available #}
              unavailable
            {% endif %}
          {% else %}
            {# This will happen if the 'truedata' attribute is missing #}
            unavailable
          {% endif %}

```

## Dashboard Connections
<!-- START_DASHBOARD -->
This package powers the following dashboard views:

* **[Bathroom](../dashboards/main/bathroom.md)** (Uses 1 entities)
* **[Electricity Dev](../dashboards/main/electricity-dev.md)** (Uses 1 entities)
* **[Electricity](../dashboards/main/electricity.md)** (Uses 5 entities)
* **[Home](../dashboards/main/home.md)** (Uses 2 entities)
<!-- END_DASHBOARD -->
