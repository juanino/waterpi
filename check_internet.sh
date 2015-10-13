#!/bin/bash

# setup the pin for led
gpio -1 mode 35 out

### functions ###
blink_and_sleep ()
{ # blink so we know the pi is still working
  # and that program hasn not crashed
  COUNTER=0
  while [ $COUNTER -lt 150 ]; do
      gpio -1 write 35 1
      sleep 1
      gpio -1 write 35 0
      sleep 1
      let COUNTER=COUNTER+1
      #echo $COUNTER
  done 
}

blink_rapidly ()
{ # good for showing work about to happen
  COUNTER=0
  while [ $COUNTER -lt 10 ]; do
      gpio -1 write 35 1
      sleep .1
      gpio -1 write 35 0
      sleep .1
      let COUNTER=COUNTER+1
  done
}

#### main loop
while true
 do
    echo [check_internet] checking....
    blink_rapidly
    wget -q --tries=10 --timeout=20 --spider http://google.com
    if [[ $? -eq 0 ]]; then
            echo "[check_internet] Online"
            gpio -1 write 35 0
            blink_and_sleep
    else
            echo "[check_internet] Offline"
            gpio -1 write 35 1
            echo waiting for internet to come back
            sleep 10
    fi
done
#### end main loop
