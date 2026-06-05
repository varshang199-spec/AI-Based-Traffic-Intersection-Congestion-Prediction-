from utils.data_loader import load_two_month_data
from utils.charts import forecast_chart

def main():
    df = load_two_month_data()

    forecast_chart(df)
