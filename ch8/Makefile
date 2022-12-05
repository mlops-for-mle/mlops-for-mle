init:
	pip install -U pip
	pip install mlflow==1.30.0

server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch8-source-data-generator ch8-sink-data-subscriber ch8-connect ch8-api-with-model

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

source-db-connection:
	PGPASSWORD=sourcepassword psql -h localhost -p 5432 -U sourceuser -d sourcedatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase

dependency:
	make -C ../ch3/ server
	python ../ch3/save_model_to_registry.py

dependency-clean:
	make -C ../ch3/ server-clean
