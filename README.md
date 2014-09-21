Building the docker base images
===============================

cd centos-latest
docker build -t 'abadger/ansible:centos7-ansible1.8-v2'  .

cd ubuntu-lts-latest
docker build -t 'abadger/ansible:ubuntu14.04-ansible1.8-v2'  .

With an ansible playbook
========================

The following example shows how to use the above images
to build a Docker image using a playbook:

pending
