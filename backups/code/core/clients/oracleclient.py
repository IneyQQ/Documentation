import cx_Oracle
from coreinterfaces.model import OracleCreds, OracleBackup


class OracleClient:

    def __init__(self, oracle_creds: OracleCreds):
        self.oracle_creds = oracle_creds

    def get_connect_string(self):
        return "{}/{}@{}:{}/{}".format(self.oracle_creds.get_username(),
                                       self.oracle_creds.get_password(),
                                       self.oracle_creds.get_oracle_sid().get_oracle().get_machine().get_address(),
                                       self.oracle_creds.get_oracle_sid().get_oracle().get_port(),
                                       self.oracle_creds.get_oracle_sid().get_sid_name())

    def get_connection(self):
        return cx_Oracle.connect(self.get_connect_string())

    def get_directory_path(self, dir_name):
        with self.get_connection() as conn:
            self._check_if_dir_exists(conn, dir_name)
            cur = conn.cursor()
            cur.execute("select directory_path from all_directories where directory_name='{}'".format(dir_name))
            dir_path = cur.fetchone()[0]
            cur.close()
            return dir_path

    @staticmethod
    def _get_dirs_count(conn, dir_name):
        cur = conn.cursor()
        cur.execute("select count(directory_path) from all_directories where directory_name='{}'".format(dir_name))
        count = cur.fetchone()[0]
        cur.close()
        return count

    def _check_if_dir_exists(self, conn, dir_name):
        dirs_count = self._get_dirs_count(conn, dir_name)
        if dirs_count != 1:
            raise Exception("Bad count of directories with name '{}': {} Expected: 1.".format(dir_name, dirs_count))

    def get_backup_bash_cmd(self, oracle_backup: OracleBackup, backup_file_name, log_file_name):
        with self.get_connection() as conn:
            self._check_if_dir_exists(conn, oracle_backup.get_oracle_dir_name())
        return ["expdp", self.get_connect_string(), "DIRECTORY="+oracle_backup.get_oracle_dir_name(),
                "DUMPFILE="+backup_file_name,
                "LOGFILE="+log_file_name,
                "SCHEMAS="+oracle_backup.get_oracle_schema().get_schema_name()]
