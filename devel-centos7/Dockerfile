# Latest version of centos
FROM centos:centos7
MAINTAINER James Cuzella <james.cuzella@lyraphase.com>
RUN yum clean all && \
    yum -y install epel-release && \
    yum makecache all && \
    yum -y upgrade glibc nscd ca-certificates && \
    yum -y update && yum -y swap fakesystemd systemd && \
    yum -y groups mark convert && \
    yum -y groups mark install "Development Tools" && \
    yum -y groups mark convert "Development Tools" && \
    yum -y groupinstall "Development Tools" && \
    yum -y install libffi-devel openssl-devel && \
    yum -y install python-devel MySQL-python sshpass && \
    yum -y install acl sudo && \
    sed -i -e 's/^Defaults.*requiretty/Defaults    !requiretty/' -e 's/^%wheel.*ALL$/%wheel    ALL=(ALL)    NOPASSWD: ALL/' /etc/sudoers && \
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip && \
    pip install --upgrade pip && \
    pip install requests[security] && \
    pip install pyrax pysphere boto boto3 passlib dnspython && \
    sh -c 'yum -y remove libffi-devel || yum -y --setopt=tsflags=noscripts remove libffi-devel' && \
    yum -y remove $(rpm -qa "*-devel") && \
    yum -y groupremove "Development tools" && \
    yum -y autoremove && \
    yum -y install bzip2 file findutils gem git gzip hg procps-ng svn sudo tar which unzip xz zip && \
    yum clean all && rm -rf /var/cache/yum

RUN mkdir /etc/ansible/
RUN echo -e '[local]\nlocalhost\n' > /etc/ansible/hosts
RUN mkdir /opt/ansible/
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
RUN perl -p -i -e  's/ansible\/ansible-modules-(core|extras)/ReturnPath\/ansible-modules-\1/' /opt/ansible/ansible/.gitmodules
RUN git submodule update --init
## REVERTME: When ansible module bugs are fixed, revert the forced submodule updates
# Force this even more... Git stores these submodule HEAD refs somewhere else besides .gitmodules now?? WTF!?
RUN cd /opt/ansible/ansible/lib/ansible/modules/core && git pull origin devel && git checkout devel && \
    cd /opt/ansible/ansible/lib/ansible/modules/extras && git pull origin devel && git checkout devel
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin
ENV PYTHONPATH /opt/ansible/ansible/lib
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library
# Workaround bug in pip / pylockfile: http://pad.lv/1472101
# If HOME is a volume mount, causes infinite loop in pip trying to write lock
ENV XDG_CACHE_HOME /tmp/
RUN source /opt/ansible/ansible/hacking/env-setup && \
    chmod 777 $ANSIBLE_HOME/lib/ansible.egg-info && \
    chmod -R 666 $ANSIBLE_HOME/lib/ansible.egg-info/*
RUN echo 'source /opt/ansible/ansible/hacking/env-setup' >> /etc/profile.d/ansible.sh
RUN echo 'stat --format=%a $ANSIBLE_HOME/lib/ansible.egg-info | grep -iq '^777' || chmod 777 $ANSIBLE_HOME/lib/ansible.egg-info' >> /etc/profile.d/ansible.sh
RUN echo 'stat --format=%a $ANSIBLE_HOME/lib/ansible.egg-info/* | grep -vq '^666' && chmod -R 666 $ANSIBLE_HOME/lib/ansible.egg-info/*' >> /etc/profile.d/ansible.sh

CMD /bin/bash
