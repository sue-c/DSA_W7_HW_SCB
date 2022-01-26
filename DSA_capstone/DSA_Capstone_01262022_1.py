import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

hwdata = pd.read_csv("DSA_capstone/data_capstone_dsa2021_2022.csv")

st.title('Sugene Cho-Baker: Data Science Academy Capstone')

hwdata["OneValues"]=1
hwdata["home_computer2"] = hwdata.loc[:, 'home_computer']
hwdata["home_computer2"] = hwdata.loc[:, 'home_computer'].replace("Yes", "At Home")
hwdata["home_computer2"] = hwdata.loc[:, 'home_computer'].replace("No", "On site")

genderlist = hwdata.loc[:, 'gender'].tolist()
onevaluelist =hwdata.loc[:, 'OneValues'].tolist()
testsitelist =hwdata.loc[:, 'home_computer'].tolist()
testsitelist2 =hwdata.loc[:, 'home_computer2'].tolist()
agelist =hwdata.loc[:, 'age'].tolist()
rttotallist =hwdata.loc[:, 'rt_total'].tolist()
sumscorelist =hwdata.loc[:, 'sum_score'].tolist()

st.header("Data")

hwdata.loc[:, ('rt_total', "sum_score", "gender", "age", "home_computer2")]

st.header("Descriptive Statistics")

specs1 = [[{'type':'domain'}, {'type':'domain'}]]
fig1 = make_subplots(rows=1, cols=2 , specs=specs1, subplot_titles=['Porportion of Gender', 'Porportion of Test Site'])
fig1.add_trace(go.Pie(labels=genderlist, values=onevaluelist),
    row=1, col=1)
fig1.add_trace(go.Pie(labels=testsitelist2, values=onevaluelist),
    row=1, col=2)
fig1.update_layout(title_text='Figure1. Sample Characteristics')
st.plotly_chart(fig1)

specs2 = [[{'type':'xy'}, {'type':'xy'}]]
fig2 = make_subplots(rows=1, cols=2, specs=specs2, subplot_titles=['Histogram of Age - count', 'Histogram of Age - porportion'])
fig2.add_trace(go.Histogram(x=agelist),
               row=1, col=1)
fig2.add_trace(go.Histogram(x=agelist, histnorm='probability'),
               row=1, col=2)
st.plotly_chart(fig2)

fig3 = make_subplots(rows=1, cols=2, subplot_titles=['Histogram of Rt Total', 'Histogram of Sum Scores'])
fig3.add_trace(go.Histogram(x=rttotallist),
               row=1, col=1)
fig3.add_trace(go.Histogram(x=sumscorelist),
               row=1, col=2)
fig3.update_layout(title_text='Figure2. Test Results')
fig3.show()
st.plotly_chart(fig3)

st.header("Distribution of Sum Scores accross Gender, Test Site, Age, and Rt Total")

st.subheader("Figure 3. Distribution of Sum Scores by Gender")

fig4=px.histogram(hwdata, x="sum_score", color="gender")
st.plotly_chart(fig4)

st.subheader("Figure 4. Distribution of Sum Scores by Test Site")

fig5=px.histogram(hwdata, x="sum_score", color="home_computer2")
st.plotly_chart(fig5)

st.subheader("Figure 5. Scatter plots between age and test outcomes")

fig6=px.scatter_matrix(hwdata, dimensions=["age", "rt_total", "sum_score"])
st.plotly_chart(fig6)

st.header("Associations between Rt Total and Sum Score buy Gender, Test Site, and Age")

st.subheader("Figure 6. Scatter plots between Rt Total and Sum Score buy Gender and Test Site")

ModeratorSelect = st.selectbox("Please select moderator variable: ", ["gender", "home_computer2"])

fig9 = px.scatter(hwdata, x="rt_total", y= "sum_score", trendline="ols", color=ModeratorSelect)
st.plotly_chart(fig9)

st.subheader("Figure 7. Scatter plots between Rt Total and Sum Score buy Age")

fig10=px.scatter(hwdata.sort_values('age'), x="rt_total", y= "sum_score", trendline="ols", animation_frame="age")

st.plotly_chart(fig10)
