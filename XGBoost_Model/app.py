import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="California Housing Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -------------------------------------------------
# Load XGBoost Model
# -------------------------------------------------
@st.cache_resource
def load_model():
    with open("xgboost_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


model = load_model()

# -------------------------------------------------
# Title
# -------------------------------------------------
st.title("🏠 California Housing Price Predictor")
st.write(
    "Enter the house details below to predict the median house value."
)

st.divider()

# -------------------------------------------------
# Input Fields
# -------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input(
        "Median Income (MedInc)",
        min_value=0.0,
        value=3.87,
        step=0.1
    )

    house_age = st.number_input(
        "House Age",
        min_value=0.0,
        value=28.0,
        step=1.0
    )

    ave_rooms = st.number_input(
        "Average Rooms (AveRooms)",
        min_value=0.0,
        value=5.4,
        step=0.1
    )

    ave_bedrms = st.number_input(
        "Average Bedrooms (AveBedrms)",
        min_value=0.0,
        value=1.1,
        step=0.1
    )

with col2:
    population = st.number_input(
        "Population",
        min_value=0.0,
        value=1200.0,
        step=100.0
    )

    ave_occup = st.number_input(
        "Average Occupancy (AveOccup)",
        min_value=0.0,
        value=3.0,
        step=0.1
    )

    latitude = st.number_input(
        "Latitude",
        value=35.0,
        step=0.1
    )

    longitude = st.number_input(
        "Longitude",
        value=-119.0,
        step=0.1
    )

# -------------------------------------------------
# ID-like Column
# -------------------------------------------------
# Your trained model expects 'Unnamed: 0'.
# Since this is an ID/index column, we use 0 by default.
unnamed_0 = 0

# -------------------------------------------------
# Prediction Button
# -------------------------------------------------
st.divider()

if st.button("🔮 Predict House Price", use_container_width=True):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Unnamed: 0": [unnamed_0],
        "MedInc": [med_inc],
        "HouseAge": [house_age],
        "AveRooms": [ave_rooms],
        "AveBedrms": [ave_bedrms],
        "Population": [population],
        "AveOccup": [ave_occup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    try:
        # Make prediction
        prediction = model.predict(input_data)

        predicted_value = float(prediction[0])

        # Display result
        st.success("Prediction completed successfully!")

        st.subheader("🏡 Predicted House Value")

        st.metric(
            label="Predicted Median House Value",
            value=f"${predicted_value * 100000:,.2f}"
        )

        # Optional: show model input
        with st.expander("View Input Data"):
            st.dataframe(input_data)

    except Exception as e:
        st.error("An error occurred while making the prediction.")
        st.exception(e)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.divider()

st.caption(
    "Built with Python, Streamlit, Pandas and XGBoost"
)
