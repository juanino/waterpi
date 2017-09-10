#!/bin/bash

# to install, add this line:
#      /bin/bash /home/pi/waterpi/start_sensors.sh
# 
# to the /etc/rc.local, right before the exit 0

SENSOR_HOME=/home/pi/waterpi
PATH=$SENSOR_HOME:/usr/local/bin/:$PATH
cd $SENSOR_HOME
#echo "Raspberry pi rebooted" | $SENSOR_HOME/send_slack.py

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
	  printf "My IP address is %s\n" "$_IP"
fi

#echo `ip addr  show  |grep inet` |  $SENSOR_HOME/send_slack.py
echo [`hostname`] start_sensors.sh says,  "My ip address is $_IP" | $SENSOR_HOME/send_slack.py

screen -dmS sensors -c screenSensorRc
