import pandas as pd

def load_data():

    traffic = pd.read_csv("data/Traffic.csv")
    traffic2 = pd.read_csv("data/TrafficTwoMonth.csv")

    return traffic, traffic2
