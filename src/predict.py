import joblib
import numpy as np


def predict_churn(sample_input):
    model = joblib.load("models/churn_model.pkl")
    prediction = model.predict(np.array(sample_input).reshape(1, -1))
    return prediction[0]