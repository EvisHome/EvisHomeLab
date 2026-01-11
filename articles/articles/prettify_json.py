import json
import re

file_path = r"z:\docs_site\docs\home-lab\articles\virtual-fireplace.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to capture the JSON block
# Matches ```json followed by content and ending with ```
pattern = r"(```json\s*)(.*?)(\s*```)"

def replace_json(match):
    start_tag = match.group(1)
    json_str = match.group(2)
    end_tag = match.group(3)
    
    try:
        data = json.loads(json_str)
        pretty_json = json.dumps(data, indent=2)
        return f"{start_tag}\n{pretty_json}\n{end_tag}"
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return match.group(0)

new_content = re.sub(pattern, replace_json, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("JSON prettified successfully.")
