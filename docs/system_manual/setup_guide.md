<!-- VALIDATION_CHECKLIST: [
    "## PART A: One-Time Initialization",
    "## PART B: Workstation Setup",
    "## PART C: Daily Operations",
    "The AI Architect Workflow",
    "Visual Assets Standard",
    "Task: Web Design & Image Management",
    "Task: Update Single Package",
    "Task: Generate All Package Documentation",
    "ag_regenerate_dashboards.py",
    "## PART E: Tool Reference",
    "## PART F: Troubleshooting"
] -->
# EvisHomeLab: Documentation System Manual

**Version:** 5.1
**Philosophy:** Agentic CMDB (Configuration Management Database)
**Strategy:** "Detached Docs" (Private Config -> Public Documentation)

## 1. Executive Summary

This project automates the documentation of a Home Assistant Smart Home and Home Lab. Instead of writing documentation manually, we use an **AI Agent (Google Antigravity)** to scan the live configuration files and generate a static website (**MkDocs**).

### Key Architecture

* **Repo A (Local):** The root `/config` folder. Versioned locally for safety/undo. Never pushed.
* **Repo B (Public):** The `/config/docs_site` folder. Pushed to GitHub Pages for documentation.

---

## PART A: One-Time Initialization (The Genesis)

**⚠️ STOP:** Only perform these steps if you are setting up the system **for the very first time** on a fresh Home Assistant server. If the system already exists and you just want to connect a new laptop, skip to **PART B**.

### 1. Initialize Local Safety (Root)

**Pre-requisite:** If you see a "potentially unsafe" or "dubious ownership" error, run this in the terminal first:
`git config --global --add safe.directory '*'`

Open Antigravity connected to `/config` and run this prompt in the Agent:

> "Initialize a git repository in this folder.
>
> 1. Create a `.gitignore` file with these EXACT rules to prevent bloat and security leaks:
>
>    ```
>    docs_site/
>    .ag_backups/
>    secrets.yaml
>    .jwt_secret
>    *.log*
>    *.db*
>    .vacuum
>    .timeline
>    .ha_run.lock
>    .HA_VERSION
>    .shopping_list.json
>    backups/
>    .storage/
>    .cloud/
>    .exports
>    .vscode/
>    deps/
>    model_cache/
>    tts/
>    custom_components/
>    node-red/
>    zigbee2mqtt/
>    zigbee2mqtt-2/
>    home-assistant-wakewords-collection-main/
>    __pycache__/
>    *.pyc
>    www/snapshots/
>    www/**/*.tmp
>    www/community/       <-- HACS Frontend cards (External dependency)
>    image/
>    # ESPHome - Keep YAML, ignore builds
>    esphome/.esphome/
>    esphome/trash/
>    esphome/*.bin
>    ```
>
> 2. Add all other files.
>
> 3. Commit the current state with the message 'Initial Home Assistant Backup'."

### 2. Establish Agent Rules

Create a file at `.antigravity/rules.md` in the root:

```text
CRITICAL RULES:
1. NEVER edit files inside the `.storage/` directory. Treat them as READ-ONLY sources of truth.
2. When asked to "Document Dashboards", read the JSON files in `.storage/lovelace*`, parse the configuration, and write the description to `docs/dashboards.md`.
3. Always ask for confirmation before deleting files outside of the `docs/` directory.
4. **Context & Persona:** Always consult `docs_site/AI_CONTEXT.md` for documentation standards, visual styles, and privacy rules before writing documentation.
```

### 3. Bootstrap Helper Tools

We rely on Python scripts to manage complex tasks.

**A. `ag_update_docs.py` (The Architect's Tool)**
* **Purpose:** The Source of Truth. Updates this manual, the AI Context, and scripts.
* **Safety:** Automatically creates timestamped backups (`.bak`) before overwriting files.
* **Usage:** Run `python ag_update_docs.py` whenever you update the system design.

**B. `ag_regenerate_dashboards.py` (The Formatter)**
* **Purpose:** Converts JSON dashboards to YAML and links screenshots.
* **Usage:** Run `python ag_regenerate_dashboards.py` to refresh dashboard docs.

### 4. Scaffold Documentation Site

Paste this prompt into the Agent:

> "I am setting up a fresh CMDB-style documentation site.
>
> 1. Create a new directory named `docs_site/` in the root.
>
> 2. Inside `docs_site/`, scaffold a MkDocs project with:
>    * `mkdocs.yml` (Theme: material, Features: navigation.indexes, navigation.instant)
>    * **Extensions (Crucial):** Enable `admonition`, `pymdownx.details`, `pymdownx.superfences` (for Mermaid).
>    * `docs/index.md` (CMDB Dashboard)
>    * `docs/smart-home/index.md`
>    * `docs/smart-home/packages/`
>    * `docs/assets/images/dashboards/`
>    * `docs/assets/images/packages/`
>    * `docs/assets/images/brand/`
>
> 3. Create a file `docs_site/docs/CNAME` containing: `www.evishome.com`"

### 5. Initialize AI Context

Run `python ag_update_docs.py` to generate the `AI_CONTEXT.md` file.

### 6. Link Docs to GitHub

Run these commands in the terminal:

```bash
cd docs_site
git init
git add .
git commit -m "Initial Docs Setup"
git remote add origin [https://github.com/EvisHome/EvisHomeLab.git](https://github.com/EvisHome/EvisHomeLab.git)
git branch -M main
git push -u origin main
```

---

## PART B: Workstation Setup (Adding Laptops)

**✅ START HERE:** If the system is already running and you want to work on it from a new computer (Laptop 2, 3, etc.).

### 1. Install Tools

1. **Git:** Install [Git for Windows/Mac](https://git-scm.com/downloads).
2. **Antigravity:** Install the IDE.
3. **Python (Optional but Recommended):** Install Python and check "Add to PATH". This allows the Agent to run scripts for complex formatting tasks.

### 2. Connect to Home Assistant

**Option A: Samba (Network Drive)**
1. Mount `\\homeassistant.local\config` (User/Pass required).
2. In Antigravity: **File > Open Folder** > Select the Drive.

**Option B: SSH (Remote Extension)**
1. Install "Open Remote - SSH" extension in Antigravity.
2. Connect to `root@homeassistant.local`.
3. **Drill Down:** File > Open Folder > Type `/homeassistant`.

### 3. Configure Workspace Settings (Crucial)

These settings are stored on your laptop, not the server, so you must set them again.

**A. Unhide Database Files:**
* Settings (`Ctrl+,`) > Search `files.exclude` > **Remove** `**/.*`.

**B. Fix Git Permissions (Samba Only):**
* Open Terminal (`Ctrl+``) and run:
  ```powershell
  git config --global --add safe.directory '*'
  # This trusts the network drive so Git can read the status.
  ```

### 4. Verify Access

* Open the **Source Control** tab.
* You should see the history of changes. **Do NOT run `git init`**.

---

## PART C: Daily Operations (The Workflow)

### 1. The Full Maintenance Cycle (Recommended Routine)
Run this sequence to update everything cleanly.

1.  **Update Tools:** `python ag_update_docs.py` (Ensures you have the latest manual and scripts).
2.  **Regenerate Dashboards:** `python ag_regenerate_dashboards.py` (Scans HA, redacts names, writes Markdown).
3.  **Publish:**
    ```bash
    cd docs_site; git add .; git commit -m "Routine update"; git push
    ```

### 2. The AI Architect Workflow (Resume Work)
**When starting a new Chat Session with an AI Model:**
Paste this prompt to "hydrate" the AI with the project context:

> "I am resuming work on the **EvisHomeLab** project.
>
> **Task:**
> 1. Read the attached **`docs_site/AI_CONTEXT.md`** to load your Persona, Architecture constraints, and Safety Rules.
> 2. Read the attached **`docs_site/docs/system_manual/setup_guide.md`** to understand the operational workflows.
>
> **Action:** Confirm you have loaded the context and are ready to assist with maintaining the CMDB."

### 3. Visual Assets Standard
When adding images, you **must** use the correct naming convention so the automation scripts can find them.

| Type | Folder Location | Naming Convention |
| :--- | :--- | :--- |
| **Dashboards** | `docs/assets/images/dashboards/` | `view_[path].png` (e.g. `view_kitchen.png`) |
| **Packages** | `docs/assets/images/packages/` | `[package_name].png` (e.g. `heating.png`) |
| **General** | `docs/assets/images/brand/` | Free choice |

### 4. The Agent Prompts (Execution)

**Task: Update Single Package (Focus Mode)**
> "Update the documentation for the **[PACKAGE_NAME]** package.
> 1. Read `packages/[PACKAGE_NAME].yaml`.
> 2. Find/Create `docs_site/docs/smart-home/packages/[PACKAGE_NAME].md`.
> 3. **Check Metadata:** Read the top of the Markdown file. If it contains `auto_update: false`, **ABORT**.
> 4. **Update Content:** Logic Summary & Mermaid Diagram.
> 5. **Dashboard Links:** Scan `.storage/lovelace_dashboards` for cards using these entities and embed them.
> 6. **Visuals:** Look in `assets/images/packages/` for an image named `[PACKAGE_NAME].png`.
> 7. **Tags:** Ensure frontmatter includes `tags: [package, automated]`."

**Task: Web Design & Image Management**
> "I have added new images to `docs_site/docs/assets/images/` and I want to update the styling.
> **Task 1 (Images):** Scan the `images` folder. Update the Markdown files to replace placeholder text with the actual image links.
> **Task 2 (CSS):** Check `docs_site/docs/assets/css/custom.css`. Ensure it is linked in `mkdocs.yml`. If I ask for color changes, apply them to the CSS variables."

**Task: Generate All Package Documentation (Full Scan)**
> "Perform a deep architectural scan of my `packages/` directory.
> **For EVERY YAML file found, create a corresponding Markdown file in `docs_site/docs/smart-home/packages/` containing:**
> 1. **Frontmatter:** Add tags `['package', 'automated']`.
> 2. **Executive Summary:** What does this package do?
> 3. **Architecture Diagram:** Generate a `mermaid` sequence diagram of the logic.
> 4. **The Code:** Embed the YAML content in a code block (Redact secrets!).
> 5. **Dashboard Connections:** Scan `.storage/lovelace_dashboards`. Identify cards that control entities from this package and embed their configuration.
> 6. **Visuals:** Insert a placeholder link for a screenshot (e.g., `![View](assets/images/heating.png)`).
> Finally, update `mkdocs.yml` navigation."

**Task: Update Structure Documentation**
> "Update `docs_site/docs/smart-home/structure.md`.
> 1. Re-scan the root directory and update the file tree structure description (Folders first, then files).
> 2. Read `configuration.yaml` and update the commented code block explanation."

**Task: Enable Tags & Tag Cloud**
> "Edit `docs_site/mkdocs.yml`.
> 1. Under `plugins:`, add `- tags`.
> 2. Commit changes: 'Enable MkDocs Tags plugin'."

**Task: Convert Dashboard to YAML**
> "Run `python ag_regenerate_dashboards.py`."

### 5. System Integrity Check (Audit)
**Use when:** You want to verify the system is healthy.

1.  **Run Tool Update:** `python ag_update_docs.py` (Should pass without errors).
2.  **Check Backups:** Look in `.ag_backups/` to ensure old versions are rotating (max 5).
3.  **Check Git Status:**
    * `git status` (Root): Should show no changes if you haven't edited config.
    * `cd docs_site; git status`: Should show no changes if you haven't edited docs.
4.  **Verify Web:** Check `https://www.evishome.com` for 404s.

---

## PART E: Tool Reference & Backup Strategy

### 1. `ag_update_docs.py` (The Master Installer)
* **What it is:** A Python script containing the entire System Manual and AI Context as text strings.
* **When to run:** Every time you start a work session, or after you have modified the manual in the Chat.
* **Backup Function:** It creates a hidden folder **`.ag_backups/`** in the root.
    * Before overwriting any file (e.g., `setup_guide.md`), it saves a timestamped copy (e.g., `setup_guide.md.17099.bak`).
    * **Rotation:** It keeps only the last 5 backups per file to save space.
* **Restoration:** To restore a file, go to `.ag_backups/`, find the timestamp you want, move it to the real location, and rename it (remove `.bak`).

### 2. `ag_regenerate_dashboards.py` (The Privacy Engine)
* **What it is:** A specialized script that parses Home Assistant's hidden JSON dashboard database.
* **Function:**
    * Reads `.storage/lovelace_dashboards`.
    * Performs **Case-Insensitive Redaction** of family names (e.g., Jukka -> Evis).
    * Converts the JSON into **Clean, Block-Style YAML** for readability.
    * Generates `dashboards.md` with screenshot placeholders pre-linked.

---

## PART F: Troubleshooting

### 1. `mkdocs.yml` is Red
* **Status:** False Positive. Ignore it.

### 2. "Unsafe Repository" Error
* **Run:** `git config --global --add safe.directory '*'` in the terminal.

### 3. Website shows 404
* **Check:** GitHub Repo > Settings > Pages.
* **Branch:** Must be `gh-pages`.
* **Folder:** Must be `/` (Root).
