import datetime
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCKAPI = 'PDKJ3VICPEQLLCWJ'
NEWSAPI='0883d756989140e992e5ea9c215fb1e7'
today = datetime.datetime.today().date()
most_recent_date = str(today).replace(str(today.day), str(int(today.day)-3))
day_before_mrd = str(today).replace(
    str(today.day), str(int(today.day)-4))



def news():
    news_url='https://newsapi.org/v2/top-headlines'
    news_para={
        'apiKey':NEWSAPI,
        'q':COMPANY_NAME
    }
    news_response=requests.get(url=news_url,params=news_para)
    news_response.raise_for_status()
    news_data=news_response.json()

    for news in news_data['articles']:
        print(news['title'])


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
para = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCKAPI,
}
stock_url = 'https://www.alphavantage.co/query'


stock_response = requests.get(url=stock_url, params=para)
stock_response.raise_for_status()

data = stock_response.json()
mrd_close_data = data['Time Series (Daily)'][str(most_recent_date)]['4. close']
day_before_mrd_close_data = data['Time Series (Daily)'][str(
    day_before_mrd)]['4. close']


if abs(100-((float(mrd_close_data)/float(day_before_mrd_close_data))*100)) > 5:
    news()

