FROM ansible/centos7-ansible:stable
#FROM ansible/ubuntu14.04-ansible:stable

# Add your playbooks to the image.  Here we have them in a subdirectory
ADD ansible /srv/example/
WORKDIR /srv/example

# Bootstrapping is over, now run ansible on your playbook to finish configuring
# your docker image.
RUN ansible-playbook site.yml -c local

# We can mix docker configuration of the container with ansible configuration
# if we want to
EXPOSE 22 3000 80

# And then start up our service
ENTRYPOINT ["/usr/sbin/apachectl", "-DFOREGROUND"]
#ENTRYPOINT ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
