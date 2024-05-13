import pickle
import streamlit as st
from streamlit_option_menu  import option_menu

# Load model
with open("./savemodels/Diabetes.sav", 'rb') as file:
    dia_model = pickle.load(file)
with open("./savemodels/Heart.sav", 'rb') as file:
    heart_model = pickle.load(file)



# sidebar for navigation

with st.sidebar:
    selected = st.radio("Go to", ["Home", "Diabetes", "Heart Disease",])
    

if selected == "Home":
    st.title("Home")
    st.write("Welcome to Disease Prediction App")
    st.write("Please select a disease from the sidebar to predict")
elif selected == "Diabetes":
    st.title("Diabetes Prediction")
    
    # getting the input from the user
    col1, col2 , col3 = st.columns(3)
    
    with col1:
        preg = st.text_input('Number of Pregnancies')
        
    with col2:
        glucose = st.text_input('Glucose Level')
    
    with col3:
        bp = st.text_input('Blood Pressure')
        
    with col1:
        skin = st.text_input('Skin Thickness')
        
    with col2:
        insulin = st.text_input('Insulin')
    
    with col3:
        bmi = st.text_input('BMI')
        
    with col1:
        dpf = st.text_input('Diabetes Pedigree Function')
        
    
    with col2:
        age = st.text_input('Age')
        
    
    # code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button("Diabetic test result"):
        dia_pred = dia_model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    
        if dia_pred[0] == 1:
            diab_diagnosis = "Diabetic"
        
        else:
            diab_diagnosis = "Not Diabetic"
    
    st.success(f"The patient is {diab_diagnosis}")

elif selected == "Heart Disease":
    st.title("Heart Disease Prediction")
    # column creation in the streamlit
    col1, col2 , col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    
    with col2:
        sex = st.selectbox('Sex', ('Male','Female'))
        
    with col3:
        cp = st.selectbox('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Cholestrol Level')
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar', ('>120 mg/dl', '<120 mg/dl'))
    
    with col1:
        restecg = st.selectbox('Resting ECG', ('Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'))
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate')
    
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ('Yes', 'No'))
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
        
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ('Upsloping', 'Flat', 'Downsloping'))
    
    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', ('0', '1', '2', '3'))
    
    with col1:
        thal = st.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversable Defect'))
    
    # code for prediction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button("Heart Disease test result"):
        sex = 0 if sex == 'Male' else 1
        cp = 0 if cp == 'Typical Angina' else (1 if cp == 'Atypical Angina' else (2 if cp == 'Non-anginal Pain' else 3))
        fbs = 0 if fbs == '>120 mg/dl' else 1
        restecg = 0 if restecg == 'Normal' else (1 if restecg == 'ST-T wave abnormality' else 2)
        exang = 1 if exang == 'Yes' else 0
        slope = 0 if slope == 'Upsloping' else (1 if slope == 'Flat' else 2)
        thal = 0 if thal == 'Normal' else (1 if thal == 'Fixed Defect' else 2)
        
        heart_pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if heart_pred[0] == 1:
            heart_diagnosis = "Heart Disease"
        
        else:
            heart_diagnosis = "No Heart Disease"
    
    st.success(f"The patient has {heart_diagnosis}")

    
        
    