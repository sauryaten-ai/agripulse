import streamlit as st
from logic_engine.scoring import calculate_score
from logic_engine.fertilizer import fertilizer_plan
from utils.csv_parser import parse_csv
from utils.json_builder import build_json
from ai.ai_explainer import generate_ai_explanation

# PAGE CONFIG
st.set_page_config(
    page_title="AgriPulse",
    page_icon="🌱",
    layout="wide"
)

# CUSTOM CSS FOR BETTER UI
st.markdown("""
<style>

.main-title {
    font-size:40px;
    font-weight:700;
    color:#2E7D32;
}

.card {
    padding:20px;
    border-radius:12px;
    background-color:#f5f7f6;
    box-shadow:0px 4px 10px rgba(0,0,0,0.05);
}

.metric-box {
    padding:15px;
    border-radius:10px;
    text-align:center;
}

.green {background-color:#E8F5E9;}
.yellow {background-color:#FFFDE7;}
.red {background-color:#FFEBEE;}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<p class="main-title">🌱 AgriPulse – Precision Agriculture Dashboard</p>', unsafe_allow_html=True)

st.write("Upload soil data and analyze crop suitability using AI-powered recommendations.")

# INPUT SECTION
col1, col2 = st.columns(2)

with col1:
    crop = st.selectbox(
        "🌾 Select Target Crop",
        ["TOMATO", "WHEAT", "RICE", "MAIZE"]
    )

with col2:
    file = st.file_uploader(
        "📂 Upload Soil CSV File",
        type=["csv"]
    )

st.divider()

# PROCESS DATA
if file:

    df = parse_csv(file)

    for index, row in df.iterrows():

        soil_id = row["soil_id"]
        n = row["nitrogen"]
        p = row["phosphorus"]
        k = row["potassium"]
        ph = row["ph_level"]

        score, deficiencies = calculate_score(n,p,k,ph,crop)
        fertilizer = fertilizer_plan(n,p,k)
        ai_text = generate_ai_explanation(crop, deficiencies)

        result = build_json(
            soil_id,
            crop,
            score,
            deficiencies,
            fertilizer,
            ai_text
        )

        st.subheader(f"🧪 Soil ID: {soil_id}")

        col1, col2, col3 = st.columns(3)

        # SCORE DISPLAY
        with col1:
            st.metric("Suitability Score", f"{score}%")

        # HEALTH STATUS
        with col2:

            if score >= 80:
                st.markdown('<div class="metric-box green"><b>Optimal Soil</b></div>', unsafe_allow_html=True)

            elif score >= 50:
                st.markdown('<div class="metric-box yellow"><b>Deficient Soil</b></div>', unsafe_allow_html=True)

            else:
                st.markdown('<div class="metric-box red"><b>Critical Soil</b></div>', unsafe_allow_html=True)

        # DEFICIENCIES
        with col3:
            if deficiencies:
                st.write("⚠️ Nutrient Deficiencies")
                st.write(deficiencies)
            else:
                st.write("✅ No deficiencies detected")

        st.markdown("### 🌿 Fertilizer Recommendation")
        st.info(fertilizer)

        st.markdown("### 🤖 AI Explanation")
        st.write(ai_text)

        st.markdown("### 📦 JSON Output ")
        st.json(result)

        st.divider()