from pathlib import Path

import pandas as pd

from src.data_preprocessing import preprocess_churn, preprocess_demand


def _tmp_file(name):
    root = Path("tests") / ".tmp"
    root.mkdir(parents=True, exist_ok=True)
    return root / name


def test_preprocess_churn_creates_numeric_output():
    input_csv = _tmp_file("churn.csv")
    output_csv = _tmp_file("churn_clean.csv")

    df = pd.DataFrame(
        {
            "customerID": ["c1", "c2", "c3"],
            "gender": ["Male", "Female", "Female"],
            "TotalCharges": ["10.5", " ", "30.0"],
            "Churn": ["Yes", "No", "No"],
        }
    )
    df.to_csv(input_csv, index=False)

    preprocess_churn(str(input_csv), str(output_csv))
    processed = pd.read_csv(output_csv)

    assert "customerID" not in processed.columns
    assert "TotalCharges" in processed.columns
    assert processed["TotalCharges"].notna().all()
    assert len(processed) == 2
    assert all(dtype.kind in "iufb" for dtype in processed.dtypes)


def test_preprocess_demand_extracts_calendar_features():
    input_csv = _tmp_file("demand.csv")
    output_csv = _tmp_file("demand_clean.csv")

    df = pd.DataFrame(
        {
            "Date": ["2025-01-02", "2025-02-15"],
            "Sales": [100, 120],
        }
    )
    df.to_csv(input_csv, index=False)

    preprocess_demand(str(input_csv), str(output_csv))
    processed = pd.read_csv(output_csv)

    assert "Date" not in processed.columns
    assert {"Day", "Month", "Year", "Sales"}.issubset(processed.columns)
    assert processed.loc[0, "Day"] == 2
    assert processed.loc[1, "Month"] == 2
    assert processed.loc[0, "Year"] == 2025
