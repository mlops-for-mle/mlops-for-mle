kafka-server:
	docker compose -p kafka -f kafka-docker-compose.yaml up -d

sink-server:
	docker compose -p sink -f sink-docker-compose.yaml up -d

kafka-clean:
	docker compose -f kafka-docker-compose.yaml down -v

sink-clean:
	docker compose -f sink-docker-compose.yaml down -v

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

sink-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json

server:
	make kafka-server
	make sink-server
	make source-connector
	make sink-connector

server-clean:
	echo "------------Cleaning Chapter 7 resources------------"
	make kafka-clean || true
	make sink-clean || true
	docker rmi ch7-connect || true
	docker rmi ch7-source-data-generator ch7-sink-table-creator || true
	docker rmi ch7-sink-table-creator || true
	make dependency-clean

source-db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase

dependency:
	make -C ../ch1/ server

dependency-clean:
	make -C ../ch1/ server-clean
