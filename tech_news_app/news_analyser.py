from pymongo import MongoClient


def top_5_news():
    with MongoClient() as connection:
        new_format = []
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        answer = collection.aggregate([
            {"$project": {
                "_id": 0,
                "popularity": {"$add": ["$comments_count", "$shares_count"]},
                "title": 1, "url": 1
            }},
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"title": 1, "url": 1}}
        ])
        result = list(answer)
        if len(result) < 5:
            all_notice = collection.aggregate([{"$project": {"_id": 0}}])
            return list(all_notice)
        for item in result:
            new_format.append(f"- {item['title']}: {item['url']}")
    return new_format


def top_5_categories():
    with MongoClient() as connection:
        new_format = []
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        answer = collection.aggregate([
            {"$unwind": "$categories"},
            {"$group": {
                "_id": "$categories",
                "id": {"$first": "$_id"},
                "count": {"$sum": 1},
            }},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
            {"$project": {"id": 0}}
        ])
        result = list(answer)
        for item in result:
            new_format.append(f"- {item['_id']}")
    return new_format
           

# print(top_5_news())
# print(top_5_categories())
