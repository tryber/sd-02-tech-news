from pymongo import MongoClient
import sys
from pathlib import Path
import json
from utils import check_comparison
import os.path


correct_header = ['url', 'title', 'timestamp', 'writer', 'shares_count',
                  'comments_count', 'summary', 'sources', 'categories']


def get_from_db(db, collection, projection={}):
    with MongoClient() as client:
        db = client[db]
        return db[collection].find({}, projection)


def check_if_is_list(item):
    if type(item) is list:
        return ','.join(item)
    return item


def adjust_dot_comma(lines):
    final_text = []
    for line in lines:
        adjusted_line = []

        for item in line:
            item = check_if_is_list(item)
            adjusted_line.append(item)

        final_text.append(adjusted_line)
    return final_text


def csv_exporter(file_path):
    try:
        extension = os.path.splitext(file_path)[1]
        check_comparison(extension, '.csv', 'Formato inválido')

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        all_news = list(get_from_db('web_scrape_python',
                                    'news_collection',
                                    {"_id": 0}))

        base_path = Path(__file__).parent
        file_path = (base_path / f"{file_path}").resolve()

        with open(file_path, mode="w") as file:
            lines = [list(new.values()) for new in all_news]

            final_text = adjust_dot_comma(lines)

            adjusted_line = '\n'.join([';'.join(line) for line in final_text])
            file.writelines(';'.join(correct_header) + '\n' + adjusted_line)

        print('Exportação realizada com sucesso', file=sys.stdout)


def json_exporter(file_path):
    try:
        extension = os.path.splitext(file_path)[1]
        check_comparison(extension, '.json', 'Formato inválido')

        all_news = list(get_from_db('web_scrape_python', 'news_collection'))

        base_path = Path(__file__).parent
        file_path = (base_path / f"{file_path}").resolve()

        with open(file_path, mode="w") as file:
            lines = [line for line in all_news]
            json_news = json.dumps(lines)
            file.write(json_news)

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        print('Exportação realizada com sucesso', file=sys.stdout)


csv_exporter("../news.csv")
# json_exporter("../news.json")
