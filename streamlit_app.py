import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib

# --- Page Config ---
st.set_page_config(page_title="Breast Cancer Predictor", page_icon="♋", layout="centered")

# --- Header Animation ---
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B; font-size: 40px;'>
        🚀 Experience the power of <span style='color:#4CAF50;'>AI-driven</span> early breast cancer detection — fast, accurate, and beautifully interactive.
    </h1>
    <hr style='border:1px solid #FF4B4B'>
""", unsafe_allow_html=True)

# --- Subtitle Typing Effect ---
subtitle = "Your health, your data, your confidence."
with st.empty():
    typed = ""
    for char in subtitle:
        typed += char
        st.markdown(f"<h3 style='text-align: center; color: #6c757d;'>{typed}</h3>", unsafe_allow_html=True)
        time.sleep(0.03)

st.write("---")

# --- Load Trained Model & Scaler ---
try:
    model = joblib.load("svm_model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError as e:
    st.error(f"❌ Required file not found: {e.filename}. Please place it in the app directory.")
    st.stop()

# --- Load Dataset to Get Feature Names and Ranges ---
try:
    data = pd.read_csv("Breast_cancer_dataset.csv")
except (FileNotFoundError, EOFError) as e:
    st.error("❌ Failed to load model or scaler. The file might be missing or corrupted.")
    st.stop()


X = data.drop(columns=['id', 'diagnosis', 'Unnamed: 32'], errors='ignore')
feature_names = X.columns.tolist()

# --- Sidebar Inputs ---
st.sidebar.header("Input Features")
user_inputs = {}

for feature in feature_names:
    try:
        val = st.sidebar.slider(
            label=feature.replace("_", " ").title(),
            min_value=float(np.percentile(data[feature], 0)),
            max_value=float(np.percentile(data[feature], 100)),
            value=float(np.percentile(data[feature], 50)),
            step=0.1
        )
        user_inputs[feature] = val
    except Exception:
        st.warning(f"⚠️ Skipped invalid feature: {feature}")

# --- Predict Button ---
if st.button("💡 Predict Breast Cancer Risk"):
    input_df = pd.DataFrame([user_inputs])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    prediction_proba = model.predict_proba(input_scaled)[0]

    st.success("✅ Prediction Completed!")

    if prediction == 1:
        st.error("🔴 High Risk of Breast Cancer (Malignant Detected)")
    else:
        st.success("🟢 Low Risk of Breast Cancer (Benign)")

    st.markdown(f"""
        <div style="text-align:center; font-size: 18px;">
            <strong>Confidence:</strong><br>
            🟢 Benign: {prediction_proba[0]*100:.2f}%<br>
            🔴 Malignant: {prediction_proba[1]*100:.2f}%
        </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <br><hr>
    Developed with ❤️ by <b>Saidul Islam</b> <br>
    <a href="https://www.linkedin.com/in/saidulislam2003/" target="_blank">🔗 LinkedIn</a> |
    <a href="https://github.com/saidulislam2003/Breast-Cancer-Detector" target="_blank">📂 GitHub Project</a>
</div>
""", unsafe_allow_html=True)
