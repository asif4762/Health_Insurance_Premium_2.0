import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")
st.title("💡 Insurance Premium Predictor")

st.header("📝 Enter Customer Information")

# Categorical options
gender_options = ['Female', 'Male']
region_options = ['Southeast', 'Northeast', 'Southwest', 'Northwest']
marital_options = ['Unmarried', 'Married']
activity_options = ['Medium', 'Low', 'High']
stress_options = ['Medium', 'High', 'Low']
bmi_options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
smoking_options = ['No Smoking', 'Occasional', 'Regular']
employment_options = ['Self-Employed', 'Freelancer', 'Salaried']
income_options = ['25L - 40L', '10L - 25L', '<10L', '> 40L']
medical_options = [
    'High blood pressure',
    'No Disease',
    'Thyroid',
    'High blood pressure & Heart disease',
    'Diabetes & Thyroid',
    'Diabetes',
    'Heart disease',
    'Diabetes & High blood pressure',
    'Diabetes & Heart disease'
]
insurance_options = ['Gold', 'Silver', 'Bronze']

# Collecting inputs
input_data = {}

# Numerical inputs
input_data['age'] = st.slider("Age", 18, 100, 30)
input_data['number_of_dependants'] = st.slider("Number of Dependants", 0, 10, 2)
input_data['income_lakhs'] = st.slider("Annual Income (Lakhs)", 0.0, 100.0, 10.0)

# Categorical inputs
input_data['gender'] = st.selectbox("Gender", gender_options)
input_data['region'] = st.selectbox("Region", region_options)
input_data['marital_status'] = st.selectbox("Marital Status", marital_options)
input_data['physical_activity'] = st.selectbox("Physical Activity", activity_options)
input_data['stress_level'] = st.selectbox("Stress Level", stress_options)
input_data['bmi_category'] = st.selectbox("BMI Category", bmi_options)
input_data['smoking_status'] = st.selectbox("Smoking Status", smoking_options)
input_data['employment_status'] = st.selectbox("Employment Status", employment_options)
input_data['income_level'] = st.selectbox("Income Level", income_options)
input_data['medical_history'] = st.selectbox("Medical History", medical_options)
input_data['insurance_plan'] = st.selectbox("Insurance Plan", insurance_options)

# On predict
if st.button("🎯 Predict"):
    prediction = predict(input_data)
    st.success(f'Predicted Insurance Premium: {prediction}')