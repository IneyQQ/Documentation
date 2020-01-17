Run script from remote through SSH:
``` bash
cat <<EOF | sshpass -p <password> ssh -oStrictHostKeyChecking=no oracle@$<oracle_ip|dns> sqlplus <oracle_user>/$<oracle_pass>@<oracle_address>/TCONSTRU
whenever sqlerror exit sql.sqlcode;
ALTER SESSION SET CURRENT_SCHEMA = <oracle_scheme>;
$(cat "<script_path>")
EOF
```
