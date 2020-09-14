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


def insert(obj):
    tech_news_db().pages.insert_one(obj)


def insert_all(data, header):
    for row in data:
        obj = {}
        for index, prop in enumerate(row):
            obj[header[index]] = prop

        insert(obj)


def validate_header(header):
    if not is_header_valid(header):
        raise ValueError("Cabeçalho inválido")


def is_header_valid(header):
    if len(header) != len(valid_header):
        return False
    return all([item in header for item in valid_header])


def is_row_valid(row, index):
    if not all(row):
        raise ValueError(f"Erro na notícia {index}")


def is_url_duplicated(url, urls, index):
    if url in urls:
        raise ValueError(f"Notícia {index} duplicada")


def check_file_extention(filename, extention):
    if os.path.splitext(filename)[1] != extention:
        raise ValueError("Formato inválido")


def is_valid_param(param, index):
    if not param:
        raise ValueError(f"Erro na notícia {index}")


def csv_importer_open_with(filename):
    with open(filename) as file:
        status = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = status

        validate_header(header)

        urls = []

        for index, row in enumerate(data):
            url = row[0]
            is_row_valid(row, index)
            is_url_duplicated(url, urls, index)
            urls.append(url)

        insert_all(data, header)


def csv_importer(filename):
    try:
        check_file_extention(filename, ".csv")
        csv_importer_open_with(filename)
        print("Importação realizada com sucesso")
    except ValueError as exc:
        print(exc, file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado", file=sys.stderr)


def json_importer_open_with(filename):
    with open(filename) as file:
        content = file.read()
        news = json.loads(content)

        urls = []

        for index, item in enumerate(news):
            url = item["url"]
            is_url_duplicated(url, urls, index)
            urls.append(url)
            for param in item.values():
                is_valid_param(param, index)
            insert(item)


def json_importer(filename):
    try:
        check_file_extention(filename, ".json")
        json_importer_open_with(filename)
        print("Importação realizada com sucesso")
    except ValueError as exc:
        print(exc, file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado", file=sys.stderr)
    except json.decoder.JSONDecodeError:
        print("JSON inválido", file=sys.stderr)
