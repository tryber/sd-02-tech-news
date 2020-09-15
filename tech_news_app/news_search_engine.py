import sys
import datetime
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from tech_news_data_collector.mongo_connection import (
    get_news_by_title,
    get_news_by_date,
)


def search_by_title(title):
    news_list = []
    news = list(get_news_by_title(title))
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    print(news_list)


def check_date(date):
    # solução retirada de: https://www.codevscolor.com/date-valid-check-python
    year, month, day = date.split("-")
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print("Data inválida", file=sys.stderr)
        return False
    else:
        return True


def search_by_date(date):
    news_list = []
    validDate = check_date(date)
    if not validDate:
        return
    news = list(get_news_by_date(date))
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    print(news_list)


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


# search_by_title("CELULAR")
search_by_date("2020-09-15")
