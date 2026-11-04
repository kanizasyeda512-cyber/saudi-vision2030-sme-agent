# Architecture Overview

The AI Agent follows a structured modular workflow:
1. **Planner:** Takes user input in Arabic or English and parses the financial/guidance request.
2. **Tools Execution:** Calls specialized tools for Data Loading, Financial Analysis, SDG Recommendation, and Report Generation.
3. **Structured Output:** Produces a final response with confidence scores, SDG target tags, and bilingual support.

## System Architecture Diagram
```mermaid
graph TD
    A[User Query: English / Arabic] --> B[Agent Planner / Controller]
    B --> C{Tool Selector}
    C -->|Load Data| D[Data Loader Tool]
    C -->|Analyze SME Data| E[SME Analyzer Tool]
    C -->|Generate Advice| F[SDG Recommender Tool]
    C -->|Compile Report| G[Report Generator Tool]
    D --> H[Structured Response & Report]
    E --> H
    F --> H
    G --> H
    H --> I[Output to CLI / UI]
