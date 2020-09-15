from mongo_connection import tech_news_db


def top_5_news():
    news = tech_news_db().pages.aggregate(
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
    return list(news)


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
    return list(map(lambda x: x["_id"], list(categories)))
