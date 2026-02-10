import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os


def preprocess_churn(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop customerID if exists
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    # Convert TotalCharges to numeric if needed
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df = df.dropna()

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include="object").columns:
        df[col] = le.fit_transform(df[col])

    df.to_csv(output_path, index=False)
    print("Churn preprocessing complete.")


def preprocess_demand(input_path, output_path):
    df = pd.read_csv(input_path)

    # Ensure date column exists
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df["Day"] = df["Date"].dt.day
        df["Month"] = df["Date"].dt.month
        df["Year"] = df["Date"].dt.year
        df = df.drop("Date", axis=1)

    df.to_csv(output_path, index=False)
    print("Demand preprocessing complete.")


if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)

    preprocess_churn("data/raw/churn.csv", "data/processed/churn_clean.csv")
    preprocess_demand("data/raw/demand.csv", "data/processed/demand_clean.csv")
