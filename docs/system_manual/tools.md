---
tags:
  - manual
  - operations
  - reference
---

# Documentation Operations

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
cd /;git add .; git commit -m "WIP: Config updates
```
2.  **Update Code (Git Pull):**
```
git pull
```
3.  **Regenerate Docs (The V2 Shim):**
```
cd /; python ag_v2_update.py
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
> "Scan `packages/`. Check headers. If missing/legacy, prepend:
>
> ```yaml
> # ------------------------------------------------------------------------------
> # Package: [Filename]
> # Version: 1.0.0
> # Description: [Summary]
> # Dependencies: [Entities used]
> # ------------------------------------------------------------------------------
> ```
>"

**Task: Update Package Boilerplate (Automation)**
*Use this prompt first to ensure the documentation structure is correct and versioned.*
> "Run `cd /; python ag_v2_package.py [package_name]`."

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
>    - **Architecture:** Generate a `mermaid` sequence diagram. **CRITICAL:** Write a specific narrative paragraph explaining the logic flow shown in the diagram.
> 4. **Update Documentation File:**
>    - **Target:** Locate the specific HTML comment markers (slots).
>    - **Action:** Replace the content *between* the markers.
>      - `<!-- START_SUMMARY -->` ... `<!-- END_SUMMARY -->`
>      - `<!-- START_DETAILED -->` ... `<!-- END_DETAILED -->`
>      - `<!-- START_MERMAID_DESC -->` ... `<!-- END_MERMAID_DESC -->`
>      - `<!-- START_MERMAID -->` ... `<!-- END_MERMAID -->`
>    - **Dashboard Links:** Scan `.storage/lovelace_dashboards` and embed cards into `<!-- START_DASHBOARD -->`."

**Task: Analyze Dashboard View (Intelligence Injection)**
*Use this to populate the empty summaries in your generated dashboard docs.*

> "Analyze the dashboard view: **[VIEW_PATH]** (e.g. `dashboards/main/car.md`).
> 1. **Read** the Markdown file to see the embedded YAML configuration.
> 2. **Analyze:** Understand what devices and controls are present (e.g., 'Thermostat control', 'Camera feed').
> 3. **Write Summary:** Create a 1-4 sentence non-technical summary of what this view allows the user to do.
> 4. **Inject:** Replace the content between `<!-- START_SUMMARY -->` and `<!-- END_SUMMARY -->` with your text."

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

### `ag_v2_update.py`
The Master Orchestrator. Calls the other tools to update packages and dashboards in one go.

### `ag_v2_dashboard.py`
The Privacy Engine. Reads `.storage/lovelace_dashboards`, performs regex-based name redaction (Jukka->Evis), and outputs clean YAML blocks. Logic lives in `.ag_scripts/dashboard_manager`.

### `ag_v2_package.py`
The Package Doc Generator. Reads a specific package YAML, extracts header metadata (Version/Desc), and updates the specific Markdown file. Logic lives in `.ag_scripts/package_manager`.

---

## 4. Troubleshooting
* **Red Squiggles in `mkdocs.yml`:** False positive, ignore.
* **Unsafe Repo Error:** Run `git config --global --add safe.directory '*'`.
* **404 Error:** Check GitHub Pages settings -> Branch must be `gh-pages`, Folder `/`.
