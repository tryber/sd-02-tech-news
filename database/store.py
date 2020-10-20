from pymongo import MongoClient


def store_news(data):
    with MongoClient() as client:
        db = client.tech_news

        db.news.insert_many(data)
