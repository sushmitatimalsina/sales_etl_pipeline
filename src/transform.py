def transform_data(df):
    print("Transforming data...")

    # Remove missing values
    df = df.dropna()

    # Convert amount to float
    df["amount"] = df["amount"].astype(float)

    # Add tax (13%)
    df["tax"] = df["amount"] * 0.13

    return df