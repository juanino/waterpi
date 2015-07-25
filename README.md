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

# parts list
[wire](http://www.amazon.com/gp/product/B004JO2PVA?psc=1&redirect=true&ref_=oh_aui_search_detailpage)
http://www.amazon.com/gp/product/B00L660Q10?psc=1&redirect=true&ref_=oh_aui_search_detailpage
http://www.amazon.com/Dolphin-DC-100P-Super-Connector-Pcs/dp/B000JP7FIQ/ref=sr_1_1?s=electronics&ie=UTF8&qid=1437789226&sr=1-1&keywords=b+wire+connector&pebp=1437789231631&perid=0JAVVX1432HWYRSJ3KR2
http://www.amazon.com/gp/product/B00CHPX6OI?psc=1&redirect=true&ref_=oh_aui_search_detailpage

