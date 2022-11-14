init:
	pip install -U pip
	pip install pandas psycopg2-binary scikit-learn

server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch1-data-generator
