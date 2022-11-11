from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pandas as pd
from typing import Dict, Any

MODEL_CONFIGS = {
    "n_estimators": 100,
    "criterion": "gini",
    "max_depth": 6, 
    "min_samples_split": 2, 
    "min_samples_leaf":  1, 
    "min_weight_fraction_leaf": 0, 
    "max_features": "sqrt", 
}

def train_model(
    X: pd.DataFrame,
    y: pd.Series,
    model: RandomForestClassifier
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


def save_model_to_mlflow(
    model: RandomForestClassifier,
    method: str
) -> None:
    """_summary_

    Args:
        model (RandomForestClassifier): _description_
    """
    if method == "fluent":
    elif method == "client"

def save_hp_to_mlflow(
    model_configs: Dict[str,Any] = MODEL_CONFIGS,
    method: str
) -> None:
    """_summary_

    Args:
        model_configs (Dict[str,Any], optional): _description_. Defaults to MODEL_CONFIGS.
    """

if __name__ == "__main__":
    X, y = load_iris(return_X_y=True, as_frame=True)
    
    model = RandomForestClassifier(**MODEL_CONFIGS)
    trained_model = train_model(X, y, model)

    

    
    
