import csv
import sys

from mongo_connection import export_to_csv


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


def json_exporter():
    raise NotImplementedError


csv_exporter('xablau_exp.csv')
