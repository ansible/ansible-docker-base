These are base docker images that include ansible.  Ansible maintains these
images so that people can easily build docker images using ansible playbooks.

The images in this repository use centos7 as their base.  If you'd rather base
your image on ubuntu14.04, please see
https://registry.hub.docker.com/u/ansible/ubuntu14.04-ansible/ instead


Supported tags and respective Dockerfile links
==============================================

* latest, devel ([Dockerfile](https://github.com/ansible/ansible-docker-base/blob/master/devel-ubuntu14.04/Dockerfile))
* stable ([Dockerfile](https://github.com/ansible/ansible-docker-base/blob/master/stable-ubuntu14.04/Dockerfile))
* $major_version.$minor_version

devel and latest point to an image built with a recent checkout of ansible's
development branch.

stable is built with the latest ansible release on pypi.

The $major.$minor tags are useful if you have to use a specific older version
of the images for some reason.  Note that we do not build new versions of these
older images.  We only build for versions that correspond to the devel and
stable tags.


Building your Docker images with an ansible playbook
====================================================

The following example shows how to use the above images
to build a Docker image using a playbook:

[pending]

files for this can be found in the examples directory



Rebuilding automatically when the ansible image updates
-------------------------------------------------------

If you are using a docker hub automated build to build your images you can set
your image to rebuild whenever the base ansible image is updated:

1) Go to the docker hub page for your repository.
2) In the sidebar labeled Settings, find the entry marked "Repository Links"
3) On the Repository Links page, enter the ansible repository you are layering
   your image on top of.  For instance, if you are using the
   ubuntu14.04-ansible repository, enter ansible/ubuntu14.04-ansible
   into the "Repository Name" box and click "add".
4) Docker hub will now automatically rebuild your image whenever that ansible
   repository has a new build.
