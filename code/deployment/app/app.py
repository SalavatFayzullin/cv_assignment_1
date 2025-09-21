import streamlit as st
import requests
import json

st.title("Titanic Survival Prediction")

# Input fields
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Female", "Male"])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=30.0)
sibsp = st.number_input("Siblings/Spouses", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=1000.0, value=50.0)
embarked = st.selectbox("Embarked", ["Southampton", "Cherbourg", "Queenstown"])

if st.button("Predict Survival"):
    # Convert inputs
    sex_encoded = 1 if sex == "Male" else 0
    embarked_encoded = {"Southampton": 0, "Cherbourg": 1, "Queenstown": 2}[embarked]
    
    data = {
        "pclass": pclass,
        "sex": sex_encoded,
        "age": age,
        "sibsp": sibsp,
        "parch": parch,
        "fare": fare,
        "embarked": embarked_encoded
    }
    
    try:
        response = requests.post("http://api:8000/predict", json=data)
        result = response.json()
        
        if result["survived"]:
            st.success(f"✅ Survived! (Probability: {result['probability']:.2%})")
        else:
            st.error(f"❌ Did not survive (Probability: {result['probability']:.2%})")
    except:
        st.error("API connection failed")