#FROM ansible/centos7-ansible:stable
FROM ansible/ubuntu14.04-ansible:stable


# Retrieve your playbooks.  Here we have them stored in a git repo
RUN mkdir /srv/example
WORKDIR /srv/example
ADD site.yml /srv/example/

# For this one we're going to retrieve a prebuilt memcached role from
# ansible-galaxy.  This could be an easy way to evaluate a role or to quickly
# get a service up and running in your infrastructure.
RUN ansible-galaxy install geerlingguy.memcached

# Bootstrapping is over, now run ansible on your playbook to finish configuring
# your docker image.
RUN ansible-playbook site.yml -c local

# We can mix docker configuration of the container with ansible configuration
# if we want to
EXPOSE 11211

# And then start up our service
ENTRYPOINT ["/usr/bin/memcached", "-u", "memcache", "-l", "0.0.0.0", "-c", "1024", "-p", "11211"]
