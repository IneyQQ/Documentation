FROM centos
ARG repository=
RUN \
    # Nagios + ssmtp + apache \
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y perl-DBD-MySQL perl-DBI ssmtp httpd nagios && \
    sed -i 's/=mail/=mailin.iba/' /etc/ssmtp/ssmtp.conf && \
    cp /usr/share/zoneinfo/Etc/GMT-3 /etc/localtime && \
    sed -i 's/index.html/index.php/' /etc/httpd/conf/httpd.conf && \
    rm -f /etc/httpd/conf.d/welcome.conf && \
    sed -i 's/\/nagios "\(.*\)"/\/ \1\//' /etc/httpd/conf.d/nagios.conf && \
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
RUN rm -rf /root/install
VOLUME /etc/nagios /usr/lib64/nagios/plugins /var/log/nagios
EXPOSE 80
COPY nagios-run /usr/local/bin/
CMD [ "/usr/local/bin/nagios-run" ]
