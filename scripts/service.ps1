#!/bin/sh

# Preparing the java home path for execution
$JAVA_EXEC='java'
# JVM Parameters and Spring boot parameters
$JVM_PARAM='-Xms512m','-Xmx1024m'
# Absolute path to service application home directory
$APP_BIN=$PSScriptRoot

# Service application jar file name prefix
$APP_NAME=$args[0]
# Command to execute
$COMMAND=$args[1]
# Application arguments

$APP_ARGUMENTS=$args[2..($args.Length)]

echo "------------------------------------------------------"
echo "| APP NAME : $APP_NAME"
echo "| COMMAND  : $COMMAND"
if ( $APP_ARGUMENTS.Length -ne 0 ) {
  echo "| ARGUMENTS: $APP_ARGUMENTS"
}
echo "------------------------------------------------------"

$HELP_MESSAGE="Usage: $($MyInvocation.myCommand.Name) {application} {start|start-in-background|start-in-foreground|stop|status|restart|kill} [--arg1=value1] [--arg2=value2] ..."
$SHUTDOWN_TIMEOUT=120

function app_pid() {
  $processes=WmiObject Win32_Process -Filter "commandline like '%$JAVA_EXEC%$APP_NAME%.jar%'"
  if ( $processes -eq $null ) {
    return $null
  }
  if ( $processes.processId -eq $null ) {
    if ( $processes.Length -ne $null ) {
	    throw "Too many processes found: $processes.Length"
	  } else {
	    throw "app_pid function got unknown object: $processes"
  	}
  }
  return $processes.processId
}

function status() {
  $APP_PID=app_pid
  if ( $APP_PID -ne $null ) { 
    echo "Application [$APP_NAME] is running with pid: $APP_PID"
  } else {
    echo "Application [$APP_NAME] is not running"
  }
}

function start_app() {
  param ($START_TYPE)
  $APP_PID=app_pid
  if ( $APP_PID -eq $null ) {
    $JAR_FILE=(ls "$APP_BIN/*$APP_NAME*.jar")[0].FullName
    echo "JarFile: $JAR_FILE"

     # Running application with params
	  $STARTUP_ARGS = $JVM_PARAM+'-jar'+$JAR_FILE+$APP_ARGUMENTS
	  $STARTUP_ARGS = [String[]]$STARTUP_ARGS
	
    echo "Exec: $JAVA_EXEC $STARTUP_ARGS"
    if ( $START_TYPE -eq 'background' ) {
      Start-Process $JAVA_EXEC -ArgumentList $STARTUP_ARGS
    } elseif ( $START_TYPE -eq 'foreground' ) {
      Start-Process $JAVA_EXEC -ArgumentList $STARTUP_ARGS -NoNewWindow
    } else {
      echo "Unknown start type: $START_TYPE"
      exit 1
    }
    
    # Check if application was started
    $APP_PID=app_pid
    if ( $APP_PID -ne $null ) { 
      echo "Starting application [$APP_NAME] with pid: $APP_PID"
    } else {
      echo "Failed to start application [$APP_NAME]"
      return 1
  	}
  } else {
    echo "Application [$APP_NAME] is already running with pid: $APP_PID"
  }
}

function stop_app() {
  $APP_PID=$(app_pid)
  if ( $APP_PID -ne $null ) {
    echo "Stoping application [$APP_NAME]"
    taskkill /T /PID $APP_PID
    sleep 2
 
    $count=0
    $kwait=$SHUTDOWN_TIMEOUT
	
	while( ((WmiObject Win32_Process -Filter "processId = '$APP_PID'") -ne $null) -and ($count -ne $kwait) ) {
      echo "waiting for processes to exit $count sec\n"
	  $count++
	  sleep 1
	}
 
    if ( $count -gt $kwait ) {
      echo "killing processes didn't stop after $SHUTDOWN_TIMEOUT seconds\n"
      terminate
    } else {
      echo "Application [$APP_NAME] is not running"
	}
  }
}

function terminate() {
  echo "Terminating application [$APP_NAME]"
  taskkill /T /F /PID $(app_pid)
}

switch( $COMMAND ) {
  "start-in-background" { start_app background }
  "start-in-foreground" { start_app foreground }
  "start" { start_app background }
  "stop" { stop_app }
  "restart" { 
    stop
    start
  }
  "status" { status }
  "kill" { terminate }
  default {
    echo $HELP_MESSAGE
  }
} 
exit 0
