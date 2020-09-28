import csv
import json
import sys
import os
from pymongo import MongoClient


def find_news_by_url(url):
    with MongoClient() as client:
        db = client.tech_news
        return db.teste2.find({'url': url})


correct_header = [
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


def csv_importer(file_name):
    news_values = []
    if not os.path.exists(file_name):
        print(f"Arquivo {file_name} não econtrado", file=sys.stderr)
        return
    if not file_name.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return
    with open(file_name) as file:
        teste = csv.reader(file, delimiter=";")
        header, *data = teste
        if header != correct_header:
            print("Cabeçalho inválido", file=sys.stderr)
            return
        for idx, news in enumerate(data):
            if len(news) != 9:
                print(f"Erro na notícia {idx + 1}", file=sys.stderr)
                return
            is_new_exist = list(find_news_by_url(news[0]))
            if (is_new_exist or len(is_new_exist) != 0):
                print(f'Noticía {idx} duplicada', file=sys.stderr)
                return
            print(news[0])
            news[7] = news[7].split()
            news[8] = news[8].split()
            dict_news = {
                correct_header[i]: news[i] for i in range(len(correct_header))
            }
            news_values.append(dict_news)
        print(news_values)


def json_importer():
    raise NotImplementedError


csv_importer("news.csv")
