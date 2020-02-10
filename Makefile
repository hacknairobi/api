.PHONY: docs test

help:
	@echo "  env          create a development environment using virtualenv"
	@echo "  deps         install dependencies using pip"
	@echo "  clean        remove unwanted files like .pyc's"
	@echo "  lint         check style with flake8"
	@echo "  test         run all your tests using py.test"
	@echo "  docker-test  test with docker image & mysql (like CI)"
	@echo "  docker-build Build cs61a/ok-server image"

env:
	python3 -m venv .env && \
	source .env/bin/activate && \
	make deps

deps:
	python3 -m pip install -r dev-requirements.txt


run:
	open http://127.0.0.1:8000/
	python3 manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

clean:
	rm -rf .env

lint:
	flake8 --exclude=env,tests .

tests: test
test:
	py.test --cov-report term-missing --cov=server tests/

docker-test:
	docker-compose -f docker/docker-compose.yml -f docker/docker-compose.test.yml run --rm web

docker-build:
	find . | grep -E "(__pycache__|\.pyc|\.DS_Store|\.db|\.pyo$\)" | xargs rm -rf
	docker build -t cs61a/ok-server .