import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plost


st.write(""""  
# Air Quality Web Appssss
#### This app provides air quality Analysis at 5 city in China
In addition to the basic Air Quality Index, the application provides the dataset concentration of polluting gases, such as Carbon monoxide (CO), Nitrogen dixide (NO2), Ozone (O3), Sulphur dioxide (SO2), Ammonia (NH3), and particulates (PM2.5 and PM10). 
 """)

  

add_selectcity = st.sidebar.selectbox(
    "Please choose the city",
    ('Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan')
)

all_df = pd.read_csv('../dashboard/data_concat.csv')

st.write("Maximal Value each city")
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
st.write('Average over the past 3 years')
col6, col7, col8, col9, col10 = st.columns([1,1,1,1,1])






max_temp1 = all_df.CO.max()
max_temp2 = all_df.NO2.max()
max_temp3 = all_df.O3.max()
max_temp4 = all_df.SO2.max()
max_temp5 = all_df.TEMP.max()


with col1:
    st.metric("Carbon Monoxide ", value=max_temp1)
with col2:
    st.metric("Nitrogen Dixide", value=max_temp2)
with col3:
    st.metric("Ozone", value=max_temp3)
with col4:
    st.metric("Sulphur Dioxide", value=max_temp4)
with col5:
    st.metric("Temperature", value=max_temp5 )




station = pd.DataFrame(
   {
       "Station": all_df['station'],
       "CO": all_df['CO'],
       "NO2": all_df['NO2'],
       "O3": all_df['O3'],
       "SO2": all_df['SO2'],
       "TEMP": all_df['TEMP'],
   }
)
station2 = pd.DataFrame(
   {
       "Station": all_df['station'],
       "CO": all_df['CO'],
       "NO2": all_df['NO2'],
       "O3": all_df['O3'],
       "SO2": all_df['SO2'],
       "TEMP": all_df['TEMP'],
   }
)

st.bar_chart(station, x="Station", y=["CO", "NO2", "O3", "SO2", "TEMP" ], color=["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"] )



mean_temp1 = all_df.CO.mean()
mean_temp2 = all_df.NO2.mean()
mean_temp3 = all_df.O3.mean()
mean_temp4 = all_df.SO2.mean()
mean_temp5 = all_df.TEMP.mean()

with col6:
    st.metric("Carbon Monoxide ", value=mean_temp1)
with col7:
    st.metric("Nitrogen Dixide", value=mean_temp2)
with col8:
    st.metric("Ozone", value=mean_temp3)
with col9:
    st.metric("Sulphur Dioxide", value=mean_temp4)
with col10:
    st.metric("Temperature", value=mean_temp5 )
