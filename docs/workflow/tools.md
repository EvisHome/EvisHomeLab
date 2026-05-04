---
tags:
  - manual
  - operations
  - reference
---

# Tools Reference

**Version:** 2.0 (Modularized)
**Philosophy:** Agentic CMDB
**Reference:** [Setup Guide](setup_guide.md) works hand-in-hand with this operations manual.

## 1. Core Concepts & Standards

### Visual Assets Standard
Images must be sorted into subfolders to keep the repo clean.
* **Dashboards:** `docs/assets/images/dashboards/dashboard_[slug]_[view].png`
* **Packages:** `docs/assets/images/packages/[name].png`
* **Brand:** `docs/assets/images/brand/`

### Locking Files (Prevent Overwrite)
To protect a manually written page from the Agent:
* Add `auto_update: false` to the YAML frontmatter at the top of the Markdown file.

### Tagging Strategy
Use YAML frontmatter to categorize pages for the Tag Cloud.
* **Standard Tags:** `package`, `dashboard`, `network`, `automated`, `manual`.

---

## 2. Daily Operations (The Workflow)

### The Full Maintenance Cycle (Recommended)
Run these commands in order to keep everything synced.

1.  **Commit Config (Local Repo A):**
```
cd /; git add .; git commit -m "WIP: Config updates"
```
2.  **Update Code (Git Pull):**
```
git pull
```
3.  **Regenerate Docs (The V2 Shim):**
```
cd /; python .ag_scripts/orchestrator/update_all.py
```
4.  **Publish Docs (Public Repo B):**
```
cd docs_site; git add .; git commit -m "Routine update"; git push
```

### The AI Architect Workflow
**Start new chats with:** 
> "Read `z:\.antigravity\master_init.md` and initialize your context. We are going to work on [Brief Task Description]."

### Dual-Track Logging Workflow
The AI is instructed to maintain strict logs for all completed tasks:
*   **Internal Journal:** `.antigravity/logs/internal_journal.md` (Raw technical data, unredacted, private).
*   **Public Changelog:** `/docs_site/docs/history/changelog.md` (Sanitized summaries, redacted names/secrets, pushed to GitHub).

### Quick Start Scenarios (Manual Script Execution)

#### Scenario 1: I just updated a package
You changed `packages/car.yaml` and want to see the docs update.
```powershell
python ag_v2_package.py car
```
*   **What it does:** Reads `car.yaml`, updates `docs/smart-home/packages/car.md`.

#### Scenario 2: I added a new view to my dashboard
You edited the dashboard in the UI. Now you want the docs to match.
```powershell
python ag_v2_dashboard.py
```
*   **What it does:** Scans your Lovelace config, anonymizes names, and rebuilds the dashboard docs.

#### Scenario 3: I want the AI to analyze my code
You want the AI (in VS Code) to write a summary for you.
```powershell
python ag_v2_agent.py car
```
*   **What it does:** Generates a "Prompt" that you can copy-paste to your AI Assistant to get a perfect analysis.

#### Scenario 4: I want to update EVERYTHING
You are done for the day and want to sync up.
```powershell
python ag_v2_update.py
```
*   **What it does:** Runs all of the above in sequence.

---

## 3. Tool Reference

### `.ag_scripts/orchestrator/update_all.py`
The Master Orchestrator. Coordinates the update of all documentation components (Packages, Dashboards, Structure, Indices).
*   **Command:** `python .ag_scripts/orchestrator/update_all.py [optional_package_name]`

### `.ag_scripts/dashboard_manager/main.py`
The Dashboard Engine. Reads `.storage/lovelace_dashboards`, performs name redaction (Jukka->Evis), and generates dashboard documentation.
*   **Command:** `python .ag_scripts/dashboard_manager/main.py [optional_dashboard_slug]`

### `.ag_scripts/package_manager/main.py`
The Package Engine. Reads specific package YAML files, extracts metadata, and ensures the markdown skeleton exists.
*   **Command:** `python .ag_scripts/package_manager/main.py [package_name]`

### Structure & Index Generators
New tools to keep the site structure automated.
*   **Structure:** `.ag_scripts/structure_manager/generate_structure.py` (Maintains `structure.md`)
*   **Automations:** `.ag_scripts/structure_manager/generate_automations_doc.py` (Maintains `automations.md` for UI logic)
*   **Package Index:** `.ag_scripts/package_manager/generate_index.py` (Maintains `packages/index.md`)

---

## 4. Troubleshooting
* **Red Squiggles in `mkdocs.yml`:** False positive, ignore.
* **Unsafe Repo Error:** Run `git config --global --add safe.directory '*'`.
* **404 Error:** Check GitHub Pages settings -> Branch must be `gh-pages`, Folder `/`.
