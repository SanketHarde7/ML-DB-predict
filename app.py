import streamlit as st
import joblib
import numpy as np
model=joblib.load("diabetes_model.pkl")



st.set_page_config(page_title="DIABETIES PREDICTIOR",layout='centered')
#user inputs
st.markdown("<h1 styles='text-align:center;color:#4CAF50;'>DIABETES PREDIICTION</h1>",unsafe_allow_html=True)
preg=st.number_input("Pregnancies",min_value=0)
glucose=st.number_input("Glucose Level",min_value=0)
bp=st.number_input("Blood Pressure",min_value=0)
skin=st.number_input("Skin Thickness",min_value=0)
insulin=st.number_input("Insulin Level",min_value=0)
bml=st.number_input("BMI",min_value=0.0)
dpf=st.number_input("Diabetes Pedigree Function",min_value=0.0)
age=st.number_input("Age",min_value=1,max_value=100,step=1)

if st.button("Predict"):
    input_data=np.array([[preg,glucose,bp,skin,insulin,bml,dpf,age]])
    
    prediction=model.predict(input_data)

    if prediction[0]==1:
        st.error("you may have diabetes")
    else:
        st.success("you are safe from diabetes")
        
