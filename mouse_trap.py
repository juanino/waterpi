#!/usr/bin/python3

import time
import RPi.GPIO as io
from alert_lib import wateralert

# go to physical pin numbers 1-40
# see writeup http://pi4j.com/pins/model-3b-rev1.html
# image http://pi4j.com/images/j8header-3b-large.png

io.setmode(io.BOARD)

trap_pin = 32 # gpio pin
max_reads = 720 # number of times the sensor can read closed before alerting
silent = 0 # set to 1 to turn off alerts
double_check_interval = 5 # how often sensor is checked once tripped to confirm up to max_reads

io.setup(trap_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp

while True:
    currtime = time.strftime('%Y/%m/%d %H:%M:%S')
    if io.input(trap_pin):
        trip_counter = 0
        while (io.input(trap_pin) and  trip_counter < max_reads):
            # at long distances voltage can drop often so double check
            # plus I shouldn't use aluminum foil so much instead of wire
            # this is the inside loop. read the sensor max_reads times to be sure
            # and sleep double_check_interval
            print("tripped but sleeping to double check")
            print("trip counter is", trip_counter)
            time.sleep(double_check_interval)
            trip_counter = trip_counter + 1
        if (io.input(trap_pin) and trip_counter == max_reads): # if still closed after ten, alert
            currtime = time.strftime('%Y/%m/%d %H:%M:%S')
            print(currtime + "->trap closed - clear debris and reset")
            if silent !=1:
                wateralert("alert")
    else:
        print(currtime + "->trap is open")
        if silent !=1:
            wateralert("clear") 
    time.sleep(5)

