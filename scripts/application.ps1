# Service application jar file name prefix
$APP_NAME='app-service'

# Get service application home directory
$APP_HOME=$PSScriptRoot

# Application Service control script
$SVC_EXEC='bin\service.ps1'

# Script command
$COMMAND=$args[0]

# Application arguments
$APP_ARGUMENTS=$args[1..($args.Length)]

# App path and startuo args

$STARTUP_ARGS = $APP_NAME,$COMMAND+$APP_ARGUMENTS
$STARTUP_ARGS = [String[]]$STARTUP_ARGS

$APP_PATH = "$APP_HOME\$SVC_EXEC"

# Print exec

echo "Exec: $APP_PATH $STARTUP_ARGS"

# Run
Invoke-Expression "& `"$APP_PATH`" $STARTUP_ARGS"
