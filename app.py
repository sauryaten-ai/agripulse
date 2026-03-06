import streamlit as st
from logic_engine.scoring import calculate_score
from logic_engine.fertilizer import fertilizer_plan
from utils.csv_parser import parse_csv
from utils.json_builder import build_json
from ai.ai_explainer import generate_ai_explanation

# PAGE SETTINGS
st.set_page_config(
    page_title="AgriPulse",
    page_icon="🌱",
    layout="wide"
)

# CUSTOM UI STYLE
st.markdown("""
<style>
/* App background - Soft, modern earthy tone */
.stApp {
    background-color: #f7f9f7;
}

/* Clean up the main block layout */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Typography & All Headings strictly Black */
h1, h2, h3, h4, h5, h6 {
    color: black !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
    font-weight: 800;
    letter-spacing: -0.5px;
}

h2, h3 {
    font-weight: 700;
    margin-top: 1rem;
}

/* Make all standard paragraph text black */
div[data-testid="stMarkdownContainer"] p {
    color: black !important;
    font-size: 1.1rem;
}

/* TARGET INPUT LABELS (Selectbox, Uploader) TO BE WHITE */
label, [data-testid="stWidgetLabel"] p {
    color: white !important;
    font-weight: 600;
    font-size: 1.05rem;
}

/* Style the Metrics to look like premium dashboard cards */
div[data-testid="metric-container"] {
    background-color: #ffffff;
    border: 1px solid #e0e6e0;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.08);
}

/* Suitability Score Number */
div[data-testid="stMetricValue"] {
    color: #2e7d32;
    font-size: 2.2rem !important;
    font-weight: 800;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #43a047, #2e7d32);
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(46, 125, 50, 0.2);
}
.stButton>button:hover {
    background: linear-gradient(135deg, #2e7d32, #1b5e20);
    box-shadow: 0 6px 12px rgba(46, 125, 50, 0.3);
    transform: translateY(-1px);
    color: white;
}

/* File Uploader outer styling */
[data-testid="stFileUploader"] {
    background-color: #ffffff; 
    border: 1px dashed #43a047;
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

/* MAKE DROPZONE TEXT ("Browse files") WHITE */
[data-testid="stFileUploadDropzone"] * {
    color: white !important;
}

/* KEEP UPLOADED FILE NAME BLACK */
[data-testid="stUploadedFile"] * {
    color: black !important;
}

/* JSON Output Box */
.stJson {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    border: 1px solid #e0e6e0;
    padding: 1rem;
}

/* Subheaders for individual soil IDs */
div[data-testid="stMarkdownContainer"] > h3[id^="soil-id"] {
    background-color: #e8f5e9;
    padding: 0.8rem 1.2rem;
    border-radius: 8px;
    border-left: 5px solid #2e7d32;
    margin-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.title("🌱 AgriPulse – Smart Soil Analyzer")
st.write("AI-powered precision agriculture tool for soil nutrient analysis and crop suitability.")

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

# PROCESS CSV
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

        ai_text = generate_ai_explanation(crop, deficiencies, fertilizer)

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

        with col1:
            st.metric("Suitability Score", f"{score}%")

        with col2:
            if score >= 80:
                st.success("Optimal Soil")
            elif score >= 50:
                st.warning("Deficient Soil")
            else:
                st.error("Critical Soil")

        with col3:
            if deficiencies:
                st.write("⚠️ Nutrient Deficiencies")
                st.write(deficiencies)
            else:
                st.write("✅ No deficiencies")

        st.markdown("### 🌿 Fertilizer Recommendation")
        st.info(fertilizer)

        st.markdown("### 🤖 AI Explanation")
        st.write(ai_text)

        st.markdown("### 📦 JSON Output")
        st.json(result)

        st.divider()
# ===============================
# WHAT IF SIMULATOR
# ===============================

st.header("🔬 Manual Simulator")

st.write("Adjust soil nutrients and simulate how the crop would perform under different soil conditions.")

sim_col1, sim_col2 = st.columns(2)

with sim_col1:
    sim_n = st.slider("Nitrogen Level (mg/kg)", 0, 100, 25)
    sim_p = st.slider("Phosphorus Level (mg/kg)", 0, 100, 20)

with sim_col2:
    sim_k = st.slider("Potassium Level (mg/kg)", 0, 300, 180)
    sim_ph = st.slider("Soil pH Level", 3.0, 9.0, 6.5)

simulate = st.button("Run Simulation")

if simulate:

    score, deficiencies = calculate_score(sim_n, sim_p, sim_k, sim_ph, crop)

    fertilizer = fertilizer_plan(sim_n, sim_p, sim_k)

    ai_text = generate_ai_explanation(crop, deficiencies, fertilizer)

    st.subheader("🌾 Simulation Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Simulated Suitability Score", f"{score}%")

    with col2:
        if score >= 80:
            st.success("Healthy Crop Growth")
        elif score >= 50:
            st.warning("Moderate Crop Condition")
        else:
            st.error("Poor Crop Growth")

    with col3:
        if deficiencies:
            st.write("Missing Nutrients:")
            st.write(deficiencies)
        else:
            st.write("No nutrient deficiencies")

    st.markdown("### 🌿 Recommended Fertilizer")
    st.info(fertilizer)

    st.markdown("### 🤖 AI Agronomy Insight")
    st.write(ai_text)

    st.markdown("### 🌱 Crop Health Indicator")

    st.progress(score/100)

    st.write(f"Estimated Crop Health: **{score}%**")