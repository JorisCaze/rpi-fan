#!/bin/sh

# This script allows to quickly configure to run fan.py on boot.
# It is based on init.d which start/stop services during system initialization/shutdown.
# Other methods could be to use crontab with @reboot flag but it was not working for my old RPi
# or to add the script path into /etc/rc.local but this method is considered deprecated. 
# See https://unix.stackexchange.com/questions/188042/running-a-script-during-booting-startup-init-d-vs-cron-reboot

# init.d specific script is called fan.sh

set -e

echo "Installing fan controller..."
sudo cp fan.py /usr/local/bin/
sudo chmod +x /usr/local/bin/fan.py

echo "Starting fan controller..."
sudo cp fan.sh /etc/init.d/
sudo chmod +x /etc/init.d/fan.sh

sudo update-rc.d fan.sh defaults
/etc/init.d/fan.sh start

echo "Fan controller installed."
