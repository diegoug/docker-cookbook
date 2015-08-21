FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update && yum clean all

RUN yum -y install epel-release && yum clean all
RUN yum -y install python-devel python-setuptools python-pip && yum clean all
RUN pip install --upgrade pip
RUN yum -y install gcc gcc-c++ && yum clean all
RUN yum -y install supervisor && yum clean all

RUN cd /opt && mkdir django

ADD ./start.sh /django_dev.sh
RUN chmod 755 /django_dev.sh

ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

ADD django.ini /etc/supervisord.d/django.ini
RUN mkdir /var/log/django/
RUN touch /var/log/django/supervisor.log
RUN touch /var/log/django/supervisor.error.log

EXPOSE 8001

CMD ["/bin/bash", "/start.sh"]