FROM centos:centos7
MAINTAINER diego.uribe.gamez@gmail.com

RUN yum -y update

RUN yum -y install epel-release
RUN yum -y install gcc gcc-c++
RUN yum -y install mariadb mariadb-devel MySQL-python

RUN yum -y install python-devel python-setuptools python-pip
RUN pip install --upgrade pip

RUN yum -y install ssh openssh-server passwd

RUN yum clean all

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm -f /tmp/requirements.txt

COPY entry.sh /entry.sh
RUN chmod 0777 /entry.sh
RUN chmod +x /entry.sh

RUN mkdir /root/.ssh/

EXPOSE 22
ENTRYPOINT ["/entry.sh"]

CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]

EXPOSE 8000