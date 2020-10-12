import csv
import sys

from mongo_connection import news_to_database, find_duplicate


def csv_importer(csv_file):
    try:
        with open(csv_file) as file:
            if not csv_file.endswith(".csv"):
                print("Formato inválido", file=sys.stderr)
                sys.exit(1)
            csv_reader = csv.DictReader(file, delimiter=";", quotechar='"')
            headers = ["url", "title", "timestamp", "writer", "shares_count",
                       "comments_count", "summary", "sources", "categories"]
            all_news = []
            line = 1
            for row in csv_reader:
                new_dict = {}
                for header in headers:
                    dict_value = row[header]
                    try:
                        if header == "shares_count" or header == "comments_count":
                            new_dict[header] = int(dict_value)
                        elif header == "sources" or header == "categories":
                            new_dict[header] = dict_value.split(",")
                        else:
                            new_dict[header] = row[header]
                    except ValueError:
                        print(f'Erro na notícia {line}')
                        exit(1)
                all_news.append(new_dict)
                line += 1
            duplicated_new = find_duplicate(all_news)
            if duplicated_new:
                print(f"Notícia {duplicated_new} duplicada")
                sys.exit(1)
            news_to_database(all_news)
        print("Importação realizada com sucesso")
    except KeyError:
        print("Cabeçalho inválido")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Arquivo {csv_file} não encontrado", file=sys.stderr)
        sys.exit(1)


def json_importer():
    raise NotImplementedError


csv_importer("xablau.csv")
