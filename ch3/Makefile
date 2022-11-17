init:
	pip install -U pip
	pip install boto3 mlflow scikit-learn

server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch3-mlflow-server

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
