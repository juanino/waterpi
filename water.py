#!/usr/bin/env python

# Author: Jerry Uanino
# Purpose: Monitor your basement for nuisances
#          Built after being tired of checking the basement 
#          For floods, dehumidifier failures, rotting mice in traps

import RPi.GPIO as GPIO
import time 
import os
import sys
import urllib

print "Water sensor starting up. please wait."

red = 36
green = 11
water_sensor = 8 
buzzer = 40
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
           message="\"water CLEAR for " + sensor_name + "\""
           os.system("/home/pi/sendtxt.sh 1 " + message)
           # turn pump off on clear
           #os.system("python /home/pi/powertail_off.py")
       if state == "alert":
           os.system("/home/pi/alert.sh")
           message="\"water ALARM for " + sensor_name + "\""
           os.system("/home/pi/sendtxt.sh 1 " + message)
           #os.system("python /home/pi/powertail_on.py")
           # turn pump on then sleep for a bit to drain pit
           # adjust sleep if using pump to 6 minutes or more depending on pump sensitivity
           # change sleep for amount of time to run pump
           time.sleep(5)
    wateralertstate=state

def update_dashboard(dweet_thing,dash_element,dash_state):
    #print "dweeting for thing " + dweet_thing
    #print "Updating dashboard element" + dash_element
    #print "Setting state to " + dash_state
    sensor1_l = urllib.quote_plus(currtime)
    url = 'curl \'https://dweet.io/dweet/for/jgu1?sensor1=' + dash_state + '&sensor1_l=' + sensor1_l + '\''
    #print "url is " + url
    os.system(url);



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(water_sensor, GPIO.IN, GPIO.PUD_UP)
while True:

    # turn on led if  alert is on
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)
    if wateralertstate == "alert":
       GPIO.output(red, 1)
       GPIO.output(buzzer, 1)
       GPIO.output(green, 0)
    else:
       GPIO.output(red, 0)
       GPIO.output(buzzer, 0)
       GPIO.output(green, 1)
       # show we are sleeping
       time.sleep(1)
       GPIO.output(green, 0)

    # check water sensor
    if GPIO.input(water_sensor):
        currtime = time.strftime('%Y/%m/%d %H:%M:%S')
        print currtime + " \n\n Sensor [" + sensor_name + "] water: is dry \n"
        wateralert("clear")
        update_dashboard("jgu1",sensor_name,"0")
    else:
        print "Sensor water: is wet"
        wateralert("alert")
        update_dashboard("jgu1",sensor_name,"1")
    time.sleep(1)
