import csv
import sys
from pymongo import MongoClient


def csv_importer(file):
    try:
        csv_file = open(file)
    except FileNotFoundError:
        return print(f"Arquivo {file} não encontrado", file=sys.stderr)

    if not file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return csv_file.close()

    reader = csv.DictReader(csv_file, delimiter=";", quotechar='"')
    try:
        line = 1
        documents = []
        for row in reader:
            url = row["url"]
            title = row["title"]
            timestamp = row["timestamp"]
            writer = row["writer"]
            shares_count = row["shares_count"]
            comments_count = row["comments_count"]
            summary = row["summary"]
            sources = row["sources"]
            categories = row["categories"]

            if not (url and title and timestamp and writer and shares_count and comments_count and summary and sources and categories):
                print(f"Erro na notícia {line}", file=sys.stderr)
                return csv_file.close()
            for document in documents:
                if document["url"] == url:
                    print(f"Notícia {line} duplicada", file=sys.stderr)
                    return csv_file.close()

            line += 1
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
    except KeyError:
        print("Cabeçalho inválido", file=sys.stderr)
        return csv_file.close()

    client = MongoClient()
    db = client.tech_news
    db.news.insert_many(documents)

    print("Importação realizada com sucesso", file=sys.stdout)
    csv_file.close()


def json_importer():
    raise NotImplementedError
