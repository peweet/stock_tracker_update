from dotenv import load_dotenv
import os
import requests
from utility import return_date
load_dotenv()
class News:
    def __init__(self):
        self.news_api_key = os.getenv("NEWS_API_KEY")
        self.url = 'https://newsapi.org/v2/everything?'
        self.news_params = {
            "q": "tesla",
            "from": return_date(30),
            "sortBy": "publishedAt",
            "apiKey": self.news_api_key
        }

    def get_news(self):
        nws = requests.get(self.url, params=self.news_params)
        reputable_authors = ['Reuters', 'bloomberg.com', 'euronews.com', 'Bloomberg News', 'nytimes.com', 'barrons.com']
        news_articles = nws.json()
        news_articles = news_articles["articles"]
        filtered_articles = [article for article in news_articles if article.get('author') in reputable_authors]
        get_urls = filtered_articles[:10]
        url = [url['url'] for url in get_urls]
        return url

