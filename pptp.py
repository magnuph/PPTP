#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import pprint

def deprint(lista): 
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(lista)

from_mail = ''
nyckelord = ''
url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning?nyckelord=" + nyckelord
headers = {'Accept' :'application/json', 'Accept-Language':'sv', 'From':from_mail}
r = requests.get(url, headers=headers)

jd = r.json()
jn = jd['matchningslista']
jm = jd['matchningslista']['matchningdata']

annonsids = [item["annonsid"] for item in jm]

for i, value in jn.iteritems():
    if i == "antal_platsannonser":
        antal_ledigajobb = value

print "Klockan: " + (time.strftime("%H:%M:%S"))
print "Datum: " + (time.strftime("%d/%m/%Y"))
print "Antal lediga jobb: " + str(antal_ledigajobb)

#deprint(jd)
#time.sleep(4)

#PUSHOVER NOTIFICATION
import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "TOKEN",
    "user": "USER",
    "message": "Klockan: " + (time.strftime("%H:%M:%S")) + " | " + "Antal ptp-platser: " + str(antal_ledigajobb),
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
