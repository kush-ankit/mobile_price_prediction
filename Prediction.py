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
st.write(lm.predict(new_data))
    