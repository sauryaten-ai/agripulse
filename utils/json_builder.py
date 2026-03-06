def build_json(soil_id, crop, score, deficiencies, fertilizer, ai_text):

    if score >= 80:
        health = "Optimal"
    elif score >= 50:
        health = "Deficient"
    else:
        health = "Critical"

    return {
        "soil_id": soil_id,
        "target_crop": crop,
        "health_metrics": {
            "overall_health": health,
            "critical_deficiencies": deficiencies
        },
        "recommendation": {
            "fertilizer_plan": fertilizer,
            "suitability_score": score
        },
        "ai_explanation": ai_text
    }