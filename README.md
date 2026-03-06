# 🌱 AgriPulse – AI-Powered Precision Agriculture Dashboard

AgriPulse is an AI-powered web application designed to help farmers and agricultural analysts interpret soil nutrient data and determine crop suitability.

The system analyzes soil chemical composition (NPK + pH), calculates a crop suitability score, recommends fertilizers, and generates AI-based agricultural insights in simple farmer-friendly language.

It also includes an interactive What-If Soil Simulator that allows users to simulate crop growth under different soil conditions.

---

# 🚀 Features

## 1️⃣ Soil Data Upload
Users can upload a `.csv` file containing soil nutrient information.

Required format:

soil_id,nitrogen,phosphorus,potassium,ph_level  
SOIL_001,25,20,180,6.5  
SOIL_002,12,18,160,6.2  

---

## 2️⃣ Crop Selection

Users can analyze soil suitability for the following crops:

- TOMATO  
- WHEAT  
- RICE  
- MAIZE  

Each crop has different ideal pH ranges and nutrient demands.

---

## 3️⃣ Suitability Scoring Engine

AgriPulse calculates a Suitability Score (0–100%) based on soil nutrient levels.

### Base Score
100%

### pH Penalty
-20 points if soil pH is outside crop ideal range.

### Nutrient Deficiency Penalties

| Nutrient | Threshold | Penalty |
|--------|--------|--------|
| Nitrogen | <20 mg/kg | -15 |
| Phosphorus | <15 mg/kg | -15 |
| Potassium | <150 mg/kg | -15 |

### Critical Crop Nutrient Penalty
If the crop's key nutrient demand is not met:

-10 additional points

---

## 4️⃣ Fertilizer Recommendation Engine

AgriPulse suggests fertilizers based on nutrient deficiencies.

| Nutrient Deficiency | Fertilizer |
|---|---|
| Nitrogen | Urea |
| Phosphorus | DAP |
| Potassium | MOP |

Example output:

Apply Urea Fertilizer  
Apply DAP Fertilizer  

---

## 5️⃣ AI Agronomy Explanation

The application uses a Large Language Model (LLM) to generate a farmer-friendly explanation of:

- why nutrients are important
- how fertilizers help crop growth

Example:

Nitrogen helps wheat plants grow strong leaves and stems. When nitrogen levels are low, crop growth slows down. Applying urea fertilizer restores nitrogen in the soil and improves yield.

---

## 6️⃣ JSON Output

The system generates structured JSON output for each soil sample.

Example:

{
  "soil_id": "SOIL_001",
  "target_crop": "TOMATO",
  "health_metrics": {
    "overall_health": "Optimal",
    "critical_deficiencies": []
  },
  "recommendation": {
    "fertilizer_plan": "No fertilizer needed",
    "suitability_score": 95
  },
  "ai_explanation": "Soil conditions are ideal for tomato growth..."
}

---

## 7️⃣ Color-Coded Dashboard

The UI uses visual indicators:

Optimal → Green  
Deficient → Yellow  
Critical → Red  

This helps farmers quickly understand soil health.

---

## 8️⃣ What-If Soil Simulator

The What-If Simulator allows users to adjust soil parameters manually and simulate crop outcomes.

Users can adjust:

- Nitrogen level
- Phosphorus level
- Potassium level
- Soil pH

The system then predicts:

- crop suitability score
- nutrient deficiencies
- fertilizer recommendations
- AI agronomy insights

---

## 9️⃣ Mini Weather Condition Panel

AgriPulse includes a small weather indicator showing:

- Temperature
- Humidity
- Weather condition

Weather conditions can influence nutrient absorption and crop growth.

---

# 🖥️ Technology Stack

Frontend & UI  
Streamlit

Backend  
Python

AI Integration  
LLM API (Gemini / OpenAI)

Data Processing  
Pandas

---

# 📂 Project Structure

agripulse/

app.py  

logic_engine/  
    scoring.py  
    fertilizer.py  
    crop_rules.py  

utils/  
    csv_parser.py  
    json_builder.py  

ai/  
    ai_explainer.py  

data/  
    sample_soil.csv  
    optimal_soil.csv  
    deficient_soil.csv  
    critical_soil.csv  

README.md

---

# ⚙️ Installation

Clone the repository

git clone https://github.com/your-repo/agripulse.git

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

---

# 🧪 Example CSV Files

The repository includes sample soil datasets:

optimal_soil.csv  
deficient_soil.csv  
critical_soil.csv  

These demonstrate different soil conditions for testing.

---

# 🎯 Use Cases

AgriPulse can be used by:

- farmers
- agricultural consultants
- agri-tech companies
- research institutions
- crop planners

to analyze soil health and crop suitability.

---

# 🌍 Future Improvements

Potential upgrades:

- satellite weather integration
- crop yield prediction
- fertilizer optimization using AI
- crop recommendation system
- irrigation advisory system

---

# 👨‍💻 Authors

Developed as part of the AgriPulse Precision Agriculture AI Project.
