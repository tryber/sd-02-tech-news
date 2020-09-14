import csv
import sys
from mongo_connection import insert_news_importer


def check_file_and_extension(file, content):
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
    if not file.endswith(".csv"):
        print("Formato inválido", file=sys.stderr)
        return False
    if content.fieldnames != headers:
        print("Cabeçalho inválido", file=sys.stderr)
        return False
    return True


def check_row(row, index):
    row_keys = len(row.keys()) == 9
    row_values = all(row.values())
    if not row_values or not row_keys:
        print(f"Erro na notícia {index}", file=sys.stderr)
        return False
    return True


def csv_importer(csv_file):
    all_news = []
    try:
        with open(csv_file) as file:
            news_reader = csv.DictReader(file, delimiter=";", quotechar='"')
            validFile = check_file_and_extension(csv_file, news_reader)
            if not validFile:
                return
            for index, row in enumerate(news_reader, start=1):
                validRow = check_row(row, index)
                if not validRow:
                    return
                all_news.append(dict(row))
    except FileNotFoundError:
        print(f"Arquivo {csv_file} não encontrado")
    else:
        insert_news_importer(all_news)
        print("Importação realizada com sucesso", file=sys.stdout)


def json_importer():
    raise NotImplementedError


csv_importer("./csv_examples/news.csv")
