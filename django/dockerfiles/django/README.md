dockerfiles-sct-django
======================

Based on CentOS-Dockerfiles

This repo contains a recipe for making Docker container for django on CentOS7.

Setup
-----

Perform the build the container:

    $ sudo docker build --rm -t <username>/django .

Launching Django
----------------

To run container:

    $ sudo docker run --name django -d -v /opt/dockerfiles/django/app/:/opt/django/ --privileged=true <username>/django
    
To work in development mode with container:

    $ sudo docker run --name dev-django -d -p 8000:8000 -v /opt/dockerfiles/django/app/:/opt/django/ --privileged=true <username>/django

Using your django container in development mode
-----------------------------------------------

To run the application on development mode 

    $ sudo docker exec -it dev-django /django_dev.sh

To acces in the application on development mode
    
    http://127.0.0.1:8000
