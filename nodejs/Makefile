
create-network:
	docker network create cookbook

# ------------------------------------------------------------------------------
# production -------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-production:
	# nodejs
	cp -r app/ docker/production/nodejs/app/
	cd docker/production/nodejs/ && docker build -t "cookbook/n-nodejs-production" .
	rm -rf docker/production/nodejs/app/

start-production:
	cd docker/production/ && docker-compose up -d

stop-production:
	cd docker/production/ && docker-compose stop

# ------------------------------------------------------------------------------
# development ------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-development:
	# nodejs
	cp app/package.json docker/development/nodejs/
	cd docker/development/nodejs/ && docker build -t "cookbook/n-nodejs-development" .
	rm -rf docker/development/nodejs/package.json

start-development:
	cd docker/development/ && docker-compose up -d

stop-development:
	cd docker/development/ && docker-compose stop
