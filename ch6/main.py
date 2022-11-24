import os

import mlflow
import pandas as pd
from fastapi import FastAPI
from schemas import PredictIn, PredictOut

MLFLOW_TRACKING_URI = "http://localhost:5000"
MLFLOW_S3_ENDPOINT_URL = "http://localhost:9000"

os.environ["MLFLOW_S3_ENDPOINT_URL"] = MLFLOW_S3_ENDPOINT_URL
os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "miniostorage"

# Get run info
df = mlflow.search_runs(max_results=10, experiment_names=["new-exp"])
run_id_list = [id for id in df["run_id"]]

# Get run_id
run_id_sample = run_id_list[0]

# Load model
MODEL = mlflow.pyfunc.load_model(model_uri=f"runs:/{run_id_sample}/sk_model")

# Create a FastAPI instance
app = FastAPI()


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn) -> PredictOut:
    df = pd.DataFrame([data.dict()])
    pred = MODEL.predict(df).item()
    return PredictOut(iris_class=pred)
