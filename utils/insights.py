def generate_insights(df):

    total = df["Vehicle_Count"].sum()

    peak_hour = (
        df.groupby("Hour")["Vehicle_Count"]
        .sum()
        .idxmax()
    )

    return {
        "Total Vehicles": total,
        "Peak Hour": peak_hour
    }
