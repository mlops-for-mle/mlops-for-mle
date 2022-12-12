init:
	pip install -U pip
	pip install "fastapi[all]"

main:
	uvicorn main:app --reload

crud-path:
	uvicorn crud_path:app --reload

crud-query:
	uvicorn crud_query:app --reload

crud-pydantic:
	uvicorn crud_pydantic:app --reload

server:
	docker build -f Dockerfile -t ch5-api-server .
	docker run --name api-server -p 8000:8000 -d ch5-api-server

server-clean:
	docker rm -f api-server
	docker rmi ch5-api-server
