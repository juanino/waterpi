#!/usr/bin/env python

# Author: Jerry Uanino
# Purpose: Monitor your basement for nuisances
#          Built after being tired of checking the basement 
#          For floods, dehumidifier failures, rotting mice in traps

import RPi.GPIO as GPIO
import time 
import os
import sys

print "Water sensor starting up. please wait."

red = 3
green = 7
water_sensor = 8 
sensor_name = "basement bathroom"

wateralertstate = "clear" # zero is clear

def wateralert(state):
    global wateralertstate
    if state == wateralertstate:
       pass
    else:
       print "---------------------------------------->state change!"
       if state == "clear":
           os.system("/home/pi/clear.sh")
           # turn pump off on clear
           #os.system("python /home/pi/powertail_off.py")
       if state == "alert":
           os.system("/home/pi/alert.sh")
           os.system("/home/pi/sendtxt.sh 1")
           #os.system("python /home/pi/powertail_on.py")
           # turn pump on then sleep for a bit to drain pit
           # adjust sleep if using pump to 5 minutes or more depending on pump sensitivity
           # change sleep for amount of time to run pump
           time.sleep(5)
    wateralertstate=state

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(water_sensor, GPIO.IN, GPIO.PUD_UP)
while True:

    # turn on led if  alert is on
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    if wateralertstate == "alert":
       GPIO.output(red, 1)
       GPIO.output(green, 0)
    else:
       GPIO.output(red, 0)
       GPIO.output(green, 1)
       # show we are sleeping
       time.sleep(1)
       GPIO.output(green, 0)

    # check water sensor
    if GPIO.input(water_sensor):
        currtime = time.strftime('%Y/%m/%d %H:%M:%S')
        print currtime + " Sensor [" + sensor_name + "] water: is dry"
        wateralert("clear")
    else:
        print "Sensor water: is wet"
        wateralert("alert")
    time.sleep(1)
