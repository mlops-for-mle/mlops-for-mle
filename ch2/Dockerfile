FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -U pip &&\
    pip install mlflow psycopg2-binary boto3
RUN cd /tmp && \
    wget https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc
