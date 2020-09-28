import csv
import sys
import json
from mongo_connection import get_news


def csv_exporter(csv_file):
    if not csv_file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return
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
    with open(csv_file, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)
        news = get_news()
        for row in news:
            row["sources"] = ",".join(row["sources"])
            row["categories"] = ",".join(row["categories"])
            writer.writerow(row.values())
    print("Exportação realizada com sucesso", file=sys.stdout)


def json_exporter(json_file):
    if not json_file.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return
    with open(json_file, "w") as file:
        news = get_news()
        json.dump(list(news), file)
    print("Exportação realizada com sucesso", file=sys.stdout)


csv_exporter("newsss.csv")
# json_exporter("news.jso")
