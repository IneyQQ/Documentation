from core.model import *
import mysqlmodel
from mysqlset import get_mysql_connection
from typing import List


def load_filesystem_backups() -> List[FilesystemBackup]:
    query = \
        (
            "SELECT machine_address, ssh_port, ssh_username, ssh_password, from_path, dir_name, schedule, last_run, storing_days, compression "
            "FROM filesystem_backup NATURAL JOIN ssh_creds WHERE active='y'"
        )
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    backups = []
    for (machine_address, ssh_port, ssh_username, ssh_password, from_path, dir_name, schedule, last_run, storing_days, compression) in cursor:
        ssh = SSH(Machine(machine_address), ssh_port)
        backup = mysqlmodel.FilesystemBackupMySQL(SSHCreds(ssh, ssh_username, ssh_password), from_path, dir_name,
                                                  Backup(Schedule(schedule, last_run), storing_days, compression))
        backups.append(backup)
    connection.close()
    return backups


def load_mysql_backups() -> List[MySQLBackup]:
    query = \
        (
            "SELECT machine_address, mysql_port, mysql_db_name, mysql_username, mysql_password, schedule, last_run, storing_days, compression "
            "FROM mysql_backup NATURAL JOIN mysql_creds WHERE active='y'"
        )
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    backups = []
    for (machine_address, mysql_port, mysql_db_name, mysql_username, mysql_password, schedule, last_run, storing_days, compression) in cursor:
        mysql = MySQL(Machine(machine_address), mysql_port)
        backup = mysqlmodel.MySQLBackupMySQL(MySQLDB(mysql, mysql_db_name), MySQLCreds(mysql, mysql_username, mysql_password),
                                             Backup(Schedule(schedule, last_run), storing_days, compression))
        backups.append(backup)
    connection.close()
    return backups


def load_mysql_backup(machine_address, mysql_port, mysql_db_name) -> MySQLBackup:
    query = \
        (
            "SELECT machine_address, mysql_port, mysql_db_name, mysql_username, mysql_password, schedule, last_run, storing_days, compression "
            "FROM mysql_backup NATURAL JOIN mysql_creds WHERE machine_address=%s AND mysql_port=%s AND mysql_db_name=%s"
        )
    parameters = (machine_address, mysql_port, mysql_db_name)
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    backup = None
    for (machine_address, mysql_port, mysql_db_name, mysql_username, mysql_password, schedule, last_run, storing_days, compression) in cursor:
        mysql = MySQL(Machine(machine_address), mysql_port)
        backup = mysqlmodel.MySQLBackupMySQL(MySQLDB(mysql, mysql_db_name), MySQLCreds(mysql, mysql_username, mysql_password),
                                             Backup(Schedule(schedule, last_run), storing_days, compression))
    connection.close()
    return backup


def load_mysql_backup_checks() -> List[MySQLBackupCheck]:
    query = \
        (
            "SELECT machine_address, mysql_port, mysql_db_name, schedule, last_run "
            "FROM mysql_backup_check WHERE active='y'"
        )
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    backup_checks = []
    for (machine_address, mysql_port, mysql_db_name, schedule, last_run) in cursor:
        backup = mysqlmodel.MySQLBackupCheckMySQL(load_mysql_backup(machine_address, mysql_port, mysql_db_name),
                                                  Schedule(schedule, last_run))
        backup_checks.append(backup)
    connection.close()
    return backup_checks


def load_oracle_backups() -> List[OracleBackup]:
    query = \
        (
            "SELECT machine_address, oracle_port, oracle_sid_name, oracle_schema_name, oracle_username, oracle_password, oracle_dir_name, ssh_port, ssh_username, ssh_password, schedule, last_run, storing_days, compression "
            "FROM oracle_backup NATURAL JOIN oracle_creds NATURAL JOIN ssh_creds WHERE active='y'"
        )
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    backups = []
    for (machine_address, oracle_port, oracle_sid_name, oracle_schema_name, oracle_username, oracle_password, oracle_dir_name, ssh_port, ssh_username, ssh_password, schedule, last_run, storing_days, compression) in cursor:
        ssh = SSH(Machine(machine_address), ssh_port)
        oracle_sid = OracleSID(Oracle(Machine(machine_address), oracle_port), oracle_sid_name)
        backup = mysqlmodel.OracleBackupMySQL(OracleSchema(oracle_sid, oracle_schema_name),
                                              OracleCreds(oracle_sid, oracle_username, oracle_password),
                                              SSHCreds(ssh, ssh_username, ssh_password),
                                              oracle_dir_name,
                                              Backup(Schedule(schedule, last_run), storing_days, compression))
        backups.append(backup)
    connection.close()
    return backups
