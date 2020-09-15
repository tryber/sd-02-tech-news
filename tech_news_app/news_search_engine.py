import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from tech_news_data_collector.mongo_connection import get_news_by_title


def search_by_title(title):
    news_list = []
    news = list(get_news_by_title(title))
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    print(news_list)


def search_by_date():
    raise NotImplementedError


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


search_by_title("CELULAR")
