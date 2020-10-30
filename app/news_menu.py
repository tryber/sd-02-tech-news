import inquirer
# import click

from app.news_analyser import (top_5_categories, top_5_news)
from app.news_search_engine import (
    search_by_title, search_by_date, search_by_source, search_by_category)

choices = [
    "1 - Buscar notícias por título;",
    "2 - Buscar notícias por data;",
    "3 - Buscar notícias por fonte;",
    "4 - Buscar notícias por categoria;",
    "5 - Listar top 5 notícias;",
    "6 - Listar top 5 categorias;",
    "7 - Sair."
]


def show_list(data):
    for each in data:
        print(each)


def prompt_search_by_title():
    questions = [inquirer.Text(
        "title", message="Digite o título")]
    title = inquirer.prompt(questions)['title']
    show_list(search_by_title(title))


def prompt_search_by_date():
    questions = [inquirer.Text(
        "data", message="Digite a data")]
    data = inquirer.prompt(questions)['data']
    show_list(search_by_date(data))


def prompt_search_by_source():
    questions = [inquirer.Text(
        "source", message="Digite a fonte")]
    source = inquirer.prompt(questions)['source']
    show_list(search_by_source(source))


def prompt_search_by_category():
    questions = [inquirer.Text(
        "category", message="Digite a categoria")]
    category = inquirer.prompt(questions)['category']
    show_list(search_by_category(category))


def prompt_top_5_categories():
    show_list(top_5_categories())


def prompt_top_5_news():
    show_list(top_5_news())


def exit_code():
    print("Bye")
    pass


interface = {
    "1": prompt_search_by_title,
    "2": prompt_search_by_date,
    "3": prompt_search_by_source,
    "4": prompt_search_by_category,
    "5": prompt_top_5_news,
    "6": prompt_top_5_categories,
    "7": exit_code
}


def main():
    questions = [inquirer.List(
        "option", message="Selecione uma das opções a seguir", choices=choices)]
    answer = inquirer.prompt(questions)
    index = answer["option"][0]
    interface[index]()

# @click.group(name="tech_news")


def tech_news():
    # try:
    main()
    # except KeyboardInterrupt:
    #     print("Bye!")


# @tech_news.command()
# @click.option('--param', help='path do arquivo CSV')
# def exporter(param: str):
#     """Importar notícias a partir de um arquivo CSV"""
#     print(param)


if __name__ == '__main__':
    tech_news()
