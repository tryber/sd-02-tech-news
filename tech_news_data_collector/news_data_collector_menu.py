import sys

from tech_news_data_collector.news_importer import csv_importer, json_importer
from tech_news_data_collector.news_exporter import csv_exporter, json_exporter
from tech_news_data_collector.news_scrapper import scrape


def one():
    path_arq = input("Digite o path do arquivo CSV a ser importado:")
    csv_importer(path_arq)


def two():
    path_arq = input("Digite o path do arquivo CSV a ser exported:")
    csv_exporter(path_arq)


def tree():
    path_arq = input("Digite o path do arquivo JSON a ser importado:")
    json_importer(path_arq)


def four():
    path_arq = input("Digite o path do arquivo JSON a ser exported:")
    json_exporter(path_arq)


def five():
    num_pages = input("Digite a quantidade de páginas a serem raspadas:")
    scrape(num_pages)


def six():
    sys.exit(0)


dict1 = {
  '1': one,
  '2': two,
  '3': tree,
  '4': four,
  '5': five,
  '6': six
}


if "__main__":
    print("1 - Importar notícias a partir de um arquivo CSV")
    print("2 - Exportar notícias para CSV")
    print("3 - Importar notícias a partir de um arquivo JSON")
    print("4 - Exportar notícias para JSON")
    print("5 - Raspar notícias online")
    print("6 - Sai")


def menu():
    while (True):
        choose = input()
        if (dict1[choose]):
            dict1[choose]()
            sys.exit(0)
        else:
            print("Opção inválida", file=sys.stderr)
