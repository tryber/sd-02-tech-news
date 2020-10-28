from collector.news_service import (
    exported_directory,
    headers,
    check_extension,
    file_not_found,
    check_headers
)

from database.index import find_news

# from tests.test_news_fakers import correct_csv


import csv

import json


def csv_exporter(csv_file_name):
    data = find_news()

    csv_path = exported_directory + "/" + csv_file_name

    check_extension(csv_path)

    try:
        with open(csv_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow(headers)

            for line, csv_row in enumerate(data):
                check_headers(list(csv_row.keys()),
                              "Erro na notícia {}".format(line))
                csv_writer.writerow(csv_row.values())
# Conferir com o Cássio
    except Exception as err:
        raise ValueError("Other error occurred: {}".format(err))

    else:
        print("Exportação realizada com sucesso")


def json_exporter(json_file_name):
    data = find_news()

    json_path = exported_directory + "/" + json_file_name

    check_extension(json_path)

    try:
        with open(json_path, "w") as json_file:
            json.dump(data, json_file)

    except Exception as err:
        raise ValueError("Other error occurred: {}".format(err))

    else:
        print("Exportação realizada com sucesso")
