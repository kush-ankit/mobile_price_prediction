import streamlit as st
import numpy as np
import pandas as pd

about = st.Page("About.py", title="About Project", icon=":material/science:")
docs = st.Page("Documentation.py", title="Documentation", icon=":material/delete:")
linear = st.Page("LinearModel.py", title="LinearRegression Model", icon=":material/delete:")
random = st.Page("RandomForest.py", title="RandomForestRegressor Model", icon=":material/delete:")

pg = st.navigation([about, docs,linear, random])
st.set_page_config(page_title="ML Models")
pg.run()

# st.sidebar.title("Dashboard")
# app_mode = st.sidebar.selectbox("Select Page",["About Project","Documentation","Prediction"])
# st.sidebar.divider()
