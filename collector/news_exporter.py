from collector.news_service import (
    exported_directory,
    headers,
    remove_id,
    check_extension,
    file_not_found,
    check_headers
)

from database.index import find_news

# from tests.test_news_importer_fakers import correct_csv

import csv


def csv_exporter(csv_file_name):
    data = find_news()

    csv_path = exported_directory + "/" + csv_file_name

    check_extension(csv_path)

    with open(csv_path, "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(headers)

        for line, row in enumerate(data):
            csv_row = remove_id(row)
            check_headers(list(csv_row.keys()),
                          "Erro na notícia {}".format(line))
            csv_writer.writerow(csv_row)

    print("Exportação realizada com sucesso")


def json_exporter():
    raise NotImplementedError
