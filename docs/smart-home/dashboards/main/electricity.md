---
tags:
  - dashboard
  - view
  - automated
---

# Electricity

**Dashboard:** Main Dashboard  
**Path:** `electricity`

## Related Packages
This view contains entities managed by:

* [Aqara W500](../../packages/aqara_w500.md)
* [Nordpool Prices](../../packages/nordpool_prices.md)


![View Screenshot](../../../assets/images/dashboards/dashboard_main_electricity.png)

## Configuration
```yaml
type: sections
max_columns: 4
title: Electricity
path: electricity
sections:
- type: grid
  cards:
  - type: heading
    heading: Today's Energy Prices Per Hour
    heading_style: subtitle
  - square: false
    columns: 1
    type: grid
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
            height: 280px
            width: 115%
            offsetX: -30
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
            enabled: false
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
              rotate: 0
              offsetX: -25
              offsetY: -90
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
              rotate: 0
              offsetX: 25
              offsetY: -90
              style:
                color: skyblue
                fontSize: 10px
                fontFamily: verdana
        series:
        - entity: sensor.electricity_prices
          name: Price
          yaxis_id: cost
          type: column
          opacity: 0.8
          stroke_width: 0
          show:
            legend_value: false
            extremas: true
            in_header: true
            header_color_threshold: true
          data_generator: "return entity.attributes.data.map(entry => {\n  return\
            \ [new Date(entry.start).getTime(), entry.price];\n});\n"
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
  - type: heading
    heading: Tomorrow's Energy Prices Per 15 minutes
    heading_style: subtitle
  - square: false
    columns: 1
    type: grid
    cards:
    - type: custom:config-template-card
      variables:
        PRICEHIGH: states['sensor.nordpool_today_32nd_highest_price'].state
        PRICELOW: states['sensor.nordpool_today_32nd_lowest_price'].state
      entities:
      - sensor.nordpool_kwh_fi_eur
      card:
        type: custom:apexcharts-card
        graph_span: 1d
        span:
          start: day
        apex_config:
          stroke:
            dashArray: 2
          chart:
            height: 180px
            width: 115%
            offsetX: -30
          title:
            text: Energy Price Today
            align: center
            offsetY: 10
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
          legend:
            show: false
            itemMargin:
              vertical: 10
              horizontal: 10
          tooltip:
            enabled: false
            style:
              fontSize: 14px
        show:
          last_updated: true
        experimental:
          color_threshold: true
        header:
          show_states: true
          colorize_states: true
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
              rotate: 0
              offsetX: -25
              offsetY: -70
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
              rotate: 0
              offsetX: 25
              offsetY: -70
              style:
                color: skyblue
                fontSize: 10px
                fontFamily: verdana
        series:
        - entity: sensor.nordpool_kwh_fi_eur
          name: Price
          yaxis_id: cost
          type: column
          opacity: 0.8
          stroke_width: 0
          show:
            extremas: true
            in_header: raw
            header_color_threshold: true
          data_generator: "return entity.attributes.raw_today.map((start, index) =>\
            \ {\n  return [new Date(start[\"start\"]).getTime(), entity.attributes.raw_today[index][\"\
            value\"]];\n});\n"
          color_threshold:
          - value: -10
            color: lightgreen
          - value: ${PRICELOW*1}
            color: orange
          - value: ${PRICEHIGH * 1}
            color: darkred
        - entity: sensor.home_total_energy_hourly
          name: Energy (kWh)
          color: skyblue
          type: line
          opacity: 1
          yaxis_id: energy
          stroke_width: 2
          float_precision: 1
          extend_to: false
          unit: kWh
          group_by:
            duration: 15min
            func: diff
          show:
            legend_value: false
            datalabels: false
            extremas: true
            in_header: raw
            header_color_threshold: true
  - type: custom:config-template-card
    variables:
      PRICEHIGH: states['sensor.electricity_tomorrow_32nd_highest_price'].state
      PRICELOW: states['sensor.electricity_tomorrow_32nd_lowest_price'].state
    entities:
    - sensor.electricity_prices
    card:
      type: custom:apexcharts-card
      graph_span: 1d
      span:
        start: day
        offset: +1d
      apex_config:
        stroke:
          dashArray: 4
        chart:
          height: 180px
          width: 115%
          offsetX: -30
        title:
          text: Energy Price Tomorrow
          align: center
          offsetY: 10
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
        legend:
          show: false
          itemMargin:
            vertical: 10
            horizontal: 10
        tooltip:
          enabled: false
          style:
            fontSize: 14px
      show:
        last_updated: true
      experimental:
        color_threshold: true
      header:
        show_states: true
        colorize_states: true
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
            rotate: 0
            offsetX: -25
            offsetY: -70
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
            rotate: 0
            offsetX: 25
            offsetY: -70
            style:
              color: skyblue
              fontSize: 10px
              fontFamily: verdana
      series:
      - entity: sensor.electricity_prices
        name: Price
        yaxis_id: cost
        type: column
        opacity: 0.8
        stroke_width: 0
        show:
          extremas: true
          in_header: raw
          header_color_threshold: true
        data_generator: "const tomorrow = new Date();\ntomorrow.setHours(0, 0, 0,\
          \ 0);\ntomorrow.setDate(tomorrow.getDate() + 1);\n\nreturn entity.attributes.data\n\
          \  .filter(entry => new Date(entry.start) >= tomorrow)\n  .map(entry =>\
          \ [new Date(entry.start).getTime(), entry.price]);\n"
        color_threshold:
        - value: -10
          color: lightgreen
        - value: ${PRICELOW * 1}
          color: orange
        - value: ${PRICEHIGH * 1}
          color: darkred
      - entity: sensor.home_total_energy_hourly
        name: Energy (kWh)
        color: skyblue
        type: line
        opacity: 1
        yaxis_id: energy
        stroke_width: 2
        float_precision: 1
        extend_to: false
        unit: kWh
        group_by:
          duration: 1hour
          func: max
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: raw
          header_color_threshold: true
    visibility:
    - condition: state
      entity: sensor.electricity_tomorrow_valid
      state: 'True'
- type: grid
  cards:
  - type: heading
    heading: Energy Usage
    heading_style: subtitle
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
        height: 180px
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
        offsetY: -8
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
        offsetY: 10
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
          offsetX: -25
          offsetY: -70
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
      stroke_width: 1
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
  - square: false
    columns: 1
    type: grid
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
            height: 180px
            width: 115%
            offsetX: -30
          title:
            text: Energy Price Today
            align: center
            offsetY: 10
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
          legend:
            show: false
            itemMargin:
              vertical: 10
              horizontal: 10
          tooltip:
            enabled: true
            style:
              fontSize: 14px
        show:
          last_updated: true
        experimental:
          color_threshold: true
        header:
          show_states: true
          colorize_states: true
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
              rotate: 0
              offsetX: -25
              offsetY: -70
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
              rotate: 0
              offsetX: 25
              offsetY: -70
              style:
                color: skyblue
                fontSize: 10px
                fontFamily: verdana
        series:
        - entity: sensor.electricity_prices
          name: Price
          yaxis_id: cost
          type: column
          opacity: 0.8
          stroke_width: 0
          show:
            extremas: true
            in_header: raw
            header_color_threshold: true
          data_generator: "return entity.attributes.data.map(entry => {\n  return\
            \ [new Date(entry.start).getTime(), entry.price];\n});\n"
          color_threshold:
          - value: -10
            color: lightgreen
          - value: ${PRICELOW * 1}
            color: orange
          - value: ${PRICEHIGH * 1}
            color: darkred
        - entity: sensor.home_total_energy_hourly
          name: Energy (kWh)
          color: skyblue
          type: line
          opacity: 1
          yaxis_id: energy
          stroke_width: 2
          float_precision: 1
          extend_to: false
          unit: kWh
          group_by:
            duration: 1hour
            func: max
          show:
            legend_value: false
            datalabels: false
            extremas: true
            in_header: raw
            header_color_threshold: true
  - type: custom:config-template-card
    variables:
      PRICEHIGH: states['sensor.electricity_tomorrow_32nd_highest_price'].state
      PRICELOW: states['sensor.electricity_tomorrow_32nd_lowest_price'].state
    entities:
    - sensor.electricity_prices
    card:
      type: custom:apexcharts-card
      graph_span: 1d
      span:
        start: day
        offset: +1d
      apex_config:
        stroke:
          dashArray: 4
        chart:
          height: 180px
          width: 115%
          offsetX: -30
        title:
          text: Energy Price Tomorrow
          align: center
          offsetY: 10
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
        legend:
          show: false
          itemMargin:
            vertical: 10
            horizontal: 10
        tooltip:
          shared: false
          enabled: true
          followCursor: false
          style:
            fontSize: 11px
          x:
            show: false
      show:
        last_updated: true
      experimental:
        color_threshold: true
      header:
        show_states: true
        colorize_states: true
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
            rotate: 0
            offsetX: -25
            offsetY: -70
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
            rotate: 0
            offsetX: 25
            offsetY: -70
            style:
              color: skyblue
              fontSize: 10px
              fontFamily: verdana
      series:
      - entity: sensor.electricity_prices
        name: Price
        yaxis_id: cost
        type: column
        opacity: 0.8
        stroke_width: 0
        show:
          extremas: true
          in_header: raw
          header_color_threshold: true
        data_generator: "const tomorrow = new Date();\ntomorrow.setHours(0, 0, 0,\
          \ 0);\ntomorrow.setDate(tomorrow.getDate() + 1);\n\nreturn entity.attributes.data\n\
          \  .filter(entry => new Date(entry.start) >= tomorrow)\n  .map(entry =>\
          \ [new Date(entry.start).getTime(), entry.price]);\n"
        color_threshold:
        - value: -10
          color: lightgreen
        - value: ${PRICELOW * 1}
          color: orange
        - value: ${PRICEHIGH * 1}
          color: darkred
      - entity: sensor.home_total_energy_hourly
        name: Energy (kWh)
        color: skyblue
        type: line
        opacity: 1
        yaxis_id: energy
        stroke_width: 2
        float_precision: 1
        extend_to: false
        unit: kWh
        group_by:
          duration: 1hour
          func: max
        show:
          legend_value: false
          datalabels: false
          extremas: true
          in_header: raw
          header_color_threshold: true
  - type: custom:apexcharts-card
    graph_span: 1d
    span:
      start: day
    header:
      show: false
      show_states: true
      colorize_states: true
    apex_config:
      stroke:
        dashArray: 0
      chart:
        height: 200px
        width: 115%
        offsetX: -30
      title:
        text: Energy Price Today
        align: center
        offsetY: 10
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
          format: HH
        hideOverlappingLabels: true
      tooltip:
        enabled: false
        style:
          fontSize: 14px
    now:
      show: true
    experimental:
      color_threshold: true
    yaxis:
    - id: price
      opposite: true
      decimals: 1
      apex_config:
        tickAmount: 4
        labels:
          show: true
        title:
          text: c/kWh
          rotate: 0
          offsetX: -25
          offsetY: -70
          style:
            fontSize: 10px
            fontFamily: verdana
            color: orange
    - id: energy
      max: ~1
      min: 0
      decimals: 1
      apex_config:
        tickAmount: 4
        labels:
          show: true
        title:
          text: kWh
          rotate: 0
          offsetX: 25
          offsetY: -70
          style:
            color: skyblue
            fontSize: 10px
            fontFamily: verdana
    series:
    - entity: sensor.electricity_prices
      name: Price
      yaxis_id: price
      type: column
      opacity: 0.6
      show:
        extremas: true
        in_header: raw
        header_color_threshold: true
      data_generator: "if (!entity.attributes.data) return [];\nconst today = new\
        \ Date();\ntoday.setHours(0, 0, 0, 0);\nconst tomorrow = new Date(today);\n\
        tomorrow.setDate(today.getDate() + 1);\n\nreturn entity.attributes.data\n\
        \  .filter(entry => {\n    const start = new Date(entry.start);\n    return\
        \ start >= today && start < tomorrow;\n  })\n  .map(entry => [new Date(entry.start).getTime(),\
        \ entry.price]);\n"
      color_threshold:
      - value: -10
        color: lightgreen
      - value: 15
        color: orange
      - value: 20
        color: red
    - entity: sensor.home_total_energy
      name: Energy
      yaxis_id: energy
      type: line
      group_by:
        duration: 15min
        func: diff
      color: skyblue
      opacity: 1
      stroke_width: 2
      show:
        extremas: true
        in_header: raw
        header_color_threshold: true
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
      chart:
        height: 180px
      stroke:
        dashArray: 4
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
  - type: custom:apexcharts-card
    graph_span: 1d
    span:
      start: day
    header:
      show: false
      show_states: true
      colorize_states: true
    apex_config:
      stroke:
        dashArray: 2
      chart:
        height: 200px
        width: 115%
        offsetX: -30
      title:
        text: Energy Price Today
        align: center
        offsetY: 10
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
          format: HH
        hideOverlappingLabels: true
      tooltip:
        enabled: false
        style:
          fontSize: 14px
    now:
      show: true
    experimental:
      color_threshold: true
    yaxis:
    - id: price
      opposite: true
      decimals: 1
      apex_config:
        tickAmount: 4
        labels:
          show: true
        title:
          text: c/kWh
          rotate: 0
          offsetX: -25
          offsetY: -70
          style:
            fontSize: 10px
            fontFamily: verdana
            color: orange
    - id: energy
      max: ~1
      min: 0
      decimals: 1
      apex_config:
        tickAmount: 4
        labels:
          show: true
        title:
          text: kWh
          rotate: 0
          offsetX: 25
          offsetY: -70
          style:
            color: skyblue
            fontSize: 10px
            fontFamily: verdana
    series:
    - entity: sensor.electricity_prices
      name: Price
      yaxis_id: price
      type: line
      opacity: 0.8
      stroke_width: 2
      show:
        extremas: true
        in_header: raw
        header_color_threshold: true
      data_generator: "if (!entity.attributes.data) return [];\nconst today = new\
        \ Date();\ntoday.setHours(0, 0, 0, 0);\nconst tomorrow = new Date(today);\n\
        tomorrow.setDate(today.getDate() + 1);\n\nreturn entity.attributes.data\n\
        \  .filter(entry => {\n    const start = new Date(entry.start);\n    return\
        \ start >= today && start < tomorrow;\n  })\n  .map(entry => [new Date(entry.start).getTime(),\
        \ entry.price]);\n"
      color_threshold:
      - value: 10
        color: lightgreen
      - value: 17
        color: orange
      - value: 25
        color: red
    - entity: sensor.home_total_energy
      name: Energy
      yaxis_id: energy
      type: column
      group_by:
        duration: 15min
        func: diff
      color_threshold:
      - value: 0.25
        color: skyblue
      - value: 1
        color: lightblue
      opacity: 0.5
      stroke_width: 0
      show:
        extremas: true
        in_header: raw
        header_color_threshold: true
  - type: custom:apexcharts-card
    graph_span: 24h
    span:
      start: day
    header:
      title: 15-Minute Energy Cost
      show: true
    apex_config:
      stroke:
        dashArray: 2
      chart:
        height: 200px
      title:
        text: Energy Expenses
        align: center
        offsetY: 10
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
          format: HH
        hideOverlappingLabels: true
      tooltip:
        enabled: false
        style:
          fontSize: 14px
    yaxis:
    - id: cost
      opposite: true
      decimals: 3
      max: 1
      min: 0
      apex_config:
        tickAmount: 4
        labels:
          show: true
        title:
          text: €
          rotate: 0
          offsetX: -30
          offsetY: -90
          style:
            fontSize: 14px
            fontFamily: verdana
            color: orange
    series:
    - entity: sensor.15_minute_energy_cost_block
      name: Cost
      type: column
      group_by:
        duration: 15min
        func: max
      yaxis_id: cost
      show:
        extremas: true
        in_header: raw
- type: grid
  cards:
  - type: heading
    heading_style: subtitle
    heading: Settings
  - type: custom:mushroom-entity-card
    entity: input_number.electricity_high_price_threshold
    grid_options:
      columns: 12
      rows: 1
  - type: markdown
    content: Price Threshold controls devices and appliances that have high impact
      on energy usage. These devices will be turned off or can't be used when the
      Electoricity price is above this treshold.
  - type: entities
    entities:
    - entity: input_number.energy_tax_c_kwh
    - entity: input_number.energy_transfer_fee
    - entity: input_number.energy_vat
    - entity: input_number.energy_transfer_base_fee
    - entity: input_number.energy_monthly_base_fee
  - type: custom:apexcharts-card
    graph_span: 24h
    update_interval: 5min
    header:
      title: Energy & Cost per 15min
      show: true
    apex_config:
      stroke:
        dashArray: 2
      chart:
        height: 200
      tooltip:
        shared: true
      grid:
        show: true
        borderColor: rgba(255,255,255,0.2)
    yaxis:
    - id: energy
      show: true
      opposite: false
      decimals: 2
    - id: cost
      show: true
      opposite: true
      decimals: 2
    series:
    - entity: sensor.shelly_home_energy_15min
      name: Energy
      type: column
      opacity: 0.8
      yaxis_id: energy
      unit: kWh
      group_by:
        duration: 15min
        func: max
      color: '#1E90FF'
    - entity: sensor.energy_cost_15min_c
      name: Cost
      type: line
      stroke_width: 2
      yaxis_id: cost
      unit: c
      group_by:
        duration: 15min
        func: max
      color: '#FF6347'

```
