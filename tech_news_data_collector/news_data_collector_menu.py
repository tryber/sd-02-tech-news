from news_importer import csv_importer, json_importer
from news_exporter import csv_exporter, json_exporter
from news_scrapper import scrape
import sys


def option_1():
    file = input("Digite o path do arquivo CSV a ser importado: ")
    csv_importer(file)


def option_2():
    file = input("Digite o nome do arquivo CSV a ser exportado: ")
    csv_exporter(file)


def option_3():
    file = input("Digite o path do arquivo JSON a ser importado: ")
    json_importer(file)


def option_4():
    file = input("Digite o nome do arquivo JSON a ser exportado: ")
    json_exporter(file)


def option_5():
    n = input("Digite a quantidade de páginas a serem raspadas: ")
    if n == "":
        scrape()
    else:
        scrape(int(n))


def option_6():
    sys.exit(0)


choices = {1: option_1(), 2: option_2(), 3: option_3()}


if __name__ == "__main__":
    selected_option = input(
        """
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Importar notícias a partir de um arquivo JSON;
4 - Exportar notícias para JSON;
5 - Raspar notícias online;
6 - Sair.

"""
    )

    if selected_option == "1":
        option_1()
    elif selected_option == "2":
        option_2()
    elif selected_option == "3":
        option_3()
    elif selected_option == "4":
        option_4()
    elif selected_option == "5":
        option_5()
    elif selected_option == "6":
        option_6()
    else:
        print("Opção inválida", file=sys.stderr)