stream-server:
	docker compose -p ch8-stream -f stream-docker-compose.yaml up -d

dashboard-server:
	docker compose -p ch8-dashboard -f grafana-docker-compose.yaml up -d

stream-server-clean:
	docker compose -p ch8-stream down -v
	docker rmi -f ch8-stream-data-subscriber

dashboard-server-clean:
	docker compose -p ch8-dashboard down -v
	docker rmi -f grafana/grafana

server:
	make stream-server
	make dashboard-server

server-clean:
	make stream-server-clean
	make dashboard-server-clean

dependency:
	make -C ../ch1/ server
	make -C ../ch6/ server
	make -C ../ch7/ server

dependency-clean:
	make -C ../ch7/ server-clean
	make -C ../ch6/ server-clean
	make -C ../ch1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean

target-db-connection:
	PGPASSWORD=targetpassword psql -h localhost -p 5433 -U targetuser -d targetdatabase
