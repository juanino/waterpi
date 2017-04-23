#!/bin/sh

# this will send 3v down to physical pin 40
# since that is where we have the audible buzzer

gpio -1 write 40 1

# it should auto shut off when the next poll for the sensor kicks in
# if it does not, then your water.py is broken
# you can send gpio -1 write 40 0 if you want to switch off the buzzer
