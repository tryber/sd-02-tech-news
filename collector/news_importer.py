from collector.news_service import (
    check_extension,
    check_field,
    check_headers,
    check_url,
    file_not_found,
)

from database.index import create_news

# from tests.test_news_importer_fakers import correct_csv

import csv

import json


def csv_importer(csv_path):
    check_extension(csv_path)

    try:
        with open(csv_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            check_headers(csv_reader.fieldnames, "Cabeçalho inválido")
            data = []
            urls = []
            for line, csv_row in enumerate(csv_reader):
                for field in csv_row:
                    check_field(csv_row[field], line)
                url = csv_row["url"]
                check_url(urls, url, line)
                urls.append(url)
                data.append(csv_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(csv_path))

    else:
        create_news(data)
        print("Importação realizada com sucesso")


# csv_importer(correct_csv)


def json_importer(json_path):
    check_extension(json_path)

    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
            urls = []
            for line, json_row in enumerate(data):
                check_headers(list(json_row.keys()),
                              "Erro na notícia {}".format(line))
                url = json_row["url"]
                check_url(urls, url, line)
                urls.append(url)

    except(FileNotFoundError):
        raise ValueError(file_not_found(json_path))

    except(json.decoder.JSONDecodeError):
        raise ValueError("JSON inválido")

    else:
        create_news(data)
        print("Importação realizada com sucesso")
