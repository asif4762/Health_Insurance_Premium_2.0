import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Premium Predictor", layout="centered")
st.title("💼 Health Insurance Premium Predictor")
st.markdown("Predict insurance premium cost based on lifestyle, health, and demographic attributes.")

st.divider()
st.header("🧍 Personal & Demographic Info")

with st.form("insurance_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("🎂 Age", 18, 100, 30)
        gender = st.selectbox("⚥ Gender", ['Female', 'Male'])
        marital_status = st.selectbox("💍 Marital Status", ['Unmarried', 'Married'])
        region = st.selectbox("🌍 Region", ['Southeast', 'Northeast', 'Southwest', 'Northwest'])

    with col2:
        number_of_dependants = st.slider("👨‍👩‍👧‍👦 Number of Dependants", 0, 10, 2)
        employment_status = st.selectbox("💼 Employment Status", ['Self-Employed', 'Freelancer', 'Salaried'])
        income_lakhs = st.slider("💰 Annual Income (Lakhs)", 0.0, 100.0, 10.0)
        income_level = st.selectbox("📊 Income Bracket", ['25L - 40L', '10L - 25L', '<10L', '> 40L'])

    st.divider()
    st.header("🏃 Lifestyle & Health Indicators")

    col3, col4 = st.columns(2)
    with col3:
        physical_activity = st.selectbox("🏋️ Physical Activity", ['Medium', 'Low', 'High'])
        stress_level = st.selectbox("😥 Stress Level", ['Medium', 'High', 'Low'])
        bmi_category = st.selectbox("⚖️ BMI Category", ['Normal', 'Overweight', 'Obesity', 'Underweight'])

    with col4:
        smoking_status = st.selectbox("🚬 Smoking Status", ['No Smoking', 'Occasional', 'Regular'])
        medical_history = st.selectbox("🩺 Medical History", [
            'No Disease',
            'High blood pressure',
            'Thyroid',
            'Diabetes',
            'Heart disease',
            'Diabetes & Thyroid',
            'Diabetes & High blood pressure',
            'Diabetes & Heart disease',
            'High blood pressure & Heart disease'
        ])
        insurance_plan = st.selectbox("📄 Insurance Plan", ['Gold', 'Silver', 'Bronze'])

    submitted = st.form_submit_button("🔍 Predict Insurance Premium")

    if submitted:
        input_data = {
            'age': age,
            'gender': gender,
            'region': region,
            'marital_status': marital_status,
            'number_of_dependants': number_of_dependants,
            'income_lakhs': income_lakhs,
            'income_level': income_level,
            'employment_status': employment_status,
            'physical_activity': physical_activity,
            'stress_level': stress_level,
            'bmi_category': bmi_category,
            'smoking_status': smoking_status,
            'medical_history': medical_history,
            'insurance_plan': insurance_plan
        }

        prediction = predict(input_data)
        st.success(f"💡 **Estimated Insurance Premium:** ₹ {prediction}")
