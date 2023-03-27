import re
import requests
from bs4 import BeautifulSoup

date = input("Enter the Date to create a playlist (YYYY-MM-DD): ")

billboard_link = f"https://www.billboard.com/charts/billboard-global-200/{date}/"

response = requests.get(billboard_link).text

soup = BeautifulSoup(response, features="html.parser")

songs = [f"{idx+1}> "+re.sub("[\t\n]", "", i.get_text())
         for idx, i in enumerate(soup.select(selector="li ul li h3"))]

print(songs)
