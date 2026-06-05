import pandas as pd


def load_data():
    return pd.read_csv("data/Traffic.csv")


def load_two_month_data():
    return pd.read_csv("data/TrafficTwoMonth.csv")
