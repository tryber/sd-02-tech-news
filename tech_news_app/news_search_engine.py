from pymongo import MongoClient
from datetime import datetime


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
    results_null = True
    for result in results:
        results_null = False
        print(f'["- {result["title"]}: {result["url"]}"]')
    if results_null:
        print([])


def search_by_title(user_text):
    aggregate = {"title": {"$regex": user_text, "$options": "i"}}
    results = connect_to_mongo(aggregate)
    print_correct_name(results)

search_by_title("re")

def search_by_date(user_date):
    try:
        result = datetime.fromisoformat(user_date)
        result = str(result).split(" ")[0]
        aggregate = {"timestamp": {"$regex": result}}
        results = connect_to_mongo(aggregate)
        print_correct_name(results)
    except ValueError:
        print("Data inválida")


def search_by_source(user_text):
    aggregate = {"sources": user_text}
    results = connect_to_mongo(aggregate)
    print_correct_name(results)


def search_by_category(user_text):
    aggregate = {"categories": user_text}
    results = connect_to_mongo(aggregate)
    print_correct_name(results)
