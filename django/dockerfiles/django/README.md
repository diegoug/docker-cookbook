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

    $ sudo docker run --name django -d -v /opt/dockerfiles/django/app/:/opt/django/Django/ --privileged=true <username>/django
    
To work in development mode with container:

    $ sudo docker run --name dev-django -it -p 8000:8000 -v /opt/dockerfiles/django/app/:/opt/django/Django/ --privileged=true <username>/django /bin/bash

### Commands to work in development mode with container ###

    $ cd /opt/django/
    $ source bin/activate
    $ cd Django
    ## if not install requirements
    $ pip install -r requirements.txt
    ## end if
    $ python manage.py runserver 0.0.0.0:8000
