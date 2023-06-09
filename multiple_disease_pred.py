import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('trained_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinson_model = pickle.load(open('parkinson.sav','rb'))
breast_cancer_model = pickle.load(open('breast_cancer.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                            icons=['activity','heart','person'],
                            default_index=0) # the page which is selected
    
# Diabetes prediction page

if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction')

    st.write('This is the Diabetes Prediction page')
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col2:
        Insulin = st.number_input('Insulin', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col3:
        BMI = st.number_input('BMI', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=200.0, step=1.0, value=0.0)
    with col2:
        Age = st.number_input('Age', min_value=1.0, max_value=200.0, step=1.0, value=1.0)

                 
    # code for prediction
    diab_diagnosis = ''

    # creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if(diab_diagnosis[0] == 0):
            diab_diagnosis ='The patient is NOT diabetes patient'
        else:
            diab_diagnosis ='The patient IS diabetes patient'
    st.success(diab_diagnosis)
        

    
        
    



if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    st.write('This is the Heart Disease Prediction page')
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        age = st.number_input('Age', min_value=0, max_value=200, step=1, value=0)
    with col2:
        #sex = st.selectbox('Sex', ('Male', 'Female'))  1 =male
        sex = st.number_input('Sex', min_value=0, max_value=1, step=1, value=0)
    with col3:
        #cp = st.selectbox('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
        cp = st.number_input('Chest Pain Type', min_value=0, max_value=3, step=1, value=0)
    with col4:
        trestbps = st.number_input('Resting Blood Pressure', min_value=90, max_value=210, step=1, value=90)
    with col1:
        chol = st.number_input('Cholesterol', min_value=120, max_value=600, step=1, value=120)
    with col2:
        # fbs = st.selectbox('Fasting Blood Sugar', ('True', 'False'))  0 false
        fbs = st.number_input('Fasting Blood Sugar', min_value=0, max_value=1, step=1, value=0)

    with col3:
        #restecg = st.selectbox('Resting ECG', ('Normal', 'ST-T wave Abnormality', 'Left Ventricular Hypertrophy'))
        restecg = st.number_input('Resting ECG', min_value=0, max_value=2, step=1, value=0)
    with col4:
        thalach = st.number_input('Maximum Heart Rate', min_value=65, max_value=250, step=1, value=65)
    with col1:
        #exang = st.selectbox('Exercise Induced Angina', ('Yes', 'No')) # 1 =yes
        exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1, value=0)
    with col2:
        oldpeak = st.number_input('ST Depression induced by exercise', min_value=0.0, max_value=7.0, step=0.1, value=0.0)
    with col3:
        #slope = st.selectbox('ST Slope', ('Upsloping', 'Flat', 'Downsloping'))
        slope = st.number_input('ST Slope', min_value=0, max_value=2, step=1, value=0)
    with col4:
        #ca = st.selectbox('Number of Major Vessels', ('0', '1', '2', '3','4'))
        ca = st.number_input('Number of Major Vessels', min_value=0, max_value=4, step=1, value=0)
    with col1:
        #thal = st.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversable Defect')) # 1 = normal, 2 = fixed
        thal = st.number_input('Thalassemia', min_value=1, max_value=3, step=1, value=1)
    
    # code for prediction
    heart_diagnosis = ''

    # creating button for prediction
    if st.button('Predict'):
        heart_diagnosis = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heart_diagnosis[0] == 0):
            heart_diagnosis ='The person is NOT heart disease patient'
        else:
            heart_diagnosis ='The person IS heart disease patient'
    st.success(heart_diagnosis)

    
    
    
        

if(selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction')
    


if(selected == 'Breast Cancer Prediction'):
    st.title('Breast Cancer Prediction')
    st.write('This is the Breast Cancer Prediction Page')
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:  
        radius_mean = st.number_input('Radius Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        texture_mean = st.number_input('Texture Mean', min_value=0.0, max_value=40.0, step=0.1, value=0.0)
    with col3:
        perimeter_mean = st.number_input('Perimeter Mean', min_value=0.0, max_value=200.0, step=0.1, value=0.0)
    with col4:
        area_mean = st.number_input('Area Mean', min_value=0.0, max_value=2600.0, step=0.1, value=0.0)
    with col5:
        smoothness_mean = st.number_input('Smoothness Mean', min_value=0.0, max_value=0.20, step=0.01, value=0.0)
    with col1:
        compactness_mean = st.number_input('Compactness Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        concavity_mean = st.number_input('Concavity Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col3:
        concave_points_mean = st.number_input('Concave Points Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col4:
        symmetry_mean = st.number_input('Symmetry Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col5:
        fractal_dimension_mean = st.number_input('Fractal Dimension Mean', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col1:
        radius_se = st.number_input('Radius SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        texture_se = st.number_input('Texture SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col3:
        perimeter_se = st.number_input('Perimeter SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col4:
        area_se = st.number_input('Area SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col5:
        smoothness_se = st.number_input('Smoothness SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col1:
        compactness_se = st.number_input('Compactness SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        concavity_se = st.number_input('Concavity SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col3:
        concave_points_se = st.number_input('Concave Points SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col4:
        symmetry_se = st.number_input('Symmetry SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col5:
        fractal_dimension_se = st.number_input('Fractal Dimension SE', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col1:
        radius_worst = st.number_input('Radius Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        texture_worst = st.number_input('Texture Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col3:
        perimeter_worst = st.number_input('Perimeter Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col4:
        area_worst = st.number_input('Area Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col5:
        smoothness_worst = st.number_input('Smoothness Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col1:
        compactness_worst = st.number_input('Compactness Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col2:
        concavity_worst = st.number_input('Concavity Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col3:
        concave_points_worst = st.number_input('Concave Points Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col4:
        symmetry_worst = st.number_input('Symmetry Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col5:
        fractal_dimension_worst = st.number_input('Fractal Dimension Worst', min_value=0.0, max_value=30.0, step=0.1, value=0.0)
    with col1:
        #diagnosis = st.selectbox('Diagnosis', ('Malignant', 'Benign'))
        diagnosis = st.number_input('Diagnosis', min_value=0, max_value=1, step=1, value=0)
   
    # code for prediction
    breast_cancer_diagnosis = ''

    # creating button for prediction
    if st.button('Predict'):
        breast_cancer_diagnosis = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])

        if(breast_cancer_diagnosis[0] == 0):
            breast_cancer_diagnosis ='The person is NOT breast cancer patient'
        else:
            breast_cancer_diagnosis ='The person IS breast cancer patient'

    st.success(breast_cancer_diagnosis)
   




     
    
