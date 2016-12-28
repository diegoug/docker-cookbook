# Docker CookBook
It is a compilation of best practices and techniques in Docker, applied to small projects that can be executed in local or production environments; Through these examples you will have a very clear idea of how to extend or optimize your development environments.

**Share your knowledge**
If you see that you can contribute to improve a technique or want to show a technique please send a pull request.

## Index
* [Dependencies](#dependencies)
* [Compose](#compose)
* [Best practices](#best-practices)
	* [Make file](#make-file)
	* [Environment variables](#enviroment-variables)
	* [Application directory](#application-directory)
	* [Application ports](#application-ports)
	* [Network aliase](#network-aliase)
* [Example Applications](#example-applications)
	* Main aplication
		* [Django](#django)
		* [Nodejs]()
		* [Django + Nodejs]()
	* Native services
	    * [Nginx]()
	    * [SSH]()
		* [Redis - MongoDB - Mysql - PostgreSQL]()
		* [Sentry]()
		* [Kibana - LogStach - ElasticSearch]()
		* [Jenkins]()

## Dependencies
To work with these examples it is necessary to have docker and Compose installed in versions that can work with the YAML compose configuration file in version two.

- [Docker compose file V2 reference](https://docs.docker.com/compose/compose-file/#version-2)
- [Docker Engine 1.10.0+](https://docs.docker.com/engine/installation/) - Installation guide in Linux
- [Compose 1.6.0+](https://docs.docker.com/compose/install/#/install-using-pip) - Installation guide using PIP

## Compose
Docker compose allows us to efficiently deploy our development or production environments, compose is responsible for running and managing services (such as containers) that we have configured in the YAML file.

##### Example:
Docker-compose.yml
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
##### execution:
```
$ docker-compose up -d
Starting cookbook-n-nodejs-development
$ docker-compose ps
             Name                        Command                 State            Ports
----------------------------------------------------------------------------------------------------
cookbook-n-nodejs-development    /bin/sh -c forever start / ...   Up      0.0.0.0:8000->8000/tcp, 0.0.0.0:8081->8081/tcp
```

[Back to Index](#index)

## Best practices
This is a compilation of many good practices that can be found to work at Docker.

[Back to Index](#index)

### Make file
When compiling a list of useful terminal commands the Make file is an excellent option, because it is simple and straightforward, making this the best option even above adding an alias command in the bashrc or even above creating A bash script; Allowing us to quickly perform the necessary tasks on each project, such as compiling, initializing or stopping a project

##### Example:
Dockerfile
```
build-development:
	cp app/requirements.txt docker/development/django/
	cd docker/development/django/ && docker build -t "cookbook/django-development" .
	rm -rf docker/development/django/requirements.txt
```
##### execution:
```
$ make build-development
cp app/requirements.txt docker/development/django/
cd docker/development/django/ && docker build -t "cookbook/django-development" .
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM centos:centos7
 ---> 980e0e4c79ec
Step 2 : MAINTAINER diego.uribe.gamez@gmail.com
 ---> Using cache
 ---> 80022fc9df12
Step 3 : RUN yum -y update
 ---> Using cache
 ---> a53cb821ced1
[...]
Successfully built 7fc6fe2c7fbb
rm -rf docker/development/django/requirements.txt
```

[Back to Index](#index)

### Enviroment variables
Writing directly in the code configuration variables is a bad practice, and passing code files with variables is not so useful, because we will have to ignore files that may or may not break our application; A healthy way to pass this information is through environment variables, but if we write these variables directly in the compose file we would also have to ignore it for production and it is not combeniente, that is why using an .env file may be the best option, then We configure the compose file with environment variables and this takes them by default of the .env file unless it is told otherwise, in this way we only ignore the .env file for production, and as this only has the definition of the Environment variables do not put at risk the architecture and neither the integrity of the application.

##### Example:
.env
```
DJANGO_PORT=8000
```
Docker-compose.yml
```
version: '2'
services:
  django:
    image: cookbook/django-development
    container_name: cookbook-d-django-development
    volumes:
      - ../../app:/opt/app
    ports:
      - "${DJANGO_PORT}:${DJANGO_PORT}"
```
##### execution:
```
docker ps
CONTAINER ID        IMAGE                 COMMAND                      PORTS               NAMES
4abc29037371 cookbook/django-development "/bin/sh -c 'cd /opt/" 0.0.0.0:8000->8000/tcp   django-dev
```

[Back to Index](#index)

### Application directory
Developing the application both in production and in a development environment is very important for any product.
* [Production](#application-directory-production)
* [Development](#application-directory-development)

[Back to Index](#index)

#### Application directory production
Add the directory of the application in the image of Docker, this way we can keep anonymous the directory of our application of the file system of the server, and in this way we anticipate that any changes of our application in the file system can affect our server , Also allows us to perform a better handling of the containers in the deployment for production.

##### Example:
Dockerfile
```
build-production:
	cp -r app/ docker/production/django/app/
	cd docker/production/django/ && docker build -t "cookbook/django-production" .
	rm -rf docker/production/django/app/
```
##### Execution:
```
$ make build-production
cp -r app/ docker/production/django/app/
cd docker/production/django/ && docker build -t "cookbook/django-production" .
Sending build context to Docker daemon  29.7 kB
Step 1 : FROM centos:centos7
 ---> 980e0e4c79ec
Step 2 : MAINTAINER diego.uribe.gamez@gmail.com
 ---> Using cache
 ---> 80022fc9df12
Step 3 : RUN yum -y update
 ---> Using cache
 ---> a53cb821ced1
[...]
Step 10 : COPY app/ /opt/app/
 ---> c2b3e2d08834
Removing intermediate container 37435aced59b
Step 11 : RUN pip install -r /opt/app/requirements.txt
 ---> Running in e8cdc7913f82
[...]
Successfully installed Django-1.9.7 MySQL-python-1.2.5 gunicorn-19.6.0
 ---> 7c5d2a58fcf4
Removing intermediate container e8cdc7913f82
Successfully built 7c5d2a58fcf4
rm -rf docker/production/django/app/
```

[Back to Index](#index)

#### Application directory development
the application directory must be in bypass between our local host and the main application container, to be able to program and view the results of the changes in execution.

##### Example:
Dockerfile
```
build-development:
	cp app/requirements.txt docker/development/django/
	cd docker/development/django/ && docker build -t "cookbook/django-development" .
	rm -rf docker/development/django/requirements.txt
```
docker-compose.yml
```
services:
  django:
    image: cookbook/django-development
    container_name: cookbook-d-django-development
    volumes:
      - ../../app:/opt/app
```
##### Execution:
```
$ make build-development
cp app/requirements.txt docker/development/django/
cd docker/development/django/ && docker build -t "cookbook/django-development" .
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM centos:centos7
 ---> 980e0e4c79ec
Step 2 : MAINTAINER diego.uribe.gamez@gmail.com
 ---> Using cache
 ---> 80022fc9df12
Step 3 : RUN yum -y update
 ---> Using cache
 ---> a53cb821ced1
[...]
Step 10 : COPY requirements.txt /tmp/requirements.txt
 ---> Using cache
 ---> 621ea63d6336
Step 11 : RUN pip install -r /tmp/requirements.txt
 ---> Using cache
 ---> 283e44f624a5
Step 12 : RUN rm -f /tmp/requirements.txt
 ---> Using cache
 ---> 7fc6fe2c7fbb
Successfully built 7fc6fe2c7fbb
rm -rf docker/development/django/requirements.txt
$ make start-development
cd docker/development/ && docker-compose up -d
Creating cookbook-d-django-development
```

[Back to Index](#index)

### Application ports
Exposing or sharing ports is a key part of working on an application.
* [Production](#application-ports-production)
* [Development](#application-ports-development)

[Back to Index](#index)

### Application ports production
In a production environment it is convenient to expose the container ports that provide a service that is running in the container, it is quite useful to scale the application.

##### Example:
Docker-compose.yml
```
version: '2'
services:
  django:
    restart: always
    image: cookbook/django-production
    container_name: cookbook-d-django
    expose:
      - '${DJANGO_PORT}'
```
##### execution:
```
docker ps
CONTAINER ID          IMAGE                      COMMAND                PORTS        NAMES
90329f1d94bd   cookbook/django-production   "/bin/sh -c 'cd /opt/"      80/tcp      d-django
```

[Back to Index](#index)

### Application ports development
It is convenient to share the local ports with the ports of the containers to obtain access to the different services that are running in the development environment, such as http server, databases, debugging, etc.

##### Example:
Docker-compose.yml
```
version: '2'
services:
  django:
    image: cookbook/django-development
    container_name: cookbook-d-django-development
    volumes:
      - ../../app:/opt/app
    ports:
      - "${DJANGO_PORT}:${DJANGO_PORT}"
```
##### execution:
```
docker ps
CONTAINER ID        IMAGE                 COMMAND                      PORTS               NAMES
4abc29037371 cookbook/django-development "/bin/sh -c 'cd /opt/" 0.0.0.0:8000->8000/tcp   django-dev
```

[Back to Index](#index)

### Network aliase
We create a network, and attach it to a group of containers, it is very useful not only to assign the network to the container; If we see that the container is a service that can be used by other containers we can put an alias on the network so that the containers that are in the same network can see the alias that we place to the container that will provide the service, a example can be with a database.

##### Example:
Docker-compose.yml
```
version: '2'
networks:
   cookbook:
     external: true
services:
  mysql:
    image: mysql
    container_name: mysql-development
    ports:
      - "${MYSQL_PORT}:${MYSQL_PORT}"
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE_NAME}
    volumes:
      - /var/lib/mysql-cookbook:/var/lib/mysql
    networks:
        cookbook:
            aliases:
                - ${MYSQL_HOST}
```
##### execution:
```
$ docker-compose up -d
Starting cookbook-n-nodejs-development
$ docker-compose ps
CONTAINER ID IMAGE         COMMAND            CREATED      STATUS              PORTS             NAMES
9e593025020d  mysql "docker-entrypoint.sh" 6 hours ago  Up 4 seconds 0.0.0.0:3306->3306/tcp mysql-development
```

[Back to Index](#index)

## Example Applications
Through a clear example of different technologies we can give an idea of how to use them and also how to scale our own developments.

[Back to Index](#index)

### Django
Django is a MVT Framework written in Python, quite robust and powerful, with many characteristics that help to develop an aplicicon in a fast and professional way.

#### Production
Python is not the best to run Django in production, that's why we need an additional layer between Nginx and Django, for that we run Django with Gunicorn as an intermediate layer and let Gunicorn handle the HTTP requests sent by Nginx, let's see the command we need to run.

##### Example:
Docker-compose.yml
```
services:
  django:
    restart: always
    image: cookbook/django-production
    container_name: cookbook-d-django
    command: /bin/sh -c "cd /opt/app; gunicorn mysite.wsgi -w 4 --max-requests 1000 --timeout 60 -b 0.0.0.0:${DJANGO_PORT}"
```
Logs
```
$ docker logs -f cookbook-d-django
[2016-12-11 23:52:55 +0000] [7] [INFO] Starting gunicorn 19.6.0
[2016-12-11 23:52:55 +0000] [7] [INFO] Listening at: http://0.0.0.0:80 (7)
[2016-12-11 23:52:55 +0000] [7] [INFO] Using worker: sync
[2016-12-11 23:52:55 +0000] [12] [INFO] Booting worker with pid: 12
[2016-12-11 23:52:55 +0000] [13] [INFO] Booting worker with pid: 13
[2016-12-11 23:52:55 +0000] [22] [INFO] Booting worker with pid: 22
[2016-12-11 23:52:55 +0000] [27] [INFO] Booting worker with pid: 27
```

Note: to know more about why use Gunicorn see the following link:
[Why do I need Nginx and something like Gunicorn?](http://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn?answertab=active#tab-top)

#### Development
To work with django in development mode is necessary to run it and if it sees a change is restarted, to achieve this directly run the command in development mode and review the logs to see its changing state.

##### Example:
Docker-compose.yml
```
services:
  django:
    image: cookbook/django-development
    container_name: cookbook-d-django-development
    volumes:
      - ../../app:/opt/app
    command: /bin/sh -c "cd /opt/app; python manage.py runserver 0.0.0.0:${DJANGO_PORT}"
```
Logs
```
$ docker logs -f cookbook-d-django-development
[11/Dec/2016 20:49:10] "GET / HTTP/1.1" 200 40
Not Found: /favicon.ico
[11/Dec/2016 20:49:10] "GET /favicon.ico HTTP/1.1" 404 1944
```

[Back to Index](#index)

### Nodejs
Node.js is a server-side engine based on Google's V8 engine.

#### Production
Nodejs in production mode can be run directly on the container

##### Example:
Docker-compose.yml
```
services:
  nodejs:
    image: cookbook/n-nodejs-production
    container_name: cookbook-n-nodejs
    command: /bin/sh -c "cd /opt/app/; node server.js"
```
Logs
```
$ docker logs -f cookbook-d-nodejs

```

#### Development
To work with django in development mode is necessary to run it and if it sees a change is restarted, to achieve this directly run the command in development mode and review the logs to see its changing state.

##### Example:
Docker-compose.yml
```
services:
  django:
    image: cookbook/django-development
    container_name: cookbook-d-django-development
    volumes:
      - ../../app:/opt/app
    ports:
      - "${DJANGO_PORT}:${DJANGO_PORT}"
    command: /bin/sh -c "cd /opt/app; python manage.py runserver 0.0.0.0:${DJANGO_PORT}"
```
Logs
```
$ docker logs -f cookbook-d-django-development
[11/Dec/2016 20:49:10] "GET / HTTP/1.1" 200 40
Not Found: /favicon.ico
[11/Dec/2016 20:49:10] "GET /favicon.ico HTTP/1.1" 404 1944
```

[Back to Index](#index)