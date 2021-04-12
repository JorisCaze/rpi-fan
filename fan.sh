#!/bin/sh

### BEGIN INIT INFO
# Provides:          fan.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short description: Initialize script to run fan.py on boot
### END INIT INFO

start() {
  echo "Starting fan.py"
  /usr/local/bin/fan.py &
}

stop() {
  echo "Stopping fan.py"
  pkill -f /usr/local/bin/fan.py
}

restart() {
    echo "Restarting fan.py"
    stop
    start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    restart
    ;;
  *)
    echo "Usage: $0 {start|stop|restart}"
    ;;
esac

exit 0