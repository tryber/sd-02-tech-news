import sys
import datetime
from tech_news_data_collector.mongo_connection import (
    get_news_by_title,
    get_news_by_date,
    get_news_by_source,
    get_news_by_category,
)


def search_by_title(title):
    news_list = []
    news = get_news_by_title(title)
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    return news_list


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
    news = get_news_by_date(date)
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    return news_list


def search_by_source(source):
    news_list = []
    news = get_news_by_source(source)
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    return news_list


def search_by_category(category):
    news_list = []
    news = get_news_by_category(category)
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    return news_list
