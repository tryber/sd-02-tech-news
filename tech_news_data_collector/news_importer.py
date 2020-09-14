import csv
import re
import sys
import os
from pymongo import MongoClient

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
                    "Notícia " + str(index + 2) + " duplicada", file=sys.stderr
                )


def headers_len(news):
    for index in range(len(news)):
        if len(news[index]) < len(defaultHeaders):
            print("Erro na notícia " + str(index + 2), file=sys.stderr)
            exit()


def check_news(headers, news):
    conjunto = set(headers)
    initiallen = len(conjunto)
    for header in defaultHeaders:
        conjunto.add(header)
    if len(conjunto) != initiallen:
        print("Cabeçalho inválido")
        exit()
    else:
        headers_len(news)


def csv_importer(arquive):
    if os.path.exists(arquive):
        with open(arquive.lower()) as file:
            writer = csv.reader(file, delimiter=";")
            headers, *news = writer
            check_news(headers, news)
            mongo_insert(news)
            print("Importação realizada com sucesso")
    else:
        print(
            "Arquivo "
            + os.path.abspath(os.getcwd())
            + "/"
            + arquive
            + " não encontrado"
        )
        exit()


def json_importer():
    raise NotImplementedError


arquive = input("Digite o nome do arquivo com .csv\n")
if re.search(".csv$", arquive, re.IGNORECASE):
    csv_importer(arquive)
else:
    print("Formato inválido", file=sys.stderr)
    exit()
