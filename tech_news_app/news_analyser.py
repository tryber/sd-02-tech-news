from mongo_connection import tech_news_db


def format_results(results):
    return [f" - {i['url']}: {i['title']}" for i in list(results)]


def format_categories(categories):
    return [f" - {i['_id']}" for i in list(categories)]


def top_5_news():
    results = tech_news_db().pages.aggregate(
        [
            {
                "$addFields": {
                    "total": {
                        "$sum": [
                            {"$toInt": "$comments_count"},
                            {"$toInt": "$shares_count"},
                        ]
                    }
                }
            },
            {"$sort": {"title": 1}},
            {"$limit": 5},
            {
                "$project": {"_id": 0, "title": 1, "url": 1},
            },
        ]
    )
    return format_results(results)


def top_5_categories():
    categories = tech_news_db().pages.aggregate(
        [
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                    "categories_count": {"$sum": 1},
                }
            },
            {"$sort": {"categories_count": -1}},
            {"$limit": 5},
            {"$project": {"_id": 1, "categories_count": 0}},
        ]
    )
    return format_categories(categories)
