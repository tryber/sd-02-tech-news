import csv
import sys
from pymongo import MongoClient


def csv_exporter(file):
    if not file.endswith(".csv"):
        return print("Formato inválido", file=sys.stderr)

    with open(file, "w") as csv_file:
        header = [
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
        writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=header)
        writer.writeheader()

        client = MongoClient()
        documents = client.tech_news.news.find({}, {"_id": 0})

        for document in documents:
            row = {}
            for name, value in document.items():
                if name == "sources" or name == "categories":
                    row[name] = ",".join(value)
                else:
                    row[name] = value
            writer.writerow(row)

        print("Exportação realizada com sucesso", file=sys.stdout)
        client.close()


def json_exporter():
    raise NotImplementedError
