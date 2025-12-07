<!-- VALIDATION_CHECKLIST: ["## PART A", "## PART B", "## PART C", "## PART D", "## PART E", "## PART F", "Visual Assets Standard", "Task: Standardize Package Headers"] -->
# EvisHomeLab: Documentation System Manual

**Version:** 8.1 (Modularized)
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
## PART C: Core Concepts & Standards

### 1. Visual Assets Standard
Images must be sorted into subfolders to keep the repo clean.
* **Dashboards:** `docs/assets/images/dashboards/view_[path].png`
* **Packages:** `docs/assets/images/packages/[name].png`
* **Brand:** `docs/assets/images/brand/`

### 2. Locking Files (Prevent Overwrite)
To protect a manually written page from the Agent:
* Add `auto_update: false` to the YAML frontmatter at the top of the Markdown file.

### 3. Tagging Strategy
Use YAML frontmatter to categorize pages for the Tag Cloud.
* **Standard Tags:** `package`, `dashboard`, `network`, `automated`, `manual`.

---

## PART D: Daily Operations (The Workflow)

### 1. The Full Maintenance Cycle (Recommended)
Run these commands in order to keep everything synced.

1.  **Commit Config (Local Repo A):**
    * `git add .; git commit -m "WIP: Config updates"`
2.  **Update Tools:**
    * `python ag_update_docs.py` (Refreshes manual/scripts).
3.  **Regenerate Docs:**
    * Dashboards: `python ag_regenerate_dashboards.py`
    * Packages: `python ag_update_package.py --all`
4.  **Publish Docs (Public Repo B):**
    * `cd docs_site; git add .; git commit -m "Routine update"; git push`

### 2. The AI Architect Workflow
**Start new chats with:** "I am resuming EvisHomeLab. Read `docs_site/AI_CONTEXT.md` and `docs_site/docs/system_manual/setup_guide.md`. Adopt the persona."

### 3. The Agent Prompts

```markdown
> **Task: Standardize Package Headers (Source Code Management)**
> 
> Scan `packages/`. Check headers. If missing/legacy, prepend:
> 
> ```yaml
> # ------------------------------------------------------------------------------
> # Package: [Filename]
> # Version: 1.0.0
> # Description: [Summary]
> # Dependencies: [Entities used]
> # ------------------------------------------------------------------------------
> ```
```

**Task: Deep Package Analysis (Mermaid & Summary)**
*Use this prompt to add diagrams and intelligence to an existing package document.*
> "Update the documentation for the **[PACKAGE_NAME]** package.
>
> 1. Read `packages/[PACKAGE_NAME].yaml` and `docs_site/docs/smart-home/packages/[PACKAGE_NAME].md`.
> 2. **Guard Check:** If the Markdown contains `auto_update: false`, **ABORT**.
> 3. **Smart Analysis:**
>    - **Summary:** Provide a detailed executive summary of the package's functionality.
>    - **Architecture:** Generate a `mermaid` sequence diagram illustrating the primary logic flow (e.g., `Trigger -> Condition -> Action`).
> 4. **Update Documentation File:**
>    - **Do NOT** overwrite the entire file.
>    - **Find & Replace:** Insert the generated Summary and Diagram into the relevant sections/placeholders in the existing Markdown content."

**Task: Update Package Documentation (Boilerplate & Version Stamp)**
*Use this prompt to quickly update versioning, tags, and code block content.*
> "Run `python ag_update_package.py [package_name]`."
> *(Fallback: "Update `[package].md` reading from `[package].yaml`. Check `auto_update` lock.")*


**Task: Update Architecture (Structure & Overview)**
> "Update `docs_site/docs/smart-home/structure.md` AND `docs_site/docs/index.md`.
>
> 1. **Structure:** Re-scan root. Update file tree.
> 2. **Overview:** Update 'High Level Architecture' with new integrations."

**Task: Web Design & Image Management**
> "Scan `assets/images/`. Update Markdown files to replace placeholder text with actual image links. If asking for CSS changes, edit `assets/css/custom.css`."

**Task: Generate All Package Documentation**
> "Deep scan `packages/`. Create Markdown for all files with: Frontmatter tags, Summary, Architecture Diagram, Redacted Code, Dashboard connections, and Visuals."

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
