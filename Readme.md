# Saudi Vision 2030 AI Workforce & SDG Alignment Agent

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An autonomous AI agent addressing Saudi Vision 2030 workforce optimization, female labor force participation, and Nitaqat regulatory compliance, mapped directly to United Nations Sustainable Development Goals (SDGs 8, 5, and 9).

---

## 🌟 Vision 2030 & SDG Badges

| Pillar / Program | Target Metric | SDG Mapping |
| :--- | :--- | :--- |
| **Thriving Economy & Vibrant Society** | Saudi Unemployment Rate < 7% & Female Participation > 35% | **SDG 8** (Decent Work) & **SDG 5** (Gender Equality) |

---

## 🏛️ Architecture Overview

```mermaid
graph TD
    User([User / CLI Typer App]) -->|Query / Enterprise ID| Agent[Vision Agent Core]
    Agent -->|Planner Loop| Anthropic[Anthropic Claude / Mock LLM]
    
    subgraph Agent Tools
        Anthropic -->|Call Tool| DataLoader[Data Loader Tool]
        Anthropic -->|Call Tool| SkillAnalyzer[Skill Analyzer Tool]
        Anthropic -->|Call Tool| NitaqatOpt[Nitaqat Optimizer Tool]
        Anthropic -->|Call Tool| ReportGen[Report Generator Tool]
    end

    DataLoader -->|Read JSON| Data[(data/sample/)]
    SkillAnalyzer -->|Evaluate Skills| Metrics[SDG 8 & 5 Metrics]
    NitaqatOpt -->|Calculate Quotas| Tiers[Nitaqat Tiers]
    ReportGen -->|Synthesize Output| Output[Bilingual Structured Report]
    
    Output --> User
