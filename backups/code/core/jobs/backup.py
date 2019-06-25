from coreinterfaces.job import Job
from coreinterfaces.model import Backup
from core.info import Info, ListInfo
from core.cli import CLI
from core.clients.compressionclient import CompressionClient
from subprocess import Popen
from core.clients.filesystemclient import FilesystemClient
from typing import List
import os


class BackupSubJob:
    def __init__(self):
        self.info = ListInfo()

    def get_info(self) -> Info:
        return self.info

    def get_backup_file_path(self):
        return "{}/{}".format(self.get_backup_dir_path(), self.get_backup_file_name())

    def get_backup_file_name(self):
        pass

    def get_backup_dir_path(self) -> str:
        pass

    def get_backup(self) -> Backup:
        pass

    def do_backup(self):
        pass


class BackupJob(Job):

    @staticmethod
    def get_backups_dir():
        return "/opt/backups"

    @staticmethod
    def popen(args, **options):
        popen = CLI(args, **options)
        popen.wait()
        return popen

    @staticmethod
    def exception_by_return_code(popen: Popen, good_return_codes: List[int], stdout: str=None, stderr: str=None):
        return_code = popen.returncode
        for good_return_code in good_return_codes:
            if return_code == good_return_code:
                return
        raise Exception("Bad return code: {}\n\nstdout:\n{}\n\nstderr:\n{}\n".format(
                    popen.returncode, stdout, stderr))

    def __init__(self, backup_sub_job: BackupSubJob):
        super().__init__()
        self.backup_sub_job = backup_sub_job

    def do(self):
        if not os.path.exists(self.backup_sub_job.get_backup_dir_path()):
            os.makedirs(self.backup_sub_job.get_backup_dir_path())
        self.backup_sub_job.do_backup()
        if self.backup_sub_job.get_backup().get_compression() != 'no':
            BackupJob.popen(CompressionClient.get_compress_cmd(self.backup_sub_job.get_backup_file_path(),
                                                               self.backup_sub_job.get_backup().get_compression()))
            BackupJob.popen(['rm', '-rf', self.backup_sub_job.get_backup_file_path()])
        msg_list = FilesystemClient.delete_files_from_dir_older_then(
            self.backup_sub_job.get_backup_dir_path(), days=self.backup_sub_job.get_backup().get_storing_days())
        self.get_info().add("\n".join(msg_list))

    def get_info(self) -> Info:
        return self.backup_sub_job.get_info()

    def __repr__(self):
        return self.backup_sub_job.__repr__()
