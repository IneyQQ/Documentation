Create user:
``` sql
CREATE USER <user> IDENTIFIED BY <pass>;
```
Create directory:
``` sql
CREATE DIRECTORY <dir> as <path to dir>;
```
Grant privileges:
``` sql
GRANT CONNECT TO <user>;
GRANT EXP_FULL_DATABASE TO <user>;
GRANT READ, WRITE ON DIRECTORY <dir> TO <user>;
ALTER USER <user> QUOTA 100M ON USERS;
```
Export schema(you must be at oracle db machine logged on as oracle user):
``` bash
expdp <user>/<pass>@<SID> DIRECTORY=<dir> DUMPFILE=<dump_filename> LOGFILE=<log_filename> SCHEMAS=<schema>
```
