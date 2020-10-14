import csv
import json
import sys

from mongo_connection import news_to_database, find_duplicate, import_from_json


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


def json_importer(json_file):
    try:
        with open(json_file) as file:
            if not json_file.endswith(".json"):
                print("Formato inválido", file=sys.stderr)
                sys.exit(1)
            news = json.load(file)
            for new in news:
                headers = ["url", "title", "timestamp", "writer",
                           "shares_count", "comments_count",
                           "summary", "sources", "categories"]
                for header in headers:
                    if header not in new.keys():
                        print(f"Erro na notícia {news.index(new) + 1}")
                        sys.exit(1)
                for key in new.keys():
                    if key not in headers:
                        print(f"Erro na notícia {news.index(new) + 1}")
                        sys.exit(1)
            duplicated_new = find_duplicate(news)
            if duplicated_new:
                print(f"Notícia {duplicated_new} duplicada")
                sys.exit(1)
            import_from_json(news)
            print("Importação realizada com sucesso")
    except FileNotFoundError:
        print(f"Arquivo {json_file} não encontrado", file=sys.stderr)
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print("JSON inválido", file=sys.stderr)
        return json_file.close()


json_importer("xablau.json")
