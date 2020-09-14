import csv
from pymongo import MongoClient
import re
import sys


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


def json_exporter():
    raise NotImplementedError


arquive = input("Digite o nome do arquivo com .csv\n")
if(re.search(".csv$", arquive, re.IGNORECASE)):
    csv_exporter(arquive)
else:
    print("Formato inválido", file=sys.stderr)
