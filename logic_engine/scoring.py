from logic_engine.crop_rules import CROP_RULES, UNIVERSAL_THRESHOLDS


def calculate_score(n, p, k, ph, crop):

    score = 100
    deficiencies = []

    rules = CROP_RULES[crop]

    ph_low, ph_high = rules["ph_range"]

    # pH penalty
    if not (ph_low <= ph <= ph_high):
        score -= 20

    # Universal deficiency
    if n < UNIVERSAL_THRESHOLDS["N"]:
        score -= 15
        deficiencies.append("Nitrogen")

    if p < UNIVERSAL_THRESHOLDS["P"]:
        score -= 15
        deficiencies.append("Phosphorus")

    if k < UNIVERSAL_THRESHOLDS["K"]:
        score -= 15
        deficiencies.append("Potassium")

    # Critical crop penalty
    key = rules["key_nutrient"]
    threshold = rules["high_demand_threshold"]

    if key == "N" and n < threshold:
        score -= 10

    if key == "P" and p < threshold:
        score -= 10

    if key == "K" and k < threshold:
        score -= 10

    return max(score,0), deficiencies