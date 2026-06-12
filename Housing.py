import streamlit as st
import pandas as pd
import pickle

# Load model
with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load preprocessor
with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

st.title("🏠 House Price Prediction")

# Numerical Inputs
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
stories = st.number_input("Stories", min_value=1, step=1)
parking = st.number_input("Parking Spaces", min_value=0, step=1)

# Categorical Inputs
mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["unfurnished", "semi-furnished", "furnished"]
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    # Transform input
    input_transformed = preprocessor.transform(input_df)

    # Predict
    prediction = model.predict(input_transformed)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.0f}"
    )
    st.balloons()