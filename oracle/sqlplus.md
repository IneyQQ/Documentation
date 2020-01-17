Run script from remote through SSH:
``` bash
cat <<EOF | sshpass -p <password> ssh -oStrictHostKeyChecking=no oracle@$<oracle_ip|dns> sqlplus <oracle_user>/$<oracle_pass>@<oracle_address>/TCONSTRU
whenever sqlerror exit sql.sqlcode;
ALTER SESSION SET CURRENT_SCHEMA = <oracle_scheme>;
$(cat "<script_path>")
EOF
```
Import schema
``` bash
impdp ${DBUSER}/${DBPASSWORD}@${DBADDRESS}/TCONSTRU DIRECTORY=ADMIN_DUMPS DUMPFILE=${BACKUP_FILE} LOGFILE=${LOG_FILE} SCHEMAS=${DATABASE}
impdp ${DBUSER}/${DBPASSWORD}@${DBADDRESS}/TCONSTRU DIRECTORY=ADMIN_DUMPS DUMPFILE=${BACKUP_FILE} LOGFILE=${LOG_FILE} REMAP_SCHEMA=${DUMP_SCHEMA}:${NEW_SCHEMA}
```
Set lang for SqlPlus. You can add this to .bashrc
```bash
export NLS_LANG="AMERICAN_AMERICA.UTF8"
```
