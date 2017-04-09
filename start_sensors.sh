#!/bin/bash

SENSOR_HOME=/home/pi/waterpi
PATH=$SENSOR_HOME:/usr/local/bin/:$PATH
cd $SENSOR_HOME
screen -dmS sensors -c screenSensorRc
