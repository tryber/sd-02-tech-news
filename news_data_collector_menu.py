import sys
import os
import time
from tech_news_data_collector.news_scrapper import scrape
from tech_news_data_collector.news_importer import csv_importer, json_importer
from tech_news_data_collector.news_exporter import csv_exporter, json_exporter
from os import system


def option_1():
    path_csv = input("Digite o path do arquivo CSV a ser importado: ")


def option_2():
    name_csv = input("Digite o nome do arquivo CSV a ser exportado: ")


def option_3():
    path_json = input("Digite o path do arquivo JSON a ser importado: ")


def option_4():
    name_json = input("Digite o nome do arquivo JSON a ser exportado: ")


def option_5():
    system('clear')
    page_number = input(
        "Digite a quantidade de páginas a serem raspadas: "
    ) or 1
    scrape(page_number)
    print("")
    return_main = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        system('clear')
        if return_main == "Y":
            os.execv(sys.executable, ['python'] + sys.argv)
        elif return_main == "N":
            print("Encerrando CLI")
            print(". ", end="")
            print(". ", end="")
            print(". ")
            time.sleep(1)
            sys.exit()
        else:
            print("Opção Inválida", file=sys.stderr)
            sys.exit()


if __name__ == "__main__":
    pass
    system('clear')
    print("Selecione uma das opções a seguir:")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print(f" {1} - Importar notícias a partir de um arquivo CSV")
    time.sleep(0.1)
    print(f" {2} - Exportar notícias para CSV")
    time.sleep(0.1)
    print(f" {3} - Importar notícias a partir de um arquivo JSON")
    time.sleep(0.1)
    print(f" {4} - Exportar notícias para JSON")
    time.sleep(0.1)
    print(f" {5} - Raspar notícias online")
    time.sleep(0.1)
    print(f" {6} - Sair")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)

    first_choice = input("Digite uma opção: ")
    time.sleep(0.1)
    if first_choice == "1":
        option_1()
    elif first_choice == "2":
        option_2()
    elif first_choice == "3":
        option_3()
    elif first_choice == "4":
        option_4()
    elif first_choice == "5":
        option_5()
    elif first_choice == "6":
        print("Até a próxima =)")
        sys.exit()
    else:
        print("Opção inválida", file=sys.stdout)
        sys.exit()
