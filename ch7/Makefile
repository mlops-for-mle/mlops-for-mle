kafka-server:
	docker compose -p kafka -f kafka-docker-compose.yaml up -d

sink-server:
	docker compose -p sink -f sink-docker-compose.yaml up -d

kafka-clean:
	docker compose -p kafka down -v || true
	docker rmi kafka_connect || true

sink-clean:
	docker compose -p sink down -v || true
	docker rmi sink_sink-table-creator || true

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
	PGPASSWORD=sourcepassword psql -h localhost -p 5433 -U sourceuser -d sourcedatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5434 -U sinkuser -d sinkdatabase
