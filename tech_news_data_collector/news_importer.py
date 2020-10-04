import csv
import sys
from pymongo import MongoClient
import json


def csv_importer(file):
    try:
        csv_file = open(file)
    except FileNotFoundError:
        return print(f"Arquivo {file} não encontrado", file=sys.stderr)

    if not file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return csv_file.close()

    reader = csv.DictReader(csv_file, delimiter=";", quotechar='"')
    client = MongoClient()
    db = client.tech_news

    line = 1
    documents = []
    for row in reader:
        try:
            url = row["url"]
            title = row["title"]
            timestamp = row["timestamp"]
            writer = row["writer"]
            shares_count = row["shares_count"]
            comments_count = row["comments_count"]
            summary = row["summary"]
            sources = row["sources"]
            categories = row["categories"]
        except KeyError:
            print("Cabeçalho inválido", file=sys.stderr)
            client.close()
            return csv_file.close()

        if not (url and title and timestamp and writer and shares_count and comments_count and summary and sources and categories):
            print(f"Erro na notícia {line}", file=sys.stderr)
            client.close()
            return csv_file.close()

        document_exists = db.news.find_one({"url": url})
        if document_exists:
            print(f"Notícia {line} duplicada", file=sys.stderr)
            client.close()
            return csv_file.close()

        documents.append({
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "shares_count": int(shares_count),
            "comments_count": int(comments_count),
            "summary": summary,
            "sources": sources.split(","),
            "categories": categories.split(","),
        })
        line += 1

    db.news.insert_many(documents)
    print("Importação realizada com sucesso", file=sys.stdout)
    client.close()
    csv_file.close()


def json_importer(file):
    try:
        json_file = open(file)
    except FileNotFoundError:
        return print(f"Arquivo {file} não encontrado", file=sys.stderr)

    if not file.endswith(".json"):
        print("Formato inválido", file=sys.stderr)
        return json_file.close()

    content = json_file.read()

    try:
        documents = json.loads(content)
    except json.decoder.JSONDecodeError:
        print("JSON inválido", file=sys.stderr)
        return json_file.close()

    client = MongoClient()
    db = client.tech_news

    for index, document in enumerate(documents):
        try:
            url = document["url"]
            title = document["title"]
            timestamp = document["timestamp"]
            writer = document["writer"]
            shares_count = document["shares_count"]
            comments_count = document["comments_count"]
            summary = document["summary"]
            sources = document["sources"]
            categories = document["categories"]
        except KeyError:
            print(f"Erro na notícia {index + 1}", file=sys.stderr)
            client.close()
            return json_file.close()

        document_exists = db.news.find_one({"url": url})
        if document_exists:
            print(f"Notícia {index + 1} duplicada", file=sys.stderr)
            client.close()
            return json_file.close()

    db.news.insert_many(documents)
    print("Importação realizada com sucesso", file=sys.stdout)
    client.close()
    json_file.close()
