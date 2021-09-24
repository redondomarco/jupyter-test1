include .env
RUN = docker-compose run --no-deps --rm -u root jupyterhub

build:
	docker build -t jupyterhubmr:0.1 .

rebuild: stop build-JRM start ipython3

start:
	@docker-compose up -d
	@echo 'jupyterhub inicializado en http://localhost:8000'

stop:
	@docker-compose down

restart: stop start
	
status:
	@docker-compose ps

shell:
	${RUN} /bin/bash

crea_home:
	mkdir -p datos

install: crea_home start build set-perms

ipython3:
	docker-compose run --no-deps --rm -u jupyter jupyterhub ipython3
