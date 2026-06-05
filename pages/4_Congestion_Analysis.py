from utils.data_loader import load_data
from utils.charts import congestion_heatmap

def main():
    df = load_data()

    congestion_heatmap(df)
