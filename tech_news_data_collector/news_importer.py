import sys
import csv

need_keys = ["url", "title", "timestamp", "writer", "shares_count", "comments_count", "summary", "sources", "categories"]


def verify_keys(all_dict, key):
    if f"{key}" not in all_dict:
        return print(f'Chave \"{key}\" não presente no arquivo.')


def csv_importer(path):
    csv_list = []
    if not path.endswith('.csv'):
        return print('Formato inválido')

    with open(path) as csv_data:
        csv_news = csv.DictReader(csv_data, delimiter=";", quotechar='"')
        for row in csv_news:
            csv_list.append(dict(row))
    for key in need_keys:
        verify_keys(csv_list, key)


def json_importer():
    raise NotImplementedError


csv_importer(sys.argv[1])
