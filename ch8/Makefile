server:
	docker compose -p stream-serving up -d

server-clean:
	echo "------------Cleaning Chapter 8 resources------------"
	docker compose down -v
	docker rmi -f stream-serving-sink-data-subscriber

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
