from coreinterfaces.job import Job
from coreinterfaces.model import MySQLBackupCheck
from core import model
from core.helper import gzip_open, get_last_modified_file_from_wildcard
from core.jobs.backup import BackupJob
from core.clients.mysqlclient import MySQLClient
from subprocess import PIPE
from coreinterfaces.info import Info
from core.info import ListInfo
from tempfile import TemporaryFile


class MySQLBackupCheckJob(Job):
    mysql_creds_test = model.MySQLCreds(model.MySQL(model.Machine("host"), 3306), "root", "password")

    #mysql_creds_test = model.MySQLCreds(model.MySQL(model.Machine("172.20.12.218"), 3306), "root", "root")
#mysql_creds_test = model.MySQLCreds(model.MySQL(model.Machine("mysql-for-backups.lsbt.iba"), 3306), "root", "Passw0rd")

    mysql_client_test = MySQLClient(mysql_creds_test)
    mysql_db_test = "test"

    def __init__(self, mysql_backup_check: MySQLBackupCheck):
        self.mysql_backup_check = mysql_backup_check
        self.mysql_client_main = MySQLClient(self.mysql_backup_check.get_mysql_backup().get_mysql_creds())
        self.backups_wildcard = "{}/{}/mysql/{}/*".format(
            BackupJob.get_backups_dir(),
            self.mysql_backup_check.get_mysql_backup().get_mysql_db().get_mysql().get_machine().get_address(),
            self.mysql_backup_check.get_mysql_backup().get_mysql_db().get_db_name()
        )
        self.info = ListInfo()

    def do(self):
        latest_backup = get_last_modified_file_from_wildcard(self.backups_wildcard)
        self.mysql_client_test.drop_db(self.mysql_db_test)
        self.mysql_client_test.create_db(self.mysql_db_test)
        with gzip_open(latest_backup) as backup:
            BackupJob.popen(self.mysql_client_test.get_mysql_db_cmd(self.mysql_db_test), stdin=backup)
        mysql_backup_cmd = \
            MySQLClient.get_mysqldbcompare_cmd(
                self.mysql_creds_test, self.mysql_db_test,
                self.mysql_backup_check.get_mysql_backup().get_mysql_creds(),
                self.mysql_backup_check.get_mysql_backup().get_mysql_db().get_db_name()
            )
        with TemporaryFile() as file:
            popen = BackupJob.popen(mysql_backup_cmd, stdout=file, stderr=PIPE)
            file.seek(0)
            stdout_txt = file.read().decode()
            stderr_txt = popen.stderr.read().decode()
            self.get_info().add(stdout_txt)
            self.get_info().add(stderr_txt)
            BackupJob.exception_by_return_code(popen, [0], stdout_txt, stderr_txt)

    def get_info(self) -> Info:
        return self.info
