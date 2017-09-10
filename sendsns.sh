#!/bin/bash -x

# this is is meant to be called from water.py or water2.py
# edit your /etc/waterpi.yaml for your sns arn

# requires "pip install awscli" then "aws configure"
# requires an aws sns topic to be created and subscribed to

# useage:  ./example-sendsns.sh 1 "this is a test"

msg=$2

/usr/local/bin/aws sns publish --topic-arn `cat /etc/waterpi.yaml |grep arn  |awk {'print $2'}` --message "${msg}"
