#!/usr/bin/env python3

import os
import time
import sys

wateralertstate = "clear" # zero is clear
sensor_name = "mouse trap in storage closet"
max_alerts = 5
total_alerts = 0
max_msg_sent = 0

def wateralert(state):
    global wateralertstate
    global max_alerts
    global total_alerts
    global max_msg_sent
    if state == wateralertstate:
       pass
    else:
       total_alerts = total_alerts + 1
       if total_alerts > max_alerts:
           print("too many alerts, reset")
           if (max_msg_sent == 0):
               message="\"must reset: too many alerts for " + sensor_name + "\""
               os.system("/home/pi/waterpi/sendsns.sh 1 " + message)
           max_msg_sent = 1
       else:
           print("---------------------------------------->state change!")
           print("this system has sent" + str(total_alerts))
           if state == "clear":
               os.system("banner clear")
               message="\"CLEAR for " + sensor_name + "\""
               os.system("/home/pi/waterpi/sendsns.sh 1 " + message)
           if state == "alert":
               os.system("banner alert")
               message="\"ALARM for " + sensor_name + "\""
               os.system("/home/pi/waterpi/sendsns.sh 1 " + message)
               time.sleep(5)
    wateralertstate=state
