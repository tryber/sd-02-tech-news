import csv
import json
import sys
import os
from pymongo import MongoClient


def find_news_by_url(url):
    with MongoClient() as client:
        db = client.tech_news
        return db.news_details.find({"url": url})


def insert_many_news(news):
    with MongoClient() as client:
        db = client.tech_news
        return db.news_details.insert_many(news)


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


def check_path_and_format(file_name, file_ext):
    if not os.path.exists(file_name):
        print(f"Arquivo {file_name} não econtrado", file=sys.stderr)
        return True
    if not file_name.endswith(file_ext):
        print("Formato inválido", file=sys.stderr)
        return True
    return False


def check_duplicate(idx, news):
    is_new_exist = list(find_news_by_url(news))
    if is_new_exist or len(is_new_exist) != 0:
        print(f"Noticía {idx + 1} duplicada", file=sys.stderr)
        return True


def check_all_json_news(imported_news):
    for idx, news in enumerate(imported_news):
        if list(news.keys()) != correct_header:
            print(f"Erro na notícia {idx + 1}", file=sys.stderr)
            return True
        if check_duplicate(idx, news["url"]):
            return True
    return False


def check_all_csv_news(data):
    news_values = []
    for idx, news in enumerate(data):
        if len(news) != 9:
            print(f"Erro na notícia {idx + 1}", file=sys.stderr)
            return False
        if check_duplicate(idx, news[0]):
            return False
        news[4] = int(news[4])
        news[5] = int(news[5])
        news[7] = news[7].split(',')
        news[8] = news[8].split(',')
        dict_news = {
            correct_header[i]: news[i] for i in range(len(correct_header))
        }
        news_values.append(dict_news)
    return news_values


def csv_importer(file_name):
    news_values = []
    if check_path_and_format(file_name, ".csv"):
        return
    with open(file_name) as file:
        imported_news = csv.reader(file, delimiter=";")
        header, *data = imported_news
        if header != correct_header:
            print("Cabeçalho inválido", file=sys.stderr)
            return
        news_values = check_all_csv_news(data)
        if not news_values:
            return
        insert_many_news(news_values)
    print("Importação realizada com sucesso", file=sys.stdout)


def json_importer(file_name):
    imported_news = []
    if check_path_and_format(file_name, ".json"):
        return
    with open(file_name) as file:
        try:
            imported_news = json.loads(file.read())
        except ValueError:
            print("JSON inválido", file=sys.stderr)
            return
        if check_all_json_news(imported_news):
            return
    insert_many_news(imported_news)
    print("Importação realizada com sucesso", file=sys.stdout)


# csv_importer("news.csv")
# json_importer("news.json")
