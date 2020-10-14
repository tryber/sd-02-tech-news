import csv
import json
import sys

from mongo_connection import export_to_csv, export_to_json


def csv_exporter(filename):
    with open(filename, "w") as file:  # só confia
        if not filename.endswith(".csv"):
            print("Formato inválido", file=sys.stderr)
            sys.exit(1)
        # escreve o cabeçalho
        headers = [
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
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        array_from_db = export_to_csv()
        # thx miguel-miguelito
        for document in array_from_db:
            row = {}
            for name, value in document.items():
                if name == "sources" or name == "categories":
                    row[name] = ",".join(value)
                else:
                    row[name] = value
            writer.writerow(row)
        print("Exportação realizada com sucesso")


def json_exporter(filename):
    if not filename.endswith(".json"):
        return print("Formato inválido", file=sys.stderr)
    with open(filename, "w") as file:
        json_to_write = json.dumps(export_to_json(), ensure_ascii=False)
        file.write(json_to_write)
        print("Exportação realizada com sucesso")


json_exporter('xablau_exp.json')
