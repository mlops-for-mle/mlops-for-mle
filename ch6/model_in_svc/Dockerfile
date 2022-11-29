FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip \
    && pip install pandas scikit-learn joblib "fastapi[all]"

COPY db_pipeline.joblib db_pipeline.joblib
COPY schemas.py schemas.py
COPY model_in_svc/ model_in_svc/

CMD ["uvicorn", "model_in_svc.app:app", "--host", "0.0.0.0", "--reload"]
