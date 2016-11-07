dockerfiles-sct-nginx
=====================

Based on CentOS-Dockerfiles

This repo contains a recipe for making Docker container for nginx on CentOS7.

Setup
-----

Perform the build the container:

    $ sudo docker build -rm -t <username>/nginx .

Launching Nginx
---------------

### Recommendation ###
if you run the container in production, remember that you must run the container nodejs.

To run container:

    $ sudo docker run -d --name=nginx -p 80:80 --link nodejs:nodejs <username>/nginx

