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


def createObjectMongo(arrayInfo):
    arrayToObject = {}
    for index in range(len(arrayInfo)):
        arrayToObject[defaultHeaders[index]] = arrayInfo[index]
    return arrayToObject


def mongoInsert(arquive):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for index in range(len(arquive)):
            objToInsert = createObjectMongo(arquive[index])
            existObject = db["news"].find_one({"url": objToInsert["url"]})
            if existObject == None:
                db["news"].insert_one(objToInsert)
            else:
                print("Notícia " + str(index) + " duplicada", file=sys.stderr)


def csv_importer(arquive):
    if os.path.exists(arquive):
        with open(arquive.lower()) as file:
            writer = csv.reader(file, delimiter=";")
            headers, *news = writer
            conjunto = set(headers)
            initiallen = len(conjunto)
            for header in defaultHeaders:
                conjunto.add(header)
            if len(conjunto) != initiallen:
                print("Cabeçalho inválido")
                exit()
            else:
                for index in range(len(news)):
                    if len(news[index]) < len(defaultHeaders):
                        print("Erro na notícia " + str(index), file=sys.stderr)
                        exit()
            mongoInsert(news)
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
