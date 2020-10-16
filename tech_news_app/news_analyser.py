from mongo_connection_tech_news_app import (
    db_top_5_news,
    db_top_5_categories
)
from datetime import datetime
import sys


def top_5_news():
    news_list = db_top_5_news()
    return [
        f"- {news['title']}: {news['url']}"
        for news in news_list
    ]


def top_5_categories():
    categories_list = db_top_5_categories()
    return [
        f"- {news['title']}: {news['url']}"
        for news in categories_list
    ]


top_5_categories()
