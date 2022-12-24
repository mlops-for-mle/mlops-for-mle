init:
	pip install -U pip
	pip install pandas psycopg2-binary scikit-learn

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f part1-data-generator postgres:14.0

db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase
