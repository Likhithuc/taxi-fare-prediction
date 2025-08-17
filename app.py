import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("taxi_fare_model.pkl")

# Streamlit UI
st.title("🚕 Taxi Fare Prediction")
st.write("Enter trip details to predict the taxi fare.")

# User inputs
distance = st.number_input("Distance (km)", min_value=0.1, max_value=50.0, value=5.0, step=0.1)
passengers = st.number_input("Number of Passengers", min_value=1, max_value=6, value=1, step=1)

if st.button("Predict Fare"):
    # Prepare input
    input_data = pd.DataFrame({'distance': [distance], 'passenger_count': [passengers]})
    
    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Fare: ${round(prediction, 2)}")
