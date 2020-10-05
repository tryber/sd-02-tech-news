from pymongo import MongoClient
import json
import csv
import sys


def get_news():
    news = []
    with MongoClient() as client:
        db = client.tech_news
        news = db.news_details.find({}, {"_id": 0})
        return list(news)


def csv_exporter(file_name):
    if not file_name.endswith('.csv'):
        print('Formato inválido', file=sys.stderr)
        return
    with open(file_name, "w") as file:
        writer = csv.writer(file, delimiter=';')
        news = get_news()
        headers = [
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
        writer.writerow(headers)
        for single_new in news:
            single_new['sources'] = ','.join(single_new['sources'])
            single_new['categories'] = ','.join(single_new['categories'])
            writer.writerow(single_new.values())
        print("Exportação realizada com sucesso", file=sys.stdout)


def json_exporter(file_name):
    if not file_name.endswith('.json'):
        print('Formato inválido', file=sys.stderr)
        return
    with open(file_name, "w") as file:
        news = get_news()
        json.dump(news, file)
        print("Exportação realizada com sucesso", file=sys.stdout)
