init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" pandas scikit-learn

app:
	uvicorn app:app --reload

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f part6-api-with-model

dependency:
	make -C ../part1/ server
	sleep 100
	make -C ../part3/ server
	python ../part3/save_model_to_registry.py

dependency-clean:
	make -C ../part3/ server-clean
	make -C ../part1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean
