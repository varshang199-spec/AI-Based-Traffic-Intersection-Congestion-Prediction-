import streamlit as st
import plotly.express as px
from analysis import *

st.set_page_config(
    page_title="Traffic Analytics Dashboard",
    page_icon="🚦",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------
df = load_data("traffic.csv")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("🚦 Traffic Analytics")

junctions = st.sidebar.multiselect(
    "Select Junction",
    df["Junction"].unique(),
    default=df["Junction"].unique()
)

df = df[df["Junction"].isin(junctions)]

# ----------------------------
# Header
# ----------------------------
st.title("🚦 Smart Traffic Analytics Dashboard")

st.markdown(
"""
Advanced Traffic Flow Monitoring and Analytics using Streamlit
"""
)

# ----------------------------
# KPIs
# ----------------------------
kpis = get_kpis(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Vehicles", f"{kpis['Total Vehicles']:,}")
c2.metric("Average Traffic", kpis["Average Traffic"])
c3.metric("Maximum Traffic", kpis["Maximum Traffic"])
c4.metric("Junctions", kpis["Total Junctions"])

st.divider()

# ----------------------------
# Hourly Trend
# ----------------------------
hour_df = hourly_traffic(df)

fig1 = px.line(
    hour_df,
    x="Hour",
    y="Vehicles",
    title="Average Hourly Traffic"
)

st.plotly_chart(fig1, use_container_width=True)

# ----------------------------
# Junction Analysis
# ----------------------------
junc_df = junction_traffic(df)

fig2 = px.bar(
    junc_df,
    x="Junction",
    y="Vehicles",
    title="Traffic by Junction"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Monthly Analysis
# ----------------------------
month_df = monthly_traffic(df)

fig3 = px.area(
    month_df,
    x="Month",
    y="Vehicles",
    title="Monthly Traffic Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------
# Weekday Analysis
# ----------------------------
week_df = weekday_traffic(df)

fig4 = px.bar(
    week_df,
    x="Weekday",
    y="Vehicles",
    title="Weekday Traffic Pattern"
)

st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# Raw Data
# ----------------------------
with st.expander("View Dataset"):
    st.dataframe(df)

# ----------------------------
# Insights
# ----------------------------
st.subheader("📊 Key Insights")

peak_hour = hour_df.loc[
    hour_df["Vehicles"].idxmax(),
    "Hour"
]

best_junction = junc_df.loc[
    junc_df["Vehicles"].idxmax(),
    "Junction"
]

st.success(
    f"""
    • Peak Traffic Hour: {peak_hour}:00

    • Most Busy Junction: {best_junction}

    • Average Traffic Flow: {round(df['Vehicles'].mean(),2)}

    • Total Recorded Vehicles: {df['Vehicles'].sum():,}
    """
)
