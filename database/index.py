from pymongo import MongoClient


def create_news(data):
    with MongoClient() as client:
        db = client.tech_news

        db.news.insert_many(data)


def find_news():
    with MongoClient() as client:
        db = client.tech_news

        return list(db.news.find())
