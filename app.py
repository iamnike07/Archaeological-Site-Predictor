import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Load model, scaler, and dataset ---
model = joblib.load("archaeo_rf_model.pkl")
scaler = joblib.load("archaeo_scaler.pkl")
df = pd.read_csv("india_archaeo_dataset_500.csv")

# --- Streamlit page setup ---
st.set_page_config(page_title="Archaeological Site Predictor", layout="wide")
st.title("🏺 Archaeological Site Predictor (India)")

# --- Sidebar input ---
st.sidebar.header("Enter Location Details")
latitude = st.sidebar.number_input("Latitude (8–37)", 8.0, 37.0, 26.9124)
longitude = st.sidebar.number_input("Longitude (68–97)", 68.0, 97.0, 75.7873)
elevation = st.sidebar.number_input("Elevation (meters)", 0.0, 3000.0, 431.2)
distance_to_river = st.sidebar.number_input("Distance to River (km)", 0.0, 50.0, 6.5)
vegetation_index = st.sidebar.slider("Vegetation Index (0–1)", 0.0, 1.0, 0.68)
soil_type_encoded = st.sidebar.selectbox(
    "Soil Type",
    options=[0,1,2,3,4],
    format_func=lambda x: {0:"Alluvial",1:"Red",2:"Laterite",3:"Black",4:"Arid"}[x]
)

# --- Prediction button ---
if st.sidebar.button("Predict"):

    # --- Make prediction ---
    sample = np.array([[latitude, longitude, elevation, distance_to_river, vegetation_index, soil_type_encoded]])
    sample_scaled = scaler.transform(sample)
    pred = model.predict(sample_scaled)[0]
    result = "✅ Likely Archaeological Site" if pred==1 else "❌ Not Likely"

    st.subheader("Prediction Result")
    st.write(result)

    # --- Find nearby positive sites ---
    nearby = df[df['is_archaeological_site']==1].copy()
    nearby['distance'] = np.sqrt((nearby['latitude']-latitude)**2 + (nearby['longitude']-longitude)**2)
    nearby = nearby.nsmallest(5, 'distance')

    if not nearby.empty:
        st.subheader("Nearby Positive Sites")
        st.dataframe(nearby[['latitude','longitude','elevation','distance_to_river','vegetation_index','soil_type']])
    else:
        st.write("No nearby positive sites found.")