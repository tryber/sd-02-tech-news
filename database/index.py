from pymongo import MongoClient


def create_news(data):
    with MongoClient() as client:
        db = client.tech_news
        if data:
            db.news.insert_many(data)


def find_new(url):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.find({"url": url}, {"_id": 0}))


def find_news():
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.find({}, {"_id": 0}))


def search_news(query):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.find(query))


def aggregate_news(query):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.aggregate(query))


def upsert_news(data):
    with MongoClient() as client:
        db = client.tech_news
        for new in data:
            db.news.update_one({"url": new["url"]}, {
                               "$set": new}, **{"upsert": True})
