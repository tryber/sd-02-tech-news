import csv
import sys
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
            writer.writerow(row.values())
    print("Exportação realizada com sucesso", file=sys.stdout)


def json_exporter():
    raise NotImplementedError


csv_exporter("news.cs")
