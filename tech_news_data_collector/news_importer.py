import csv
import sys
from os import path
from pymongo import MongoClient

def_headers = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]

data_to_insert = []


def mongo_insert_if_not_found(data_to_insert):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        for index, data in enumerate(data_to_insert):
            item_exists = bool(collection.find_one({"url": data[0]}))
            if not item_exists:
                collection.insert_one({
                    "url": data[0],
                    "title": data[1],
                    "timestamp": data[2],
                    "writer": data[3],
                    "shares_count": data[4],
                    "comments_count": data[5],
                    "summary": data[6],
                    "sources": data[7],
                    "categories": data[8],
                })


def csv_importer(csv_file):
    if not path.exists(csv_file):
        print(f"Arquivo {csv_file} não encontrado", file=sys.stderr)
        return
    if not csv_file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return

    with open(csv_file) as file:
        csv_info = csv.reader(file, delimiter=";")
        header, *all_data = csv_info
        if not header == def_headers:
            print("Cabeçalho inválido", file=sys.stderr)

        for index, data in enumerate(all_data):
            if not len(data) == 9:
                print(f"Erro na notícia {index}", file=sys.stderr)
                return
            for column in data:
                if column == '':
                    print(f"Erro na notícia {index}", file=sys.stderr)
                    return
            data_to_insert.append(data)

    mongo_insert_if_not_found(data_to_insert)
    print("Importação realizada com sucesso")


def json_importer():
    raise NotImplementedError


csv_importer("sucesso.csv")
