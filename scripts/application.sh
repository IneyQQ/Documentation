#!/bin/sh

# Service application jar file name prefix
APP_NAME='app-service'

# Get service application home directory
APP_HOME=$(cd "$(dirname "$0")"; pwd -P)
# Application Service control script
SVC_EXEC=bin/service

# Script command
COMMAND="$1"
shift

# Application arguments
APP_ARGUMENTS="$@"

exec $APP_HOME/$SVC_EXEC $APP_NAME $COMMAND $APP_ARGUMENTS
