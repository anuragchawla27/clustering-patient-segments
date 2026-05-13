import streamlit as st
import joblib
import numpy as np

# Load model and scaler
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

# Cluster names
cluster_names = {
    0: "Low-Risk Male Group",
    1: "Obesity-Associated Mild Distress",
    2: "Moderate Anxiety-Depression with Sleep Issues",
    3: "Older Adult Mild Distress Group",
    4: "High-Risk Severe Anxiety & Depression",
    5: "Low-Risk Healthy Female Group"
}

# App title
st.title("Mental Health Patient Segmentation System")

st.write("Enter patient details below:")

# Inputs
phq = st.slider("PHQ Score", 0, 27, 5)

gad = st.slider("GAD Score", 0, 21, 5)

age = st.number_input("Age", 15, 100, 20)

bmi = st.number_input("BMI", 10.0, 50.0, 22.0)

epworth = st.slider("Epworth Sleepiness Score", 0, 24, 5)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

# Encode gender
gender_value = 0 if gender == "Female" else 1

# Predict button
if st.button("Predict Cluster"):

    input_data = np.array([
        [phq, gad, age, bmi, epworth, gender_value]
    ])

    scaled_input = scaler.transform(input_data)

    cluster = kmeans.predict(scaled_input)[0]

    profile = cluster_names[cluster]

    st.success(f"Predicted Cluster: {cluster}")

    st.info(f"Patient Profile: {profile}")
    
 