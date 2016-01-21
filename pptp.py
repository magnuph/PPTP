import requests
import time


url = "http://api.arbetsformedlingen.se/af/v0/platsannonser/soklista/yrken/PTP-psykolog"
headers = {'Accept' :'application/json', 'Accept-Language':'sv', 'From':'admin@ganstarr.nu'}
r = requests.get(url, headers=headers)

jd = r.json()

jm = jd['soklista']['sokdata']

antal_ledigajobb = [item["antal_ledigajobb"] for item in jm]
antal_platsannonser = [item["antal_platsannonser"] for item in jm]

print "Klockan: " + (time.strftime("%H:%M:%S"))
print "Datum: " + (time.strftime("%d/%m/%Y"))
print "Antal lediga jobb: " + str(antal_ledigajobb)
print "Antal platsannonser: " + str(antal_platsannonser)

time.sleep(4)


#PUSHOVER NOTIFICATION
import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "TOKEN",
    "user": "USER",
    "message": "Klockan: " + (time.strftime("%H:%M:%S")) + " | " + "Antal platsannonser: " + str(antal_platsannonser),
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
