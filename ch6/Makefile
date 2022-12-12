init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" pandas scikit-learn

app:
	uvicorn app:app --reload

build:
	docker build -f Dockerfile -t ch6-api-with-model .

server: build
	docker run --network "ch1_default" --name api-with-model -p 8000:8000 -d ch6-api-with-model

server-clean:
	echo "------------Cleaning Chapter 6 resources------------"
	docker rm -f api-with-model || true
	docker rmi ch6-api-with-model || true
	make dependency-clean

dependency:
	make -C ../ch1/ server
	sleep 100
	make -C ../ch3/ server
	python ../ch3/save_model_to_registry.py

dependency-clean:
	make -C ../ch3/ server-clean
	make -C ../ch1/ server-clean
