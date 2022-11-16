import os

import mlflow
import pandas as pd
import psycopg2
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

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
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

train_pred = rf.predict(X_train)
valid_pred = rf.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

# 3. save model
mlflow.set_experiment("fluent_case")

with mlflow.start_run(run_name="rf"):
    mlflow.log_metrics({"train_acc": train_acc, "valid_acc": valid_acc})
    mlflow.sklearn.log_model(rf, "sk_models")