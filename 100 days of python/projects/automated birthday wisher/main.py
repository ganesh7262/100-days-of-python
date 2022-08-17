import datetime as dt
import random
import smtplib
import pandas as pd


birthday_date=pd.DataFrame({
    'name':['ganesh','naresh'],
    'birthday':[dt.datetime(year=2000,month=8,day=14),dt.datetime(year=2002,month=11,day=13)]
})

dt_obj=dt.datetime.now()

email = 'abc@gmail.com'
password = 'abc'



for i,date in enumerate(birthday_date.birthday):
    if date.month == dt.datetime.month() and date.day==dt.datetime.day():
        with smtplib.SMTP(host='smtp.gmail.com') as connection:
            connection.starttls()        
            connection.login(user=email,password=password)
            bday_person=birthday_date[birthday_date.index==i]
            birthday_msg=f'''Subject:Happy Birtday {bday_person}
            
            'Happy bday'''
            connection.sendmail(from_addr=email,to_addrs='abc@yahoo.com',msg=birthday_msg)


    