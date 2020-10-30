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
    if not param and param != 0:
        raise ValueError(f"Erro na notícia {index}")


def param_treatments(item, i):
    if (i == 7 or i == 8):
        return item.split(",")
    if (i == 4 or i == 5):
        return int(item)
    return item


def return_url_dont_exist():
    all_news = tech_news_db().pages.find({}, {"_id": 0, "url": 1})
    return {item['url'] for item in all_news}


def csv_importer_open_with(filename):
    with open(filename) as file:
        check_file_extention(filename, ".csv")
        status = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = status

        validate_header(header)

        urls = []
        url_dont_exist = return_url_dont_exist()

        for index, row in enumerate(data):
            if (row[0] in url_dont_exist):
                raise ValueError(f"Notícia {index} duplicada")
            url = row[header.index('url')]
            is_row_valid(row, index)
            is_url_duplicated(url, urls, index)
            urls.append(url)

        insert_all(
            [
                [param_treatments(item, i) for i, item in enumerate(row)]
                for row in data
            ], header)


def csv_importer(filename):
    try:
        csv_importer_open_with(filename)
        print("Importação realizada com sucesso")
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado", file=sys.stderr)
    except ValueError as exc:
        print(exc, file=sys.stderr)


def json_importer_open_with(filename):
    with open(filename) as file:
        check_file_extention(filename, ".json")
        content = file.read()
        news = json.loads(content)

        urls = []
        url_dont_exist = return_url_dont_exist()

        for index, item in enumerate(news):
            if (item["url"] in url_dont_exist):
                raise ValueError(f"Notícia {index} duplicada")
            url = item["url"]
            is_url_duplicated(url, urls, index)
            urls.append(url)
            for param in item.values():
                is_valid_param(param, index)
            insert(item)


def json_importer(filename):
    try:
        json_importer_open_with(filename)
        print("Importação realizada com sucesso")
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado", file=sys.stderr)
    except json.decoder.JSONDecodeError:
        print("JSON inválido", file=sys.stderr)
    except ValueError as exc:
        print(exc, file=sys.stderr)
