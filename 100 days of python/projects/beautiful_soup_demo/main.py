from bs4 import BeautifulSoup

with open(r"100 days of python\projects\beautiful_soup_demo\index.html", encoding="utf8") as file:
    contents = file.read()
    print(contents)

soup = BeautifulSoup(markup=contents, features="html.parser")

for i in soup.find_all("a"):
    print(i.get("href"))
