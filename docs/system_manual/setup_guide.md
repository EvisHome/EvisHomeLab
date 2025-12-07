<!-- VALIDATION_CHECKLIST: ["## PART A", "## PART B", "## PART C", "Visual Assets Standard", "Task: Standardize Package Headers", "Task: Update Structure Documentation", "Task: Web Design & Image Management"] -->
# EvisHomeLab: Documentation System Manual

**Version:** 7.5 (Modular & Audited)
**Philosophy:** Agentic CMDB (Configuration Management Database)
**Strategy:** "Detached Docs" (Private Config -> Public Documentation)

## 1. Executive Summary
This project automates the documentation of a Home Assistant Smart Home and Home Lab. Instead of writing documentation manually, we use an **AI Agent (Google Antigravity)** to scan the live configuration files and generate a static website (**MkDocs**).

---
## PART A: One-Time Initialization (The Genesis)

**⚠️ STOP:** Only perform these steps if setting up from scratch.

### 1. Initialize Local Safety (Root)
* **Git:** Initialize `/config` with `.gitignore` (secrets, logs, dbs).
* **Permissions:** `git config --global --add safe.directory '*'`
* **First Commit:** "Initial Home Assistant Backup".

### 2. Establish Agent Rules
Create `.antigravity/rules.md`:
* NEVER edit `.storage` manually.
* Consult `AI_CONTEXT.md` before writing.

### 3. Bootstrap Helper Tools
* Run `python ag_update_docs.py` to generate the tooling (`ag_regenerate_dashboards.py`, `ag_update_package.py`) and context files.

### 4. Scaffold Documentation Site
* Use Agent to create `docs_site/` with MkDocs Material theme.
* Ensure `docs/CNAME` exists (`www.evishome.com`).
* Initialize Git in `docs_site/` and push to GitHub (`gh-pages`).

---
## PART B: Workstation Setup (Adding Laptops)

**✅ START HERE:** If the system is already running and you are on a new computer.

### 1. Install Tools
* Git (Windows/Mac)
* Antigravity IDE
* Python (Check "Add to PATH")

### 2. Connect & Configure
* Mount `\\homeassistant.local\config`.
* Open Folder in Antigravity.
* **Unhide Files:** Settings > `files.exclude` > Remove `**/.*`.
* **Trust Git:** Terminal > `git config --global --add safe.directory '*'`.

---
## PART C: Daily Operations (The Workflow)

### 1. The Full Maintenance Cycle
1.  **Update Tools:** `python ag_update_docs.py` (Refreshes manual/scripts from definitions).
2.  **Regenerate Dashboards:** `python ag_regenerate_dashboards.py`.
3.  **Publish Docs:** `cd docs_site; git add .; git commit -m "Routine update"; git push`

### 2. The AI Architect Workflow
**Start new chats with:** "I am resuming EvisHomeLab. Read `docs_site/AI_CONTEXT.md` and `docs_site/docs/system_manual/setup_guide.md`. Adopt the persona."

### 3. Visual Assets Standard
* **Dashboards:** `docs/assets/images/dashboards/view_[path].png`
* **Packages:** `docs/assets/images/packages/[name].png`
* **Brand:** `docs/assets/images/brand/`

### 4. The Agent Prompts

**Task: Standardize Package Headers (Source Code Management)**
> "Scan the `packages/` directory. For every YAML file:
> 1. Check if it has a standard header block.
> 2. If missing, analyze the file to determine its dependencies (entities used) and purpose.
> 3. **Prepend** this header to the file (do not delete code):
>    ```yaml
>    # ------------------------------------------------------------------------------
>    # Package: [Filename]
>    # Version: 1.0.0
>    # Description: [Agent-generated summary]
>    # Dependencies: [List of major entities/integrations detected]
>    # ------------------------------------------------------------------------------
>    ```"

**Task: Update Single Package (Focus Mode)**
> "Run `python ag_update_package.py [package_name]`."
> *(Or use Agent fallback: "Update `[package].md` reading from `[package].yaml` with frontmatter `auto_update: true` check.")*

**Task: Update Structure Documentation**
> "Update `docs_site/docs/smart-home/structure.md`.
> 1. Re-scan the root directory and update the file tree structure description (Folders first, then files).
> 2. Read `configuration.yaml` and update the commented code block explanation."

**Task: Web Design & Image Management**
> "Scan `assets/images/`. Update Markdown files to replace placeholder text with actual image links. If asking for CSS changes, edit `assets/css/custom.css`."

**Task: Generate All Package Documentation**
> "Deep scan `packages/`. Create Markdown for all files with: Frontmatter tags, Summary, Architecture Diagram, Redacted Code, Dashboard connections, and Visuals."

**Task: Enable Tags & Tag Cloud**
> "Edit `docs_site/mkdocs.yml`. Add `- tags` under `plugins:`."

---
## PART E: Tool Reference

### 1. `ag_update_docs.py`
The Master Orchestrator. Imports content from `.ag_definitions/`, validates it, performs backups, and overwrites the documentation files.

### 2. `ag_regenerate_dashboards.py`
The Privacy Engine. Reads `.storage/lovelace_dashboards`, performs regex-based name redaction (Jukka->Evis), and outputs clean YAML blocks.

### 3. `ag_update_package.py`
The Package Doc Generator. Reads a specific package YAML, extracts header metadata (Version/Desc), and updates the specific Markdown file.

---
## PART F: Troubleshooting
* **Red Squiggles in `mkdocs.yml`:** False positive, ignore.
* **Unsafe Repo Error:** Run `git config --global --add safe.directory '*'`.
* **404 Error:** Check GitHub Pages settings -> Branch must be `gh-pages`, Folder `/`.
