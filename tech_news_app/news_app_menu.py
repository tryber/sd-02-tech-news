from news_search_engine import search_by_title, search_by_date, search_by_source, search_by_category
from news_analyser import top_5_news, top_5_categories
import sys


def case_1():
    search = input("Digite o título: ")
    print(search_by_title(search))


def case_2():
    search = input("Digite a data: ")
    print(search_by_date(search))


def case_3():
    search = input("Digite a fonte: ")
    print(search_by_source(search))


def case_4():
    search = input("Digite a categoria: ")
    print(search_by_category(search))


def case_5():
    print(top_5_news())


def case_6():
    print(top_5_categories())


def case_7():
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
        case_1()
    elif selected_option == "2":
        case_2()
    elif selected_option == "3":
        case_3()
    elif selected_option == "4":
        case_4()
    elif selected_option == "5":
        case_5()
    elif selected_option == "6":
        case_6()
    elif selected_option == "7":
        case_7()
    else:
        print("Opção inválida", file=sys.stderr)
