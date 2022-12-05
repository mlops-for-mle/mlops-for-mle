server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch7-source-data-generator ch7-sink-table-creator ch7-connect

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

sink-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink_connector.json

source-db-connection:
	PGPASSWORD=sourcepassword psql -h localhost -p 5432 -U sourceuser -d sourcedatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase
