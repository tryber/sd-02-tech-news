import sys
import csv


def csv_importer(path):
    with open(path) as csv_data:
        csv_list = []
        csv_news = csv.DictReader(csv_data, delimiter=";", quotechar='"')
        for row in csv_news:
            csv_list.append(dict(row))
        print(csv_list)


def json_importer():
    raise NotImplementedError


csv_importer(sys.argv[1])
