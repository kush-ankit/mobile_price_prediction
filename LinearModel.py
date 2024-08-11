import streamlit as st
import numpy as np
import pandas as pd
import pickle


pickle_in = open('model.pkl','rb')
lm = pickle.load(pickle_in)

st.markdown('>LinearRegression Model')
st.header('Linear Regression')
st.write('Fill the form to use the linear regression model to predict the price of mobile devices')
st.sidebar.markdown('Linear Regresssion Model')

with st.form("linear_form_input"):
    st.write('fill the specifiction of the mobile device')
    rating = st.slider("Rating",min_value=0,max_value=5)
    ram = st.selectbox('RAM in GB', [2,4,6,8,12])
    rom = st.selectbox('ROM in GB', [8,16,32,64,128,256])
    size = st.slider('Screen size', min_value=2.0,max_value=7.0)
    pcam = st.slider('Primary camera in pixels', min_value=5,max_value=64)
    scam = st.slider('Secondary camera in pixels', min_value=1, max_value=23)
    battery = st.number_input('Battery in mAh',min_value=500, max_value=6000)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(rating, ram, rom, size, pcam, scam, battery)
        st.write('The predicted price is:' , lm.predict(pd.DataFrame({'Ratings': [rating], 'RAM': [ram], 'ROM': [rom], 'Mobile_Size': [size], 'Primary_Cam': [pcam], 'Selfi_Cam': [scam], 'Battery_Power': [battery]}))[0])

    