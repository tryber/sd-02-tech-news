from pymongo import MongoClient
import sys
from pathlib import Path


correct_header = ['url', 'title', 'timestamp', 'writer', 'shares_count',
                  'comments_count', 'summary', 'sources', 'categories']


def get_from_db(db, collection):
    with MongoClient() as client:
        db = client[db]
        return db[collection].find()


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


def csv_exporter():
    all_news = list(get_from_db('web_scrape_python', 'news_collection'))

    base_path = Path(__file__).parent
    file_path = (base_path / "../news.txt").resolve()

    with open(file_path, mode="w") as file:
        lines = [list(new.values())[1:] for new in all_news]

        final_text = adjust_dot_comma(lines)

        adjusted_line = '\n'.join([';'.join(line) for line in final_text])
        file.writelines(';'.join(correct_header) + '\n' + adjusted_line)

    print('Exportação realizada com sucesso', file=sys.stdout)


def json_exporter():
    raise NotImplementedError


csv_exporter()
