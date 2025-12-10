<!-- VALIDATION_CHECKLIST: ["## PART A", "## PART B", "Visual Assets Standard", "Task: Standardize Package Headers"] -->
# Setup Guide

**Version:** 8.1 (Modularized)

**Philosophy:** Agentic CMDB (Configuration Management Database)

**Strategy:** "Detached Docs" (Private Config -> Public Documentation)

## 1. Executive Summary
This project automates the documentation of a Home Assistant Smart Home and Home Lab. Instead of writing documentation manually, we use an **AI Agent (Google Antigravity)** to scan the live configuration files and generate a static website (**MkDocs**).

For daily operations, workflows, and tool references, please see:
[**📄 Documentation Operations Manual**](tools.md)

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
* Ensure `.ag_scripts/` exists (Git Pull).
* Run `python ag_v2_update.py` to verify the system works.

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
*End of Setup Guide. Proceed to [Documentation Operations](tools.md).*
