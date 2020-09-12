from pymongo import MongoClient


def insert_news(news):
    with MongoClient() as client:
        db = client.tech_news
        for item in news:
            db.extracted_news.find_one_and_replace(
                {"url": item["url"]},
                {
                    "url": item["url"],
                    "title": item["title"],
                    "timestamp": item["timestamp"],
                    "writer": item["writer"],
                    "shares_count": item["shares_count"],
                    "comments_count": item["comments_count"],
                    "summary": item["summary"],
                    "sources": item["sources"],
                    "categories": item["categories"],
                },
                upsert=True,
            )
