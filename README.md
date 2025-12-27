# Archaeological-Site-Predictor
This is a Streamlit-based interactive web app that predicts whether a given location in India is likely to be an archaeological site. Users can input location coordinates and environmental features, and the app returns a prediction along with nearby known positive sites.

The prediction is powered by a Random Forest machine learning model trained on simulated archaeological site data for India.

✨ Features

🔹 Predict if a location is a likely archaeological site

🔹 Show up to 5 nearby positive sites with coordinates and features

🔹 Simple one-page interface using Streamlit

🔹 Fully interactive and easy to use

🔹 Handles missing nearby sites gracefully

🔹 Lightweight (no maps required)

🛠 Requirements

Python 3.8+

Streamlit

Pandas

Numpy

Joblib

Optional (for future map integration):

Folium 🌍

streamlit-folium 🗺️

⚡ Install Dependencies pip install streamlit pandas numpy joblib

Or with requirements.txt:

pip install -r requirements.txt

📂 Files File Description app.py Streamlit application script 🖥️ archaeo_rf_model.pkl Trained Random Forest model 🤖 archaeo_scaler.pkl StandardScaler for feature scaling 📊 india_archaeo_dataset_500.csv Sample dataset used for nearby site suggestions 🗺️

🚀 How to Run

Navigate to the folder containing all files:

cd path/to/archaeo_app

Run the Streamlit app:

streamlit run app.py

A browser window will open. Use the sidebar to input the location and features.

Click Predict to see:

✅ Prediction result: Likely / Not Likely Archaeological Site

📋 Table of nearby positive sites (if any)

📝 Example Usage

Latitude: 26.9124 📍

Longitude: 75.7873 📍

Elevation: 431.2 m ⛰️

Distance to River: 6.5 km 🌊

Vegetation Index: 0.68 🌿

Soil Type: Alluvial 🌱

Click Predict → Result: ✅ Likely Archaeological Site Nearby positive sites table shows the closest 5 positive sites.

🌱 Future Enhancements

Automatically infer missing features (elevation, vegetation index, etc.) from coordinates

Add interactive map visualization of input and nearby sites 🗺️

Deploy online using Streamlit Cloud ☁️

Improve model using real archaeological datasets 📚
