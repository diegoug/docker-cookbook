# Docker CookBook
It is a compilation of best practices and techniques in Docker, applied to small projects that can be executed in local or production environments; Through these examples you will have a very clear idea of how to extend or optimize your development environments.

**Share your knowledge**
If you see that you can contribute to improve a technique or want to show a technique please send a pull request.

## Index
* [Dependencies](#dependencies)
* [Compose](#compose)
* [Best practices](#best-practices)
	* [Make file]()
		* [Build development]()
		* [Build production]()
		* [Other commands]()
	* [Environment variables]()
		* [.env]()
		* [.yml]()
	* [Command]()
		* [development]()
		* [production]()
* [Examples]()
	* [Main aplication]()
		* [Django]()
		* [Nodejs]()
		* [Django + Nodejs]()
	* [Native services]()
		* [Redis - MongoDB - Mysql - PostgreSQL]()
		* [Nginx]()
		* [Sentry]()
		* [Kibana - LogStach - ElasticSearch]()
		* [Jenkins]()
* [Production - Dedicated server]()
* [Production - Swarm mode]()

## Dependencies
To work with these examples it is necessary to have docker and Compose installed in versions that can work with the YAML compose configuration file in version two.

- [Docker compose file V2 reference](https://docs.docker.com/compose/compose-file/#version-2)
- [Docker Engine 1.10.0+](https://docs.docker.com/engine/installation/) - Installation guide in Linux
- [Compose 1.6.0+](https://docs.docker.com/compose/install/#/install-using-pip) - Installation guide using PIP

## Compose
Docker compose allows us to efficiently deploy our development or production environments, compose is responsible for running and managing services (such as containers) that we have configured in the YAML file.

#### Example:
[docker-compose.yml](https://github.com/diegoug/docker-cookbook/blob/master/nodejs/docker/production/docker-compose.yml) - Based on the development file for Node.js:
```
version: '2'
networks:
   cookbook:
     external: true
services:
  nodejs:
    image: cookbook/n-nodejs-development
    container_name: cookbook-n-nodejs-development
    volumes:
      - ../../app:/opt/app
    ports:
      - "${NODEJS_PORT}:${NODEJS_PORT}"
      - "${NODEJS_DEBUGGER_PORT}:${NODEJS_DEBUGGER_PORT}"
    environment:
      - NODE_PATH=/opt/node_modules/
      - NODEJS_PORT=${NODEJS_PORT}
    networks:
      - cookbook
```
#### execution:
```
$ docker-compose up -d
Starting cookbook-n-nodejs-development
$ docker-compose ps
             Name                        Command                 State            Ports
----------------------------------------------------------------------------------------------------
cookbook-n-nodejs-development    /bin/sh -c forever start / ...   Up      0.0.0.0:8000->8000/tcp, 0.0.0.0:8081->8081/tcp
```

