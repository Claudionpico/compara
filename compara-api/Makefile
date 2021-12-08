ifndef ENVIRONMENT
ENVIRONMENT=prod
endif

help:
	@echo "compara-api"
	@echo "Environment: "$(ENVIRONMENT)
	@echo "Docker"
	@echo "make build"
	@echo "make run"
	@echo "make kill"

clean:
	rm -rf *-dev*.yaml
	rm -rf *-prod*.yaml

build:
	docker build --rm -t $(IMAGE) .

run:
	docker run -d --name $(TAG) --env-file $(ENV) -p $(LPORT):$(DPORT) $(IMAGE)

dev:
	@if [ "$(shell $(LS) )" != "" ]; then\
        docker rm -f `docker ps -a -f "status=exited" -f "name=$(TAG)" -q`;\
  fi
	docker run -it -v $(BASE_REPO):/opt/$(TAG) --name $(TAG) --env-file $(ENV) -p $(LPORT):$(DPORT) $(IMAGE) ash

kill:
	docker kill $(TAG)
	docker rm $(TAG)

rm:
	docker rmi -f `docker images $(TAG) -q`

tag:
	docker tag $(IMAGE) $(REG)/$(IMAGE)

push:
	docker push $(REG)/$(IMAGE)


LPORT=8000
DPORT=8000
BASE_REPO=$(shell pwd)/src
TAG=compara-api
IMAGE=$(TAG):$(ENVIRONMENT)
ENV=./Environment

SHELL := /bin/bash
LS=docker ps -a -f "status=exited" -f "name=$(TAG)" -q
include $(ENV)
