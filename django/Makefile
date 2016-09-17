
create-network:
	docker network create cookbook

# ------------------------------------------------------------------------------
# production -------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-production:
	cp -r app/ docker/production/django/app/
	cd docker/production/django/ && docker build -t "cookbook/django-production" .
	rm -rf docker/production/django/app/

start-production:
	cd docker/production/ && docker-compose up -d

stop-production:
	cd docker/production/ && docker-compose stop

# ------------------------------------------------------------------------------
# development ------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-development:
	cp app/requirements.txt docker/development/django/
	cd docker/development/django/ && docker build -t "cookbook/django-development" .
	rm -rf docker/development/django/requirements.txt

start-development:
	cd docker/development/ && docker-compose up -d

stop-development:
	cd docker/development/ && docker-compose stop
