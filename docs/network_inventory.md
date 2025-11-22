# 📦 Home Lab Inventory ## 📊 Device Overview {% for device in devices %} {% endfor %}
Name	Type	Model	IP Address	Location	Status
{{ device.name }}	{{ device.type }}	{{ device.model }}	{{ device.get('ip', 'DHCP') }}	{{ device.location }}	{% if device.status == "Active" %} ● Active {% elif device.status == "Planned" %} ● Planned {% else %} ● Offline {% endif %}
## 📍 By Location ### 🏢 Office Rack
{% for device in devices %} {% if device.location == "Office Rack" %}
{{ device.name }} ({{ device.model }})
{% endif %} {% endfor %}
### 🪜 Staircase & Upstairs
{% for device in devices %} {% if "Staircase" in device.location or "Guest" in device.location %}
{{ device.name }} ({{ device.model }})
{% endif %} {% endfor %}
### 🌳 Outdoor & Porch
{% for device in devices %} {% if "Porch" in device.location or "Backyard" in device.location or "Front Door" in device.location %}
{{ device.name }} ({{ device.model }})
{% endif %} {% endfor %}
### 🛋️ Living Room
{% for device in devices %} {% if "Living Room" in device.location %}
{{ device.name }} ({{ device.model }})
{% endif %} {% endfor %}
```
