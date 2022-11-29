init:
	pip install -U pip
	pip install fastapi[all] pandas psycopg2-binary scikit-learn

app:
	uvicorn app:app --reload

server-with-model:
	docker build -f image_with_model/Dockerfile -t ch6-api-with-model .
	docker run --name api-with-model -p 8000:8000 -d ch6-api-with-model

server-without-model:
	docker build -f image_without_model/Dockerfile -t ch6-api-without-model .
	docker run --name api-without-model --network ch3_default -p 8000:8000 -d ch6-api-without-model

server-clean:
	docker rm -f api-with-model api-without-model
	docker rmi -f ch6-api-with-model ch6-api-without-model

dependency:
	make -C ../ch1/ server
	sleep 100
	make -C ../ch3/ server
	python ../ch3/upload_model.py

dependency-clean:
	make -C ../ch1/ server-clean
	make -C ../ch3/ server-clean
