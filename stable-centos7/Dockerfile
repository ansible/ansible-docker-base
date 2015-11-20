# Latest version of centos
FROM centos:centos7
MAINTAINER James Cuzella <james.cuzella@lyraphase.com>
RUN yum clean all && \
    yum -y install epel-release && \
    yum -y groupinstall "Development tools" && \
    yum -y install python-devel MySQL-python sshpass && \
    yum -y install acl sudo && \
    sed -i -e 's/^Defaults.*requiretty/Defaults    !requiretty/' -e 's/^%wheel.*ALL$/%wheel    ALL=(ALL)    NOPASSWD: ALL/' /etc/sudoers && \
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip \
    pip install pyrax pysphere boto passlib dnspython && \
    yum -y remove $(rpm -qa "*-devel") && \
    yum -y groupremove "Development tools" && \
    yum -y autoremove && \
    yum -y install bzip2 file findutils gem git gzip hg procps-ng svn sudo tar which unzip xz zip

RUN mkdir /etc/ansible/
RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts
RUN pip install ansible

CMD ["/bin/bash"]
