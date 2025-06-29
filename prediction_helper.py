import pandas as pd
from joblib import load

# Load model and scaler
model = load('artifacts/model.joblib')
scaler_model = load('artifacts/scaler.joblib')

# Risk score calculation based on disease history
def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    diseases = medical_history.lower().split(' & ')
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)
    max_score = 14
    normalized_risk = (total_risk_score - 0) / (max_score - 0)
    return normalized_risk

# Lifestyle risk calculation
def calculate_normalized_life_style_risk(physical_activity, stress_level):
    physical_activity_score = {'High': 0, 'Medium': 1, 'Low': 4}
    stress_level_score = {'High': 4, 'Medium': 1, 'Low': 0}
    total_sum = physical_activity_score.get(physical_activity, 0) + stress_level_score.get(stress_level, 0)
    max_score = 8
    normalized_life_style_risk = (total_sum - 0) / (max_score - 0)
    return normalized_life_style_risk

# Prepare input for model
def preprocess_input(input_data):
    expected_cols = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
        'normalized_total_risk_score', 'normalized_total_life_style_score',
        'gender_Male', 'region_Northwest', 'region_Southeast',
        'region_Southwest', 'marital_status_Unmarried', 'bmi_category_Obesity',
        'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    df = pd.DataFrame(0, columns=expected_cols, index=[0])
    df['income_level'] = 0
    for key, value in input_data.items():
        if key == 'age':
            df['age'] = value
        elif key == 'number_of_dependants':
            df['number_of_dependants'] = value
        elif key == 'income_lakhs':
            df['income_lakhs'] = value
        elif key == 'insurance_plan':
            df['insurance_plan'] = insurance_plan_encoding.get(value, 1)
        elif key == 'gender' and value == 'Male':
            df['gender_Male'] = 1
        elif key == 'region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1
        elif key == 'marital_status' and value == 'Unmarried':
            df['marital_status_Unmarried'] = 1
        elif key == 'bmi_category':
            if value == 'Obesity':
                df['bmi_category_Obesity'] = 1
            elif value == 'Underweight':
                df['bmi_category_Underweight'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
        elif key == 'smoking_status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1
        elif key == 'employment_status':
            if value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1
            elif value == 'Salaried':
                df['employment_status_Salaried'] = 1

    # Calculate normalized scores
    df['normalized_total_risk_score'] = calculate_normalized_risk(input_data['medical_history'])
    df['normalized_total_life_style_score'] = calculate_normalized_life_style_risk(
        input_data['physical_activity'], input_data['stress_level']
    )

    # Apply scaling
    df = handle_scaling(df)

    return df

# Apply scaler
def handle_scaling(df):
    scaler_object = scaler_model
    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    return df

# Predict using model
def predict(input_data):
    input_df = preprocess_input(input_data)
    prediction = model.predict(input_df.drop('income_level',axis=1))
    return int(prediction)
