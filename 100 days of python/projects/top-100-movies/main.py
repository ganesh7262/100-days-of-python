import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, features="html.parser")
movies = [i.text for i in soup.find_all(name="h3", class_="title")]
movies = movies[::-1]

with open(r"100 days of python\projects\top-100-movies\top 100 movies", mode="w", encoding="utf-8") as txt:
    for i in movies:
        txt.write(f"{i}\n")
