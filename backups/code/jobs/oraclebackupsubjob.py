from core.jobs.backup import BackupSubJob, BackupJob
from coreinterfaces.model import OracleBackup
from core.helper import get_date_with_file_format
from core.clients.oracleclient import OracleClient
from core.clients.sshclient import SSHClient
from subprocess import PIPE


class OracleBackupSubJob(BackupSubJob):
    def __init__(self, oracle_backup: OracleBackup):
        super().__init__()
        self.oracle_backup = oracle_backup
        self.oracle_client = OracleClient(self.oracle_backup.get_oracle_creds())
        self.ssh_client = SSHClient(self.oracle_backup.get_ssh_creds())
        self.backup_file_name = None
        self.backup_dir_path = "{}/{}/oracle/{}".format(
            BackupJob.get_backups_dir(),
            self.oracle_backup.get_oracle_schema().get_oracle_sid().get_oracle().get_machine().get_address(),
            self.oracle_backup.get_oracle_schema().get_schema_name()
        )
        self.backup_name = self.oracle_backup.get_oracle_schema().get_schema_name() + ".dmp"
        self.log_name = self.oracle_backup.get_oracle_schema().get_schema_name() + ".log"

    def get_backup_file_name(self):
        return self.backup_file_name

    def get_backup_dir_path(self):
        return self.backup_dir_path

    def get_backup(self):
        return self.oracle_backup

    def do_backup(self):
        self.backup_file_name = "{}.{}".format(self.backup_name, get_date_with_file_format())
        log_file_name = "{}.{}".format(self.log_name, get_date_with_file_format())
        remote_directory_path = self.oracle_client.get_directory_path(self.oracle_backup.get_oracle_dir_name())
        remote_backup_path = "{}/{}".format(remote_directory_path, self.backup_file_name)

        # Create backup
        popen = BackupJob.popen(
            self.ssh_client.popen_cmd(
                self.oracle_client.get_backup_bash_cmd(self.oracle_backup, self.backup_file_name, log_file_name)),
            stdout=PIPE, stderr=PIPE)
        stdout_txt = popen.stdout.read().decode()
        stderr_txt = popen.stderr.read().decode()
        self.get_info().add(stdout_txt)
        self.get_info().add(stderr_txt)
        BackupJob.exception_by_return_code(popen, [0], stdout_txt, stderr_txt)

        # Move backup to local repository
        popen = BackupJob.popen(
            self.ssh_client.rsync_from_remote_to_local(remote_backup_path, self.get_backup_file_path()),
            stdout=PIPE, stderr=PIPE)
        stdout_txt = popen.stdout.read().decode()
        stderr_txt = popen.stderr.read().decode()
        self.get_info().add(stdout_txt)
        self.get_info().add(stderr_txt)
        BackupJob.exception_by_return_code(popen, [0], stdout_txt, stderr_txt)

        # Delete backup from remote machine
        popen = BackupJob.popen(self.ssh_client.popen_cmd(["rm", "-f", remote_backup_path]), stdout=PIPE, stderr=PIPE)
        stdout_txt = popen.stdout.read().decode()
        stderr_txt = popen.stderr.read().decode()
        self.get_info().add(stdout_txt)
        self.get_info().add(stderr_txt)
        BackupJob.exception_by_return_code(popen, [0], stdout_txt, stderr_txt)

