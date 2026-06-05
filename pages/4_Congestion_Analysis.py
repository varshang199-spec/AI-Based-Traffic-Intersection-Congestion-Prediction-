import streamlit as st
import plotly.express as px

from analysis import load_data

traffic, traffic2 = load_data()

st.title("🚥 Congestion Analysis")

numeric_cols = traffic.select_dtypes(include='number')

column = st.selectbox(
    "Select Metric",
    numeric_cols.columns
)

fig = px.scatter(
    traffic,
    y=column,
    title="Congestion Visualization"
)

st.plotly_chart(fig, use_container_width=True)
