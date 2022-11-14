import os
import pickle as pkl
import sys
from typing import Any, Dict

import mlflow
import pandas as pd
from mlflow.client import MlflowClient
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

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


def train_model(
    X: pd.DataFrame,
    y: pd.Series,
    model: RandomForestClassifier,
) -> RandomForestClassifier:
    """
    Train scikit-learn RandomForest model.

    Args:
        X (pd.DataFrame): wind datasets' input x DataFrame.
        y (pd.Series): wind datasets' output y Series.
        model (RandomForestClassifier): scikit-learn RandomForest model.

    Returns:
        model (RandomForestClassifier): model that trained by wine datasets.
    """
    model.fit(X, y)

    return model


def save_to_mlflow(
    method: str,
    model: RandomForestClassifier,
    model_configs: Dict[str, Any],
    result_metrics: Dict[str, float],
) -> None:
    """
    Save model, hyper parameters and metrics to mlflow run.

    Args:
        method (str):
            how to save informations to mlflow.
            fluent or client case is available.
        model (RandomForestClassifier):
            RandomForestClassifier model in sklearn.emsemble module.
            all of sklearn fit-predict pattern modules' instance are allowed.
        model_configs (Dict[str, Any]):
            hyper parameters at model.
        result_metrics (Dict[str, int]):
            model's results to determine how model is trained.
    """
    if method == "fluent":
        fluent_case(model, model_configs, result_metrics)
    elif method == "client":
        client_case(model, model_configs, result_metrics)


def fluent_case(
    model: RandomForestClassifier,
    model_configs: Dict[str, Any],
    result_metrics: Dict[str, float],
) -> None:
    """
    Fluent case to save model to mlflow
    """
    mlflow.set_experiment("fluent_case")

    with mlflow.start_run(run_name="rf"):
        mlflow.log_params(model_configs)
        mlflow.log_metrics(result_metrics)
        mlflow.sklearn.log_model(model, "sk_models")


def client_case(
    model: RandomForestClassifier,
    model_configs: Dict[str, Any],
    result_metrics: Dict[str, float],
) -> None:
    """
    Client case to save model to mlflow
    """
    exp = mlflow.set_experiment("client-case")

    file_path = "sk_model.pkl"
    with open(file_path, "wb") as fp:
        pkl.dump(model, fp)

    client = MlflowClient(MLFLOW_TRACKING_URI)

    run = client.create_run(exp.experiment_id)
    run_id = run.info.run_id

    client.log_artifact(run_id=run_id, local_path=file_path)
    for key, val in model_configs.items():
        client.log_param(run_id=run_id, key=key, value=val)
    for key, val in result_metrics.items():
        client.log_metric(run_id=run_id, key=key, value=val)


if __name__ == "__main__":
    # Setup environments
    print("-------- Setup system environment --------")
    setup_environs()

    # Load datasets.
    print("-------- Load datasets --------")
    X, y = load_iris(return_X_y=True, as_frame=True)

    # Split data for experiment.
    print("-------- Split datasets --------")
    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        train_size=0.8,
        random_state=2022,
    )

    # Setup model configuration.
    print("-------- Setup model hyperparameters --------")
    model_configs = {
        "n_estimators": 100,
        "criterion": "gini",
        "max_depth": 6,
        "min_samples_split": 2,
        "min_samples_leaf": 1,
        "min_weight_fraction_leaf": 0,
        "max_features": "sqrt",
    }

    # Assign model instance.
    print("-------- Train model --------")
    model = RandomForestClassifier(**model_configs)

    # Train model.
    trained_model = train_model(X_train, y_train, model)

    # Calculates model results
    print("-------- Calculate model results --------")
    train_pred = trained_model.predict(X_train)
    train_real = y_train

    valid_pred = trained_model.predict(X_valid)
    valid_real = y_valid

    result_metrics = {
        "train_accuracy": accuracy_score(train_real, train_pred),
        "validation_accuracy": accuracy_score(train_real, train_pred),
        "train_f1_score": f1_score(valid_real, valid_pred, average="macro"),
        "validation_f1_score": f1_score(valid_real, valid_pred, average="macro"),
    }
    assert (
        len(sys.argv) == 2
    ), "Give additional arguments to file in (fluent, client)\ne.g. python make_model.py fluent"

    print("-------- Save results to MLFlow --------")
    save_to_mlflow(
        method=sys.argv[1],
        model=trained_model,
        model_configs=model_configs,
        result_metrics=result_metrics,
    )
