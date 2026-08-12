import pandas as pd

def load_flight_data(file_path):
    return pd.read_csv(file_path,encoding="utf-8-sig")

