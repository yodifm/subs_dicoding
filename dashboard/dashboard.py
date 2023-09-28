import streamlit as st
import pandas as pd
import numpy as np
import pickle
 
st.write("""" 
# Udara Terpanas dan paling kotor
         
 """)

st.sidebar.header('Data From asdada')

st.sidebar.markdown("""
[Example CSV input]('../dashboard/all-data.csv')            
""")

uploaded_file = st.sidebar.file_uploader("upload your data")
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        city = st.sidebar.selectbox('City', ('Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan'))
        temp = st.sidebar.selectbox('Tempherature', ('Cold', 'Hot', 'Warm'))
