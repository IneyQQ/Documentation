from core import model
from core.model import datetime
from mysqlset import run_mysql_query


class MySQLBackupMySQL(model.MySQLBackup):
    def set_last_run(self, last_run: datetime):
        super().set_last_run(last_run)
        query = \
            (
                "UPDATE mysql_backup SET last_run=%s "
                "WHERE machine_address=%s AND mysql_port=%s AND mysql_db_name=%s"
            )
        parameters = (
            self.get_last_run(),
            self.get_mysql_db().get_mysql().get_machine().get_address(),
            self.get_mysql_db().get_mysql().get_port(),
            self.get_mysql_db().get_db_name(),
        )
        run_mysql_query(query, parameters)


class MySQLBackupCheckMySQL(model.MySQLBackupCheck):
    def set_last_run(self, last_run: datetime):
        super().set_last_run(last_run)
        query = \
            (
                "UPDATE mysql_backup_check SET last_run=%s "
                "WHERE machine_address=%s AND mysql_port=%s AND mysql_db_name=%s"
            )
        parameters = (
            self.get_last_run(),
            self.get_mysql_backup().get_mysql_db().get_mysql().get_machine().get_address(),
            self.get_mysql_backup().get_mysql_db().get_mysql().get_port(),
            self.get_mysql_backup().get_mysql_db().get_db_name(),
        )
        run_mysql_query(query, parameters)


class OracleBackupMySQL(model.OracleBackup):
    def set_last_run(self, last_run: datetime):
        super().set_last_run(last_run)
        query = \
            (
                "UPDATE dumps.oracle_backup SET last_run=%s "
                "WHERE machine_address=%s AND oracle_port=%s AND oracle_sid_name=%s AND oracle_schema_name=%s"
            )
        parameters = (
            self.get_last_run(),
            self.get_oracle_schema().get_oracle_sid().get_oracle().get_machine().get_address(),
            self.get_oracle_schema().get_oracle_sid().get_oracle().get_port(),
            self.get_oracle_schema().get_oracle_sid().get_sid_name(),
            self.get_oracle_schema().get_schema_name()
        )
        run_mysql_query(query, parameters)


class FilesystemBackupMySQL(model.FilesystemBackup):
    def set_last_run(self, last_run: datetime):
        super().set_last_run(last_run)
        query = \
            (
                "UPDATE filesystem_backup SET last_run=%s "
                "WHERE machine_address=%s AND ssh_port=%s AND from_path=%s"
            )
        parameters = (
            self.get_last_run(),
            self.get_ssh_creds().get_ssh().get_machine().get_address(),
            self.get_ssh_creds().get_ssh().get_port(),
            self.get_from_path()
        )
        run_mysql_query(query, parameters)
