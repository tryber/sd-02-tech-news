import sys
import csv
import time
import json
from pymongo import MongoClient
from os import path


def add_to_mongo(data):
    with MongoClient() as connection:
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        for notice in data:
            time.sleep(0.2)
            print(
                f"Verificando duplicação da noticia {data.index(notice) + 1}"
            )
            exist = collection.find({"url": notice[0]}, {"_id": 0})
            if len(list(exist)) != 0:
                print(
                    f"Notícia {data.index(notice) +1 } duplicada",
                    file=sys.stderr
                )
                return
            collection.insert_one({
                "url": notice[0],
                "title": notice[1],
                "timestamp": notice[2],
                "writer": notice[3],
                "shares_count": int(notice[4]),
                "comments_count": int(notice[5]),
                "summary": notice[6],
                "sources": notice[7].split(","),
                "categories": notice[8].split(",")
            })
        return print("Importação realizada com sucesso")


def add_json_mongo(data):
    with MongoClient() as connection:
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        for notice in data:
            time.sleep(0.2)
            print(
                f"Verificando duplicação da noticia {data.index(notice) + 1}"
            )
            exist = collection.find({"url": notice["url"]}, {"_id": 0})
            if len(list(exist)) > 0:
                print(
                    f"Noticia {data.index(notice) + 1 } duplicada",
                    file=sys.stderr
                )
                return
        collection.insert_many(data)
    return print("Importação realizada com sucesso")


def csv_importer(file_name):
    notices_add = []
    exist = path.exists(file_name) or path.exists(f"./{file_name}")
    if not exist:
        print(f"Arquivo {file_name} não encontrado", file=sys.stderr)
        return
    if not file_name.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return

    with open(file_name, "r") as csvdata:
        default_header = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories"
        ]
        notices = csv.reader(csvdata, delimiter=";", quotechar='"')
        header, *data = notices
        if header != default_header:
            print("Cabeçalho inválido", file=sys.stderr)
            return
        for notice in data:
            print(f"Lendo notícia {data.index(notice) + 1}")
            time.sleep(0.2)
            if len(notice) != 9:
                print(f"Erro na noticia {data.index(notice)}", file=sys.stderr)
                return
            for item in notice:
                if item == "":
                    print(
                        f"Erro na noticia {data.index(notice) + 1}",
                        file=sys.stderr
                    )
                    return
            notices_add.append(notice)
    add_to_mongo(notices_add)


def json_importer(file_name):
    exist = path.exists(file_name) or path.exists(f"./{file_name}")
    if not exist:
        print(f"Arquivo {file_name} não encontrado", file=sys.stderr)
        return
    if not file_name.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return
    with open(file_name, "r") as jsondata:
        try:
            content = json.load(jsondata)
        except ValueError:
            raise ValueError("JSON inválido")
        for notice in content:
            time.sleep(0.2)
            print(f"Lendo notícia {content.index(notice) + 1}")
            if len(notice.keys()) != 9:
                print(
                    f"Erro na noticia {content.index(notice) + 1}",
                    file=sys.stderr
                )
                return
            for index, (item) in enumerate(notice.values()):
                if item == "" or item == []:
                    print(f"Erro na notícia {content.index(notice) + 1}")
                    return
        add_json_mongo(content)


# print(csv_importer("teste.csv"))
# print(json_importer("teste.json"))
