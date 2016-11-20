
create-network:
	docker network create cookbook

# ------------------------------------------------------------------------------
# production -------------------------------------------------------------------
# ------------------------------------------------------------------------------

build-production:
	# logstash
	cd docker/production/logstash/ && docker build -t "cookbook/logstash" .

start-production:
	# sysctl -w vm.max_map_count=262144
	cd docker/production/ && docker-compose up -d

stop-production:
	cd docker/production/ && docker-compose stop
