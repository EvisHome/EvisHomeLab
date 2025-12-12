---
tags:
  - dashboard
  - view
  - automated
---

# Electricity Dev

**Dashboard:** Main Dashboard  
**Path:** `electricity-dev`

<!-- START_DESCRIPTION -->
Development version of the electricity dashboard for testing new charts.
<!-- END_DESCRIPTION -->

![View Screenshot](../../../assets/images/dashboards/dashboard_electricity_dev.png)

## Summary
<!-- START_SUMMARY -->
This is a development view for the main Electricity dashboard, used for testing new chart configurations and layouts (Panel mode). It replicates the core pricing and usage visualizations but may contain experimental features or alternative display styles like vertical stacks.
<!-- END_SUMMARY -->

## Related Packages
This view contains entities managed by:

* [Aqara W500](../../packages/aqara_w500.md)
* [Nordpool Prices](../../packages/nordpool_prices.md)


## Dependencies (Custom Cards)
Required HACS frontend resources:

* `custom:apexcharts-card`
* `custom:config-template-card`


## Configuration
```yaml
type: panel
path: electricity-dev
title: Electricity Dev
cards:
- type: vertical-stack
  cards:
  - type: custom:config-template-card
    variables:
      PRICEHIGH: states['sensor.electricity_today_32nd_highest_price'].state
      PRICELOW: states['sensor.electricity_today_32nd_lowest_price'].state
    entities:
    - sensor.electricity_prices
    card:
      type: custom:apexcharts-card
      graph_span: 1d
      span:
        start: day
      apex_config:
        stroke:
          dashArray: 4
        chart:
          height: 250%
          width: 100%
        title:
          text: Energy Price Today
          align: center
          offsetY: 0
          margin: 30
          style:
            fontSize: 13px
            fontFamily: Verdana
            fontWeight: normal
        grid:
          show: true
          borderColor: rgba(255,255,255,0.2)
        xaxis:
          position: bottom
          labels:
            format: H
            hideOverlappingLabels: true
            offsetX: 0
          axisTicks:
            offsetX: 0
          all_series_config:
            show:
              offset_in_name: true
        legend:
          show: true
          position: bottom
          horizontalAlign: left
          fontSize: 14px
          itemMargin:
            vertical: 10
            horizontal: 10
        tooltip:
          enabled: true
          style:
            fontSize: 14px
      header:
        title: Electricity Today
        standard_format: false
        show: false
        show_states: true
        colorize_states: true
      show:
        last_updated: true
      experimental:
        color_threshold: true
      now:
        show: true
      yaxis:
      - id: cost
        opposite: true
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: c/kWh
            rotate: -90
            style:
              fontSize: 10px
              fontFamily: verdana
              color: orange
      - id: energy
        max: ~2
        min: 0
        decimals: 1
        apex_config:
          tickAmount: 4
          labels:
            show: true
          title:
            text: kWh
            rotate: -90
            style:
              color: skyblue
              fontSize: 10px
              fontFamily: verdana
      series:
      - entity: sensor.electricity_prices
        name: Price (snt/kWh)
        yaxis_id: cost
        type: column
        opacity: 0.8
        stroke_width: 0
        show:
          legend_value: false
          extremas: true
          in_header: true
          header_color_threshold: true
        data_generator: "return entity.attributes.data.map(entry => {\n  return [new\
          \ Date(entry.start).getTime(), entry.price];\n});\n"
        color_threshold:
        - value: -10
          color: lightgreen
        - value: ${PRICELOW * 1}
          color: orange
        - value: ${PRICEHIGH * 1}
          color: darkred
      - entity: sensor.electricity_daily_average_cents
        name: Avg Price
        yaxis_id: cost
        type: line
        color: yellow
        stroke_width: 1
        opacity: 0.8
        group_by:
          func: last
          duration: 24h
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: true
      - entity: sensor.home_total_energy_hourly
        name: Energy (kWh)
        color: skyblue
        type: line
        opacity: 1
        yaxis_id: energy
        stroke_width: 2
        float_precision: 1
        unit: kWh
        group_by:
          duration: 1h
          func: delta
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: raw
          header_color_threshold: true
  - type: horizontal-stack
    cards:
    - type: custom:apexcharts-card
      graph_span: 7d
      update_interval: 15min
      apex_config:
        fill:
          opacity: 0.5
        markers:
          size: 3
        xaxis:
          showDuplicates: true
          position: bottom
          labels:
            format: ddd
            hideOverlappingLabels: false
        chart:
          height: 200vh
        grid:
          show: true
          borderColor: rgba(255,255,255,0.2)
        legend:
          show: true
          itemMargin:
            vertical: 10
            horizontal: 10
        dataLabels:
          enabled: true
          position: top
          offsetY: -9
          background:
            enabled: false
        tooltip:
          style:
            fontSize: 14px
        stroke:
          dashArray: 0
        title:
          text: Energy Daily
          align: center
          offsetY: 8
          style:
            fontSize: 13px
            fontFamily: Verdana
            fontWeight: normal
      header:
        show: false
      yaxis:
      - id: cost
        max: ~100
        min: 0
        decimals: 0
        apex_config:
          tickAmount: 4
          labels:
            show: true
      - id: power
        opposite: true
        max: ~35
        min: 0
        decimals: 0
        apex_config:
          tickAmount: 7
          labels:
            show: true
          title:
            text: kWh
            rotate: 0
            offsetX: 0
            offsetY: 0
            style:
              fontSize: 10px
              fontFamily: verdana
              color: orange
      series:
      - entity: sensor.home_total_energy_daily
        name: Energy (kWh)
        color: skyblue
        type: column
        yaxis_id: power
        stroke_width: 0
        float_precision: 1
        unit: kWh
        statistics:
          type: state
        group_by:
          duration: 1day
          func: max
        show:
          legend_value: false
          datalabels: true
    - type: custom:apexcharts-card
      header:
        title: Shelly 3M - Energy Usage Today
      graph_span: 1d
      span:
        start: day
      update_interval: 5min
      apex_config:
        title:
          text: Energy Usage Today
          align: center
          offsetY: 10
          style:
            fontSize: 13px
            fontFamily: Verdana
            fontWeight: normal
        stroke:
          dashArray: 4
        chart:
          height: 200vh
        grid:
          show: true
          borderColor: rgba(255,255,255,0.2)
        xaxis:
          position: bottom
          labels:
            format: HH
        tooltip:
          enabled: false
          style:
            fontSize: 14px
      yaxis:
      - decimals: 2
        min: 0
      series:
      - entity: sensor.home_total_3em_energy
        name: Energy Usage
        type: column
        group_by:
          duration: 15min
          func: diff
        color: skyblue
        opacity: 0.8
        stroke_width: 0
        show:
          extremas: true
          in_header: raw
          header_color_threshold: true

```
