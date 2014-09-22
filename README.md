These are base docker images that include ansible.  Ansible maintains these
images so that people can easily build docker images using ansible playbooks.

Building the docker base images
===============================

pushd devel-centos7
docker build -t 'abadger/ansible:centos7-ansible1.8-v1' .
popd

pushd devel-ubuntu14.04
docker build -t 'abadger/ansible:ubuntu14.04-ansible1.8-v1' .
popd

pushd stable-centos7
docker build -t 'abadger/ansible:centos7-ansible1.7-v1' .
popd

pushd stable-ubuntu14.04
docker build -t 'abadger/ansible:ubuntu14.04-ansible1.7-v1' .
popd


With an ansible playbook
========================

The following example shows how to use the above images
to build a Docker image using a playbook:

pending
