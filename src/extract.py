import pandas as pd

def extract_data():
    print("Extracting data...")
    df = pd.read_csv("../data/raw/sales.csv")
    return df