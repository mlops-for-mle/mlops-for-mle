import mlflow
import pandas as pd
from fastapi import FastAPI
from schemas import PredictIn, PredictOut


def get_model():
    model = mlflow.sklearn.load_model(model_uri="./sk_model")
    return model


MODEL = get_model()

# Create a FastAPI instance
app = FastAPI()


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn) -> PredictOut:
    df = pd.DataFrame([data.dict()])
    pred = MODEL.predict(df).item()
    return PredictOut(iris_class=pred)
