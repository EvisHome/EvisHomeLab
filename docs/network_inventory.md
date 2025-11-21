📦 Home Lab Inventory

📊 Device Overview

Name

Type

Model

IP Address

Location

Status

{% for device in devices %}











{{ device.name }}

{{ device.type }}

{{ device.model }}

{{ device.ip if device.ip is defined else 'DHCP' }}

{{ device.location }}

{% if device.status == "Active" %}🟢{% elif device.status == "Planned" %}🟡{% else %}🔴{% endif %} {{ device.status }}

{% endfor %}











📍 By Location

🏢 Office Rack

{% for device in devices %}
{% if device.location == "Office Rack" %}

{{ device.name }} ({{ device.model }})
{% endif %}
{% endfor %}

🪜 Staircase & Upstairs

{% for device in devices %}
{% if "Staircase" in device.location or "Guest" in device.location %}

{{ device.name }} ({{ device.model }})
{% endif %}
{% endfor %}

🌳 Outdoor & Porch

{% for device in devices %}
{% if "Porch" in device.location or "Backyard" in device.location or "Front Door" in device.location %}

{{ device.name }} ({{ device.model }})
{% endif %}
{% endfor %}

🛋️ Living Room

{% for device in devices %}
{% if "Living Room" in device.location %}

{{ device.name }} ({{ device.model }})
{% endif %}
{% endfor %}
