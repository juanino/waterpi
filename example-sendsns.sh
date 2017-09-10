#!/bin/bash -x

# this is is meant to be called from water.py or water2.py
# change the 999999999999 to your proper ARN for the topic to publish to

# requires "pip install awscli" then "aws configure"

msg=$2

/usr/local/bin/aws sns publish --topic-arn "arn:aws:sns:us-east-1:999999999999:waterpi" --message "${msg}"
