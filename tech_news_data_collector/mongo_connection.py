from pymongo import MongoClient
import re
import datetime


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


def get_news():
    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find({}, {"_id": 0})


def get_news_by_title(title):
    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find(
            {"title": re.compile(f".*{title}.*", re.IGNORECASE)},
            {"_id": 0, "url": 1, "title": 1},
        )


def get_news_by_date(date):
    year, month, day = date.split("-")
    # solução encontrada em:
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat
    begin = datetime.datetime(int(year), int(month), int(day)).isoformat(
        sep="T"
    )

    end = datetime.datetime(
        int(year), int(month), int(day), 23, 59, 59
    ).isoformat(sep="T")

    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find(
            {
                "timestamp": {
                    "$gte": begin,
                    "$lte": end,
                }
            },
            {"_id": 0, "url": 1, "title": 1},
        )


def get_news_by_source(source):
    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find(
            {"sources": re.compile(f"^{source}$", re.IGNORECASE)},
            {"_id": 0, "url": 1, "title": 1},
        )


def get_news_by_category(category):
    with MongoClient() as client:
        db = client.tech_news
        return db.extracted_news.find(
            {"categories": re.compile(f"^{category}$", re.IGNORECASE)},
            {"_id": 0, "url": 1, "title": 1},
        )
