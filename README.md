These are base docker images that include ansible.  Ansible maintains these
images so that people can easily build docker images using ansible playbooks.

Naming convention:


Organization/BaseImage-Software:SoftwareVersion

SoftwareVersion == devel will be a snapshot from the github devel branch

SoftwareVersion == stable will be the latest release on pypi

Example: ansible/centos7-ansible:1.7




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
