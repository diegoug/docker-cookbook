
create-network:
	docker network create cookbook

# ------------------------------------------------------------------------------
# production -------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-production:
	# django
	cp -r app/django/ docker/production/django/app/
	cd docker/production/django/ && docker build -t "cookbook/dn-django-production" .
	rm -rf docker/production/django/app/
	# nodejs
	cp -r app/nodejs/ docker/production/nodejs/app/
	cd docker/production/nodejs/ && docker build -t "cookbook/dn-nodejs-production" .
	rm -rf docker/production/nodejs/app/

start-production:
	cd docker/production/ && docker-compose up -d

stop-production:
	cd docker/production/ && docker-compose stop

# ------------------------------------------------------------------------------
# development ------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-development:
	# django
	cp app/django/requirements.txt docker/development/django/
	cd docker/development/django/ && docker build -t "cookbook/dn-django-development" .
	rm -rf docker/development/django/requirements.txt
	# nodejs
	cp app/nodejs/package.json docker/development/nodejs/
	cd docker/development/nodejs/ && docker build -t "cookbook/dn-nodejs-development" .
	rm -rf docker/development/nodejs/package.json

start-development:
	cd docker/development/ && docker-compose up -d

stop-development:
	cd docker/development/ && docker-compose stop
