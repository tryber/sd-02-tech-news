from pymongo import MongoClient
from datetime import datetime


def print_content(findForText):
    boolean = True
    for content in findForText:
        boolean = False
        print([f'- {content["title"]}: {content["url"]}'])
    if boolean:
        print([])


def mongo_query(query):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        findForText = db["news"].aggregate(
            [
                {"$match": query},
                {"$project": {"title": 1, "url": 1, "_id": 0}},
            ]
        )
    return findForText


def search_by_title(title):
    findForText = mongo_query({"title": {"$regex": title, "$options": "i"}})
    print_content(findForText)


def search_by_date(date):
    try:
        formatdate = datetime.fromisoformat(date)
        findForText = mongo_query({"timestamp": {
                "$regex": str(formatdate).split(" ")[0]
            }})
        print_content(findForText)
    except ValueError:
        print("Data inválida")


def search_by_source(param):
    findForText = mongo_query({"sources": {"$regex": param, "$options": "i"}})
    print_content(findForText)


def search_by_category(param):
    findForText = mongo_query({"categories": {"$regex": param, "$options": "i"}})
    print_content(findForText)
