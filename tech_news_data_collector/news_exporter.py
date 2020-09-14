import csv
import json
import sys
import os
from mongo_connection import tech_news_db


valid_header = [
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


def check_file_extention(filename, extention):
    if os.path.splitext(filename)[1] != extention:
        raise IOError


def find_all():
    cur = tech_news_db().pages.find({}, {"_id": 0})
    arr = []
    for doc in cur:
        arr.append(doc)
    return arr


def is_header_valid(header):
    if len(header) != len(valid_header):
        return False
    return all([item in header for item in valid_header])


def validate_header(header):
    if not is_header_valid(header):
        raise ValueError("Cabeçalho inválido")


def csv_exporter(filename):
    try:
        check_file_extention(filename, ".csv")
        with open(filename, "w") as file:
            writer = csv.writer(file)
            news = find_all()
            header = []

            validate_header(news[0])

            for param in news[0]:
                header.append(param)
            writer.writerow(header)

            for row in news:
                writer.writerow(row)
        print("Exportação realizada com sucesso")
    except ValueError as exc:
        print(exc, file=sys.stderr)
    except IOError:
        print("Formato inválido", file=sys.stderr)


def json_exporter(filename):
    try:
        check_file_extention(filename, ".json")
        with open(filename, "w") as file:
            news = find_all()
            json.dump(news, file)
    except ValueError as exc:
        print(exc, file=sys.stderr)
    except IOError:
        print("Formato inválido", file=sys.stderr)
