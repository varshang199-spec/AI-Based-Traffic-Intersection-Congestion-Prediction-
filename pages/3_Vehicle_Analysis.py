from utils.data_loader import load_data
from utils.charts import vehicle_distribution_chart

def main():
    df = load_data()

    vehicle_distribution_chart(df)
