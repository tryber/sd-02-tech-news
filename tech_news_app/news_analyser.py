from pymongo import MongoClient


def connect_to_mongo(results):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        return collection.aggregate(results)


def print_correct_name(results):
    items = []
    for result in results:
        items.append(f"- {result['title']}: {result['url']}")
    return items


def top_5_news():
    aggregate = [
        {
            "$addFields":
            {
                "totalLikes":
                {"$add": ["$comments_count", "$shares_count"]}
            }
        },
        {
            "$sort": {"totalLikes": -1, "title": 1}
        },
        {"$limit": 5},
        {"$project": {"title": 1, "url": 1, "_id": 0}}
    ]
    get_db = connect_to_mongo(aggregate)
    return print_correct_name(get_db)


def top_5_categories():
    aggregate = [
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories",  "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]
    get_db = connect_to_mongo(aggregate)
    items = []
    for result in get_db:
        items.append(f"- {result['_id']}")
    return items
