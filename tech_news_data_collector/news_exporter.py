from pymongo import MongoClient
import sys
import json
from tech_news_data_collector.utils import check_comparison
import os.path
import csv


correct_header = [
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


def get_from_db(db, collection, projection={"_id": 0}):
    with MongoClient() as client:
        db = client[db]
        return db[collection].find({}, projection)


def check_if_is_list(item):
    if type(item) is list:
        return ",".join(item)
    return item


def adjust_dot_comma(lines):
    final_text = []
    for line in lines:
        adjusted_line = []

        for item in line:
            item = check_if_is_list(item)
            adjusted_line.append(item)

        final_text.append(adjusted_line)
    return final_text


def write_in_file(file_path, all_news):
    with open(file_path, mode="w") as csv_file:

        csv_columns = all_news[0].keys()

        writer = csv.DictWriter(
            csv_file, fieldnames=csv_columns, delimiter=";"
        )
        writer.writeheader()
        for line in all_news:
            writer.writerow(line)


def csv_exporter(file_path):
    try:
        extension = os.path.splitext(file_path)[1]
        check_comparison(extension, ".csv", "Formato inválido")

        all_news = list(get_from_db("web_scrape_python", "news_collection"))

        write_in_file(file_path, all_news)

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        print("Exportação realizada com sucesso", file=sys.stdout)


def json_exporter(file_path):
    try:
        extension = os.path.splitext(file_path)[1]
        check_comparison(extension, ".json", "Formato inválido")

        all_news = list(get_from_db("web_scrape_python", "news_collection"))

        with open(file_path, mode="w") as file:
            lines = [line for line in all_news]
            json_news = json.dumps(lines)
            file.write(json_news)

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        print("Exportação realizada com sucesso", file=sys.stdout)
