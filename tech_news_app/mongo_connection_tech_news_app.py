from pymongo import MongoClient
import re


def db_search_by_title(text):
    client = MongoClient()
    db = client.tech_news
    return db.news_collection.find(
        {"title": re.compile(f".*{text}.*", re.IGNORECASE)},
        {"_id": 0, "url": 1, "title": 1},
    )


def db_search_by_date(date):
    client = MongoClient()
    db = client.tech_news
    searched_news = list(db.news_collection.find(
        {"timestamp": re.compile(f"{date}")},
        {"title": 1, "url": 1, "_id": 0}
    ))
    return searched_news


def db_search_by_source(source):
    client = MongoClient()
    db = client.tech_news  # determina o banco de dados
    searched_news = list(db.news_collection.find(
        {"sources": re.compile(source, re.IGNORECASE)},
        {"title": 1, "url": 1, "_id": 0}
    ))
    return searched_news


def db_search_by_category(category):
    client = MongoClient()
    db = client.tech_news  # determina o banco de dados
    searched_news = list(db.news_collection.find(
        {"categories": re.compile(category, re.IGNORECASE)},
        {"title": 1, "url": 1, "_id": 0}
    ))
    return searched_news


def db_top_5_news():
    client = MongoClient()
    db = client.tech_news  # determina o banco de dados
    top_5_news = list(db.news_collection.aggregate([
            {
                "$addFields": {
                    "shares_and_comments": {
                        "$sum": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"shares_and_comments": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"title": 1, "url": 1, "_id": 0}}
        ]))
    return top_5_news


def db_top_5_categories():
    client = MongoClient()
    db = client.tech_news  # determina o banco de dados
    top_5_categories = list(db.news.aggregate([
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5}
        ]))
    return top_5_categories
