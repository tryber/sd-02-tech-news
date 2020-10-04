import sys
from pymongo import MongoClient
from datetime import datetime


def return_content(find_for_text):
    final_array = []
    for content in find_for_text:
        final_array.append(f'- {content["title"]}: {content["url"]}')
    return final_array


def mongo_query(query):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        find_for_text = db["news"].aggregate(
            [
                {"$match": query},
                {"$project": {"title": 1, "url": 1, "_id": 0}},
            ]
        )
    return find_for_text


def search_by_title(title):
    find_for_text = mongo_query({
        "title": {"$regex": title, "$options": "i"}
        })
    return return_content(find_for_text)


def search_by_date(date):
    try:
        formatdate = datetime.fromisoformat(date)
        find_for_text = mongo_query({"timestamp": {
                "$regex": str(formatdate).split(" ")[0]
            }})
        return return_content(find_for_text)
    except ValueError:
        print("Data inválida", file=sys.stderr)


def search_by_source(param):
    find_for_text = mongo_query({
        "sources": {"$regex": param, "$options": "i"}
        })
    return return_content(find_for_text)


def search_by_category(param):
    find_for_text = mongo_query({
        "categories": {"$regex": param, "$options": "i"}
        })
    return return_content(find_for_text)
