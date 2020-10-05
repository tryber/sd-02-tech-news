from pymongo import MongoClient
from datetime import datetime
import sys


def connect_to_mongo(results):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        aggregation = [
            {"$match": results},
            {"$project": {"title": 1, "url": 1, "_id": 0}}
        ]
        return collection.aggregate(aggregation)


def print_correct_name(results):
    items = []
    for result in results:
        items.append(f"- {result['title']}: {result['url']}")
    return items


def search_by_title(user_text):
    aggregate = {"title": {"$regex": user_text, "$options": "i"}}
    results = connect_to_mongo(aggregate)
    return print_correct_name(results)


def search_by_date(user_date):
    try:
        result = datetime.fromisoformat(user_date)
        result = str(result).split(" ")[0]
        aggregate = {"timestamp": {"$regex": result}}
        results = connect_to_mongo(aggregate)
    except ValueError:
        print("Data invalida", file=sys.stderr) 
        return ""
    else:
        return print_correct_name(results)


def search_by_source(user_text):
    aggregate = {"sources": {"$regex": user_text, "$options": "i"}}
    results = connect_to_mongo(aggregate)
    return print_correct_name(results)


def search_by_category(user_text):
    aggregate = {"categories": {"$regex": user_text, "$options": "i"}}
    results = connect_to_mongo(aggregate)
    return print_correct_name(results)
