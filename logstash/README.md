# Manage docker logs
This example is based on the tutorial given by Marcos Lilijedahl [@marcosnils](https://twitter.com/marcosnils) for the docker professional course in Platzi, the main difference is that the project uses the most updated versions of compose and the containers used in that example.

## Makefile command's
To use the commands put in parallel to the Makefile and execute the command that you want to use:

* [Create network](#create-network)
* [Build production](#build-production)
* [Start production](#start-production)
* [Stop production](#stop-production)

`$ make <command>`
##### Example:
`$ make create-network            `

### Create network
`$ make create-network           `
==
`$ docker network create cookbook`

### Build production
`$ make build-production         `
==
`$ cd docker/production/logstash/ && docker build -t "cookbook/logstash" .`

### Start production
`$ make start-production         `
==
`$ cd docker/production/ && docker-compose up -d`

[Requirement](https://www.elastic.co/guide/en/elasticsearch/reference/5.0/vm-max-map-count.html)
since 5.0, Elasticsearch only listens on localhost by default, so this image sets network.host to 0.0.0.0

As a result, Elasticsearch is more strict about the bootstrap checks that it performs, especially when checking the value of vm.max_map_count which is not namespaced and thus must be set to an acceptable value on the host

`$ sudo sysctl -w vm.max_map_count=262144`

### Stop production
`$ stop-production             `
==
`$ cd docker/production/ && docker-compose stop`
