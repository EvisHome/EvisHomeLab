---
title: System Changelog
description: Tracking changes to the documentation and configuration systems.
---

# 📝 System Changelog

## [2026-05-04] - Privacy System Update
*   **Security:** Centralized the "Allowed Person Views" logic for dashboard generation into the main privacy module. This ensures all redaction and visibility rules are governed by a single source of truth, preventing accidental leaks of private views.
*   **Security:** Expanded the automated privacy scrubber to generically detect and redact hardcoded passwords, API keys, and tokens from any files before they are published to the documentation site.
*   **Documentation:** Restructured the Workflow documentation (`architecture.md` and `tools.md`) to clearly separate system design from daily operations. Removed deprecated AI prompts from the public docs and integrated them directly into the internal agent modules.
