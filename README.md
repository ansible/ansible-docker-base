Ansible-Docker-Base
===================

These are base docker images that include Ansible.  

Ansible, Inc maintains these images so that people can easily build docker images from ansible playbooks.

While Ansible modules can help you deploy container images, this document is about how to use ansible to efficiently describe and build them as well.

Obtaining these Images from DockerHub
=====================================

Ansible, Inc content on DockerHub lives at https://registry.hub.docker.com/u/ansible/

There are base images available currently for CentOS 7 and Ubuntu 14.04 LTS, using both the latest
stable version of Ansible as well as development branch snapshots.

Building Your Own Container Based on an Ansible Image
=====================================================

By specifying a Dockerfile, it is easy to describe a container image primarily defined by an ansible-playbook.

Take a look at [this Dockerfile](https://github.com/ansible/ansible-docker-base/blob/master/examples/webserver-simple/Dockerfile) for a sample Dockerfile

To build this image, simply cd into the Dockerfile directory and run:

    docker build -t webserver_simple .
    
This will produce an image tagged "webserver_simple" based on the Ansible playbook run.  [Here's the playbook describing the configuration](https://github.com/ansible/ansible-docker-base/blob/master/examples/webserver-simple/ansible/site.yml).

You may wish to connect your repository with this information to DockerHub, to trigger automatic rebuilds of your container
images when your ansible playbooks change.

Selecting Versions of Ansible
=============================

The example dockerfile above selects the latest CentOS tag of Ansible's Docker images.  The first line of the Dockerfile can be changed to select another base operating system or Ansible version should you wish to use a different OS or different Ansible version.

Examples:

    FROM ansible/centos7-ansible:stable
    FROM ansible/centos7-ansible:devel
    FROM ansible/ubuntu14.04-ansible:stable
    FROM ansible/ubuntu14.04-ansible:stable
    
Ansible images on DockerHub will be updated periodically.


Deploying Your Ansible-Built Docker Containers with Ansible
===========================================================

Once available on a registry, images can be deployed using the [Ansible Docker Module](http://docs.ansible.com/docker_module.html).  This can be a lightweight
way to specify what containers should run on which hosts.

Here's a minimal example of running a Tomcat container on all of your hosts:

    - hosts: web
      sudo: yes
      tasks:
        - name: run tomcat servers
          docker: image=my-tomcat command="service tomcat6 start" ports=8080

Replace the "image" parameter with the name of the image above in your registry.

For more information, consult the [Ansible Docker module documentation](http://docs.ansible.com/docker_module.html)

Rebuilding Automatically when the Ansible Image Updates
=======================================================

If you are using a Docker Hub automated build to build your images you can set
your image to rebuild whenever the base ansible image (hosted by Ansible, Inc) is updated:

1) Go to the docker hub page for your repository.
2) In the sidebar labeled Settings, find the entry marked "Repository Links"
3) On the Repository Links page, enter the ansible repository you are layering
   your image on top of.  For instance, if you are using the
   ubuntu14.04-ansible repository, enter ansible/ubuntu14.04-ansible
   into the "Repository Name" box and click "add".
4) Docker hub will now automatically rebuild your image whenever that ansible
   repository has a new build.
   
Questions?
==========

If you'd like to talk about Ansible+Docker, stop by the [ansible-project mailing list](https://groups.google.com/forum/#!forum/ansible-project) or #ansible on irc.freenode.net for IRC.


