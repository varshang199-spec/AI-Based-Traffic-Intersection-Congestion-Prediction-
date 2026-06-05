from utils.data_loader import load_data
from utils.charts import create_kpi_cards

def main():
    df = load_data()

    create_kpi_cards(df)
