FROM centos
ARG repository=
RUN \ 
    # Python 3.6
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u && \
    yum install -y python36u-pip.noarch && \
    pip3.6 install mysql-connector cx-Oracle heapq-max croniter && \
    # MySQL
    yum install -y mysql && \
    # MySQL Utilities
    rpm -i https://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-python-2.1.7-1.el7.x86_64.rpm && \
    rpm -i https://cdn.mysql.com/archives/mysql-utilities/mysql-utilities-1.6.5-1.el7.noarch.rpm && \
    # Oracle instantclient
    yum install -y http://$repository/oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm http://$repository/oracle-instantclient18.3-devel-18.3.0.0.0-1.x86_64.rpm && \
    # Other
    yum install -y sshpass rsync openssh-clients libaio
VOLUME /opt/backups /opt/main-script
ENV LD_LIBRARY_PATH=/usr/lib/oracle/18.3/client64/lib
CMD [ "/usr/bin/python3.6", "/opt/main-script/main.py" ]
