from pymongo import MongoClient


def find_top_5_news():
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.aggregate(
            [
                {
                    "$project": {
                        "_id": 0,
                        "url": 1,
                        "title": 1,
                        "sum_share_comments": {
                            "$add": [
                                "$shares_count",
                                "$comments_count",
                            ]
                        },
                    }
                },
                {"$sort": {"sum_share_comments": -1, "title": 1}},
                {"$limit": 5},
            ]
        )
    return list(news)


def find_top_5_categories():
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.aggregate(
            [
                {"$unwind": "$categories"},
                {
                    "$group": {
                        "_id": "$categories",
                        "sum_categories": {"$sum": 1},
                    }
                },
                {"$sort": {"sum_categories": -1, "_id": 1}},
                {"$limit": 5},
                {
                    "$project": {
                        "_id": 0,
                        "category": "$_id",
                        "sum_categories": 1,
                    }
                },
            ]
        )
    return list(news)


def top_5_news():
    return [f"- {news['title']}: {news['url']}" for news in find_top_5_news()]


def top_5_categories():
    return [f"- {news['category']}" for news in find_top_5_categories()]
