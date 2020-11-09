from collector.news_service import (
    check_extension,
    check_field,
    check_fields,
    check_url,
    fill_news_data,
    file_not_found,
)

from database.index import create_news

import csv

import json


def csv_importer(csv_path):
    try:
        with open(csv_path) as csv_file:
            check_extension(csv_path, ".csv")
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            check_fields(csv_reader.fieldnames, "Cabeçalho inválido")
            news_data = []
            urls = []
            for line, csv_row in enumerate(csv_reader):
                for field in csv_row:
                    check_field(csv_row[field], line)
                url = csv_row["url"]
                check_url(urls, url, line)
                fill_news_data(news_data, csv_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(csv_path))

    else:
        create_news(news_data)
        print("Importação realizada com sucesso")


def json_importer(json_path):
    try:
        with open(json_path) as json_file:
            check_extension(json_path, ".json")
            json_data = json.load(json_file)
            urls = []
            news_data = []
            for line, json_row in enumerate(json_data):
                check_fields(list(json_row.keys()),
                             "Erro na notícia {}".format(line))
                url = json_row["url"]
                check_url(urls, url, line)
                fill_news_data(news_data, json_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(json_path))

    except(json.decoder.JSONDecodeError):
        raise ValueError("JSON inválido")

    else:
        create_news(news_data)
        print("Importação realizada com sucesso")
