from typing import Dict, Any, List


def analyze_workforce_gaps(candidates: List[Dict[str, Any]], enterprise: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze skill matching between candidates and enterprise sector requirements."""
    sector = enterprise.get("sector", "Information Technology")
    total = enterprise.get("total_employees", 100)
    saudi = enterprise.get("saudi_employees", 30)
    current_ratio = saudi / total if total > 0 else 0

    matched_candidates = []
    for cand in candidates:
        match_score = len(set(cand.get("skills", [])) & set(["Python", "Data Analysis", "Project Management", "Cybersecurity"]))
        if match_score > 0:
            matched_candidates.append({
                "id": cand["id"],
                "name": cand["name"],
                "gender": cand["gender"],
                "match_strength": f"{match_score * 25}%",
                "desired_role": cand["desired_role"]
            })

    return {
        "sector": sector,
        "current_saudi_percentage": round(current_ratio * 100, 2),
        "qualified_matches_found": len(matched_candidates),
        "matched_candidates": matched_candidates,
        "sdg_alignment": "SDG 8.5 (Decent Work & Employment) & SDG 5.5 (Gender Equality)"
    }
