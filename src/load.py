def load_data(df):
    print("Loading data...")

    df.to_csv("../data/processed/cleaned_sales.csv", index=False)