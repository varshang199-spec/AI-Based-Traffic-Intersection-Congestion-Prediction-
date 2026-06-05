import streamlit as st
import plotly.express as px


def create_kpi_cards(df):
    st.metric(
        "Total Vehicles",
        len(df)
    )


def traffic_pattern_chart(df):
    fig = px.line(
        df,
        x="Time",
        y="Vehicle_Count",
        title="Traffic Flow Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def vehicle_distribution_chart(df):
    fig = px.pie(
        df,
        names="Vehicle_Type",
        values="Vehicle_Count",
        title="Vehicle Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def congestion_heatmap(df):
    fig = px.density_heatmap(
        df,
        x="Hour",
        y="Congestion_Level",
        title="Congestion Heatmap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def forecast_chart(df):
    fig = px.line(
        df,
        x="Date",
        y="Vehicle_Count",
        title="Traffic Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
