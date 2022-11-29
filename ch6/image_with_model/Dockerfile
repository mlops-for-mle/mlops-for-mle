FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip \
    && pip install pandas scikit-learn joblib "fastapi[all]"

COPY db_pipeline.joblib db_pipeline.joblib
COPY schemas.py schemas.py
COPY image_with_model/ image_with_model/

CMD ["uvicorn", "image_with_model.app:app", "--host", "0.0.0.0", "--reload"]
