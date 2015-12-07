FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install redis; yum clean all

EXPOSE 6379

CMD [ "redis-server" ]

