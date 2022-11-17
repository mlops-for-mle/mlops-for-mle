import os
import time

import pandas as pd
import psycopg2
from psycopg2.extensions import connection
from sklearn.datasets import load_iris

DB_HOST = os.getenv("DB_HOST", "localhost")


def get_data() -> pd.DataFrame:
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
    }
    df = df.rename(columns=rename_rule)
    return df


def insert_data(db_connect: connection, data: pd.DataFrame) -> None:
    insert_row_query = f"""
    INSERT INTO iris_data
        (sepal_length, sepal_width, petal_length, petal_width, target)
        VALUES (
            {data.sepal_length},
            {data.sepal_width},
            {data.petal_length},
            {data.petal_width},
            {data.target}
        );
    """
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()


def generate_data(db_connect: connection, df: pd.DataFrame) -> None:
    idx = 0
    while True:
        insert_data(db_connect, df.loc[idx].squeeze())
        idx += 1
        idx %= len(df)
        time.sleep(5)


if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host=DB_HOST,
        port=5432,
        database="mydatabase",
    )
    df = get_data()
    generate_data(db_connect, df)
