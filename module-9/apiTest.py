#Brett Fuller
#12/08/2024
#CSD 325  – Assignment 9.2

import requests
import json

#Function to output a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#finst validate that api's are working
response = requests.get('http://www.google.com')
print("Printing the test connection to google to make sure api is working:")
print(response.status_code)
print()

#Query the astros.json api from open notify
response = requests.get("http://api.open-notify.org/astros.json")
#print status
print("Testing connection to open-notify:")
print(response.status_code)
print()

#print unformatted response from opennotify
print("Unformatted response on astronauts from open-notify:")
print(response.json())
print()

#Print formatted response from opennotify using jprint function
print("Formatted open-notify response:")
jprint(response.json())
print()

#connect to unofficial star wars api, pull information on Empire Strikes Back
response = requests.get('https://swapi.dev/api/films/2/')

#print status
print("Testing connection to unofficial star wars api:")
print(response.status_code)
print()

#print unformatted text
print()
print("Unformatted response on empire from unofficial star wars api:")
print(response.json())

#print formatted text using jprint function
print()
print("Formatted jpl response:")
jprint(response.json())