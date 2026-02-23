# MLOps Churn and Demand Project

This project includes data preprocessing, model training, evaluation, and a simple Streamlit app for churn prediction and demand forecasting.

## Jenkins CI

A Jenkins pipeline is defined in `Jenkinsfile` with these stages:

1. Checkout source code
2. Install Python dependencies from `requirements.txt`
3. Run unit tests with `pytest`
4. Run a Python import smoke check

Test reports are generated at `reports/pytest.xml` and published with Jenkins `junit`.

### Reproducible Docker Agent Pipeline

A containerized Jenkins pipeline is also available at `Jenkinsfile.docker`.

It runs the same stages inside a pinned image:

- `python:3.10.14-slim-bookworm`

To use it in Jenkins, set Pipeline `Script Path` to:

- `Jenkinsfile.docker`

Prerequisite:

- Jenkins agent must have Docker available and Jenkins Docker Pipeline support enabled.

## Local Setup

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
```
