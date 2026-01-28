---
title: AI Automation Roadmap
description: Tracking next-generation AI features for the Smart Home.
render_macros: true
---

# 🧠 AI Automation Roadmap

This document tracks planned "Intelligence Upgrades" to move beyond simple automation into proactive assistance.

<div class="grid cards" markdown>

-   **Gemini Guardian (Active Diagnosis)**
    
    ---
    
    <span class="twemoji">:material-shield-check:</span> **Status:** On Hold  
    <span class="twemoji">:material-robot:</span> **Role:** Sysadmin
    
    **Concept:**
    Instead of just reporting "Unavailable" devices, this agent actively investigates *why* they failed.
    
    **Workflow:**
    1. Detect `unavailable` / `unknown` state.
    2. Grep Docker/Z2M logs for exact Device ID.
    3. Analyze error pattern (Timeout vs Power Loss vs USB Crash).
    4. Suggest fix to User.

-   **True Night Mode (Context Aware)**
    
    ---
    
    <span class="twemoji">:material-weather-night:</span> **Status:** Idea  
    <span class="twemoji">:material-sleep:</span> **Role:** Lifestyle
    
    **Concept:**
    Eliminate fixed-time schedules (`23:00`). The house should sleep when *you* sleep.
    
    **Triggers:**
    *   **Garmin:** Sleep State = True
    *   **Phone:** Charging + Screen Off + After 22:00
    *   **House:** Living Room FP2 = Empty for 15m
    
-   **Bio-Rhythm (Global CCT)**
    
    ---
    
    <span class="twemoji">:material-lightbulb-auto:</span> **Status:** Idea  
    <span class="twemoji">:material-sun-clock:</span> **Role:** Wellness
    
    **Concept:**
    A single "Global Health Clock" that coordinates color temperature (CCT) across all distinct lighting systems (Hue, WLED, Zigbee).
    
    **Logic:**
    *   **06:00 - 18:00:** Energize (5500K - 4000K)
    *   **18:00 - 22:00:** Relax (3000K - 2700K)
    *   **22:00 - 06:00:** Melatonin (2000K / Red Shift)
    *   *Override:* "Focus Mode" triggers allow specific rooms to break the rhythm temporarily.

</div>

## 🔮 Backlog & Exploration

<div class="grid cards" markdown>

-   **Chat with Docs (HA Voice)**
    
    ---
    
    <span class="twemoji">{% include ".icons/material/chat-processing.svg" %}</span> **Type:** RAG / Voice
    
    **Concept:**
    Query device manuals via voice (Assist). "How do I reset the dishwasher?" -> pulls from `dishwasher` manual PDF -> sends steps to companion app.

-   **Auto-Screenshots (CI/CD)**
    
    ---
    
    <span class="twemoji">{% include ".icons/material/camera-iris.svg" %}</span> **Type:** Tooling
    
    **Concept:**
    Use Playwright to auto-capture dashboard screenshots during build.
    *   **Level 1:** Full viewport of View paths.
    *   **Level 2:** CSS Selector capture for individual component cards.

-   **AI Changelogs**
    
    ---
    
    <span class="twemoji">{% include ".icons/material/file-document-edit.svg" %}</span> **Type:** Git / Workflow
    
    **Concept:**
    Auto-generate "Why this changed" summaries for git commits based on diff analysis.

-   **Multi-language Notifications**
    
    ---
    
    <span class="twemoji">{% include ".icons/material/translate.svg" %}</span> **Type:** Logic
    
    **Concept:**
    Dynamic notification language based on User Profile settings (English/Finnish).

</div>
