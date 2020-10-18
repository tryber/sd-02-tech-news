import csv

from collector.news_importer_service import (
    check_extension,
    check_field,
    check_headers,
    check_url,
    file_not_found,
)

from database.store import store_list


def csv_importer(csv_string):
    check_extension(csv_string)

    try:
        '''
        encapsulamento da utilização de um recurso
        gerenciamento de contexto
        ações tomadas independente do status da resposta
        '''
        with open(csv_string) as csv_file:
            '''
            return a reader object
            which will iterate over lines
            in the given csvfile
            '''
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            check_headers(csv_reader.fieldnames)

            data = []

            line = 0

            urls = []

            for csv_row in csv_reader:
                for field in csv_row:
                    check_field(csv_row[field], line)

                url = csv_row["url"]

                check_url(urls, url, line)

                urls.append(url)

                line += 1

                data.append(csv_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(csv_string))

    store_list(data)

    print("Exportação realizada com sucesso")


def json_importer():
    raise NotImplementedError
