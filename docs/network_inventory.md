# 📦 Master Hardware Inventory

| Name | Model | IP Address | Location | Status |
|------|-------|------------|----------|--------|
{% for device in devices %}
| **{{ device.name }}** | {{ device.model }} | `{{ device.ip }}` | {{ device.location }} | {{ device.status }} |
{% endfor %}
