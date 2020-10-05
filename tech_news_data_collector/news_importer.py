import csv
import json
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


def mongo_insert_if_not_found_csv(data_to_insert):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        for index, data in enumerate(data_to_insert):
            item_exists = bool(collection.find_one({"url": data[0]}))
            if item_exists:
                print(f'Notícia {index+1} duplicada')
            if not item_exists:
                collection.insert_one({
                    "url": data[0],
                    "title": data[1],
                    "timestamp": data[2],
                    "writer": data[3],
                    "shares_count": int(data[4]),
                    "comments_count": int(data[5]),
                    "summary": data[6],
                    "sources": data[7].split(","),
                    "categories": data[8].split(","),
                })


def mongo_insert_if_not_found_json(data_to_insert):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        for index, data in enumerate(data_to_insert):
            item_exists = bool(collection.find_one({"url": data["url"]}))
            if not item_exists:
                collection.insert_one(data)
            else:
                print(f'Notícia {index +1} duplicada', file=sys.stderr)


def csv_importer(csv_file):
    if not path.exists(csv_file):
        print(f"Arquivo {csv_file} não encontrado", file=sys.stderr)
        return

    with open(csv_file) as file:
        if not csv_file.endswith(".csv"):
            print("Formato inválido", file=sys.stderr)
            return
        csv_info = csv.reader(file, delimiter=";")
        header, *all_data = csv_info
        if not header == def_headers:
            print("Cabeçalho inválido", file=sys.stderr)
            return

        for index, data in enumerate(all_data):
            if not len(data) == 9:
                print(f"Erro na notícia {index + 1}", file=sys.stderr)
                return
            for column in data:
                if column == '':
                    print(f"Erro na notícia {index}", file=sys.stderr)
                    return
            data_to_insert.append(data)

    mongo_insert_if_not_found_csv(data_to_insert)
    print("Importação realizada com sucesso")


def validate_json(json_file):
    try:
        result = json.load(json_file)
    except ValueError:
        raise ValueError("JSON inválido")
    return result


def json_importer(json_file):
    try:
        with open(json_file) as file:
            if not json_file.endswith(".json"):
                raise ValueError("Formato inválido")
            all_data = validate_json(file)
            for index, data in enumerate(all_data):
                if not len(data) == 9:
                    print(f"Erro na notícia {index + 1}", file=sys.stderr)
                    return
                for column in data:
                    if data[column] == '':
                        print(f"Erro na notícia {index + 1}", file=sys.stderr)
                        return
                data_to_insert.append(data)

    except FileNotFoundError:
        print(f"Arquivo {json_file} não encontrado", file=sys.stderr)
    except ValueError as invalid_format:
        print(invalid_format, file=sys.stderr)
    else:
        mongo_insert_if_not_found_json(data_to_insert)
        print("Importação realizada com sucesso")
