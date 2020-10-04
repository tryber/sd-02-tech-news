import csv
import re
import sys
import os
from pymongo import MongoClient
import json


default_headers = [
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


def create_object_mongo(array_info):
    array_To_object = {}
    for index in range(len(array_info)):
        if (
            default_headers[index] == "shares_count"
            or default_headers[index] == "comments_count"
        ):
            array_To_object[default_headers[index]] = int(array_info[index])
        elif (
            default_headers[index] == "sources" or 
            default_headers[index] == "categories"
        ):
            array_To_object[
                default_headers[index]
                ] = array_info[index].split(",")
        else:
            array_To_object[default_headers[index]] = array_info[index]
    return array_To_object


def mongo_insert(arquive):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for index in range(len(arquive)):
            obj_to_insert = create_object_mongo(arquive[index])
            exist_object = db["news"].find_one({"url": obj_to_insert["url"]})
            if exist_object is None:
                db["news"].insert_one(obj_to_insert)
            else:
                print(
                    "Notícia " + str(index + 1) + " duplicada",
                    file=sys.stderr
                )


def headers_len(news):
    for index in range(len(news)):
        if len(news[index]) < len(default_headers):
            print("Erro na notícia " + str(index + 1), file=sys.stderr)
            exit()


def check_news(headers, news):
    conjunto = set(headers)
    initial_len = len(conjunto)
    for header in default_headers:
        conjunto.add(header)
    if len(conjunto) != initial_len:
        print("Cabeçalho inválido", file=sys.stderr)
        exit()
    else:
        headers_len(news)


def csv_importer(arquive):
    if os.path.exists(arquive):
        if re.search(".csv$", arquive, re.IGNORECASE):
            with open(arquive.lower()) as file:
                writer = csv.reader(file, delimiter=";")
                headers, *news = writer
                check_news(headers, news)
                mongo_insert(news)
                print("Importação realizada com sucesso")
        else:
            print("Formato inválido", file=sys.stderr)
    else:
        print(
            "Arquivo "
            + os.path.abspath(os.getcwd())
            + "/"
            + arquive
            + " não encontrado",
            file=sys.stderr,
        )


def insert_json(array_to_include):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for index in range(len(array_to_include)):
            exist_object = db["news"].find_one({
                "url": array_to_include[index]["url"]
            })
            if exist_object is None:
                db["news"].insert_one(array_to_include[index])
            else:
                print(
                        "Notícia " + str(index + 1) + " duplicada",
                        file=sys.stderr
                    )


def json_check(news):
    for index in range(len(news)):
        if len(news[index].keys()) < len(default_headers) + 1:
            print("Erro na notícia " + str(index + 1), file=sys.stderr)
            exit()
    insert_json(news)


def json_importer(arquive):
    if os.path.exists(arquive):
        if re.search(".json$", arquive, re.IGNORECASE):
            file = open(arquive.lower(), "r")
            try:
                news = json.load(file)
                json_check(news)
                print("Importação realizada com sucesso")
            except ValueError:
                print("JSON inválido", file=sys.stderr)
            finally:
                file.close()
        else:
            print("Formato inválido", file=sys.stderr)
    else:
        print(
            "Arquivo "
            + os.path.abspath(os.getcwd())
            + "/"
            + arquive
            + " não encontrado",
            file=sys.stderr,
        )

