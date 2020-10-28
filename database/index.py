from pymongo import MongoClient


def create_news(data):
    with MongoClient() as client:
        db = client.tech_news

        db.news.insert_many(data)


def find_news():
    with MongoClient() as client:
        db = client.tech_news

        return list(db.news.find())


def create_or_update_news(data):
    with MongoClient() as client:
        db = client.tech_news

        for new in data:
            exist = list(db.news.find({"url": new["url"]}))
            if exist:
                url = new.pop("url")
                db.news.update_one({"url": url}, {"$set": new})
            else:
                db.news.insert_one(new)
