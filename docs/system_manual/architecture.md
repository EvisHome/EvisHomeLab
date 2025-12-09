---
tags:
  - meta
  - architecture
  - manual
---

# Documentation System Architecture

**Philosophy:** "Everything as Code"
**Status:** Self-Validating & Modular

## 1. The Core Concept
Unlike traditional wikis where documentation is written manually and eventually goes stale, **EvisHomeLab** uses an **Agentic CMDB** approach.

The documentation is not just text; it is the output of an **Orchestration Engine**. We treat documentation updates exactly like software deployments: **Source -> Build -> Deploy**.

### The "Russian Doll" Architecture
To prevent data loss and ensure consistency, we separate **Logic** from **Content**.

```mermaid
graph TD
    subgraph Hidden Source [The Source of Truth]
        Def[/.ag_definitions/]
        Man[system_manual.py]
        Ctx[ai_context.py]
        Tools[dashboard_script.py]
    end

    subgraph The Orchestrator [The Builder]
        Upd[ag_update_docs.py]
        Audit{Integrity Audit}
        Backup[/.ag_backups/]
    end

    subgraph The Output [The Living System]
        MD[docs/*.md]
        LiveTools[ag_*.py Scripts]
        Web[GitHub Pages]
    end

    Def --> Upd
    Upd --> Audit
    Audit -- Fail --> Backup
    Audit -- Pass --> MD
    Audit -- Pass --> LiveTools
    MD --> Web
```

## 2. The Toolchain

### A. The Orchestrator (`ag_update_docs.py`)
This is the master script located in the root.
* **Function:** It reads the blueprints from `.ag_definitions/`, verifies that no critical sections (like "Part C") are missing, creates a timestamped backup, and then overwrites the live files.
* **Safety:** It implements a **Contextual Integrity Check**. If the new version is missing required headers or sections, it aborts the write operation to prevent accidental deletion.

### B. The Privacy Engine (`ag_regenerate_dashboards.py`)
A specialized tool for the Lovelace Dashboards.
* **Problem:** Dashboards contain personal names and sensitive IDs.
* **Solution:** This script reads the raw JSON, applies a **Regex Privacy Map** (anonymizing the names), and generates clean YAML documentation. It creates the documentation *programmatically*, ensuring it never drifts from the actual configuration.

### C. The Package Manager (`ag_update_package.py`)
A hybrid tool for documenting YAML packages.
* **Phase 1 (The Stamper):** Reads the YAML file, extracts `# Version:` and `# Description:` headers, and creates the Markdown file structure with specific **Intelligence Slots**.
* **Phase 2 (The Agent):** The AI Architect fills these slots (`<!-- PACKAGE_SUMMARY_SLOT -->`) with deep analysis and diagrams.
* **Result:** We get the precision of a script (correct versions) with the intelligence of an LLM (summaries).

## 3. The Workflow (How we work)

We do not edit `setup_guide.md` directly. We edit the **Definition**.

| Goal | Action |
| :--- | :--- |
| **Update Manual** | Edit `.ag_definitions/system_manual.py` $\rightarrow$ Run `python ag_update_docs.py` |
| **Update Privacy Rules** | Edit `.ag_definitions/ai_context.py` $\rightarrow$ Run `python ag_update_docs.py` |
| **Update Dashboard Docs** | Run `python ag_regenerate_dashboards.py` |
| **New Package** | Run `python ag_update_package.py [name]` $\rightarrow$ Ask Agent to analyze. |

## 4. Safety Features

1.  **Hidden Definitions:** The actual content lives in `.ag_definitions/` (hidden), keeping the root directory clean.
2.  **Backups:** Every time the Orchestrator runs, it saves the old version to `.ag_backups/filename.timestamp.bak`. It keeps a rolling history of the last 5 versions.
3.  **Self-Validation:** The Orchestrator scans its own input for a `VALIDATION_CHECKLIST`. If the input is missing "Troubleshooting" or "Daily Operations", it refuses to build.
