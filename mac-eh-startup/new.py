import os 
import requests 
import json
from time import sleep

#url 
url = 'https://api.kanye.rest'

#turns API into a quote stored as quote
def quote():
    r = requests.get(url = url)
    data = r.json()
    quote = data['quote']
    return(quote)

#function used to notify me with applescript
def notify(title, text):
    os.system("""
    osascript -e 'display notification "{}"'

    """.format(text, title))
while True:
    sleep(900)
    notify("title", quote())

    