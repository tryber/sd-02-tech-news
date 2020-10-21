from mongo_connection_tech_news_app import (
    db_search_by_title,
    db_search_by_date,
    db_search_by_source,
    db_search_by_category
)
from datetime import datetime
import sys


def search_by_title(search):
    all_news = []
    news = db_search_by_title(search)
    for new in news:
        title = new["title"]
        url = new["url"]
        all_news.append(f"- {title}: {url}")
    return all_news


def check_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d")
        return str(format_date).split(" ")[0]
    except ValueError:
        print("Data inválida", file=sys.stderr)
        return False


def search_by_date(date):
    valid_date = check_date(date)
    if not valid_date:
        sys.exit(1)
    news = db_search_by_date(valid_date)
    return news


def search_by_source(source):
    searched_news = db_search_by_source(source)
    return [
        f"- {new['title']}: {new['url']}"
        for new in searched_news
    ]


def search_by_category(category):
    searched_news = db_search_by_category(category)
    return [
        f"- {new['title']}: {new['url']}"
        for new in searched_news
    ]
