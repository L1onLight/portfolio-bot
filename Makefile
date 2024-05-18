SHELL := /bin/bash

init:
	python3 -m venv .venv && source ./.venv/bin/activate && pip install -r requirements.txt

docker_build:
	docker compose -f docker-compose.yaml up --build

docker_up:
	docker compose up