# base_train.py

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 1. get data
X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    train_size=0.8,
    random_state=2022,
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
joblib.dump(rf, "rf.joblib")
