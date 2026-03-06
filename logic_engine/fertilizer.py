def fertilizer_plan(n, p, k):

    plan = []

    if n < 20:
        plan.append("Apply Urea Fertilizer")

    if p < 15:
        plan.append("Apply DAP (Diammonium Phosphate)")

    if k < 150:
        plan.append("Apply MOP (Muriate of Potash)")

    if len(plan) == 0:
        return "No fertilizer needed"

    return ", ".join(plan)