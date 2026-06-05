import streamlit as st
import plotly.express as px

from analysis import load_data

traffic, traffic2 = load_data()

st.title("🚗 Vehicle Analysis")

numeric_cols = traffic.select_dtypes(include='number')

column = st.selectbox(
    "Vehicle Metric",
    numeric_cols.columns
)

fig = px.box(
    traffic,
    y=column,
    title="Vehicle Distribution"
)

st.plotly_chart(fig, use_container_width=True)
