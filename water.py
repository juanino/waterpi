#!/usr/bin/env python

# Author: Jerry Uanino
# Purpose: Monitor your basement for nuisances
#          Built after being tired of checking the basement 
#          For floods, dehumidifier failures, rotting mice in traps
#

import RPi.GPIO as GPIO
import time 
import os
import sys
import urllib

# pushover
import httplib
import yaml

print "Water sensor starting up. please wait."


red = 36
green = 11
water_sensor = 8 
buzzer = 40
sensor_name = "basement bathroom"
dashboard_counter = 0

wateralertstate = "clear" # zero is clear

def send_pushover(message):

    # read yaml
    with open('/etc/waterpi.yaml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    app_token = cfg['pushover']['app_token']
    user_key = cfg['pushover']['user_key'] 
    retry = cfg['pushover']['retry'] 
    expire = cfg['pushover']['expire'] 

    print("app token is " + app_token)
    print("user_key is " + user_key)
    print("message is " + message)

    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
      "token": app_token,
      "user": user_key,
      "message": message,
      "priority": 2,
      "retry": retry,
      "expire": expire,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    print conn.getresponse()

def wateralert(state):
    global wateralertstate
    if state == wateralertstate:
       pass
    else:
       print "---------------------------------------->state change!"
       if state == "clear":
           os.system("/home/pi/clear.sh")
           message="\"water CLEAR for " + sensor_name + "\""
           os.system("/home/pi/waterpi/sendsns.sh 1 " + message)
           send_pushover(message)
           # turn pump off on clear
           #os.system("python /home/pi/powertail_off.py")
       if state == "alert":
           os.system("/home/pi/alert.sh")
           message="\"water ALARM for " + sensor_name + "\""
           os.system("/home/pi/waterpi/sendsns.sh 1 " + message)
           send_pushover(message)
           #os.system("python /home/pi/powertail_on.py")
           # turn pump on then sleep for a bit to drain pit
           # adjust sleep if using pump to 6 minutes or more depending on pump sensitivity
           # change sleep for amount of time to run pump
           time.sleep(5)
    wateralertstate=state

def update_dashboard(dweet_thing,dash_element,dash_state,dashboard_counter):
    #print "dweeting for thing " + dweet_thing
    #print "Updating dashboard element" + dash_element
    #print "Setting state to " + dash_state
    dashboard_counter=dashboard_counter + 1
    if dashboard_counter == 60:
        print "max number checks before dashboard update met"
        sensor1_l = urllib.quote_plus(currtime)
        url = 'curl \'https://dweet.io/dweet/for/jgu1?sensor1=' + dash_state + '&sensor1_l=' + sensor1_l + '\''
        print "url is " + url
        os.system(url)
        dashboard_counter = 0
    #print "dashboard counter is " + str(dashboard_counter)
    return(dashboard_counter)

print("sending test message")
send_pushover("sensors starting up: " + __file__ + " " + sensor_name)

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
        print currtime + "Sensor [" + sensor_name + "] water: is dry "
        wateralert("clear")
        dashboard_counter=update_dashboard("jgu1",sensor_name,"0",dashboard_counter)
    else:
        print "Sensor water: is wet"
        wateralert("alert")
        dashboard_counter=update_dashboard("jgu1",sensor_name,"1",dashboard_counter)
    time.sleep(1)
