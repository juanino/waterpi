#!/usr/bin/env python
import yaml
import pprint
import json
import requests
import sys

# sample usage:
# echo blah | ./send_slack.py
# 
# this is used by the startup scripts to notify of a raspberry pi reboot


# debug
pp = pprint.PrettyPrinter(indent=4)

# read yaml
with open('/etc/waterpi.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def dump_config(cfg):
    pp.pprint(cfg)

dump_config(cfg)

url = cfg['slack']['webhook']
do_slack = cfg['slack']['enable']

print "----------"
pp.pprint(url)
print "----------"
pp.pprint(do_slack)


lines=[]
for line in sys.stdin:
    lines.append(line)

strline = ''.join(lines)

if (len(lines) > 0):
    if do_slack:
        data = {
                'text': strline
        }
        print "the data is " 
        print data
        response = requests.post(
            url, data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
