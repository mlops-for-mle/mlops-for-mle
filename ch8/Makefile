server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi ch8-connect ch8-source-data-generator ch8-sink-data-subscriber ch8-api-with-model

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

source-db-connection:
	PGPASSWORD=sourcepassword psql -h localhost -p 5433 -U sourceuser -d sourcedatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5434 -U sinkuser -d sinkdatabase

dependency:
	make -C ../ch1/ server
	make -C ../ch6/ server
	make -C ../ch7/ server

dependency-clean:
	make -C ../ch7/ server-clean
	make -C ../ch6/ server-clean
	make -C ../ch3/ server-clean
	make -C ../ch1/ server-clean
