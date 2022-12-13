init:
	pip install -U pip
	pip install pandas psycopg2-binary scikit-learn

server:
	docker compose -p db up -d

server-clean:
	echo "------------Cleaning Chapter 1 resources------------"
	docker compose -p db down -v
	docker image prune -a -f
