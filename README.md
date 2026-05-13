# 🛠️ devkit

Ce projet a été réalisé dans le cadre du module de CLI durant le semestre 8 à Télécom Saint-Étienne. Ce projet, nommé devkit, est un toolkit en ligne de commande développé en Python. Il unifie la gestion de GitHub (issues, pull requests), l'automatisation des workflows Git et l'intégration de l'intelligence artificielle (Claude, Gemini, Copilot) au sein d'une interface terminal pour optimiser la productivité des développeurs.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-FF6B6B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A modern developer toolkit that brings GitHub, Git, and AI directly into your terminal.**

[Getting Started](#-getting-started) · [Features](#-features--command-showcase) · [Live Demo](#-live-demo) · [Commands](#-features--command-showcase)

</div>

---

## 📖 Project Description

`devkit` is a modern Command Line Interface (CLI) tool built to **supercharge developer workflows**. Instead of juggling multiple tabs, browser windows, and tools, `devkit` brings everything you need into a single, unified terminal experience.

### Why devkit?

Modern software development involves constantly switching contexts: checking GitHub issues, reviewing pull requests, writing commit messages, starting feature branches, and understanding complex commands. Each of these tasks traditionally requires separate tools or manual steps.

`devkit` solves this by integrating:

- **🐙 GitHub CLI (`gh`)** — Query issues, pull requests, and repository data without leaving the terminal.
- **🌿 Git** — Automate repetitive branching and commit workflows with intelligent defaults.
- **🤖 AI Tools** — Leverage **Claude**, **Gemini**, and **GitHub Copilot** to review code, generate commit messages, plan features, and explain commands — all from one place.

Built with **Python**, powered by **Typer** for a clean CLI experience, and styled with **Rich** for beautiful, readable terminal output — `devkit` is designed to be both powerful and a pleasure to use.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python **3.10** or higher
- `git`
- GitHub CLI (`gh`) — [Installation guide](https://cli.github.com/)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/1p0tato1/devkit.git
cd devkit
```

**2. Create and activate a virtual environment**

```bash
# Create the virtual environment
python -m venv .venv

# Activate it — macOS/Linux
source .venv/bin/activate

# Activate it — Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

**3. Install devkit in editable mode**

```bash
pip install -e .
```

**4. Verify the installation**

```bash
devkit --help
```

You should see the `devkit` help menu with all available commands. You're ready to go! ✅

---

## 🎬 Live Demo

See `devkit` in action with a full end-to-end terminal recording:

https://github.com/1p0tato1/devkit/raw/main/video-demo.mp4

---

## ✨ Features & Command Showcase

`devkit` is organized into two main command groups:

| Group | Purpose |
|---|---|
| `devkit gh` | GitHub integration — issues, PRs, repository data |
| `devkit ai` | AI-powered tools — review, commit, explain |
| `devkit workflow` | Automated Git + GitHub workflows |

---
## 🛠️ DevKit — Key Features & Demo

### 1️⃣ `devkit gh issues` — Overview of Work
We begin by listing pending tasks. The tool generates an elegant, color-coded table using the Rich library.

```bash
$ devkit gh issues
          GitHub Open Issues           
┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ID ┃ Title                         ┃
┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ #10 │ Performance optimization      │
│  #9 │ UI Redesign                   │
│  #1 │ My first issue                │
└─────┴───────────────────────────────┘
```
> **Key Benefit:** Stay in the terminal to pick your next task without ever opening a browser.

---

### 2️⃣ `devkit gh pr-summary` & `ai review` — Code Analysis
Before coding, we analyze existing work. This step combines GitHub data retrieval with Artificial Intelligence.

```bash
# Step A: Technical PR Summary
$ devkit gh pr-summary 8
── PR #8 : Demo Perfect1 ──
Modified files: src/devkit/commands/ai.py, workflow.py...

# Step B: AI Code Review
$ devkit ai review 8
⠸ Running claude review...
╭─────────────────────────── AI Review (claude) — PR #8 ────────────────────────────╮
│ Claude Simulation: Action plan generated successfully.                            │
╰───────────────────────────────────────────────────────────────────────────────────╯
```
> **Key Benefit:** Provides a "dual-vision" approach: a factual list of modified files paired with an AI critical analysis to ensure top-tier code quality.

---

### 3️⃣ `devkit workflow feature-start` — Full Automation
The core of the tool. A single command to automate 5 minutes of manual, repetitive tasks.

```bash
$ devkit workflow feature-start "demo-finale" --issue 5
─────────────────────────────── Starting Feature ───────────────────────────────
✓ Created branch: feature/demo-finale
✓ Draft PR created: https://github.com/1p0tato1/devkit/pull/11
╭────────────────────────── AI Implementation Plan ──────────────────────────╮
│ Claude Simulation: Action plan generated successfully.                     │
╰────────────────────────────────────────────────────────────────────────────╯
──────────────────────────────── Ready to code! ────────────────────────────────
```
> **Key Benefit:** Automates branch creation, initial push, Draft PR opening, and generates an AI implementation plan in one single action.

---

### 4️⃣ `devkit ai commit` — Intelligent Documentation
Once the code is modified, the AI analyzes the diff to suggest a relevant and descriptive commit message.

```bash
# Prepare your changes
$ git add test.txt

# Let the AI draft the message
$ devkit ai commit
╭──────────────────────── Suggested Message (claude) ────────────────────────╮
│ Claude Simulation: Action plan generated successfully.                     │
╰────────────────────────────────────────────────────────────────────────────╯
Use this message? [y/n]: y
[feature/demo-finale f80618e] Claude Simulation: Action plan generated...
✓ Committed!
```
> **Key Benefit:** Guarantees a clean, meaningful Git history with zero effort from the developer.

---

### 5️⃣ `devkit ai explain` — Learning & Onboarding
A pedagogical assistant that helps decode complex or unfamiliar commands.

```bash
$ devkit ai explain "git rebase -i HEAD~3"
╭─────────────────────────── Copilot Explanation ────────────────────────────╮
│ GitHub Copilot tool is analyzing: git rebase -i HEAD~3                     │
│                                                                            │
│ This command allows you to interactively rewrite the Git history for the   │
│ last 3 commits.                                                            │
╰────────────────────────────────────────────────────────────────────────────╯
```
> **Key Benefit:** Leverages the power of Copilot to explain any shell command, making it perfect for quick learning and smooth onboarding.
---

## 🏗️ Tech Stack

| Technology | Role |
|---|---|
| [Python 3.10+](https://www.python.org/) | Core language |
| [Typer](https://typer.tiangolo.com/) | CLI framework — commands, arguments, options |
| [Rich](https://rich.readthedocs.io/) | Terminal UI — panels, spinners, colors, tables |
| [GitHub CLI (`gh`)](https://cli.github.com/) | GitHub API integration |
| [Claude (Anthropic)](https://www.anthropic.com/) | AI code review, commit messages, planning |
| [Gemini (Google)](https://deepmind.google/technologies/gemini/) | Alternative AI provider |
| [GitHub Copilot](https://github.com/features/copilot) | Command explanation |

---

## 📁 Project Structure

```
devkit/
├── devkit/
│   ├── __init__.py
│   ├── main.py          # CLI entry point (Typer app)
│   ├── commands/
│   │   ├── gh.py        # GitHub CLI integration
│   │   ├── ai.py        # AI-powered commands
│   │   └── workflow.py  # Automated Git workflows
│   └── utils/
│       └── rich_utils.py # Rich formatting helpers
├── tests/
├── pyproject.toml
└── README.md
```

> Projet réalisé par Hakim Fayala, Mathéo Decrock & Paulin Gasquet