from typing import List, Optional
from pydantic import BaseModel, Field


class Candidate(BaseModel):
    id: str
    name: str
    city: str
    gender: str
    nationality: str
    skills: List[str]
    experience_years: int
    desired_role: str


class Enterprise(BaseModel):
    company_id: str
    name: str
    sector: str
    total_employees: int
    saudi_employees: int
    current_tier: str


class NitaqatRule(BaseModel):
    size_category: str
    thresholds: dict


class RecommendationResult(BaseModel):
    recommendation_id: str
    target_entity: str
    sdg_target: str = Field(..., description="UN SDG Target e.g., SDG 8.5")
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    bilingual_summary: dict = Field(..., description="Contains 'en' and 'ar' keys")
    actionable_steps: List[str]
