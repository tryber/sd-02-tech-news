from pymongo import MongoClient


def tech_news_db():
    client = MongoClient()
    return client.tech_news
