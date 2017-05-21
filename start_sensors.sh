#!/bin/bash

SENSOR_HOME=/home/pi/waterpi
PATH=$SENSOR_HOME:/usr/local/bin/:$PATH
cd $SENSOR_HOME
echo "Raspberry pi rebooted" | $SENSOR_HOME/send_slack.py
echo `ip addr  show eth0 |grep inet` |  $SENSOR_HOME/send_slack.py
screen -dmS sensors -c screenSensorRc
