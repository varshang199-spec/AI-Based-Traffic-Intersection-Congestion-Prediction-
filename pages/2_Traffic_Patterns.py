from utils.data_loader import load_data
from utils.charts import traffic_pattern_chart

def main():
    df = load_data()

    traffic_pattern_chart(df)
