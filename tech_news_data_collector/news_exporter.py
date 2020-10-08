import sys
import csv
import json
from pymongo import MongoClient


def get_all_mongo():
    with MongoClient() as connection:
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        model_answer = collection.find({}, {"_id": 0})
        return list(model_answer)


def csv_exporter(file_name):
    if not file_name.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return

    news = get_all_mongo()
    with open(file_name, "w") as csvdata:
        writer = csv.writer(csvdata, delimiter=";")
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

        for notice in news:
            new_notice = [
                notice["url"],
                notice["title"],
                notice["timestamp"],
                notice["writer"],
                notice["shares_count"],
                notice["comments_count"],
                notice["summary"],
                ",".join(notice["sources"]),
                ",".join(notice["categories"]),
            ]
            writer.writerow(new_notice)
        print("Exportação realizada com sucesso")


def json_exporter(file_name):
    if not file_name.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return
    with open(file_name, "w") as jsondata:
        news = get_all_mongo()
        json.dump(news, jsondata)
        print("Exportação realizada com sucesso")


# json_exporter("teste.json")
# csv_exporter("teste.csv")
