import sys

from tech_news_app.news_search_engine import search_by_title, search_by_date
from tech_news_app.news_search_engine import search_by_source
from tech_news_app.news_search_engine import search_by_category
from tech_news_app.news_analyser import top_5_categories, top_5_news


def one():
    title = input("Digite o título:")
    print(search_by_title(title))


def two():
    date = input("Digite a data:")
    print(search_by_date(date))


def tree():
    source = input("Digite a fonte:")
    print(search_by_source(source))


def four():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def five():
    print(top_5_news())


def six():
    print(top_5_categories())


def seven():
    sys.exit(0)


dict1 = {
  '1': one,
  '2': two,
  '3': tree,
  '4': four,
  '5': five,
  '6': six,
  '7': seven
}


def list_options():
    print("1 - Buscar notícias por título")
    print("2 - Buscar notícias por data")
    print("3 - Buscar notícias por fonte")
    print("4 - Buscar notícias por categoria")
    print("5 - Listar top 5 notícias")
    print("6 - Listar top 5 categorias")
    print("7 - Sair")


def menu():
    while (True):
        list_options()
        choose = input()
        if (dict1[choose]):
            dict1[choose]()
        else:
            print("Opção inválida", file=sys.stderr)
