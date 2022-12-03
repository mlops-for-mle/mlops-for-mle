init:
	pip install -U pip
	pip install fastapi[all] pandas psycopg2-binary scikit-learn

app:
	uvicorn app:app --reload

server:
	docker build -f Dockerfile -t ch6-api-with-model .
	docker run --name api-with-model -p 8000:8000 -d ch6-api-with-model

server-clean:
	docker rm -f api-with-model
	docker rmi ch6-api-with-model

dependency:
	make -C ../ch1/ server
	sleep 100
	make -C ../ch3/ server
	python ../ch3/save_model_to_registry.py

dependency-clean:
	make -C ../ch1/ server-clean
	make -C ../ch3/ server-clean
