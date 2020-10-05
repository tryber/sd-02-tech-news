from pymongo import MongoClient
import sys
import datetime


def find_by_title(title):
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.find(
            {"title": {"$regex": title, "$options": "i"}}
        )
        return list(news)


def find_by_date(date):
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.find({"timestamp": {"$regex": date}})
        return list(news)


def find_by_source(sources):
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.find(
            {"sources": {"$regex": sources, "$options": "i"}}
        )
        return list(news)


def find_by_category(category):
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.find(
            {"categories": {"$regex": category, "$options": "i"}}
        )
        return list(news)


def search_by_title(title):
    return [
        f"- {news['title']}: {news['url']}" for news in find_by_title(title)
    ]


def search_by_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return [
            f"- {news['title']}: {news['url']}"
            for news in find_by_date(date_text)
        ]
    except ValueError:
        print("Data inválida", file=sys.stderr)
        return ""


def search_by_source(sources):
    return [
        f"- {news['title']}: {news['url']}" for news in find_by_source(sources)
    ]


def search_by_category(category):
    return [
        f"- {news['title']}: {news['url']}"
        for news in find_by_category(category)
    ]
