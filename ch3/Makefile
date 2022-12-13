init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose -p model-registry up -d

server-clean:
	echo "------------Cleaning Chapter 3 resources------------"
	docker compose -p model-registry down -v
	docker image prune -a -f

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
