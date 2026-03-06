def generate_ai_explanation(crop, deficiencies):

    if not deficiencies:
        return f"The soil is healthy and suitable for growing {crop}."

    nutrients = ", ".join(deficiencies)

    return f"The soil is lacking {nutrients}. These nutrients are important for healthy {crop} growth. Applying the recommended fertilizers will improve crop yield."