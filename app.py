import streamlit as st
import pandas as pd
import joblib

# Load Models

crop_model = joblib.load("crop_model.pkl")

yield_model = joblib.load("yield_model.pkl")
area_encoder = joblib.load("area_encoder.pkl")
item_encoder = joblib.load("item_encoder.pkl")

fert_model = joblib.load("fertilizer_model.pkl")
soil_encoder = joblib.load("soil_encoder.pkl")
crop_encoder = joblib.load("crop_encoder.pkl")
fert_encoder = joblib.load("fert_encoder.pkl")

# Page Configuration

st.set_page_config(
    page_title="AI-Based Prediction in Smart Farming",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI-Based Prediction in Smart Farming")

st.sidebar.title("Navigation")

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Crop Recommendation",
        "Crop Yield Prediction",
        "Fertilizer Recommendation"
    ]
)

# Crop Recommendation

if menu == "Crop Recommendation":

    st.header("🌾 Crop Recommendation System")

    N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=42)
    K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=43)

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=25.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    ph = st.number_input(
        "pH Value",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=5000.0,
        value=200.0
    )

    if st.button("Recommend Crop"):

        sample = [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        prediction = crop_model.predict(sample)

        st.success(f"Recommended Crop: {prediction[0]}")

# Crop Yield Prediction

elif menu == "Crop Yield Prediction":

    st.header("📈 Crop Yield Prediction")

    area = st.selectbox(
        "Select Area",
        list(area_encoder.classes_)
    )

    crop = st.selectbox(
        "Select Crop",
        list(item_encoder.classes_)
    )

    year = st.number_input(
        "Year",
        min_value=1990,
        max_value=2050,
        value=2024
    )

    rainfall = st.number_input(
        "Average Rainfall (mm/year)",
        value=1200.0
    )

    pesticides = st.number_input(
        "Pesticides Used (tonnes)",
        value=25000.0
    )

    avg_temp = st.number_input(
        "Average Temperature (°C)",
        value=27.0
    )

    if st.button("Predict Yield"):

        area_encoded = area_encoder.transform([area])[0]
        crop_encoded = item_encoder.transform([crop])[0]

        sample = [[
            area_encoded,
            crop_encoded,
            year,
            rainfall,
            pesticides,
            avg_temp
        ]]

        prediction = yield_model.predict(sample)

        st.success(
            f"Predicted Crop Yield: {prediction[0]:.2f} hg/ha"
        )

# Fertilizer Recommendation

elif menu == "Fertilizer Recommendation":

    st.header("🧪 Fertilizer Recommendation")

    temperature = st.number_input(
        "Temperature",
        value=26
    )

    humidity = st.number_input(
        "Humidity",
        value=52
    )

    moisture = st.number_input(
        "Moisture",
        value=38
    )

    soil_type = st.selectbox(
        "Soil Type",
        list(soil_encoder.classes_)
    )

    crop_type = st.selectbox(
        "Crop Type",
        list(crop_encoder.classes_)
    )

    nitrogen = st.number_input(
        "Nitrogen",
        value=37
    )

    potassium = st.number_input(
        "Potassium",
        value=0
    )

    phosphorous = st.number_input(
        "Phosphorous",
        value=0
    )

    if st.button("Recommend Fertilizer"):

        soil_encoded = soil_encoder.transform([soil_type])[0]
        crop_encoded = crop_encoder.transform([crop_type])[0]

        sample = [[
            temperature,
            humidity,
            moisture,
            soil_encoded,
            crop_encoded,
            nitrogen,
            potassium,
            phosphorous
        ]]

        prediction = fert_model.predict(sample)

        fertilizer = fert_encoder.inverse_transform(prediction)

        st.success(
            f"Recommended Fertilizer: {fertilizer[0]}"
        )

# Footer

st.markdown("---")

st.markdown(
    """
    ### Project Information
    **Title:** AI-Based Prediction in Smart Farming
    
    **Developed By:** Sarvottam Kumar  
    **Entry No:** 24BCN036  
    **Branch:** Mathematics & Computing  
    **Internship Area:** AI & ML
    """
)