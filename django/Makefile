
create-network:
	docker network create cookbook

build-prod:
	cp -r app/ docker/production/django/app/
	cd docker/production/django/ && docker build -t "cookbook/production-django" .
	rm -rf docker/production/django/app/

start-prod:
	cd docker/production/ && docker-compose up -d

stop-prod:
	cd docker/production/ && docker-compose stop

build-dev:
	cp app/requirements.txt docker/development/django/
	cd docker/development/django/ && docker build -t "cookbook/development-django" .
	rm -rf docker/development/django/requirements.txt

start-dev:
	cd docker/development/ && docker-compose up -d

stop-dev:
	cd docker/development/ && docker-compose stop

django-dev:
	docker exec -it cookbook-django-dev /bin/sh -c "cd /opt/app; python manage.py runserver 0.0.0.0:8000"