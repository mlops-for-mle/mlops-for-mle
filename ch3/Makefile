init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi ch3-mlflow-server minio/minio postgres:14.0

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
