import re
import sys
from datetime import datetime
from mongo_connection import tech_news_db


def format_results(results):
    return [f" - {i['title']}: {i['url']}" for i in list(results)]


def search_by_title(input):
    regex = f"{input}"
    results = tech_news_db().pages.find(
        {"title": {"$regex": regex, "$options": "i"}},
        {"_id": 0, "title": 1, "url": 1},
    )
    return format_results(results)


def is_valid_date(date):
    if not bool(re.match(r"\d{4}-\d{2}-\d{2}", date)):
        print("Data inválida", file=sys.stderr)
        raise ValueError


def search_by_date(input_date):
    try:
        is_valid_date(input_date)
        date = datetime.fromisoformat(input_date)
        results = tech_news_db().pages.find(
            {"timestamp": {"$eq": date}},
            {"_id": 0, "title": 1, "url": 1},
        )
        return format_results(results)
    except ValueError:
        print()


def search_by_source(source):
    results = tech_news_db().pages.find(
        {"$and": [{"sources": {"$regex": source, "$options": "i"}}]},
        {"_id": 0, "title": 1, "url": 1},
    )
    return format_results(results)


def search_by_category(category):
    results = tech_news_db().pages.find(
      {"$and": [{"categories": {"$regex": category, "$options": "i"}}]},
      {"_id": 0, "title": 1, "url": 1}
    )
    return format_results(results)
