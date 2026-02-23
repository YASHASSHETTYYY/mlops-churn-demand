from unittest.mock import patch

from src.predict import predict_churn


class DummyModel:
    def predict(self, values):
        assert values.shape == (1, 3)
        return [1]


def test_predict_churn_uses_serialized_model():
    with patch("src.predict.joblib.load", return_value=DummyModel()) as load_mock:
        prediction = predict_churn([0.1, 0.2, 0.3])

    load_mock.assert_called_once_with("models/churn_model.pkl")
    assert prediction == 1
