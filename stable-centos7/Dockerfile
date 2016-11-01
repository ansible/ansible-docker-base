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
    yum -y groupinstall "Development tools" && \
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
RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts
RUN pip install ansible

CMD ["/bin/bash"]
