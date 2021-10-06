#include .env
RUN = docker-compose run --no-deps --rm -u root jupyterhub

build:
	docker build -t jupyterhubmr:0.1 .

rebuild: stop build start ipython3

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
	mkdir -p datos/fuentes

install: crea_home build set-perms

ipython3:
	docker-compose run --no-deps --rm -u jupyter jupyterhub ipython3 -i modules/shellmr.py

set-perms:
	${RUN} chown -R jupyter:jupyter /srv/jupyterhub