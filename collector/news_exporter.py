from collector.news_service import (
    available_fields,
    check_extension,
    check_fields,
    directory,
)

from database.index import find_news

import csv

import json


def csv_exporter(file_name):
    data = find_news()
    check_extension(file_name, ".csv")
    csv_path = directory + "/" + file_name

    try:
        with open(csv_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow(available_fields)
            for line, csv_row in enumerate(data):
                check_fields(list(csv_row.keys()),
                             "Erro na notícia {}".format(line))
                csv_writer.writerow(csv_row.values())

    except Exception as err:
        raise ValueError("Other error occurred: {}".format(err))

    else:
        print("Exportação realizada com sucesso")


def json_exporter(file_name):
    data = find_news()
    json_path = directory + "/" + file_name
    check_extension(json_path, ".json")

    try:
        with open(json_path, "w") as json_file:
            json.dump(data, json_file)

    except Exception as err:
        raise ValueError("Other error occurred: {}".format(err))

    else:
        print("Exportação realizada com sucesso")
