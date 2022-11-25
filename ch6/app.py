import os

import mlflow
import pandas as pd
from fastapi import FastAPI
from schemas import PredictIn, PredictOut


def get_model():
    # Set environments
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
    os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
    os.environ["AWS_ACCESS_KEY_ID"] = "minio"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "miniostorage"

    # Get run info
    df = mlflow.search_runs(max_results=1, experiment_names=["new-exp"])

    # Get run_id
    run_id = df["run_id"][0]

    # Load model
    model = mlflow.pyfunc.load_model(model_uri=f"runs:/{run_id}/sk_model")
    return model


MODEL = get_model()


# Create a FastAPI instance
app = FastAPI()


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn) -> PredictOut:
    df = pd.DataFrame([data.dict()])
    pred = MODEL.predict(df).item()
    return PredictOut(iris_class=pred)
