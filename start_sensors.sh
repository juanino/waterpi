#!/bin/bash

# to install, add this line:
#      /bin/bash /home/pi/waterpi/start_sensors.sh
# 
# to the /etc/rc.local, right before the exit 0

SENSOR_HOME=/home/pi/waterpi
PATH=$SENSOR_HOME:/usr/local/bin/:$PATH
cd $SENSOR_HOME
echo "Raspberry pi rebooted" | $SENSOR_HOME/send_slack.py
echo `ip addr  show  |grep inet` |  $SENSOR_HOME/send_slack.py
screen -dmS sensors -c screenSensorRc
