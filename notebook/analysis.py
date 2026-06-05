import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df["Year"] = df["DateTime"].dt.year
    df["Month"] = df["DateTime"].dt.month
    df["Day"] = df["DateTime"].dt.day
    df["Hour"] = df["DateTime"].dt.hour
    df["Weekday"] = df["DateTime"].dt.day_name()

    return df


def get_kpis(df):
    return {
        "Total Vehicles": int(df["Vehicles"].sum()),
        "Average Traffic": round(df["Vehicles"].mean(), 2),
        "Maximum Traffic": int(df["Vehicles"].max()),
        "Total Junctions": df["Junction"].nunique()
    }


def hourly_traffic(df):
    return (
        df.groupby("Hour")["Vehicles"]
        .mean()
        .reset_index()
    )


def junction_traffic(df):
    return (
        df.groupby("Junction")["Vehicles"]
        .sum()
        .reset_index()
    )


def monthly_traffic(df):
    return (
        df.groupby("Month")["Vehicles"]
        .sum()
        .reset_index()
    )


def weekday_traffic(df):
    return (
        df.groupby("Weekday")["Vehicles"]
        .mean()
        .reset_index()
    )
