import inquirer
# import click

from collector.news_exporter import (csv_exporter, json_exporter)
from collector.news_importer import (csv_importer, json_importer)
from collector.news_scrapper import scrape

choices = [
    "1 - Importar notícias a partir de um arquivo CSV;",
    "2 - Exportar notícias para CSV;",
    "3 - Importar notícias a partir de um arquivo JSON;",
    "4 - Exportar notícias para JSON;",
    "5 - Raspar notícias online;",
    "6 - Sair.",
]


def prompt_csv_importer():
    questions = [inquirer.Text(
        "path", message="Digite o path do arquivo CSV a ser importado")]
    answer = inquirer.prompt(questions)
    csv_exporter(answer["path"])


interface = {
    "1": prompt_csv_importer
}


def main():
    questions = [inquirer.List(
        "option", message="Selecione uma das opções a seguir", choices=choices)]
    answer = inquirer.prompt(questions)
    index = answer["option"][0]
    interface[index]()

# @click.group(name="tech_news")


def tech_news():
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")


# @tech_news.command()
# @click.option('--param', help='path do arquivo CSV')
# def exporter(param: str):
#     """Importar notícias a partir de um arquivo CSV"""
#     print(param)


if __name__ == '__main__':
    tech_news()
