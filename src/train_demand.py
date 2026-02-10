import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def train():
    df = pd.read_csv("data/processed/demand_clean.csv")

    X = df[["Day", "Month", "Year"]]
    y = df["Sales"]

    model = LinearRegression()
    model.fit(X, y)

    preds = model.predict(X)
    mse = mean_squared_error(y, preds)

    print("MSE:", mse)

    joblib.dump(model, "models/demand_model.pkl")
    print("Demand model saved.")


if __name__ == "__main__":
    train()
