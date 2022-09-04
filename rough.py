# open weather appi
import requests
import os
APIKEY='b7bbcc47b267a503b91b217e48b0a950'
# url1='https://api.openweathermap.org/data/2.5/weather'
# url='https://api.openweathermap.org/data/2.5/onecall'
# params={
#     'lat':18.520430,
#     'lon':73.856743,
#     'appid':APIKEY,
#     'exclude':'current,minutely,daily'
    
    
    
# }


# response=requests.get(url=url,params=params)
# response.raise_for_status()

# print(response.json())

print(os.getenv('OMW_API_KEY'))