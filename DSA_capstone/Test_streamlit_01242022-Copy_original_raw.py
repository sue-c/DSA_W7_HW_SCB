


import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

hwdata = pd.read_csv(r"C:\ETSProjects_SCB\UpskillTraining_2022\Week8_10\data_capstone_dsa2021_2022.csv")

st.title('Cho-Baker Streamlit Practice: DSA HW4')

GenderSelect = st.selectbox("Please select gender: ", ['Male', 'Female'])

fig = px.histogram(hwdata.query('gender==@GenderSelect'), x="sum_score", color="gender")

st.plotly_chart(fig)
