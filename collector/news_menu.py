from collector.news_exporter import (csv_exporter, json_exporter)
from collector.news_importer import (csv_importer, json_importer)
from collector.news_scrapper import scrape
import inquirer

choices = [
    "1 - Importar notícias a partir de um arquivo CSV;",
    "2 - Exportar notícias para CSV;",
    "3 - Importar notícias a partir de um arquivo JSON;",
    "4 - Exportar notícias para JSON;",
    "5 - Raspar notícias online;",
    "6 - Sair.",
]


def exit_code():
    print("Bye")
    pass


def prompt_csv_exporter():
    questions = [inquirer.Text(
        "name", message="Digite o nome do arquivo CSV a ser exportado")]
    csv_path = inquirer.prompt(questions)['name']
    csv_exporter(csv_path)


def prompt_csv_importer():
    questions = [inquirer.Text(
        "path", message="Digite o path do arquivo CSV a ser importado")]
    csv_path = inquirer.prompt(questions)['path']
    csv_importer(csv_path)


def prompt_json_exporter():
    questions = [inquirer.Text(
        "name", message="Digite o nome do arquivo JSON a ser exportado")]
    csv_path = inquirer.prompt(questions)['name']
    json_exporter(csv_path)


def prompt_json_importer():
    questions = [inquirer.Text(
        "path", message="Digite o path do arquivo JSON a ser importado")]
    json_path = inquirer.prompt(questions)['path']
    json_importer(json_path)


def prompt_scrape():
    questions = [inquirer.Text(
        "number", message="Digite a quantidade de páginas a serem raspadas")]
    pages_number = int(inquirer.prompt(questions)['number'])
    scrape(pages_number)


interface = {
    "1": prompt_csv_importer,
    "2": prompt_csv_exporter,
    "3": prompt_json_importer,
    "4": prompt_json_exporter,
    "5": prompt_scrape,
    "6": exit_code
}


def main():
    questions = [inquirer.List(
        "option", message="Selecione uma das opções a seguir", choices=choices)
    ]
    answer = inquirer.prompt(questions)
    index = answer["option"][0]
    interface[index]()


def tech_news():
    main()


if __name__ == '__main__':
    tech_news()
