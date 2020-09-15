import csv
from pymongo import MongoClient
import re
import sys
import json
from bson import ObjectId


def mongo_extract():
    results = []
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for news in db["news"].find({}):
            results.append(news)
    return results


def csv_exporter(arquive):
    documents = mongo_extract()
    with open(arquive.lower(), "w") as file:
        writer = csv.writer(file, delimiter=";")
        headers = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ]
        writer.writerow(headers)
        for document in documents:
            row = [
                document["url"],
                document["title"],
                document["timestamp"],
                document["writer"],
                document["shares_count"],
                document["comments_count"],
                document["summary"],
                document["sources"],
                document["categories"],
            ]
            writer.writerow(row)
    print("Exportação realizada com sucesso")


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def json_exporter(arquive):
    documents = mongo_extract()
    with open(arquive.lower(), "w") as file:
        json.dump(documents, file, cls=JSONEncoder)
    print("Exportação realizada com sucesso")


arquive = input("Digite o nome do arquivo com .csv ou .json\n")

if re.search(".csv$", arquive, re.IGNORECASE):
    csv_exporter(arquive)
elif re.search(".json$", arquive, re.IGNORECASE):
    json_exporter(arquive)
else:
    print("Formato inválido", file=sys.stderr)
