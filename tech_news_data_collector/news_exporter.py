import csv
import json
import sys
import os
from mongo_connection import db


def check_file_extention(filename, extention):
    if os.path.splitext(filename)[1] != extention:
        raise IOError


def find_all():
    cur = db().pages.find({},{'_id': 0})
    arr = []
    for doc in cur:
        arr.append(doc)
    return arr


def csv_exporter(filename):
    try:
        check_file_extention(filename, '.csv')
        with open(filename, "w") as file:
            writer = csv.writer(file)
            news = find_all()
            header = []

            for param in news[0]:
                header.append(param)
            writer.writerow(header)

            for row in news:
                writer.writerow(row)
        print('Exportação realizada com sucesso')

    except IOError:
        print('Formato inválido', file = sys.stderr)


def json_exporter(filename):
    try:
        check_file_extention(filename, '.json')
        with open(filename, "w") as file:
            news = find_all()
            json.dump(news, file)
    
    except IOError:
        print('Formato inválido', file = sys.stderr)
