import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import load_data

traffic, traffic2 = load_data()

st.title("📊 Executive Dashboard")

st.metric(
    "Total Records",
    len(traffic)
)

numeric_cols = traffic.select_dtypes(include='number')

if not numeric_cols.empty:

    st.metric(
        "Average Traffic",
        round(numeric_cols.mean().mean(),2)
    )

fig = px.histogram(
    numeric_cols,
    title="Traffic Distribution"
)

st.plotly_chart(fig, use_container_width=True)
