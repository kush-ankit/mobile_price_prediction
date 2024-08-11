import streamlit as st
import numpy as np
import pandas as pd
import pickle
import seaborn as sns


st.markdown('>About Project')
st.header("MOBILE PRICE PREDICTION")
st.markdown('This article was published as a project introduction.')
st.image('img.jpg')
st.subheader('Introduction')
st.sidebar.markdown('- Introduction')
st.write('Mobile phones come in all sorts of prices, features, specifications and all. Price estimation and prediction is an important part of consumer strategy. Deciding on the correct price of a product is very important for the market success of a product. A new product that has to be launched, must have the correct price so that consumers find it appropriate to buy the product.')
st.write('')
st.sidebar.markdown('- The Problem')
st.subheader('The Problem')
st.write('The data contains information regarding mobile phone features, specifications etc and their price range. The various features and information can be used to predict the price range of a mobile phone.')
lst = ['Battery Power in mAh', 'Has BlueTooth or not', 'Microprocessor clock speed','The phone has dual sim support or not','Front Camera Megapixels','Has 4G support or not','Internal Memory in GigaBytes','Mobile Depth in Cm','Weight of Mobile Phone','Number of cores in the processor','Primary Camera Megapixels','Pixel Resolution height','Pixel resolution width','RAM in MB','Mobile screen height in cm','Mobile screen width in cm','Longest time after a single charge','3g or not','Has touch screen or not','Has wifi or not']
for i in lst:
    st.markdown(' - '+ i)
st.sidebar.markdown('- Methodology')
st.subheader('Methodology')
st.write('We will proceed with reading the data, and then perform data analysis. The practice of examining data using analytical or statistical methods in order to identify meaningful information is known as data analysis. After data analysis, we will find out the data distribution and data types. We will train 4 classification algorithms to predict the output. We will also compare the outputs. Let us get started with the project implementation.')
st.write('')
st.sidebar.markdown('- About Dataset')
st.subheader('About Dataset')
st.markdown('''
            The columns available in the dataset are:
            - **Ratings**: This field contains the various rating given by customers
            - **Ram**: This field contain the Ram capacity of the phone in GB
            - **ROM**: This is field contains the number of space available in the phone in GB
            - **Mobile_Size**: This is the int size of the screen
            - **Primary_Cam**: This is the number of pixels of the Back camera
            - **Selfi_Cam**: The number of Pixels of the front camera
            - **Battery_Power**: The battery power
            - **Price**: The price of the mobile phone
            ''')

df = pd.read_csv('Mobile-Price-Prediction-cleaned_data.csv')
st.dataframe(df)

st.subheader('Price')
st.scatter_chart(data=df['Price'])

st.subheader('RAM')
st.scatter_chart(data=df['RAM'])

st.subheader('ROM')
st.scatter_chart(data=df['ROM'])

st.subheader('Mobile_Size')
st.scatter_chart(data=df['Mobile_Size'])

st.subheader('Primary_Cam')
st.scatter_chart(data=df['Primary_Cam'])

st.subheader('Selfi_Cam')
st.scatter_chart(data=df['Selfi_Cam'])

st.subheader('Battery_Power')
st.scatter_chart(data=df['Battery_Power'])