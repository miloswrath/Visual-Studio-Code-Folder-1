import requests
import os

url = 'http://api.open-notify.org/iss-now.json'
req = requests.get(url=url)
data = req.json()

a = data['iss_position']['longitude']
print(a)


