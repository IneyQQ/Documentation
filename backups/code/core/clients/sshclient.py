from core.model import SSHCreds
from core.cli import CLI


class SSHClient:
    def __init__(self, ssh_creds: SSHCreds):
        self.ssh_creds = ssh_creds

    def get_ssh_connection_str(self):
        return '{}@{}'.format(self.ssh_creds.username, self.ssh_creds.ssh.machine.address)

    def popen_cmd(self, args):
        return CLI.sshpass(
            ['ssh', '-oStrictHostKeyChecking=no', self.get_ssh_connection_str(), '-p', str(self.ssh_creds.ssh.port)]
            + args, self.ssh_creds.password)

    def rsync_from_remote_to_local(self, from_path, to_path):
        args = ['rsync', '-a', '--port='+str(self.ssh_creds.ssh.port),
                '-e', 'ssh -o StrictHostKeyChecking=no',
                '{}:{}'.format(self.get_ssh_connection_str(), from_path), to_path]
        return CLI.sshpass(args, self.ssh_creds.password)

    def rsync_from_local_to_remote(self, from_path, to_path):
        args = ['rsync', '-a', '--port='+str(self.ssh_creds.ssh.port),
                '-e', 'ssh -o StrictHostKeyChecking=no',
                from_path, '{}:{}'.format(self.get_ssh_connection_str(), to_path)]
        return CLI.sshpass(args, self.ssh_creds.password)
