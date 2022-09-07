#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import requests


response=requests.get(url='https://api.sheety.co/e6d78feb9ccefa13c5de92fb575d3bc3/copyOfFlightDeals/prices')
response.raise_for_status()
print(response.json())