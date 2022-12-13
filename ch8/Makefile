server:
	docker compose -p stream-serving up -d

server-clean:
	docker compose -p stream-serving down -v
	docker image prune -a -f

source-connector:
	curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source_connector.json

source-db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase

sink-db-connection:
	PGPASSWORD=sinkpassword psql -h localhost -p 5433 -U sinkuser -d sinkdatabase

dependency:
	make -C ../ch1/ server
	make -C ../ch3/ server
	make -C ../ch6/ server
	make -C ../ch7/ server

dependency-clean:
	make -C ../ch7/ server-clean
	make -C ../ch6/ server-clean
	make -C ../ch3/ server-clean
	make -C ../ch1/ server-clean
