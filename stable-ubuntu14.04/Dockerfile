# Latest Ubuntu LTS
FROM ubuntu:14.04
MAINTAINER Toshio Kuratomi <tkuratomi@ansible.com>
RUN apt-get update && \
    apt-get install --no-install-recommends -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts

