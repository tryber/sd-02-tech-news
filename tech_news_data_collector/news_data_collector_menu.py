import sys
import os
import time
from news_scrapper import scrape
from news_importer import csv_importer, json_importer
from news_exporter import csv_exporter, json_exporter
from os import system

# função animation retirada do link abaixo:
# https://www.vivaolinux.com.br/topico/Python/Criar-animacoes-com-texto-em-python


def animation(tempo=0.02):
    frase = "====#BeTrybe==== BEM VINDO AO PROJETO TECH-NEWS ====#BeTrybe===="
    for i in list(frase):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(tempo)
    print("")
    print("")


def return_main(answer):
    result = answer.lower()
    if result == "y":
        os.execv(sys.executable, ['python3'] + sys.argv)
    elif result == "n":
        print("Encerrando CLI")
        print(". ", end="")
        print(". ", end="")
        print(". ")
        time.sleep(1)
        sys.exit()
    else:
        print("Opção Inválida", file=sys.stderr)
        print("Encerrando CLI")
        print(". ", end="")
        print(". ", end="")
        print(". ")
        time.sleep(1)
        sys.exit()


def option_1():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    path_csv = input("Digite o path do arquivo CSV a ser importado: ")
    csv_importer(path_csv)
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


def option_2():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    name_csv = input("Digite o nome do arquivo CSV a ser exportado: ")
    csv_exporter(name_csv)
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


def option_3():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    path_json = input("Digite o path do arquivo JSON a ser importado: ")
    json_importer(path_json)
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


def option_4():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    name_json = input("Digite o nome do arquivo JSON a ser exportado: ")
    json_exporter(name_json)
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


def option_5():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    page_number = input(
        "Digite a quantidade de páginas a serem raspadas: "
    ) or 1
    scrape(page_number)
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


if __name__ == "__main__":
    pass
    system('clear')
    animation()
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
        print("Opção inválida", file=sys.stderr)
        sys.exit()
