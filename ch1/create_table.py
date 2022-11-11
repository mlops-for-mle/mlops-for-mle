import os

import psycopg2
from psycopg2.extensions import connection

DB_HOST = os.getenv("DB_HOST", "localhost")


def create_table(db_connect: connection) -> None:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        sepal_length float8,
        sepal_width float8,
        petal_length float8,
        petal_width float8,
        target int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser", 
        password="mypassword",
        host=DB_HOST,
        port=5432,
        database="mydatabase",
    )
    create_table(db_connect)