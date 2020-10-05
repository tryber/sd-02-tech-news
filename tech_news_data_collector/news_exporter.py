import csv
import json
import sys
from pymongo import MongoClient


def get_from_mongo():
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        result = collection.find({}, {"_id": 0})
        results = list(result)
        return results


def csv_exporter(csv_file):
    if not csv_file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return
    news = get_from_mongo()
    with open(csv_file, "w") as csvfile:
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
                ",".join(item["sources"]),
                ",".join(item["categories"]),
            ]
            writer.writerow(each_news)
        print("Exportação realizada com sucesso")


def json_exporter(json_file):
    if not json_file.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return
    news = get_from_mongo()
    with open(json_file, "w") as file:
        json.dump(news, file)
        print("Exportação realizada com sucesso")
