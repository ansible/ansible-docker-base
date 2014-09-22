# Latest version of centos
FROM centos:centos7
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN yum -y install epel-release
RUN yum -y update
RUN yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip
RUN pip install ansible