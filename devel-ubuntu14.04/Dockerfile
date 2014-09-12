# Latest Ubuntu LTS
FROM ubuntu:14.04
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python-yaml python-jinja2 git
RUN mkdir /opt/ansible/
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
ENV PATH /opt/ansible/ansible/bin:/sbin:/usr/sbin:/usr/bin
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library
ENV PYTHONPATH /opt/ansible/ansible/lib:$PYTHON_PATH
