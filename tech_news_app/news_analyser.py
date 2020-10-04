from pymongo import MongoClient


def print_content(findForText):
    array_final = []
    for index, content in enumerate(findForText):
        if index == 5:
            break
        array_final.append(f'- {content["title"]}: {content["url"]}')
    return array_final


def mongo_query(pipeline):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        find = db["news"].aggregate(pipeline)
    return find


def top_5_news():
    results = mongo_query(
        [
            {"$addFields": {
                "total": {"$add": ["$comments_count", "$shares_count"]}
            }},
            {"$sort": {"total": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"url": 1, "title": 1, "_id": 0}},
        ]
    )
    return print_content(results)


def print_content_categories(categories):
    array_final = []
    for index, content in enumerate(categories):
        if index == 5:
            break
        array_final.append(f'- {content["_id"]}')
    return array_final


def top_5_categories():
    results = mongo_query(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"total": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    return print_content_categories(results)
