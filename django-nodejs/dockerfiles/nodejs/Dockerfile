FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update
RUN yum -y install epel-release && yum clean all
RUN yum -y install gcc gcc-c++ && yum clean all
RUN yum -y install wget tar make
RUN yum clean all

RUN mkdir build-node
RUN cd build-node && wget http://nodejs.org/dist/v4.2.2/node-v4.2.2.tar.gz
RUN cd build-node && tar xvf node-v4.2.2.tar.gz && rm node-v4.2.2.tar.gz
RUN cd build-node && cd * && ./configure && make && make install
RUN ln -s /usr/local/bin/node /usr/bin/node
RUN ln -s /usr/local/bin/npm /usr/bin/npm
RUN cd ../../ && rm build-node/ -r -f

RUN cd /opt/ && mkdir nodejs

EXPOSE 3000