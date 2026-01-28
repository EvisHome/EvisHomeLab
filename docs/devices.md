---
title: Device Inventory
description: Centralized catalog of smart home devices / CMDB.
render_macros: true
---

# Device Inventory

<div class="grid cards" markdown>

<!-- Debug: {{ devices }} -->


<!-- This section will be populated by the devices.yaml data -->

{% for device in devices %}
-   **{{ device.name }}**
    
    ---
    
    <span class="twemoji">:material-map-marker:</span> {{ device.area }}  
    <span class="twemoji">:material-connection:</span> {{ device.integration }}  
    {% if device.model %}
    <span class="twemoji">:material-tag-text:</span> {{ device.brand }} {{ device.model }}
    {% endif %}

    {% if device.components %}
    **Components:** {{ device.components | join(', ') }}
    {% endif %}

    {% if device.package %}
    [View Package](../packages/{{ device.package }}){ .md-button .md-button--primary }
    {% endif %}

    {% if device.manual %}
    [User Manual]({{ device.manual }})
    {% endif %}

    {% for tag in device.tags %}
    <span class="md-tag">{{ tag }}</span>
    {% endfor %}

{% endfor %}

</div>
