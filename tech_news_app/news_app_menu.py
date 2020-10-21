from news_search_engine import search_by_title, search_by_date, search_by_source, search_by_category
from news_analyser import top_5_news, top_5_categories
import sys


def option_1():
    by_title = input("Digite o título: ")
    print(search_by_title(by_title))


def option_2():
    by_date = input("Digite a data: ")
    print(search_by_date(by_date))


def option_3():
    by_source = input("Digite a fonte: ")
    print(search_by_source(by_source))


def option_4():
    by_category = input("Digite a categoria: ")
    print(search_by_category(by_category))


def option_5():
    print(top_5_news())


def option_6():
    print(top_5_categories())


def option_7():
    sys.exit(0)


if __name__ == "__main__":
    selected_option = input(
        """
Selecione uma das opções a seguir:
1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por fonte;
4 - Buscar notícias por categoria;
5 - Listar top 5 notícias;
6 - Listar top 5 categorias;
7 - Sair.
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
    elif selected_option == "7":
        option_7()
    else:
        print("Opção inválida", file=sys.stderr)
