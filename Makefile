SHELL := /bin/bash

init:
	python3 -m venv .venv && source ./.venv/bin/activate && pip install -r requirements.txt
docker_build:
	docker-compose -f docker-compose.yaml up --build
docker_up:
	docker-compose up
run:
	python ./app/main.py
full-rebuild:
	docker-compose down && docker-compose -f docker-compose.yaml up --build -d
logs:
	docker-compose logs -f