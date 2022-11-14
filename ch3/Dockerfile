FROM amd64/python:3.9-slim

WORKDIR /my_app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/bin/python3:$PATH"

RUN pip install -U pip \
    && pip install fastapi "uvicorn[standard]" email-validator sqlalchemy psycopg2-binary

COPY ./my_app /my_app

EXPOSE 7777

# ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777", "--reload"]
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 7777 --reload
