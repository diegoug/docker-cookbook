FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update && yum clean all

RUN yum -y install epel-release
RUN yum -y install python-devel python-setuptools python-pip
RUN pip install --upgrade pip
RUN yum -y install gcc gcc-c++ && yum clean all

RUN cd /opt && mkdir django

EXPOSE 8000