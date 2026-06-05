# analysis.py

import pandas as pd
import numpy as np


# -----------------------------
# Load Dataset
# -----------------------------
def load_data(file_path):
    df = pd.read_csv(file_path)

    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df["Year"] = df["DateTime"].dt.year
    df["Month"] = df["DateTime"].dt.month
    df["Day"] = df["DateTime"].dt.day
    df["Hour"] = df["DateTime"].dt.hour
    df["Day_Name"] = df["DateTime"].dt.day_name()

    return df


# -----------------------------
# KPI Metrics
# -----------------------------
def get_kpis(df):
    return {
        "Total Vehicles": int(df["Vehicles"].sum()),
        "Average Traffic": round(df["Vehicles"].mean(), 2),
        "Peak Traffic": int(df["Vehicles"].max()),
        "Junctions": int(df["Junction"].nunique())
    }


# -----------------------------
# Hourly Traffic Pattern
# -----------------------------
def hourly_traffic(df):
    return (
        df.groupby("Hour")["Vehicles"]
        .mean()
        .reset_index()
        .sort_values("Hour")
    )


# -----------------------------
# Daily Traffic Pattern
# -----------------------------
def daily_traffic(df):
    return (
        df.groupby("Day_Name")["Vehicles"]
        .mean()
        .reset_index()
    )
    

# -----------------------------
# Monthly Traffic Trend
# -----------------------------
def monthly_traffic(df):
    return (
        df.groupby("Month")["Vehicles"]
        .mean()
        .reset_index()
        .sort_values("Month")
    )


# -----------------------------
# Junction Analysis
# -----------------------------
def junction_analysis(df):
    return (
        df.groupby("Junction")["Vehicles"]
        .agg(["mean", "sum", "max"])
        .reset_index()
    )


# -----------------------------
# Congestion Detection
# -----------------------------
def congestion_analysis(df):
    threshold = df["Vehicles"].quantile(0.90)

    congested = df[df["Vehicles"] >= threshold]

    return congested, threshold


# -----------------------------
# Peak Hour Analysis
# -----------------------------
def peak_hours(df):
    return (
        df.groupby("Hour")["Vehicles"]
        .mean()
        .nlargest(5)
        .reset_index()
    )


# -----------------------------
# Forecast Dataset
# -----------------------------
def forecast_data(df):
    forecast_df = (
        df.groupby("DateTime")["Vehicles"]
        .sum()
        .reset_index()
    )

    forecast_df.columns = ["ds", "y"]

    return forecast_df


# -----------------------------
# Summary Insights
# -----------------------------
def generate_insights(df):
    busiest_junction = (
        df.groupby("Junction")["Vehicles"]
        .sum()
        .idxmax()
    )

    peak_hour = (
        df.groupby("Hour")["Vehicles"]
        .mean()
        .idxmax()
    )

    return {
        "Busiest Junction": busiest_junction,
        "Peak Hour": peak_hour,
        "Average Vehicles": round(df["Vehicles"].mean(), 2)
    }
