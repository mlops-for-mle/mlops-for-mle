# create_table.py
import psycopg2


def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
<<<<<<< HEAD
        ts timestamp,
=======
>>>>>>> 41f1007572c433c458c3572a298c8d1275cd62d6
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
        user="targetuser",
        password="targetpassword",
        host="target-postgres-server",
        port=5432,
        database="targetdatabase",
    )
    create_table(db_connect)
