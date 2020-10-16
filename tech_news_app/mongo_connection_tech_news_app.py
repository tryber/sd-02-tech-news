from pymongo import MongoClient
from datetime import datetime
import re


def mongo_search_by_title(text):
    client = MongoClient()
    db = client.tech_news_test
    return db.news_collection.find(
        {"title": re.compile(f".*{text}.*", re.IGNORECASE)},
        {"_id": 0, "url": 1, "title": 1},
    )
    client.close()


def mongo_search_by_date(date):
    client = MongoClient()
    db = client.tech_news_test
    searched_news = list(db.news_collection.find(
        {"timestamp": re.compile(f"{date}")},
        {"title": 1, "url": 1, "_id": 0}
    ))
    return searched_news


# def export_to_csv():
#     client = MongoClient()
#     db = client.tech_news_test  # determina o banco de dados
#     all_news = db.news_collection.find({}, {"_id": 0})
#     return all_news
#     client.close()


# def import_from_json(array_news):
#     client = MongoClient()
#     db = client.tech_news_test  # determina o banco de dados
#     db.news_collection.insert_many(array_news)
#     client.close()


# def export_to_json():
#     client = MongoClient()
#     db = client.tech_news_test  # determina o banco de dados
#     all_news = list(db.news_collection.find({}, {"_id": 0}))
#     return all_news
#     client.close()
