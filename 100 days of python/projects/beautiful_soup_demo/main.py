from bs4 import BeautifulSoup
import requests

live_web = "https://news.ycombinator.com/news"


response = requests.get(live_web)

soup = BeautifulSoup(markup=response.text, features="html.parser")
article_titles = [i.find(name="a").text for i in soup.find_all(
    name="span", class_="titleline")]

article_links = [i.find(name="a").get("href")
                 for i in soup.find_all(name="span", class_="titleline")]


article_score = [int(i.text.split()[0])
                 for i in soup.find_all(name="span", class_="score")]


max_score = article_score.index(max(article_score))
print(article_titles[max_score])
print(article_links[max_score])
