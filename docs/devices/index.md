---
title: Device Inventory
description: Centralized catalog of smart home devices / CMDB.
render_macros: true
---

# Device Inventory

<div id="device-inventory">

<!-- Static Filter Bar -->
<div class="inventory-filters">
    <select id="filter-area" onchange="applyFilters()">
        <option value="">All Areas</option>
        {% set areas = [] %}
        {% for device in devices %}
            {% if device.area and device.area not in areas %}
                {% set _ = areas.append(device.area) %}
            {% endif %}
        {% endfor %}
        {% for area in areas | sort %}
        <option value="{{ area }}">{{ area }}</option>
        {% endfor %}
    </select>

    <select id="filter-type" onchange="applyFilters()">
        <option value="">All Types</option>
        {% set types = [] %}
        {% for device in devices %}
            {% set t = device.type | default('Other', true) %}
            {% if t not in types %}
                {% set _ = types.append(t) %}
            {% endif %}
        {% endfor %}
        {% for t in types | sort %}
        <option value="{{ t }}">{{ t }}</option>
        {% endfor %}
    </select>

    <select id="filter-integration" onchange="applyFilters()">
        <option value="">All Integrations</option>
        {% set integrations = [] %}
        {% for device in devices %}
            {% if device.integration and device.integration not in integrations %}
                {% set _ = integrations.append(device.integration) %}
            {% endif %}
        {% endfor %}
        {% for i in integrations | sort %}
        <option value="{{ i }}">{{ i }}</option>
        {% endfor %}
    </select>

    <select id="filter-brand" onchange="applyFilters()">
        <option value="">All Brands</option>
        {% set brands = [] %}
        {% for device in devices %}
            {% set b = device.brand | default('Generic', true) %}
            {% if b not in brands %}
                {% set _ = brands.append(b) %}
            {% endif %}
        {% endfor %}
        {% for b in brands | sort %}
        <option value="{{ b }}">{{ b }}</option>
        {% endfor %}
    </select>
</div>

<div class="device-grid">
{% for device in devices %}
    <div class="device-card"
         data-area="{{ device.area }}"
         data-integration="{{ device.integration }}"
         data-brand="{{ device.brand | default('Generic', true) }}"
         data-type="{{ device.type | default('Other', true) }}">
        
        <div class="device-header">
            <h3 class="device-title">{{ device.name }}</h3>
            {% if device.tags and 'cloud' in device.tags %}
            <span class="device-badge-cloud">Cloud</span>
            {% endif %}
        </div>

        <div class="device-body">
            <!-- Image Logic: Explicit -> Brand-Model (PNG) -> Brand-Model (JPG) -> Hide -->
            {% set fallback_name = (device.brand | default('Generic', true)) ~ '-' ~ (device.model | default('Unknown', true)) %}
            {% set img_path = device.image if device.image else 'images/' ~ fallback_name ~ '.png' %}
            <img src="{{ img_path }}" 
                 alt="{{ device.name }}" 
                 class="device-image"
                 onerror="if (this.src.endsWith('.png')) { this.src = this.src.replace('.png', '.jpg'); } else { this.style.display='none'; }">


            <div class="device-meta">
                <span class="device-meta-label">Area</span>
                <span class="device-meta-value">{{ device.area }}</span>

                <span class="device-meta-label">Integration</span>
                <span class="device-meta-value">{{ device.integration }}</span>

                {% if device.brand %}
                <span class="device-meta-label">Brand</span>
                <span class="device-meta-value">{{ device.brand }}</span>
                {% endif %}

                {% if device.model %}
                <span class="device-meta-label">Model</span>
                <span class="device-meta-value">{{ device.model }}</span>
                {% endif %}
            </div>

            {% if device.tags %}
            <div class="device-tags">
                {% for tag in device.tags %}
                    {% if tag != 'cloud' %}
                    <span class="device-tag">{{ tag }}</span>
                    {% endif %}
                {% endfor %}
            </div>
            {% endif %}

            {% if device.capabilities %}
            <div class="device-data-section">
                <span class="device-section-label">Capabilities</span>
                <div class="device-chips-container">
                    {% for cap in device.capabilities %}
                    <span class="device-chip capability">{{ cap | replace('_', ' ') }}</span>
                    {% endfor %}
                </div>
            </div>
            {% endif %}

            {% if device.sensors %}
            <div class="device-data-section">
                <span class="device-section-label">Sensors</span>
                <div class="device-chips-container">
                    {% for sensor in device.sensors %}
                    <span class="device-chip sensor">{{ sensor | replace('_', ' ') }}</span>
                    {% endfor %}
                </div>
            </div>
            {% endif %}
        </div>

        <div class="device-actions">
            {% if device.package %}
            <a href="../smart-home/packages/{{ device.package | replace('.yaml', '/') }}" class="md-button md-button--primary md-button--small">View Package</a>
            {% elif device.manual %}
            <a href="{{ device.manual }}" class="md-button md-button--small">Manual</a>
            {% endif %}
        </div>
    </div>
{% endfor %}
</div>

</div>

<script>
function applyFilters() {
    const areaFilter = document.getElementById("filter-area").value;
    const typeFilter = document.getElementById("filter-type").value;
    const integrationFilter = document.getElementById("filter-integration").value;
    const brandFilter = document.getElementById("filter-brand").value;

    const cards = document.querySelectorAll(".device-card");
    
    cards.forEach(card => {
        const matchArea = !areaFilter || card.dataset.area === areaFilter;
        const matchType = !typeFilter || card.dataset.type === typeFilter;
        const matchIntegration = !integrationFilter || card.dataset.integration === integrationFilter;
        const matchBrand = !brandFilter || card.dataset.brand === brandFilter;

        card.style.display = (matchArea && matchType && matchIntegration && matchBrand) ? "" : "none";
    });
}
</script>
