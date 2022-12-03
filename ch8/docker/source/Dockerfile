FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install scikit-learn pandas psycopg2-binary

COPY data_generator.py data_generator.py

ENTRYPOINT ["python", "data_generator.py"]
