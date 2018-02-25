#!/usr/bin/python3

import time
import RPi.GPIO as io
from alert_lib import wateralert

# go to physical pin numbers 1-40
# see writeup http://pi4j.com/pins/model-3b-rev1.html
# image http://pi4j.com/images/j8header-3b-large.png

io.setmode(io.BOARD)

trap_pin = 32

io.setup(trap_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp
silent = 0 # set to 1 to turn off alerts

while True:
    currtime = time.strftime('%Y/%m/%d %H:%M:%S')
    if io.input(trap_pin):
        # at long distances voltage can drop often so double check
        # plus I shouldn't use aluminum foil so much instead of wire
        print("tripped but sleeping 5 seconds to double check")
        time.sleep(5)
        if io.input(trap_pin): # check to see if it's still shut after waiting 
            print(currtime + "->trap closed - clear debris and reset")
            if silent !=1:
                wateralert("alert")
    else:
        print(currtime + "->trap is open")
        if silent !=1:
            wateralert("clear") 
    time.sleep(0.5)

