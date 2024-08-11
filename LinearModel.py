import streamlit as st
import numpy as np
import pandas as pd
import pickle


pickle_in = open('model.pkl','rb')
lm = pickle.load(pickle_in)

new_data = pd.DataFrame({
    'Ratings': [3.8],
   'RAM': [6],
   'ROM': [32],
    'Mobile_Size': [4.54],
    'Primary_Cam': [25],
   'Selfi_Cam': [12],
    'Battery_Power': [3800]
    })  
  
st.markdown('>Prediction Page')
st.header('Linear Regression')
st.write('Fill the form to use the linear regression model to predict the price of mobile devices')

with st.form("linear_form_input"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider",min_value=0,max_value=5,step=10)
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form") 