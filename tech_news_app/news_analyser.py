from pymongo import MongoClient


def top_5_news():
    with MongoClient() as client:
        db = client.tech_news

        searched_news = list(db.news.aggregate([
            {
                "$addFields": {
                    "shares_and_comments": {
                        "$sum": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"shares_and_comments": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"title": 1, "url": 1, "_id": 0}}
        ]))

        return [
            f"- {news['title']}: {news['url']}"
            for news in searched_news
        ]


def top_5_categories():
    with MongoClient() as client:
        db = client.tech_news

        searched_news = list(db.news.aggregate([
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                    "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1}},
            {"$limit": 5},
            {"$sort": {"_id": 1}}
        ]))

        return [
            f"- {news['_id']}"
            for news in searched_news
        ]
