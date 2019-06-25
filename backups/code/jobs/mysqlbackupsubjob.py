from core.jobs.backup import BackupSubJob, BackupJob
from coreinterfaces.model import MySQLBackup
from core.helper import get_date_with_file_format
from core.clients.mysqlclient import MySQLClient
from subprocess import PIPE


class MySQLBackupSubJob(BackupSubJob):
    def __init__(self, mysql_backup: MySQLBackup):
        super().__init__()
        self.mysql_backup = mysql_backup
        self.mysql_client = MySQLClient(self.mysql_backup.get_mysql_creds())
        self.backup_file_name = None
        self.backup_dir_path = "{}/{}/mysql/{}".format(
            BackupJob.get_backups_dir(),
            self.mysql_backup.get_mysql_db().get_mysql().get_machine().get_address(),
            self.mysql_backup.get_mysql_db().get_db_name()
        )
        self.file_name = self.mysql_backup.get_mysql_db().get_db_name() + ".sql"

    def get_backup_file_name(self):
        return self.backup_file_name

    def get_backup_dir_path(self):
        return self.backup_dir_path

    def get_backup(self):
        return self.mysql_backup

    def do_backup(self):
        self.backup_file_name = "{}.{}".format(self.file_name, get_date_with_file_format())
        with open(self.get_backup_file_path(), "wb+") as file:
            popen = BackupJob.popen(self.mysql_client.get_backup_bash_cmd(self.mysql_backup), stdout=file, stderr=PIPE)
            file.seek(0)
            stderr_txt = popen.stderr.read().decode()
            self.get_info().add(stderr_txt)
            BackupJob.exception_by_return_code(popen, [0], stderr=stderr_txt)
