init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose -p model-registry up -d

server-clean:
	echo "------------Cleaning Chapter 3 resources------------"
	docker compose down -v
	docker rmi -f model-registry-mlflow-server minio/minio
	docker rmi -f postgres:14.0 || true

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
