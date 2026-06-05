import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

from analysis import load_data

traffic, traffic2 = load_data()

st.title("🔮 Traffic Forecasting")

numeric_cols = traffic.select_dtypes(include='number')

column = st.selectbox(
    "Select Column",
    numeric_cols.columns
)

data = traffic[column].dropna()

X = [[i] for i in range(len(data))]
y = data.values

model = LinearRegression()
model.fit(X, y)

future = [[i] for i in range(len(data)+20)]

pred = model.predict(future)

fig = go.Figure()

fig.add_scatter(
    y=y,
    mode="lines",
    name="Actual"
)

fig.add_scatter(
    y=pred,
    mode="lines",
    name="Forecast"
)

st.plotly_chart(fig, use_container_width=True)
