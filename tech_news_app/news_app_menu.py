import sys
import os
import time
from os import system
from news_analyser import top_5_categories, top_5_news
from news_search_engine import search_by_title, search_by_date
from news_search_engine import search_by_source, search_by_category

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
    path_csv = input("Digite o título: ")
    print(search_by_title(path_csv))
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
    name_csv = input("Digite a data: ")
    print(search_by_date(name_csv))
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
    path_json = input("Digite a fonte: ")
    print(search_by_source(path_json))
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
    name_json = input("Digite a categoria: ")
    print(search_by_category(name_json))
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
    print(top_5_news())
    print("")
    print("================================================================")
    print("")
    answer = input("Deseja retornar ao menu principal? Y/N: ")

    if __name__ == "__main__":
        return_main(answer)


def option_6():
    system("clear")
    animation(0)
    print("================================================================")
    print("")
    print(top_5_categories())
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
    print(f" {1} - Buscar notícias por título")
    time.sleep(0.1)
    print(f" {2} - Buscar notícias por data")
    time.sleep(0.1)
    print(f" {3} - Buscar notícias por fonte")
    time.sleep(0.1)
    print(f" {4} - Buscar notícias por categoria")
    time.sleep(0.1)
    print(f" {5} - Listar top 5 notícias")
    time.sleep(0.1)
    print(f" {6} - Listas top 5 categorias")
    time.sleep(0.1)
    print(f" {7} - Sair")
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
        option_6()
    elif first_choice == "7":
        print("Até a próxima =)")
        sys.exit()
    else:
        print("Opção inválida", file=sys.stderr)
        sys.exit()
