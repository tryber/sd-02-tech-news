import re
import sys
from mongo_connection import tech_news_db


def search_by_title(input):
    regex = f"{input}"
    news = tech_news_db().pages.find(
        {"title": {"$regex": regex, "$options": "i"}},
        {"_id": 0, "title": 1, "url": 1},
    )
    return list(news)


def is_valid_date(date):
    if not bool(re.match(r"\d{2}-\d{2}-\d{4}", date)):
        print("Data inválida", file=sys.stderr)
        raise ValueError


def search_by_date(date):
    try:
        is_valid_date(date)
        news = tech_news_db().pages.find(
            {"timestamp": date},
            {"_id": 0, "title": 1, "url": 1},
        )
        return list(news)
    except ValueError:
        print()


def search_by_source(source):
    news = tech_news_db().pages.find(
        {"$and": [{"sources": {"$regex": source, "$options": "i"}}]},
        {"_id": 0, "title": 1, "url": 1},
    )
    return list(news)


def search_by_category(category):
    news = tech_news_db().pages.find(
      {"$and": [{"categories": {"$regex": category, "$options": "i"}}]},
      {"_id": 0, "title": 1, "url": 1}
    )
    return list(news)
