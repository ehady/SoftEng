import requests
import json


response = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw').text
#could have used this also : requests.get(‘https://api.covid19api.com/summary’).json() which automatically converts it to a python dict
response_info = json.loads(response) #make it a python dictionary

warsaw_time = response_info['time']

print(warsaw_time)