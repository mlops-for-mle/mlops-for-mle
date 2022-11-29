FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip \
    && pip install boto3==1.26.8 mlflow==1.30.0 pandas scikit-learn "fastapi[all]"

COPY schemas.py schemas.py
COPY image_without_model/ image_without_model/

CMD ["uvicorn", "image_without_model.app:app", "--host", "0.0.0.0", "--reload"]
