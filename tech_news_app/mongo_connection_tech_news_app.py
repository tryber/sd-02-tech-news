from pymongo import MongoClient
import re


def mongo_search_by_title(text):
    client = MongoClient()
    db = client.tech_news_test
    return db.news_collection.find(
        {"title": re.compile(f".*{text}.*", re.IGNORECASE)},
        {"_id": 0, "url": 1, "title": 1},
    )
    client.close()


# def find_duplicate(array_news):
#     client = MongoClient()
#     db = client.tech_news_test  # determina o banco de dados
#     line = 1
#     for new in array_news:
#         duplicate = db.news_collection.find_one({"url": new["url"]})
#         if duplicate:
#             return line
#         line += 1
#     client.close()


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
