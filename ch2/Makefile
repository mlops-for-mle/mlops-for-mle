init:
	pip install -U pip
	pip install -r requirements.txt

server:
	docker-compose up -d

server-clean:
	docker-compose down -v
	docker rmi ch2-mlflow
