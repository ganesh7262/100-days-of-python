import requests
from bs4 import BeautifulSoup
import string
import re

TARGET_PRICE = 3400

URL = "https://www.amazon.in/dp/B08MT7DZ5Y/ref=sspa_dk_detail_4?pd_rd_i=B08MT7DZ5Y&pd_rd_w=caEC1&content-id=amzn1.sym.b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_p=b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_r=EP8R81PV5RG6WW21PBWP&pd_rd_wg=CFMQn&pd_rd_r=9fc4f584-19ea-41f6-bae3-e6903534d7df&s=shoes&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1&psc=1"


# we need to send this headers to amazon to get proper proper page source
header = {
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)


soup = BeautifulSoup(response.text, features="lxml")

price = soup.find(name="span", class_="a-price-whole").text
price = int(re.sub("[,.]", "", price))
if(price < TARGET_PRICE):
    print("buy")
