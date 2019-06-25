from coreinterfaces import model
from datetime import datetime


class Machine(model.Machine):
    def __init__(self, address):
        self.address = address

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class Schedule(model.Schedule):
    def __init__(self, schedule, last_run):
        self.schedule = schedule
        self.last_run = last_run

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_schedule(self):
        return self.schedule

    def set_last_run(self, last_run: datetime):
        self.last_run = last_run

    def get_last_run(self) -> datetime:
        return self.last_run


class Backup(model.Backup):
    def __init__(self, schedule: model.Schedule, storing_days, compression):
        self.schedule = schedule
        self.storing_days = storing_days
        self.compression = compression

    def set_schedule(self, schedule):
        self.schedule.set_schedule(schedule)

    def get_schedule(self):
        return self.schedule.get_schedule()

    def set_last_run(self, last_run: datetime):
        self.schedule.set_last_run(last_run)

    def get_last_run(self) -> datetime:
        return self.schedule.get_last_run()

    def set_storing_days(self, storing_days: int):
        self.storing_days = storing_days

    def get_storing_days(self) -> int:
        return self.storing_days

    def set_compression(self, compression):
        self.compression = compression

    def get_compression(self):
        return self.compression


class SSH(model.SSH):
    def __init__(self, machine: model.Machine, port):
        self.machine = machine
        self.port = port

    def set_machine(self, machine: model.Machine):
        self.machine = machine

    def get_machine(self) -> model.Machine:
        return self.machine

    def set_port(self, port: int):
        self.port = port

    def get_port(self) -> int:
        return self.port


class SSHCreds(model.SSHCreds):
    def __init__(self, ssh: model.SSH, username, password):
        self.ssh = ssh
        self.username = username
        self.password = password

    def set_ssh(self, ssh: model.SSH):
        self.ssh = ssh

    def get_ssh(self) -> model.SSH:
        return self.ssh

    def set_username(self, username: str):
        self.username = username

    def get_username(self) -> str:
        return self.username

    def set_password(self, password: str):
        self.password = password

    def get_password(self) -> str:
        return self.password


class FilesystemBackup(model.FilesystemBackup):
    def __init__(self, ssh_creds: model.SSHCreds, from_path, to_dir_name,
                 backup: model.Backup):
        self.ssh_creds = ssh_creds
        self.from_path = from_path
        self.to_dir_name = to_dir_name
        self.backup = backup

    def set_ssh_creds(self, ssh_creds: model.SSHCreds):
        self.ssh_creds = ssh_creds

    def get_ssh_creds(self) -> model.SSHCreds:
        return self.ssh_creds

    def set_from_path(self, from_path):
        self.from_path = from_path

    def get_from_path(self):
        return self.from_path

    def set_to_dir(self, to_dir_name):
        self.to_dir_name = to_dir_name

    def get_to_dir(self):
        return self.to_dir_name

    def set_schedule(self, schedule):
        self.backup.set_schedule(schedule)

    def get_schedule(self):
        return self.backup.get_schedule()

    def set_last_run(self, last_run: datetime):
        self.backup.set_last_run(last_run)

    def get_last_run(self) -> datetime:
        return self.backup.get_last_run()

    def set_storing_days(self, storing_days: int):
        self.backup.set_storing_days(storing_days)

    def get_storing_days(self) -> int:
        return self.backup.get_storing_days()

    def set_compression(self, compression):
        self.backup.set_compression(compression)

    def get_compression(self):
        return self.backup.get_compression()


class MySQL(model.MySQL):
    def __init__(self, machine: model.Machine, port):
        self.machine = machine
        self.port = port

    def set_machine(self, machine: model.Machine):
        self.machine = machine

    def get_machine(self) -> model.Machine:
        return self.machine

    def set_port(self, port: int):
        self.port = port

    def get_port(self) -> int:
        return self.port


class MySQLCreds(model.MySQLCreds):
    def __init__(self, mysql: model.MySQL, username, password):
        self.mysql = mysql
        self.username = username
        self.password = password

    def set_mysql(self, mysql: model.MySQL):
        self.mysql = mysql

    def get_mysql(self) -> model.MySQL:
        return self.mysql

    def set_username(self, username: str):
        self.username = username

    def get_username(self) -> str:
        return self.username

    def set_password(self, password: str):
        self.password = password

    def get_password(self) -> str:
        return self.password


class MySQLDB(model.MySQLDB):
    def __init__(self, mysql: model.MySQL, db_name):
        self.mysql = mysql
        self.db_name = db_name

    def set_mysql(self, mysql: model.MySQL):
        self.mysql = mysql

    def get_mysql(self) -> model.MySQL:
        return self.mysql

    def set_db_name(self, db_name):
        self.db_name = db_name

    def get_db_name(self):
        return self.db_name


class MySQLBackup(model.MySQLBackup):
    def __init__(self, mysql_db: model.MySQLDB, mysql_creds: model.MySQLCreds, backup: model.Backup):
        self.mysql_db = mysql_db
        self.mysql_creds = mysql_creds
        self.backup = backup

    def set_mysql_db(self, mysql_db: model.MySQLDB):
        self.mysql_db = mysql_db

    def get_mysql_db(self) -> model.MySQLDB:
        return self.mysql_db

    def set_mysql_creds(self, mysql_creds: model.MySQLCreds):
        self.mysql_creds = mysql_creds

    def get_mysql_creds(self) -> model.MySQLCreds:
        return self.mysql_creds

    def set_schedule(self, schedule):
        self.backup.set_schedule(schedule)

    def get_schedule(self):
        return self.backup.get_schedule()

    def set_last_run(self, last_run: datetime):
        self.backup.set_last_run(last_run)

    def get_last_run(self) -> datetime:
        return self.backup.get_last_run()

    def set_storing_days(self, storing_days: int):
        self.backup.set_storing_days(storing_days)

    def get_storing_days(self) -> int:
        return self.backup.get_storing_days()

    def set_compression(self, compression):
        self.backup.set_compression(compression)

    def get_compression(self):
        return self.backup.get_compression()


class MySQLBackupCheck(model.MySQLBackupCheck):
    def __init__(self, mysql_backup: model.MySQLBackup, schedule: model.Schedule):
        self.mysql_backup = mysql_backup
        self.schedule = schedule

    def set_mysql_backup(self, mysql_backup: MySQLBackup):
        self.mysql_backup = mysql_backup

    def get_mysql_backup(self) -> MySQLBackup:
        return self.mysql_backup

    def set_schedule(self, schedule):
        self.schedule.get_schedule()

    def get_schedule(self):
        return self.schedule.get_schedule()

    def set_last_run(self, last_run: datetime):
        self.schedule.set_last_run(last_run)

    def get_last_run(self) -> datetime:
        return self.schedule.get_last_run()


class Oracle(model.Oracle):
    def __init__(self, machine: model.Machine, port):
        self.machine = machine
        self.port = port

    def set_machine(self, machine: model.Machine):
        self.machine = machine

    def get_machine(self) -> model.Machine:
        return self.machine

    def set_port(self, port: int):
        self.port = port

    def get_port(self) -> int:
        return self.port


class OracleSID(model.OracleSID):
    def __init__(self, oracle: model.Oracle, sid_name):
        self.oracle = oracle
        self.sid_name = sid_name

    def set_oracle(self, oracle: model.Oracle):
        self.oracle = oracle

    def get_oracle(self) -> model.Oracle:
        return self.oracle

    def set_sid_name(self, sid_name):
        self.sid_name = sid_name

    def get_sid_name(self):
        return self.sid_name


class OracleCreds(model.OracleCreds):
    def __init__(self, oracle_sid: model.OracleSID, username, password):
        self.oracle_sid = oracle_sid
        self.username = username
        self.password = password

    def set_oracle_sid(self, oracle_sid: model.OracleSID):
        self.oracle_sid = oracle_sid

    def get_oracle_sid(self) -> model.OracleSID:
        return self.oracle_sid

    def set_username(self, username: str):
        self.username = username

    def get_username(self) -> str:
        return self.username

    def set_password(self, password: str):
        self.password = password

    def get_password(self) -> str:
        return self.password


class OracleSchema(model.OracleSchema):
    def __init__(self, oracle_sid: model.OracleSID, schema_name):
        self.oracle_sid = oracle_sid
        self.schema_name = schema_name

    def set_oracle_sid(self, oracle_sid: model.OracleSID):
        self.oracle_sid = oracle_sid

    def get_oracle_sid(self) -> model.OracleSID:
        return self.oracle_sid

    def set_schema_name(self, schema_name):
        self.schema_name = schema_name

    def get_schema_name(self):
        return self.schema_name


class OracleBackup(model.OracleBackup):
    def __init__(self, oracle_schema: model.OracleSchema, oracle_creds: model.OracleCreds, ssh_creds: model.SSHCreds,
                 oracle_dir_name, backup: model.Backup):
        self.oracle_schema = oracle_schema
        self.oracle_creds = oracle_creds
        self.ssh_creds = ssh_creds
        self.oracle_dir_name = oracle_dir_name
        self.backup = backup

    def set_oracle_schema(self, oracle_schema: model.OracleSchema):
        self.oracle_schema = oracle_schema

    def get_oracle_schema(self) -> model.OracleSchema:
        return self.oracle_schema

    def set_oracle_creds(self, oracle_creds: model.OracleCreds):
        self.oracle_creds = oracle_creds

    def get_oracle_creds(self) -> model.OracleCreds:
        return self.oracle_creds

    def set_ssh_creds(self, ssh_creds: model.SSHCreds):
        self.ssh_creds = ssh_creds

    def get_ssh_creds(self) -> model.SSHCreds:
        return self.ssh_creds

    def set_oracle_dir_name(self, oracle_dir_name):
        self.oracle_dir_name = oracle_dir_name

    def get_oracle_dir_name(self):
        return self.oracle_dir_name

    def set_schedule(self, schedule):
        self.backup.set_schedule(schedule)

    def get_schedule(self):
        return self.backup.get_schedule()

    def set_last_run(self, last_run: datetime):
        self.backup.set_last_run(last_run)

    def get_last_run(self) -> datetime:
        return self.backup.get_last_run()

    def set_storing_days(self, storing_days: int):
        self.backup.set_storing_days(storing_days)

    def get_storing_days(self) -> int:
        return self.backup.get_storing_days()

    def set_compression(self, compression):
        self.backup.set_compression(compression)

    def get_compression(self):
        return self.backup.get_compression()
