from pymongo import MongoClient
from datetime import datetime
import sys


def search_by_title(search):
    with MongoClient() as client:
        db = client.tech_news

        searched_news = list(db.news.find(
            {"title": {"$regex": search, "$options": 'i'}},
            {"title": 1, "url": 1, "_id": 0}
        ))

        return [
            f"- {news['title']}: {news['url']}"
            for news in searched_news
        ]


def search_by_date(search):
    # Código adaptado da seguinte fonte: https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
    try:
        datetime.strptime(search, "%Y-%m-%d")
    except ValueError:
        return print("Data inválida", file=sys.stderr)

    with MongoClient() as client:
        db = client.tech_news

        searched_news = list(db.news.find(
            {"timestamp": {"$regex": search}},
            {"title": 1, "url": 1, "_id": 0}
        ))

        return [
            f"- {news['title']}: {news['url']}"
            for news in searched_news
        ]


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError
