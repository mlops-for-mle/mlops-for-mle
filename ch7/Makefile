server:
	docker compose -f kafka-docker-compose.yaml up -d
	docker compose -f source-docker-compose.yaml up -d
	docker compose -f sink-docker-compose.yaml up -d
	make source-connector
	make sink-connector

kafka-server:
	docker compose -f kafka-docker-compose.yaml up -d

source-server:
	docker compose -f source-docker-compose.yaml up -d

sink-server:
	docker compose -f sink-docker-compose.yaml up -d

server-clean:
	docker compose -f kafka-docker-compose.yaml down -v
	docker compose -f source-docker-compose.yaml down -v
	docker compose -f sink-docker-compose.yaml down -v
	docker rmi ch7-connect ch7-source-data-generator ch7-sink-table-creator

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

sink-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json

source-db-connection:
	PGPASSWORD=sourcepassword psql -h localhost -p 5432 -U sourceuser -d sourcedatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase
