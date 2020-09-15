from pymongo import MongoClient


def print_content(findForText):
    boolean = True
    for index, content in enumerate(findForText):
        if index == 5:
            break
        boolean = False
        print([f'- {content["title"]}: {content["url"]}'])
    if boolean:
        print([])


def mongoQuery(pipeline):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        find = db["news"].aggregate(pipeline)
    return find


def top_5_news():
    results = mongoQuery(
        [
            {"$addFields": {"total": {"$add": ["$comments_count", "$shares_count"]}}},
            {"$sort": {"total": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"url": 1, "title": 1, "_id": 0}},
        ]
    )
    print_content(results)


def print_content_categories(categories):
    boolean = True
    for index, content in enumerate(categories):
        if index == 5:
            break
        boolean = False
        print([f'- {content["_id"]}'])
    if boolean:
        print([])


def top_5_categories():
    results = mongoQuery(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"total": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    print_content_categories(results)
