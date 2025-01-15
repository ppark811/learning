# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:32:22 2024

@author: ppark
"""

import requests, smtplib
from datetime import datetime

MY_LAT = 39.582286
MY_LNG = -104.984707
VIEW_RANGE = 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0, 
    "tzid": "America/Denver"
}

def getISS():
    ISSresponse = requests.get(url="http://api.open-notify.org/iss-now.json")
    ISSresponse.raise_for_status()
    ISSdata = ISSresponse.json()
    
    ISSLon = float(ISSdata["iss_position"]["longitude"])
    ISSLat = float(ISSdata["iss_position"]["latitude"])
    ISSPosition = [ISSLon, ISSLat]
    
    return ISSPosition

def getSun(parameters):

    sunResponse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunResponse.raise_for_status()
    sunData = sunResponse.json()
     
    sunrise = int(sunData["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunData["results"]["sunset"].split("T")[1].split(":")[0])
    sunData = [sunrise, sunset]

    return sunData

#If the ISS is close to my current position and it is currently dark
timeNow = datetime.now().hour
ISSPosition = getISS()
sunData = getSun(parameters)

latRange = [MY_LAT - VIEW_RANGE,  MY_LAT + VIEW_RANGE]
lngRange = [MY_LNG - VIEW_RANGE,  MY_LNG + VIEW_RANGE]
lightHours = [x for x in range(sunData[0], sunData[1])] 

isNightTime = timeNow not in lightHours
isInLngRange = ISSPosition[0] >= lngRange[0] and ISSPosition[0] <= lngRange[1]
isInLatRange = ISSPosition[0] >= latRange[0] and ISSPosition[0] <= latRange[1]

myEmail = "test@test.com"
myPass = "test"
mySMTPAddress= "SMTP"

if isNightTime and isInLngRange and isInLatRange:
    print("look up")

    #### Im not going to make an email for this ####
    # Then send me an email to tell me to look up.
    with smtplib.SMTP(mySMTPAddress) as connection:
        connection.starttls()
        connection.login(myEmail, myPass)
        connection.sendmail(
            from_addr=myEmail,
            to_addrs="sendAddress@test.com",
            msg="ISS overhead, look up"
            )
        

# BONUS: run the code every 60 seconds.