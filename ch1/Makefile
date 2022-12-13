init:
	pip install -U pip
	pip install pandas psycopg2-binary scikit-learn

server:
	docker compose up -d

server-clean:
	echo "------------Cleaning Chapter 1 resources------------"
	docker compose down -v
	docker rmi -f ch1-data-generator
