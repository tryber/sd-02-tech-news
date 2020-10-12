from pymongo import MongoClient
import sys


def news_to_database(array_news):
    client = MongoClient()
    db = client.tech_news_test  # determina o banco de dados
    for new in array_news:
        db.news_collection.find_one_and_replace(
            {"url": new["url"]},
            {
                "url": new["url"],
                "title": new["title"],
                "timestamp": new["timestamp"],
                "writer": new["writer"],
                "shares_count": new["shares_count"],
                "comments_count": new["comments_count"],
                "summary": new["summary"],
                "sources": new["sources"],
                "categories": new["categories"],
            },
            upsert=True,
        )


def find_duplicate(array_news):
    client = MongoClient()
    db = client.tech_news_test  # determina o banco de dados
    line = 1
    for new in array_news:
        duplicate = db.news_collection.find_one({"url": new["url"]})
        if duplicate:
            return line
        line += 1
