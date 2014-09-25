# Latest Ubuntu LTS
FROM ubuntu:14.04
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg-resources git python-pip
RUN mkdir /etc/ansible/
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
RUN pip install ansible