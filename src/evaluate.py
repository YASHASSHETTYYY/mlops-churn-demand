import joblib
import pandas as pd
from sklearn.metrics import accuracy_score


def evaluate_churn():
    model = joblib.load("models/churn_model.pkl")
    df = pd.read_csv("data/processed/churn_clean.csv")

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print("Churn Accuracy:", acc)


if __name__ == "__main__":
    evaluate_churn()
