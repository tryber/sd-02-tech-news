import csv
import json
import sys
import os
import functools
from mongo_connection import db


valid_header = [
  'url',
  'title',
  'timestamp',
  'writer',
  'shares_count',
  'comments_count',
  'summary',
  'sources',
  'categories',
]


def insert(obj):
    db().pages.insert_one(obj)


def insert_all(data, header):
    for row in data:
        obj = {}
        for index, prop in enumerate(row):
            obj[header[index]] = prop

        insert(obj)


def validate_header(header):
    if not is_header_valid(header):
        print('Cabeçalho inválido', file=sys.stderr)
        raise ValueError


def is_header_valid(header):
    if len(header) != len(valid_header):
        return False
    return all([item in header for item in valid_header])


def is_row_valid(row, index):
    if not all(row):
        print(f'Erro na notícia {index}', file=sys.stderr)
        raise ValueError


def is_url_duplicated(url, urls, index):
    if url in urls:
        print(f'Notícia {index} duplicada', file=sys.stderr)
        raise ValueError


def check_file_extention(filename, extention):
    if os.path.splitext(filename)[1] != extention:
        raise IOError


def is_valid_param(param, index):
    if not param:
        print(f'Erro na notícia {index}')
        raise ValueError


def csv_importer(filename):
    try:
        check_file_extention(filename, '.csv')
        with open(filename) as file:
            beach_status_reader = csv.reader(file, delimiter=";", quotechar='"')
            header, *data = beach_status_reader

            validate_header(header)

            urls = []

            for index, row in enumerate(data):
                url = row[0]
                is_row_valid(row, index)
                is_url_duplicated(url, urls, index)
                urls.append(url)

            insert_all(data, header)
        print('Importação realizada com sucesso')
    except ValueError:
        print()
    except FileNotFoundError:
        print('Arquivo {', filename ,'} não encontrado', file=sys.stderr)
    except IOError:
        print('Formato inválido', file=sys.stderr)


def json_importer(filename):
    try:
        check_file_extention(filename, '.json')
        with open(filename) as file:
            content = file.read()
            news = json.loads(content)

            urls = []

            for index, item in enumerate(news):
                url = item['url']
                is_url_duplicated(url, urls, index)
                urls.append(url)
                for param in item.values():
                    is_valid_param(param, index)
                insert(item)
        print('Importação realizada com sucesso')

    except ValueError:
        print()
    except FileNotFoundError:
        print('Arquivo {', filename ,'} não encontrado', file=sys.stderr)
    except IOError:
        print('Formato inválido', file=sys.stderr)
    except json.decoder.JSONDecodeError:
        print('JSON inválido')
