init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose up -d

server-clean:
	echo "------------Cleaning Chapter 3 resources------------"
	docker compose down -v || true
	docker rmi ch3-mlflow-server || true
	docker rmi minio/minio || true
	docker rmi postgres:14.0 || true

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
