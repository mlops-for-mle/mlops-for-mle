import os
import pickle as pkl
import sys

import mlflow
from mlflow.client import MlflowClient
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

MLFLOW_TRACKING_URI = "http://localhost:5000"
MLFLOW_S3_ENDPOINT_URL = "http://localhost:9000"


def setup_environs() -> None:
    """
    Setup system environments for mimic server side application.
    """
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = MLFLOW_S3_ENDPOINT_URL
    os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
    os.environ["AWS_ACCESS_KEY_ID"] = "mystorage"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "mystoragepw"


def download_from_artifact(run_id: str) -> RandomForestClassifier:
    """
    Download artifact to local and load pickle file

    Args:
        run_id (str): run id in mlflow having of one "sk_model.pkl" file.

    Returns:
        RandomForestClassifier: trained model.
    """
    client = MlflowClient(MLFLOW_TRACKING_URI)
    client.download_artifacts(run_id=run_id, path="sk_model.pkl", dst_path="./")
    model = load_from_local("sk_models.pkl")
    return model


def load_from_local(file_path: str) -> RandomForestClassifier:
    """
    Load sklearn model from local file.

    Args:
        file_path (str): downloaded local model path.

    Returns:
        RandomForestClassifier: trained model.
    """
    with open(file_path, "rb") as fp:
        model = pkl.load(fp)
    return model


def download_from_mlflow(model_uri: str):
    """
    Download MLFlow orginized model directory from remote path.

    Args:
        model_uri (str): MLFLow style model uri that contain "s3".

    Returns:
        RandomForestClassifier: trained model.
    """
    pyfunc_model = mlflow.sklearn.load_model(model_uri)
    return pyfunc_model


if __name__ == "__main__":
    print("-------- Setup system environment --------")
    setup_environs()

    assert (
        len(sys.argv) == 2
    ), "Give additional arguments to file in (fluent, client)\ne.g. python make_model.py fluent"

    print("-------- Check result type --------")
    model_path = sys.argv[1]
    if "s3" in model_path:
        model = download_from_mlflow(model_path)
    else:
        model = download_from_artifact(model_path)

    print("-------- Load test sample --------")
    X, _ = load_iris(return_X_y=True, as_frame=True)

    print("-------- Prediction --------")
    print(f"requested inputs \n{X.iloc[:10]}")
    print(
        "predicted for each row\n",
        "-------------------------",
    )
    print(model.predict(X.iloc[:10]))
