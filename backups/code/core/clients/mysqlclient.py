from coreinterfaces.model import MySQLCreds, MySQLBackup
import mysql.connector


class MySQLClient:

    @staticmethod
    def get_mysqldbcompare_cmd(client1: MySQLCreds, db1, client2: MySQLCreds, db2):
        return [
            "mysqldbcompare",
            "--server1={}:{}@{}".format(
                client1.get_username(), client1.get_password(), client1.get_mysql().get_machine().get_address()),
            "--server2={}:{}@{}".format(
                client2.get_username(), client2.get_password(), client2.get_mysql().get_machine().get_address()),
            "{}:{}".format(db1, db2),
            "--run-all-tests",
            "--skip-checksum-table",
            "--skip-diff"
        ]

    def __init__(self, mysql_creds: MySQLCreds):
        self.mysql_creds = mysql_creds

    def get_connection_list(self):
        return ["-h"+self.mysql_creds.get_mysql().get_machine().get_address(),
                "-P"+str(self.mysql_creds.get_mysql().get_port()),
                "-u"+self.mysql_creds.get_username(),
                "-p"+self.mysql_creds.get_password()]

    def get_mysql_connection(self):
        return mysql.connector.connect(
            user=self.mysql_creds.get_username(),
            password=self.mysql_creds.get_password(),
            host=self.mysql_creds.get_mysql().get_machine().get_address()
        )

    def run_mysql_query(self, query, parameters=()):
        connection = self.get_mysql_connection()
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

    def get_backup_bash_cmd(self, mysql_backup: MySQLBackup):
        backup_cmd = ["mysqldump", "-R"]
        backup_cmd.extend(self.get_connection_list())
        backup_cmd.append(mysql_backup.get_mysql_db().get_db_name())
        return backup_cmd

    def get_mysql_cmd(self):
        return ["mysql"] + self.get_connection_list()

    def get_mysql_db_cmd(self, db):
        return self.get_mysql_cmd() + [db]

    create_db_stmt = "CREATE DATABASE IF NOT EXISTS {}"

    def create_db(self, db):
        self.run_mysql_query(self.create_db_stmt.format(db))

    drop_db_stmt = "DROP DATABASE IF EXISTS {}"

    def drop_db(self, db):
        self.run_mysql_query(self.drop_db_stmt.format(db))
