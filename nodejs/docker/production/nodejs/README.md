dockerfiles-sct-nodejs
======================

Based on CentOS-Dockerfiles

This repo contains a recipe for making Docker container for nodejs on CentOS7.

Setup
-----

Perform the build the container:

    $ sudo docker build --rm -t <username>/nodejs .

Install nodejs requirements:

    $ sudo docker run --rm --privileged=true -v /opt/dockerfiles/nodejs/app/:/opt/nodejs/ <username>/nodejs /npm_install.sh

Launching NodeJS
----------------

### Recommendation ###
if you run the container in production, please remember to run the container nginx.

To run container in production:

    $ sudo docker run --name nodejs -d --privileged=true -v /opt/dockerfiles/nodejs/app/:/opt/nodejs/ <username>/nodejs


To work in development mode with container:

    $ sudo docker run --name dev-nodejs -d -p 8080:8080 -p 8081:8081 --privileged=true -v /opt/dockerfiles/nodejs/app/:/opt/nodejs/ <username>/nodejs /bin/bash /node_debugger.sh

Using your nodejs container in development mode
-----------------------------------------------

To acces in the application on development mode    
    
    http://127.0.0.1:8080

To acces in the element inspector
    
    http://127.0.0.1:8081/debug?port=5858
    
