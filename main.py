import streamlit as st
import numpy as np
import pandas as pd
import pickle


about = st.Page("About.py", title="About", icon=":material/science:")
docs = st.Page("Documentation.py", title="Docs", icon=":material/delete:")
pred = st.Page("Prediction.py", title="", icon=":material/delete:")
docs = st.Page("Documentation.py", title="Docs", icon=":material/delete:")

pg = st.navigation([about, docs])
st.set_page_config(page_title="ML Models")
pg.run()

# st.sidebar.title("Dashboard")
# app_mode = st.sidebar.selectbox("Select Page",["About Project","Documentation","Prediction"])
# st.sidebar.divider()
