# data_subscriber.py
from json import loads

import psycopg2
import requests
from kafka import KafkaConsumer


def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_prediction (
        id SERIAL PRIMARY KEY,
        iris_class int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


def insert_data(db_connect, data):
    insert_row_query = f"""
    INSERT INTO iris_prediction
        (iris_class)
        VALUES ({data["iris_class"]});
    """
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()


def subscribe_data(db_connect, consumer):
    for msg in consumer:
        print(
            f"Topic : {msg.topic}\n"
            f"Partition : {msg.partition}\n"
            f"Offset : {msg.offset}\n"
            f"Key : {msg.key}\n"
            f"Value : {msg.value}\n",
        )

        msg.value["payload"].pop("id", None)
        msg.value["payload"].pop("target", None)

        response = requests.post(
            url="http://api-with-model:8000/predict",
            json=msg.value["payload"],
            headers={"Content-Type": "application/json"},
        )
        insert_data(db_connect, response.json())


if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="sinkuser",
        password="sinkpassword",
        host="sink-postgres-server",
        port=5432,
        database="sinkdatabase",
    )
    create_table(db_connect)

    consumer = KafkaConsumer(
        "postgres-source-iris_data",
        bootstrap_servers="broker:29092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="iris",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )
    subscribe_data(db_connect, consumer)
