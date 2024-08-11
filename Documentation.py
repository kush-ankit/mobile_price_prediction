import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.markdown('>Documentation')
st.header('Introduction of Machine Learning Models')
st.sidebar.markdown('Introduction')
st.write('')
st.markdown('#### What is a Machine Learning Model?')
st.write('A machine learning model is a mathematical framework or algorithm designed to learn from data and make predictions or decisions based on that data. Instead of being explicitly programmed with specific instructions for every task, the model learns patterns and relationships from examples.')
st.write('')
st.markdown('##### How Does It Work?')
st.markdown('''
            1. Data Collection:
                - The process begins with gathering relevant data. This data could be anything from images and text to numerical values and sensor readings.
            
            2. Data Preparation:
                - The collected data often requires cleaning and preprocessing. This step might include handling missing values, normalizing or scaling features, and encoding categorical variables.
            3. Choosing a Model:
                - There are various types of machine learning models, each suited to different types of tasks. Common types include:
                    - Regression Models (predict numerical values, e.g., predicting house prices).
                    - Classification Models (categorize data into classes, e.g., spam vs. non-spam emails).
                    - Clustering Models (group similar data points, e.g., customer segmentation).
                    - Recommendation Models (suggest items, e.g., movie recommendations).
            4. Training the Model:
                - During training, the model learns from the data by finding patterns and relationships. It uses algorithms to adjust its parameters in order to minimize errors in its predictions. This involves using a training dataset, which includes input features and known output labels.
            5. Evaluation:
                - After training, the model’s performance is evaluated using a separate dataset (validation or test set) that it hasn’t seen before. Metrics like accuracy, precision, recall, or mean squared error are used to assess how well the model performs.
            6. Hyperparameter Tuning:
                - Models often have hyperparameters (settings that control the training process) that need to be tuned to improve performance. This might involve techniques like grid search or random search.
            7. Making Predictions:
                - Once the model is trained and evaluated, it can be used to make predictions on new, unseen data. For example, a trained image classification model can predict the category of new images.
            8. Deployment:
                - The final step is deploying the model into a production environment where it can interact with real-world data and provide value, such as making real-time recommendations or automating decisions.
            ''')
st.markdown('#### Key Concepts:')
st.markdown('''
                - **Features**: The input variables or attributes used by the model to make predictions.
                - **Labels**: The output or target variable the model is trying to predict or classify.
                - **Loss Function**: A measure of how well the model’s predictions match the actual results. The goal is to minimize this loss.
                - **Optimization Algorithm**: Techniques used to adjust the model’s parameters to reduce the loss function (e.g., gradient descent).
                - Machine learning models are powerful tools used across various domains, from finance and healthcare to entertainment and autonomous vehicles. The process involves iterating and refining models to achieve the best possible performance for specific tasks.
            ''')


st.write('')
st.sidebar.markdown(' Linear Regression')
st.sidebar.markdown('- Simple Linear Regression')
st.sidebar.markdown('- Multple Linear Regression')
st.subheader('What is Linear Regression?')
st.write('Linear regression predicts the relationship between two variables by assuming they have a straight-line connection. It finds the best line that minimizes the differences between predicted and actual values. Used in fields like economics and finance, it helps analyze and forecast data trends. Linear regression can also involve several variables (multiple linear regression) or be adapted for yes/no questions (logistic regression).')
st.markdown('#### Simple Linear Regression')
st.write('In a simple linear regression, there is one independent variable and one dependent variable. The model estimates the slope and intercept of the line of best fit, which represents the relationship between the variables. The slope represents the change in the dependent variable for each unit change in the independent variable, while the intercept represents the predicted value of the dependent variable when the independent variable is zero.')
st.markdown('##### **Y i =  β 0 + β 1 X i**')
st.write('where Y i  = Dependent variable,  β 0  = constant/Intercept, β 1  = Slope/Intercept, X i  = Independent variable.')
st.image('375512.jpg')
st.write('')
st.subheader('Multiple Linear Regression')
st.write('Multiple linear regression is a technique to understand the relationship between a single dependent variable and multiple independent variables.')
st.write('The formulation for multiple linear regression is also similar to simple linear regression with the small change that instead of having one beta variable, you will now have betas for all the variables used.')
st.write('The formula is given as:')
st.markdown('#### **Y = B0 + B1X1 + B2X2 + … + BpXp + ε**')
st.write('')
st.sidebar.markdown('Random Forest')
st.header('Random forest')
st.subheader('What is Random forest?')
st.write('Random forest, a popular machine learning algorithm developed by Leo Breiman and Adele Cutler, merges the outputs of numerous decision trees to produce a single outcome. Its popularity stems from its user-friendliness and versatility, making it suitable for both classification and regression tasks.')
st.subheader('Real-Life Analogy of Random Forest')
st.sidebar.markdown('- Bagging')
st.sidebar.markdown('- Boosting')
st.image('Artboard.jpg')
st.subheader('Working of Random Forest Algorithm')
st.image('Art.jpg')
st.subheader('Steps Involved in Random Forest Algorithm')
st.markdown('''
            - **Step 1**: In the Random forest model, a subset of data points and a subset of features is selected for constructing each decision tree. Simply put, n random records and m features are taken from the data set having k number of records.
            - **Step 2**: Individual decision trees are constructed for each sample.
            - **Step 3**: Each decision tree will generate an output.
            - **Step 4**: Final output is considered based on Majority Voting or Averaging for Classification and regression, respectively.
            ''')
st.image('rmf.jpg')