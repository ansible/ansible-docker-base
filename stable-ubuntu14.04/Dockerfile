# Latest Ubuntu LTS
FROM ubuntu:14.04
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu trusty universe"
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg_resources git python-pip
RUN pip install ansible