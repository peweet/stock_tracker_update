from dotenv import load_dotenv
import os
import requests
from utility import return_date, calculate_percentage_change
from news import News
load_dotenv()
class StockMarketPrice:
    def __init__(self):
        self.api_key = os.getenv("ALPHA_ADVANTAGE_API_KEY")
    def stock_price_comparison(self):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "IBM",
            "outputsize": "compact",
            "apikey": self.api_key
        }
        url = 'https://www.alphavantage.co/query?'
        r = requests.get(url, params=params)
        print(r.raw)
        yesterday_date = return_date(1)
        data = r.json()
        print(data)
        print(r.content)
        print(r.url)
        stock_price_close = data["Time Series (Daily)"][yesterday_date]['4. close']
        two_days_before_yesterday_date = return_date(2)
        two_days_before_stock_price_close = data["Time Series (Daily)"][two_days_before_yesterday_date]['4. close']
        stock_price_close_f = float(stock_price_close)
        two_days_before_stock_price_close_f = float(two_days_before_stock_price_close)
        percentage_change = calculate_percentage_change(stock_price_close_f, two_days_before_stock_price_close_f)
        if percentage_change >= 1:
            news = News()
            return news.get_news()
        else:
            return