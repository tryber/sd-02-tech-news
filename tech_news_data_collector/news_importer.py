import csv
import sys
import json
from mongo_connection import insert_news_importer


def check_file_and_extension(file, content):
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
    if not file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return False
    if content.fieldnames != headers:
        print("Cabeçalho inválido", file=sys.stderr)
        return False
    return True


def check_fields(row, index):
    row_keys = len(row.keys()) == 9
    row_values = True
    for value in row.values():
        if (value is None):
            row_values = False
    if not row_values or not row_keys:
        print(f"Erro na notícia {index}", file=sys.stderr)
        return False
    return True


def csv_importer(csv_file):
    all_news = []
    try:
        with open(csv_file) as file:
            news_reader = csv.DictReader(file, delimiter=";", quotechar='"')
            validFile = check_file_and_extension(csv_file, news_reader)
            if not validFile:
                return
            for index, row in enumerate(news_reader, start=1):
                validRow = check_fields(row, index)
                if not validRow:
                    return
                row["shares_count"] = int(row["shares_count"])
                row["comments_count"] = int(row["comments_count"])
                row["sources"] = row["sources"].split(',')
                row["categories"] = row["categories"].split(',')
                all_news.append(dict(row))
    except FileNotFoundError:
        print(f"Arquivo {csv_file} não encontrado", file=sys.stderr)
    else:
        insert_news_importer(all_news)
        print("Importação realizada com sucesso", file=sys.stdout)


def json_importer(json_file):
    if not json_file.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return
    all_news = []
    try:
        with open(json_file) as file:
            news = json.load(file)
            for index, item in enumerate(news, start=1):
                validItem = check_fields(item, index)
                if not validItem:
                    return
                all_news.append(item)
    except FileNotFoundError:
        print(f"Arquivo {json_file} não encontrado", file=sys.stderr)
    except json.decoder.JSONDecodeError:
        print("JSON inválido", file=sys.stderr)
    else:
        insert_news_importer(all_news)
        print("Importação realizada com sucesso", file=sys.stdout)


csv_importer("./news_files_mocks/news.csv")
# json_importer("./news_files_mocks/news.json")
