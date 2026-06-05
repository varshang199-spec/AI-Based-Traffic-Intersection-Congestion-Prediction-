import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import load_data

traffic, traffic2 = load_data()

st.title("📈 Traffic Patterns")

numeric_cols = traffic.select_dtypes(include='number')

column = st.selectbox(
    "Select Column",
    numeric_cols.columns
)

fig = px.line(
    traffic,
    y=column,
    title=f"{column} Trend"
)

st.plotly_chart(fig, use_container_width=True)
