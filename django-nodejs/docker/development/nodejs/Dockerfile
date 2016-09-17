FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install gcc gcc-c++
RUN yum -y install make
RUN yum -y install mongodb
RUN yum clean all

RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash -
RUN yum -y install nodejs

RUN npm install -g node-inspector supervisor forever

COPY package.json /opt/package.json
RUN cd /opt/ && npm install
RUN rm -f /opt/package.json

EXPOSE 3000
