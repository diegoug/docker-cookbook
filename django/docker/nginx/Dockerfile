FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update; yum clean all
RUN yum -y install epel-release tar ; yum clean all
RUN yum -y install nginx && yum clean all

ADD nginx.conf /etc/nginx/nginx.conf
ADD django.conf /etc/nginx/conf.d/django.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN curl https://git.centos.org/sources/httpd/c7/acf5cccf4afaecf3afeb18c50ae59fd5c6504910 \
    | tar -xz -C /usr/share/nginx/html \
    --strip-components=1
RUN sed -i -e 's/Apache/nginx/g' -e '/apache_pb.gif/d' \ 
    /usr/share/nginx/html/index.html

EXPOSE 80

CMD [ "/usr/sbin/nginx" ]

