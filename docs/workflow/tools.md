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
**Start new chats with:** "I am resuming EvisHomeLab. Read:

* `docs_site/docs/system_manual/architecture.md`
* `docs_site/docs/system_manual/tools.md`
* `docs_site/AI_CONTEXT.md`. Adopt the persona."
* `analyze all ag_* related folders` to understand the system structure.
* `analyze all ag_*.py files` to understand the system tools and logic.
* `analyze /docs_site` to understand the website structure and content.

### The Agent Prompts

**Task: Standardize Package Headers (Source Code Management)**
> "Scan `packages/`. Check headers. If missing/legacy, prepend this EXACT structure:
>
> ```yaml
> # ------------------------------------------------------------------------------
> # Package: [Filename]
> # Version: [1.0.0]
> # Description: [Summary]
> # Dependencies:
> #   - [Integration]: [Entity]
> # ------------------------------------------------------------------------------
> # IMPORTANT: Please add changes to the Changelog at the bottom of this file.
> # ------------------------------------------------------------------------------
> # <ai_instructions>
> # WHEN YOU EDIT THIS FILE:
> # 1. You MUST update the 'version' in the header.
> # 2. You MUST append a new entry to the 'Changelog' section at the bottom.
> # </ai_instructions>
> # ------------------------------------------------------------------------------
> ```
>
> **Also ensure the Changelog section exists at the bottom:**
> ```yaml
> # ------------------------------------------------------------------------------
> # 3. Changelog
> # ------------------------------------------------------------------------------
> # [Version] ([Date]):
> #   - [Change 1]
> #   - [Change 2]
> # ------------------------------------------------------------------------------
> ```
>"

**Task: Update Package Boilerplate (Automation)**
*Use this prompt first to ensure the documentation structure is correct and versioned.*
> "Run `python .ag_scripts/package_manager/main.py [package_name]`."

**Task: Deep Package Analysis (Intelligence Injection)**
*Use this prompt AFTER running the Python script to fill the intelligent content slots.*
> "I am working on the package: **[PACKAGE_NAME]**.
>
> **Task:**

> 1. **Locate Files:** Find the source YAML in `packages/` and the documentation Markdown in `docs_site/docs/smart-home/packages/` matching this name.
> 2. **Guard Check:** If the Markdown contains `auto_update: false`, **ABORT**.
> 3. **Smart Analysis:**
>    - **Executive Summary:** Technical overview for admins.
>    - **Process Description:** Non-technical explanation for users (How it works).
>    - **Integration Dependencies:** List *only* external integrations (e.g., UniFi, MQTT, Yale). **Exclude** standard Home Assistant components (Scripts, Input Helpers, Logbook).
>    - **Architecture:** Generate a `mermaid` sequence diagram. **CRITICAL:** Write a specific narrative paragraph explaining the logic flow shown in the diagram.
> 4. **Update Documentation File:**
>    - **Target:** Locate the specific HTML comment markers (slots).
>    - **Action:** Replace the content *between* the markers.
>      - `<!-- START_SUMMARY -->` ... `<!-- END_SUMMARY -->`
>      - `<!-- START_DETAILED -->` ... `<!-- END_DETAILED -->`
>      - `<!-- START_DEPENDENCIES -->` ... `<!-- END_DEPENDENCIES -->`
>      - `<!-- START_MERMAID_DESC -->` ... `<!-- END_MERMAID_DESC -->`
>      - `<!-- START_MERMAID -->` ... `<!-- END_MERMAID -->`
>    - **Dashboard Links:** Scan `.storage/lovelace_dashboards` and embed cards into `<!-- START_DASHBOARD -->`."

**Task: Analyze Dashboard View (Intelligence Injection)**
*Use this to populate the empty summaries in your generated dashboard docs.*

> "Analyze the dashboard view: **[VIEW_PATH]** (e.g. `dashboards/main/car.md`).

> 1. **Read** the Markdown file to see the embedded YAML configuration.
> 2. **Analyze:** Understand what devices and controls are present (e.g., 'Thermostat control', 'Camera feed').
> 3. **Write Short Description:** Create a 1-2 sentence *very brief* description for the Index Page (e.g. "Main control interface for living room lights and AC.").
>    - **Inject:** Replace content between `<!-- START_DESCRIPTION -->` and `<!-- END_DESCRIPTION -->`.
> 4. **Write Detailed Summary:** Create a paragraph explaining the view in detail.
>    - **Inject:** Replace content between `<!-- START_SUMMARY -->` and `<!-- END_SUMMARY -->`.

**Task: Update Architecture (Structure & Overview)**
> "Update `docs_site/docs/smart-home/structure.md` AND `docs_site/docs/index.md`.
> 1. **Structure:** Re-scan root. Update file tree.
> 2. **Overview:** Update 'High Level Architecture' with new integrations."

**Task: Web Design & Image Management**
> "Scan `assets/images/`. Update Markdown files to replace placeholder text with actual image links. If asking for CSS changes, edit `assets/css/custom.css`."

**Task: Generate All Package Documentation**
> "Deep scan `packages/`. Create Markdown for all files with: Frontmatter tags, Summary, Architecture Diagram, Redacted Code, Dashboard connections, and Visuals."

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
