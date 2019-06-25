from load.load_backups import *
from core.task import ScheduledTaskManager, ScheduledTask
from logs.filelog import FileLog
from alerts.EmailAlert import EmailAlert
from jobs.mysqlbackupsubjob import MySQLBackupSubJob
from jobs.filesystembackupsubjob import FilesystemBackupSubJob
from jobs.oraclebackupsubjob import OracleBackupSubJob
from jobs.mysqlbackupcheckjob import MySQLBackupCheckJob
from core.jobs.backup import BackupJob
from core.cli import CLI
from logs.clilog import CLILog


task_manager = ScheduledTaskManager()

# Main log
main_log = FileLog('/opt/task_manager.log')
task_manager.logs.add_log(main_log)
task_manager.error_logs.add_log(main_log)
CLI.logs.add_log(main_log)

# Error log
task_manager.error_logs.add_log(FileLog('/opt/task_manager.error.log'))

# CLI logs
task_manager.logs.add_log(CLILog())
task_manager.error_logs.add_log(CLILog())
CLI.logs.add_log(CLILog())

# Email Alerts
#task_manager.alerts.add_alert(EmailAlert("Backups", "mshauliuk@iba.by"))
task_manager.alerts.add_alert(EmailAlert("Backups", "mail@example.com,mail2@example.com"))


mysql_backups = load_mysql_backups()
mysql_backup_checks = load_mysql_backup_checks()
oracle_backups = load_oracle_backups()
filesystem_backups = load_filesystem_backups()

for backup in mysql_backups:
    task_manager.add_scheduled_task(ScheduledTask(BackupJob(MySQLBackupSubJob(backup)), backup))

for backup in oracle_backups:
    task_manager.add_scheduled_task(ScheduledTask(BackupJob(OracleBackupSubJob(backup)), backup))

for backup in filesystem_backups:
    task_manager.add_scheduled_task(ScheduledTask(BackupJob(FilesystemBackupSubJob(backup)), backup))

for backup_check in mysql_backup_checks:
    task_manager.add_scheduled_task(ScheduledTask(MySQLBackupCheckJob(backup_check), backup_check))

while True:
    task_manager.run_next_task()
