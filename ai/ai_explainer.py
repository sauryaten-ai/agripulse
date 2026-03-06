import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# configure Gemini
genai.configure(api_key=os.getenv("AIzaSyD1iuY4KEXP2uiJYNqKIttb01vUeQctggM"))

# correct model name
model = genai.GenerativeModel("models/gemini-1.5-flash")


def generate_ai_explanation(crop, deficiencies, fertilizer):

    if not deficiencies:
        return f"The soil is healthy and suitable for growing {crop}. No fertilizer is required."

    nutrients = ", ".join(deficiencies)

    prompt = f"""
You are an agricultural expert helping farmers.

Crop: {crop}
Missing nutrients: {nutrients}
Recommended fertilizer: {fertilizer}

Explain in simple farmer-friendly language:

1. Why these nutrients are important
2. How the fertilizer helps the crop
3. Keep explanation short (3–4 sentences)
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return f"The soil lacks {nutrients}. Applying the recommended fertilizer will help improve soil health and crop growth."