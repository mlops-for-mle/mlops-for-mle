import os

import joblib
import mlflow
import pandas as pd
import psycopg2
from mlflow.client import MlflowClient
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 0. set mlflow environments
MLFLOW_TRACKING_URI = "http://localhost:5000"
MLFLOW_S3_ENDPOINT_URL = "http://localhost:9000"

os.environ["MLFLOW_S3_ENDPOINT_URL"] = MLFLOW_S3_ENDPOINT_URL
os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
os.environ["AWS_ACCESS_KEY_ID"] = "mystorage"
os.environ["AWS_SECRET_ACCESS_KEY"] = "mystoragepw"

# 1. get data
db_connect = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword",
)
df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 10", db_connect)
X = df.drop(["id", "target"], axis="columns")
y = df["target"]
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    train_size=0.8,
    random_seed=2022,
)

# 2. model development and train
model_pipeline = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
model_pipeline.fit(X_train, y_train)

train_pred = model_pipeline.predict(X_train)
valid_pred = model_pipeline.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

# 3. save model

file_path = "sk_model.pkl"
with open(file_path, "wb") as fp:
    joblib.dump(model_pipeline, fp)

exp = mlflow.set_experiment("client-case")

client = MlflowClient(MLFLOW_TRACKING_URI)

run = client.create_run(exp.experiment_id)
run_id = run.info.run_id

client.log_metric(run_id=run_id, key="train_acc", value=train_acc)
client.log_metric(run_id=run_id, key="valid_acc", value=valid_acc)
client.log_artifact(run_id=run_id, local_path=file_path)
