server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi grafana/grafana

dependency:
	make -C ../ch1/ server
	make -C ../ch6/ server
	make -C ../ch7/ server
	make -C ../ch8/ server

dependency-clean:
	make -C ../ch8/ server-clean
	make -C ../ch7/ server-clean
	make -C ../ch6/ server-clean
	make -C ../ch1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean

source-db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase

target-db-connection:
	PGPASSWORD=targetpassword psql -h localhost -p 5433 -U targetuser -d targetdatabase
