import sys
import os.path
import csv
from pymongo import MongoClient


correct_header = ['url', 'title', 'timestamp', 'writer', 'shares_count',
                  'comments_count', 'summary', 'sources', 'categories']


def create_dict(keys, values):
    new_dict = {}
    for index, key in enumerate(keys, start=0):
        new_dict[key] = values[index]
    return new_dict


def check_comparison(item, item_to_check, exception_message):
    if item != item_to_check:
        raise ValueError(exception_message)


def save_db(item, db, collection):
    with MongoClient() as client:
        db = client[db]
        item_to_insert = create_dict(correct_header, item)
        db[collection].insert_one(item_to_insert)


def check_if_exists_db(value, i, db, collection, field):
    with MongoClient() as client:
        db = client[db]
        new = list(db[collection].find({field: value}))
        if len(new) > 0:
            raise ValueError(f"Notícia {i} duplicada")


def iterate_lines(csvLines):
    for line in csvLines:
        save_db(line, 'web_scrape_python', 'news_collection')


def csv_importer(arg):

    try:
        extension = os.path.splitext(arg)[1]
        check_comparison(extension, '.csv', 'Invalid extension')

        with open(arg) as file:
            header, *csvLines = csv.reader(file, delimiter=";")

            check_comparison(header, correct_header, 'Invalid header')

            for index, line in enumerate(csvLines, start=1):
                line = [item for item in line if item]
                check_comparison(len(line), len(header),
                                 f'Erro na notícia {index}')

                check_if_exists_db(line[0],
                                   index,
                                   'web_scrape_python',
                                   'news_collection',
                                   'url')
            iterate_lines(csvLines)

    except FileNotFoundError:
        print(f"Arquivo {arg} não encontrado", file=sys.stderr)

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        print('Importação realizada com sucesso', file=sys.stdout)


def json_importer():
    raise NotImplementedError


csv_importer('tech_news_data_collector/news.csv')
