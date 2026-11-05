
"""
Saudi Vision 2030 - SME Growth & Financing Agent
Python 3.11+
English and Arabic Support
"""

import os
import json
import typer
import anthropic

from typing import Optional
from pydantic import BaseModel, Field

app = typer.Typer()


# ---------------------------------
# 1. Input Validation
# ---------------------------------

class BusinessInfo(BaseModel):
    business_name: str
    sector: str
    monthly_revenue: float = Field(ge=0)
    years_operating: float = Field(ge=0)


# ---------------------------------
# 2. Financing Readiness Tool
# ---------------------------------

def financing_readiness(
    monthly_revenue: float,
    years_operating: float
):
    if monthly_revenue < 0 or years_operating < 0:
        raise ValueError("Values cannot be negative")

    return {
        "revenue": monthly_revenue,
        "business_age": years_operating,
        "checklist": [
            "Business registration documents",
            "Financial statements",
            "Business bank records",
            "Business plan",
            "Cash flow records"
        ],
        "note": "This is a readiness checklist, not loan approval."
    }


# ---------------------------------
# 3. Funding Options Tool
# ---------------------------------

def funding_options(amount: float, purpose: str):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    return {
        "requested_amount": amount,
        "purpose": purpose,
        "options": [
            "Bank financing",
            "Government SME support programs",
            "Microfinance",
            "Equity investment",
            "Business partnerships"
        ],
        "note": "Check current eligibility and terms with providers."
    }


# ---------------------------------
# 4. Business Growth Tool
# ---------------------------------

def business_growth(sector: str, goal: str):
    return {
        "sector": sector,
        "goal": goal,
        "recommendations": [
            "Improve digital marketing",
            "Develop customer relationships",
            "Control operating costs",
            "Improve product quality",
            "Explore new markets"
        ]
    }


# ---------------------------------
# 5. Business Compliance Tool
# ---------------------------------

def business_compliance(sector: str):
    return {
        "sector": sector,
        "checklist": [
            "Verify business registration",
            "Check required activity licenses",
            "Maintain financial records",
            "Review tax and Zakat obligations",
            "Follow applicable regulations"
        ],
        "note": "Requirements depend on business activity."
    }


# ---------------------------------
# 6. Vision 2030 and SDG Tool
# ---------------------------------

def vision_sdg_alignment():
    return {
        "vision": "Saudi Vision 2030",
        "vision_goal": "Thriving Economy",
        "primary_sdg": "SDG 8.3 - Entrepreneurship and SME growth",
        "secondary_sdg": "SDG 9.3 - Access to financial services",
        "impact": "Support sustainable SME development"
    }


# ---------------------------------
# 7. Tool Definitions
# ---------------------------------

TOOLS = [
    {
        "name": "financing_readiness",
        "description": "Check SME financing readiness.",
        "input_schema": {
            "type": "object",
            "properties": {
                "monthly_revenue": {"type": "number"},
                "years_operating": {"type": "number"}
            },
            "required": ["monthly_revenue", "years_operating"]
        }
    },
    {
        "name": "funding_options",
        "description": "Explore suitable funding categories.",
        "input_schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "purpose": {"type": "string"}
            },
            "required": ["amount", "purpose"]
        }
    },
    {
        "name": "business_growth",
        "description": "Generate SME growth recommendations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "sector": {"type": "string"},
                "goal": {"type": "string"}
            },
            "required": ["sector", "goal"]
        }
    },
    {
        "name": "business_compliance",
        "description": "Provide a business compliance checklist.",
        "input_schema": {
            "type": "object",
            "properties": {
                "sector": {"type": "string"}
            },
            "required": ["sector"]
        }
    },
    {
        "name": "vision_sdg_alignment",
        "description": "Show Vision 2030 and SDG alignment.",
        "input_schema": {
            "type": "object",
            "properties": {}
        }
    }
]


# ---------------------------------
# 8. Tool Execution
# ---------------------------------

def execute_tool(name, args):
    available_tools = {
        "financing_readiness": financing_readiness,
        "funding_options": funding_options,
        "business_growth": business_growth,
        "business_compliance": business_compliance,
        "vision_sdg_alignment": vision_sdg_alignment
    }

    if name not in available_tools:
        raise ValueError("Unknown tool")

    return available_tools[name](**args)


# ---------------------------------
# 9. Mock Mode
# ---------------------------------

def mock_mode():
    print("\nSAUDI VISION 2030 SME AGENT")
    print("MOCK MODE - SAMPLE DATA\n")

    results = {
        "financing": financing_readiness(15000, 2),
        "funding": funding_options(50000, "Business expansion"),
        "growth": business_growth("Technology", "Increase sales"),
        "compliance": business_compliance("Technology"),
        "alignment": vision_sdg_alignment()
    }

    print(json.dumps(results, indent=4))
    print("\nMock test completed successfully!")


# ---------------------------------
# 10. Anthropic AI Agent
# ---------------------------------

def ai_agent(question: str, language: str):

    client = anthropic.Anthropic()

    system_prompt = f"""
    You are a Saudi Vision 2030 SME Growth
    and Financing Guidance AI Agent.

    Help small and medium businesses with:
    1. Financing readiness
    2. Funding options
    3. Business growth
    4. Compliance guidance
    5. Vision 2030 and SDG alignment

    Use available tools when needed.
    Support English and Arabic.
    Respond in {language}.

    Never guarantee loan approval.
    Never invent financial programs or facts.
    Clearly identify sample or unverified data.
    Give practical and structured recommendations.
    """

    messages = [
        {"role": "user", "content": question}
    ]

    while True:

        response = client.messages.create(
            model=os.getenv(
                "ANTHROPIC_MODEL",
                "claude-sonnet-4-5"
            ),
            max_tokens=1500,
            system=system_prompt,
            tools=TOOLS,
            messages=messages
        )

        tool_results = []

        for block in response.content:

            if block.type == "text":
                print(block.text)

            elif block.type == "tool_use":

                try:
                    result = execute_tool(
                        block.name,
                        block.input
                    )

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })

                except Exception as error:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(error),
                        "is_error": True
                    })

        if response.stop_reason != "tool_use":
            break

        messages.append({
            "role": "assistant",
            "content": response.content
        })

        messages.append({
            "role": "user",
            "content": tool_results
        })


# ---------------------------------
# 11. Main CLI Application
# ---------------------------------

@app.callback()
def main(
    mock: bool = typer.Option(
        False, "--mock",
        help="Run without API connection"
    ),
    language: str = typer.Option(
        "English", "--language",
        help="English or Arabic"
    )
):
    """Saudi Vision 2030 SME Growth Agent."""

    if language not in ["English", "Arabic"]:
        raise typer.BadParameter(
            "Choose English or Arabic"
        )

    if mock:
        mock_mode()
    else:
        question = typer.prompt(
            "Enter your business question"
        )

        ai_agent(question, language)


if __name__ == "__main__":
    app()
