from core.jobs.backup import BackupSubJob, BackupJob
from coreinterfaces.model import FilesystemBackup
from core.helper import get_date_with_file_format, get_unix_basename
from core.clients.sshclient import SSHClient
from subprocess import PIPE


class FilesystemBackupSubJob(BackupSubJob):
    def __init__(self, filesystem_backup: FilesystemBackup):
        super().__init__()
        self.filesystem_backup = filesystem_backup
        self.ssh_client = SSHClient(self.filesystem_backup.get_ssh_creds())
        self.backup_file_name = None
        self.backup_dir_path = "{}/{}/files/{}".format(
            BackupJob.get_backups_dir(),
            self.filesystem_backup.get_ssh_creds().get_ssh().get_machine().get_address(),
            self.filesystem_backup.get_to_dir()
        )
        self.from_file_name = get_unix_basename(self.filesystem_backup.get_from_path())

    def get_backup_file_name(self):
        return self.backup_file_name

    def get_backup_dir_path(self):
        return self.backup_dir_path

    def get_backup(self):
        return self.filesystem_backup

    def do_backup(self):
        self.backup_file_name = "{}.{}".format(self.from_file_name, get_date_with_file_format())

        popen = BackupJob.popen(
            self.ssh_client.rsync_from_remote_to_local(self.filesystem_backup.get_from_path(),
                                                       self.get_backup_file_path()),
            stdout=PIPE, stderr=PIPE)
        stdout_txt = popen.stdout.read().decode()
        stderr_txt = popen.stderr.read().decode()
        self.get_info().add(stdout_txt)
        self.get_info().add(stderr_txt)
        BackupJob.exception_by_return_code(popen, [0], stdout_txt, stderr_txt)

