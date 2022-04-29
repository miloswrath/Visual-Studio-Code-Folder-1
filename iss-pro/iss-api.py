import json
import requests
from time import time, sleep
import subprocess, sys 
import numpy as np
import os


#setting url value
url = 'http://api.open-notify.org/iss-now.json'

#phone number 
phone = '2248294470'

#the variable of time that will be used between each pull of the api
time_var = 99

#the following sends a message using the input to a phone number of choice
def message(text, title):

    applescript = """
    set input to "iss is above bro"
    
    tell application "Messages"
        set targetBuddy to "(224)-829-4470"
        set targetService to id of 1st account whose service type = iMessage
        set textMessage to input
        set theBuddy to participant targetBuddy of account id targetService
        send textMessage to theBuddy
    end tell

    """
    args = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + args ,stdout=subprocess.PIPE )
    progname = proc.stdout.read().strip()
    sys.stdout.write(str(progname))
    #brings a system notification as well, optional

    os.system("""
    osascript -e 'display notification "{}"'

    """.format(text, title))


#this checks the api and if the longitude of the iss is within range of the longitude of a certain location then it uses the message function
def check_and_message():
    req = requests.get(url=url)
    data =req.json()
    iss_long = data['iss_position']['longitude']
    
    #if within a certain range then run message with title and text as follows
    if -98.0 <= float(iss_long) <= -78.0:
        message("THE ISS IS ABOVE", "ISS-API")
    #if not within range print the range (optional) and print not above
    else:
        print(iss_long)
        print("not above")

#waits the time variable and then runs the check and message function
while True:
    sleep(time_var)
    check_and_message()
