init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" pandas scikit-learn

app:
	uvicorn app:app --reload

server:
	docker compose -p api-serving up -d --build

server-clean:
	echo "------------Cleaning Chapter 6 resources------------"
	docker compose down -v
	docker rmi -f api-serving-api-with-model

dependency:
	make -C ../ch1/ server
	sleep 100
	make -C ../ch3/ server
	python ../ch3/save_model_to_registry.py

dependency-clean:
	make -C ../ch3/ server-clean
	make -C ../ch1/ server-clean
