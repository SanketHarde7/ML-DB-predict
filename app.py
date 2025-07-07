import streamlit as st
import joblib
import numpy as np
model=joblib.load("diabetes_model.pkl")



st.set_page_config(page_title="DIABETIES PREDICTIOR",layout='centered')
#user inputs
st.markdown("<h1 styles='text-align:center;color:#4CAF50;'>DIABETES PREDIICTION</h1>",unsafe_allow_html=True)
st.markdown("relax this is just minimum levels")
st.sidebar.header("User Input Feature")
preg=st.sidebar.number_input("Pregnancies",min_value=0)
glucose=st.sidebar.number_input("Glucose Level",min_value=50)
bp=st.sidebar.number_input("Blood Pressure",min_value=30)
skin=st.sidebar.number_input("Skin Thickness",min_value=10)
insulin=st.sidebar.number_input("Insulin Level",min_value=15)
bml=st.sidebar.number_input("BMI",min_value=10.0)
dpf=st.sidebar.number_input("Diabetes Pedigree Function",min_value=0.1)
age=st.sidebar.number_input("Age",min_value=5,max_value=100,step=1)

st.sidebar.info("relax this is just minimum levels")
if st.button("Predict"):
    input_data=np.array([[preg,glucose,bp,skin,insulin,bml,dpf,age]])
    
    prediction=model.predict(input_data)

    if prediction[0]==1:
        st.error("you may have diabetes")
    else:
        st.success("you are safe from diabetes")
        
