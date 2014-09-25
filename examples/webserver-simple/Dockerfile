FROM ansible/centos7-ansible:stable

# Retrieve your playbooks.  Here we have them stored in a git repo
ADD ansible /srv/example/
WORKDIR /srv/example

# Bootstrapping is over, now run ansible on your playbook to finish configuring
# your docker image.
RUN ansible-playbook site.yml -c local

# We can mix docker configuration of the container with ansible configuration
# if we want to
EXPOSE 22 3000 80

# And then start up our service
ENTRYPOINT [“systemctl start httpd”]
