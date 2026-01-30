import os
import re

# Base path to dashboards
DASHBOARDS_DIR = r"z:\docs_site\docs\smart-home\dashboards"
OUTPUT_FILE = os.path.join(DASHBOARDS_DIR, "index.md")

# Default Header for dashboards without an explicit group
DEFAULT_GROUP = "Other Dashboards"

def get_frontmatter_value(content, key):
    """Simple parser to extract a value from frontmatter."""
    match = re.search(fr"^{key}:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"').strip("'")
    return None

def get_markdown_field(content, key):
    """
    Extracts a value defined in the markdown body pattern like:
    **Dashboard:** Value
    """
    # Case insensitive search for **Key:** Value
    match = re.search(fr"\*\*{key}:\*\*\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def get_description(content):
    """Extracts description between <!-- START_DESCRIPTION --> tags."""
    match = re.search(r"<!-- START_DESCRIPTION -->(.*?)<!-- END_DESCRIPTION -->", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def generate_catalog():
    # Dictionary to hold groups: { "Group Name": [dashboard_dict, ...] }
    grouped_dashboards = {}

    for root, dirs, files in os.walk(DASHBOARDS_DIR):
        # Skip the root directory if needed, though we scan everything recursively
        
        for file in files:
            if file == "index.md" or not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            title = get_frontmatter_value(content, "title") or file.replace(".md", "").title()
            description = get_description(content)
            
            # Extract Dashboard Group from Markdown Body
            # Default to "Other" if not found
            dashboard_group = get_markdown_field(content, "Dashboard")
            if not dashboard_group:
                dashboard_group = DEFAULT_GROUP
            
            # Relative path for the link
            rel_path = os.path.relpath(filepath, DASHBOARDS_DIR).replace("\\", "/")
            
            entry = {
                "title": title,
                "path": rel_path,
                "description": description
            }
            
            # Add to group
            if dashboard_group not in grouped_dashboards:
                grouped_dashboards[dashboard_group] = []
            grouped_dashboards[dashboard_group].append(entry)

    # Generate Markdown Content
    md_content = """---
tags:
  - dashboard
  - index
  - automated
---

# Dashboard Catalog

Browse all available Home Assistant dashboards.

!!! info "Auto-Generated"
    This catalog is automatically maintained by the Documentation Agent.
"""

    # Sort groups alphabetically, but put "Other Dashboards" last if it exists
    sorted_groups = sorted(grouped_dashboards.keys())
    if DEFAULT_GROUP in sorted_groups:
        sorted_groups.remove(DEFAULT_GROUP)
        sorted_groups.append(DEFAULT_GROUP)

    for group_name in sorted_groups:
        dashboards = grouped_dashboards[group_name]
        
        # H2 Header for the Group
        md_content += f"\n## {group_name}\n\n"
        
        # Table Header
        md_content += "| View | Description |\n"
        md_content += "| :--- | :--- |\n"
        
        # Sort views within the group by title
        dashboards.sort(key=lambda x: x['title'])
        
        for d in dashboards:
            md_content += f"| **[{d['title']}](./{d['path']})** | {d['description']} |\n"

    # Write to index.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    total_dashboards = sum(len(v) for v in grouped_dashboards.values())
    print(f"Successfully generated catalog with {total_dashboards} dashboards across {len(grouped_dashboards)} groups.")

if __name__ == "__main__":
    generate_catalog()
