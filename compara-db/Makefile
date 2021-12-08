help:
	@echo "DB"
	@echo "Docker"
	@echo "make build [Builds docker image]"
	@echo "make run	[Runs docker image in daemons mode]"

build:
	docker build --rm -t $(TAG) .

run:
	docker run -d --name $(TAG) --env-file $(ENV) -p $(LPORT):$(DPORT) $(TAG)

connect:
	mysql -u root --password=$(MYSQL_ROOT_PASSWORD) -h 127.0.0.1 -P $(LPORT)

kill:
	docker kill $(TAG)
	docker rm $(TAG)

LPORT=3306
DPORT=3306
TAG=compara-db
ENV=./Environment
SHELL := /bin/bash
TAG=compara-db
IMAGE=compara-db

include $(ENV)
