from pymongo import MongoClient


def insert_news_scrapper(news):
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


def check_repetead_url(row):
    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find_one({"url": row["url"]})


def insert_news_importer(news):
    with MongoClient() as client:
        db = client.tech_news
        for index, row in enumerate(news, start=1):
            repetead_url = check_repetead_url(row)
            if not repetead_url:
                db.extracted_news.insert_one(
                    {
                        "url": row["url"],
                        "title": row["title"],
                        "timestamp": row["timestamp"],
                        "writer": row["writer"],
                        "shares_count": row["shares_count"],
                        "comments_count": row["comments_count"],
                        "summary": row["summary"],
                        "sources": row["sources"],
                        "categories": row["categories"],
                    },
                )
            if repetead_url:
                print(f"Notícia {index} duplicada")
