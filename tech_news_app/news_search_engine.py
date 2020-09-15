from pymongo import MongoClient
from datetime import datetime


def print_content(findForText):
    boolean = True
    for content in findForText:
        boolean = False
        print([f'- {content["title"]}: {content["url"]}'])
    if boolean:
        print([])


def mongoQuery(query):
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
    findForText = mongoQuery({"title": {"$regex": title, "$options": "i"}})
    print_content(findForText)


def search_by_date(date):
    try:
        formatdate = datetime.fromisoformat(date)
        findForText = mongoQuery({"timestamp": {"$regex": str(formatdate).split(" ")[0]}})
        print_content(findForText)
    except ValueError:
        print("Data inválida")


def search_by_source(param):
    findForText = mongoQuery({"sources": param})
    print_content(findForText)


def search_by_category(param):
    findForText = mongoQuery({"categories": param})
    print_content(findForText)


search_by_category("TikTok")
