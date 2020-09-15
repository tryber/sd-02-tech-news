import csv
from pymongo import MongoClient


def get_from_mongo():
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        result = collection.find({}, {"_id": 0})
        results = list(result)
        return results


def csv_exporter(csv_name):
    news = get_from_mongo()
    with open(csv_name + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        headers = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories"
        ]
        writer.writerow(headers)
        for item in news:
            each_news = [
                item["url"],
                item["title"],
                item["timestamp"],
                item["writer"],
                item["shares_count"],
                item["comments_count"],
                item["summary"],
                item["sources"],
                item["categories"]
            ]
            writer.writerow(each_news)


def json_exporter():
    raise NotImplementedError
