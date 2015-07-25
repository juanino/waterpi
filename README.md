# waterpi
Water sensor for raspberry pi.
Some code to monitor a basement floor or other area
for water, alert and clear when the condition is corrected.


# Features
* poll a physical sensor 
* generate an alert when wet
* generate a clear when resolved
* call out to external script for sending SMS text or other commands
* control an led, flashing = program running and solid is alarm state

# File notes
* alert and clear sh files are stubs. replace them with your actions
* water.py is a sample sensor
* water2.py is just another sensor
* one copy of the program runs per sensor for now, I'm lazy
* modify the sensor_name because its what spews to screen
