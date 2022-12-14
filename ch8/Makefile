inference:
	docker compose -p ch8-inference -f inference-docker-compose.yaml up -d

dashboard:
	docker compose -p ch8-dashboard -f grafana-docker-compose.yaml up -d

inference-clean:
	docker compose -p ch8-inference down -v
	docker rmi -f ch8-dashboard-data-subscriber

dashboard-clean:
	docker compose -p ch8-dashboard down -v
	docker rmi -f grafana/grafana

server:
	make inference
	make dashboard

server-clean:
	make inference-clean
	make dashboard-clean

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
