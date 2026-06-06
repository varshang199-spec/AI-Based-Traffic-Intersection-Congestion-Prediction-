
import streamlit as st
from pages import (
    Executive_Dashboard,
    Traffic_Patterns,
    Vehicle_Analysis,
    Congestion_Analysis,
    Forecasting
)

st.set_page_config(
    page_title="Traffic Analytics Dashboard",
    page_icon="🚦",
    layout="wide"
)

st.sidebar.title("🚦 Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Executive Dashboard",
        "Traffic Patterns",
        "Vehicle Analysis",
        "Congestion Analysis",
        "Forecasting"
    ]
)

if page == "Executive Dashboard":
    Executive_Dashboard.main()

elif page == "Traffic Patterns":
    Traffic_Patterns.main()

elif page == "Vehicle Analysis":
    Vehicle_Analysis.main()

elif page == "Congestion Analysis":
    Congestion_Analysis.main()

elif page == "Forecasting":
    Forecasting.main()


