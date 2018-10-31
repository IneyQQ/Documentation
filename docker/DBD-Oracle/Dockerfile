FROM centos
RUN \
    # SQL*PLUS \
    yum install -y libaio && \
    rpm -ivh    http://$repository/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm \
                http://$repository/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm \
                http://$repository/oracle-instantclient12.2-odbc-12.2.0.1.0-2.x86_64.rpm \
                http://$repository/oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm && \
    # CPAN \
    yum install -y cpan && \
    perl -MCPAN -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig => 1); $c->edit(prerequisites_policy => "follow"); $c->edit(build_requires_install_policy => "yes"); $c->commit'; \
    # DBD::Oracle \
    yum install -y perl-DBI make perl-Test-Simple gcc && \
    echo "get DBD::Oracle" | cpan && \
    cd ~/.cpan/build/DBD-Oracle-*/ && env ORACLE_HOME=/usr/lib/oracle/12.2/client64 LD_LIBRARY_PATH=/usr/lib/oracle/12.2/client64/lib perl ~/.cpan/build/DBD-Oracle*/Makefile.PL -l && make && make install
VOLUME /etc/nagios /usr/lib64/nagios/plugins /var/log/nagios
EXPOSE 80
CMD [ "/usr/sbin/init" ]
