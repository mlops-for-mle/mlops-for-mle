init:
	pip install -U pip
	pip install fastapi[all] pandas psycopg2-binary scikit-learn

main:
	uvicorn main:app --reload

dependency:
	make -C ../ch1/ server
	sleep 100
	make -C ../ch3/ server

dependency-clean:
	make -C ../ch1/ server-clean
	make -C ../ch3/ server-clean
