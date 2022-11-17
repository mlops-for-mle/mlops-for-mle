init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn==1.1.3

server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch3-mlflow-server
run-dependency:
	make -C ../ch1/ server
