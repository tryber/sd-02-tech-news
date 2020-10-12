from pymongo import MongoClient


def news_to_database(array_news):
    client = MongoClient()
    db = client.tech_news  # determina o banco de dados
    for new in array_news:
        db.news_collection.find_one_and_replace(
            {"url": new["url"]},
            {
                "url": new["url"],
                "title": new["title"],
                "timestamp": new["timestamp"],
                "writer": new["writer"],
                "shares_count": new["shares_count"],
                "comments_count": new["comments_count"],
                "summary": new["summary"],
                "sources": new["sources"],
                "categories": new["categories"],
            },
            upsert=True,
        )
