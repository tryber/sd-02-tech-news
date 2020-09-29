import csv
import re
import sys
import os
from pymongo import MongoClient
import json


defaultHeaders = [
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


def create_object_mongo(arrayInfo):
    arrayToObject = {}
    for index in range(len(arrayInfo)):
        if (
            defaultHeaders[index] == "shares_count"
            or defaultHeaders[index] == "comments_count"
        ):
            arrayToObject[defaultHeaders[index]] = int(arrayInfo[index])
        elif (
            defaultHeaders[index] == "sources" or defaultHeaders[index] == "categories"
        ):
            arrayToObject[defaultHeaders[index]] = arrayInfo[index].split(",")
        else:
            arrayToObject[defaultHeaders[index]] = arrayInfo[index]
    return arrayToObject


def mongo_insert(arquive):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for index in range(len(arquive)):
            objToInsert = create_object_mongo(arquive[index])
            existObject = db["news"].find_one({"url": objToInsert["url"]})
            if existObject is None:
                db["news"].insert_one(objToInsert)
            else:
                print(
                    "Notícia " + str(index + 1) + " duplicada",
                    file=sys.stderr
                )


def headers_len(news):
    for index in range(len(news)):
        if len(news[index]) < len(defaultHeaders):
            print("Erro na notícia " + str(index + 1), file=sys.stderr)
            exit()


def check_news(headers, news):
    conjunto = set(headers)
    initiallen = len(conjunto)
    for header in defaultHeaders:
        conjunto.add(header)
    if len(conjunto) != initiallen:
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


def insert_json(arrayToInclude):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for index in range(len(arrayToInclude)):
            existObject = db["news"].find_one({"url": arrayToInclude[index]["url"]})
            if existObject is None:
                db["news"].insert_one(arrayToInclude[index])
            else:
                print(
                        "Notícia " + str(index + 1) + " duplicada",
                        file=sys.stderr
                    )


def json_check(news):
    for index in range(len(news)):
        if len(news[index].keys()) < len(defaultHeaders) + 1:
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

