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

    try:
        with open(file_name, "w") as csv_file:
            csv_writer = csv.DictWriter(
                csv_file, delimiter=";", fieldnames=available_fields)
            csv_writer.writeheader()
            for line, csv_row in enumerate(data):
                check_fields(list(csv_row.keys()),
                             "Erro na notícia {}".format(line))
                csv_row["sources"] = ",".join(csv_row["sources"])
                csv_row["categories"] = ",".join(csv_row["categories"])
                csv_writer.writerow(csv_row)

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
