#!/usr/bin/env python

import os
import glob
import time
import RPi.GPIO as GPIO
import sys
import time
import urllib
 
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

sensor_name = "office temp" 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        #return temp_c, temp_f
        return temp_f
	
while True:
	#print(read_temp())	
        temp = read_temp()
	currtime = time.strftime('%Y/%m/%d %H:%M:%S')
        print("[" + currtime + "]" + sensor_name + " ->"),
        print(temp)

        #cmd = "echo \" basement temp is " + str(temp) + " \" |/home/pi/waterpi/send_slack.py"
        #print(cmd)
        #os.system(cmd)

        temp_l = urllib.quote_plus(currtime)
        # yes i know i should use pycurl
        #os.system('curl https://dweet.io/dweet/for/jgu1?temp=' + str(temp))
        url = 'curl \'https://dweet.io/dweet/for/jgu1?temp=' + str(temp) + '&temp_last=' + temp_l + '\''
        print "url is" + url
        os.system(url);
	time.sleep(60)
