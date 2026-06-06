import streamlit as st

st.set_page_config(
    page_title="Traffic Analytics Dashboard",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Traffic Analytics Dashboard")

st.markdown("""
Welcome to the Traffic Analytics Dashboard.

### Features
- Executive Dashboard
- Traffic Pattern Analysis
- Vehicle Analysis
- Congestion Analysis
- Traffic Forecasting

Use the sidebar to navigate between pages.
""")

st.sidebar.success("Select a page above.")

# Dataset Information
st.subheader("📂 Available Datasets")

st.markdown("""
- Traffic.csv
- TrafficTwoMonth.csv
""")

col1, col2 = st.columns(2)

with col1:
    st.info("Traffic.csv\n\nContains traffic volume and vehicle information.")

with col2:
    st.info("TrafficTwoMonth.csv\n\nContains extended traffic records for trend analysis and forecasting.")

st.markdown("---")

st.subheader("📈 Dashboard Modules")

st.markdown("""
1. Executive Dashboard
2. Traffic Patterns
3. Vehicle Analysis
4. Congestion Analysis
5. Forecasting
""")
