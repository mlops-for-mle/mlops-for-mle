FROM amd64/python:3.9-slim

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install scikit-learn pandas psycopg2-binary

COPY generate_data.py generate_data.py

ENTRYPOINT ["python", "data_generator.py", "--db-host"]
CMD ["localhost"]
