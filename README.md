These are base docker images that include ansible.  Ansible maintains these
images so that people can easily build docker images using ansible playbooks.

Naming convention:


Organization/BaseImage-Software:SoftwareVersion

SoftwareVersion == devel will be a snapshot from the github devel branch

SoftwareVersion == stable will be the latest release on pypi

Example: ansible/centos7-ansible:1.7


Building the docker base images
===============================


Github and Dockerhub integration
--------------------------------

For building these images, we use the docker hub build triggers to request an
automated build on docker hub.  We use this instead of a github hook so that
we can choose to test a commit in our jenkins instance before having docker
build and push it or, on the other side, can choose to create a new build when
we make a new release of ansible (which is outside of the ansible-docker-base
repository and therefore wouldn't be discovered).

On dockerhub, we have two image repositories:
* ansible/ubuntu14.04-ansible
* ansible/centos7-ansible

These both use the dockerfiles in the
https://github.com/ansible/ansible-docker-base git repository but they build
two differently named images.  We have to perform our build steps once for
each of these repositories but the steps are the same.

1) Go to the docker hub page for one of the repositories above.
   For instance: https://registry.hub.docker.com/u/ansible/ansible-ubuntu14.04/
2) In the sidebar labeled Settings, find the entry marked "Build Triggers"
3) On the Build Triggers page, copy the trigger url to your clipboard
4) Run the scripts/request-build.py script
5) When prompted, enter a name for this repository
6) At the next prompt, paste the trigger url into the script
7) The script will trigger automated rebuilds on dockerhub

Note: The script saves the build triggers into ~/.dockerhub-ansible-build.  So
on subsequent builds, you should be able to just type in the 


Testing
-------

[pending]

How do we test these images?  Perhaps a jenkins job that downloads the image
from dockerhub and checks that you can run ansible inside of each one.  Then
creates a derivative image (the eample, for instance)



Updating Tags
-------------

Eventually we'll want to change the dockerhub tags for images.  This might be
because we make a new major release and need to update the release numbers
we're tagging as devel and stable, we want to add more images, or it could be
that we want to change the tagging scheme.  To do this, go to the docker hub
page for the repository (for instance:
https://registry.hub.docker.com/u/ansible/centos7-ansible/  ).  Click on the
"Build details" tab.  Inside of the tab, at the top, there will be an
"Edit Build details" link.  Clicking on that takes you to a page where you can
edit the tags for the docker images we're building.



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
