kafka-server:
	docker compose -f kafka-docker-compose.yaml up -d

sink-server:
	docker compose -f sink-docker-compose.yaml up -d

kafka-clean:
	docker compose -f kafka-docker-compose.yaml down -v
	docker rmi -f \
		ch7-connect \
		confluentinc/cp-kafka:7.3.0 \
		confluentinc/cp-schema-registry:7.3.0 \
		confluentinc/cp-zookeeper:7.3.0

sink-clean:
	docker compose -f sink-docker-compose.yaml down -v
	docker rmi -f ch7-sink-table-creator

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

sink-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json

server:
	make kafka-server
	make sink-server
	sleep 30
	make source-connector
	make sink-connector

server-clean:
	echo "------------Cleaning Chapter 7 resources------------"
	make kafka-clean
	make sink-clean

source-db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
