import os 
import requests 
import json
from time import sleep
import subprocess, sys

#url 
url = 'https://api.kanye.rest'

#turns API into a quote stored as quote
def quote():
    r = requests.get(url = url)
    data = r.json()
    quote = data['quote']
    return(quote)

def balls():
	applescript = """
	set input to "{quote()}"

	tell application "Messages"
		set targetBuddy to "(630)-842-5122"
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
