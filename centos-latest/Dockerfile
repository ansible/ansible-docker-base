FROM centos:centos7
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN yum -y update
RUN yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git
RUN mkdir /opt/ansible/
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
ENV PATH /opt/ansible/ansible/bin:/sbin:/usr/sbin:/usr/bin
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library
ENV PYTHONPATH /opt/ansible/ansible/lib:$PYTHON_PATH
