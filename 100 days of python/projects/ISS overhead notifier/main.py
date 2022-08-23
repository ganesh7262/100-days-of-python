import time
from datetime import datetime
import requests
MY_LAT=18.520430
MY_LONG=73.856743
cur_time=datetime.now()
import smtplib 

def iss_overhead_bool():
    response=requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data=response.json()
    longitude=float(data['iss_position']['longitude'])
    latitude=float(data['iss_position']['latitude'])
    if (longitude==MY_LONG + 5 or longitude==MY_LONG-5) and (latitude==MY_LAT+5 or latitude==MY_LAT-5):
        return True
    else:
        return False
    


def is_night():
    parameters={
        'lat':MY_LAT,
        'lng':MY_LONG,
        'formatted':0
    }

    response=requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset=int(data['results']['sunset'].split('T')[1].split(':')[0])
    if cur_time.hour>=sunset or cur_time.hour<=sunrise:
        return True
    else:
        return False
    
while True:
    time.sleep(60)
    if iss_overhead_bool and is_night:
        connection=smtplib.SMTP(host='smtp.gmail.com')
        connection.starttls()
        connection.login(user='ganesh@gmail.com',password='pass')
        connection.sendmail(from_addr='ganesh@gmail.com',to_addrs='ganesh@gmail.com',msg="look up")
    
    