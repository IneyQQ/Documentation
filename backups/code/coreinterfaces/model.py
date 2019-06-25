from datetime import datetime


class Machine:
    def set_address(self, address):
        pass

    def get_address(self):
        pass


class Schedule:
    def set_schedule(self, schedule):
        pass

    def get_schedule(self):
        pass

    def set_last_run(self, last_run: datetime):
        pass

    def get_last_run(self) -> datetime:
        pass


class Backup(Schedule):
    def set_storing_days(self, storing_days: int):
        pass

    def get_storing_days(self) -> int:
        pass

    def set_compression(self, compression):
        pass

    def get_compression(self):
        pass


class SSH:
    def set_machine(self, machine: Machine):
        pass

    def get_machine(self) -> Machine:
        pass

    def set_port(self, port: int):
        pass

    def get_port(self) -> int:
        pass


class SSHCreds:
    def set_ssh(self, ssh: SSH):
        pass

    def get_ssh(self) -> SSH:
        pass

    def set_username(self, username: str):
        pass

    def get_username(self) -> str:
        pass

    def set_password(self, password: str):
        pass

    def get_password(self) -> str:
        pass


class FilesystemBackup(Backup):
    def set_ssh_creds(self, ssh_creds: SSHCreds):
        pass

    def get_ssh_creds(self) -> SSHCreds:
        pass

    def set_from_path(self, from_path):
        pass

    def get_from_path(self):
        pass

    def set_to_dir(self, to_dir):
        pass

    def get_to_dir(self):
        pass


class MySQL:
    def set_machine(self, machine: Machine):
        pass

    def get_machine(self) -> Machine:
        pass

    def set_port(self, port: int):
        pass

    def get_port(self) -> int:
        pass


class MySQLCreds:
    def set_mysql(self, mysql: MySQL):
        pass

    def get_mysql(self) -> MySQL:
        pass

    def set_username(self, username: str):
        pass

    def get_username(self) -> str:
        pass

    def set_password(self, password: str):
        pass

    def get_password(self) -> str:
        pass


class MySQLDB:
    def set_mysql(self, mysql: MySQL):
        pass

    def get_mysql(self) -> MySQL:
        pass

    def set_db_name(self, db_name):
        pass

    def get_db_name(self):
        pass


class MySQLBackup(Backup):
    def set_mysql_db(self, mysql: MySQL):
        pass

    def get_mysql_db(self) -> MySQLDB:
        pass

    def set_mysql_creds(self, mysql: MySQL):
        pass

    def get_mysql_creds(self) -> MySQLCreds:
        pass


class MySQLBackupCheck(Schedule):
    def set_mysql_backup(self, mysql: MySQLBackup):
        pass

    def get_mysql_backup(self) -> MySQLBackup:
        pass


class Oracle:
    def set_machine(self, machine: Machine):
        pass

    def get_machine(self) -> Machine:
        pass

    def set_port(self, port: int):
        pass

    def get_port(self) -> int:
        pass


class OracleSID:
    def set_oracle(self, mysql: MySQL):
        pass

    def get_oracle(self) -> Oracle:
        pass

    def set_sid_name(self, sid_name):
        pass

    def get_sid_name(self):
        pass


class OracleCreds:
    def set_oracle_sid(self, mysql: MySQL):
        pass

    def get_oracle_sid(self) -> OracleSID:
        pass

    def set_username(self, username: str):
        pass

    def get_username(self) -> str:
        pass

    def set_password(self, password: str):
        pass

    def get_password(self) -> str:
        pass


class OracleSchema:
    def set_oracle_sid(self, mysql: MySQL):
        pass

    def get_oracle_sid(self) -> OracleSID:
        pass

    def set_schema_name(self, schema_name):
        pass

    def get_schema_name(self):
        pass


class OracleBackup(Backup):
    def set_oracle_schema(self, oracle_schema: OracleSchema):
        pass

    def get_oracle_schema(self) -> OracleSchema:
        pass

    def set_oracle_creds(self, oracle_creds: OracleCreds):
        pass

    def get_oracle_creds(self) -> OracleCreds:
        pass

    def set_ssh_creds(self, ssh_creds: SSHCreds):
        pass

    def get_ssh_creds(self) -> SSHCreds:
        pass

    def set_oracle_dir_name(self, oracle_dir_name):
        pass

    def get_oracle_dir_name(self):
        pass
