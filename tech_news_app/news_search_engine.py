from pymongo import MongoClient
import re


def get_from_db(filter_query={}, projection={}):
    with MongoClient() as client:
        db = client['web_scrape_python']
        return db['news_collection'].find(filter_query, projection)


def iterate_list(news_list):
    for item in news_list:
        print(f"- {item['title']} : {item['url']}")
    if not len(news_list):
        print([])


def search_by_title(regex):
    regex_expression = {"title": {'$regex': regex, "$options": 'i'}}
    news_list = list(get_from_db(regex_expression, {"title": 1, "url": 1}))
    iterate_list(news_list)


def search_by_date(date):
    date_pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
    if not bool(date_pattern.match(date)):
        print("Data inválida")
    else:
        regex_express = {"datetime": {'$regex': '^' + date, "$options": 'i'}}
        news_list = list(get_from_db(regex_express, {"title": 1, "url": 1}))
        iterate_list(news_list)


def search_by_source(source):
    regex_expression = {
                        "sources": {
                          '$all': [re.compile(f'^{source}$', re.IGNORECASE)]}}
    news_list = list(get_from_db(regex_expression, {"title": 1, "url": 1}))
    iterate_list(news_list)


def search_by_category(cat):
    regex_expression = {
                        "categories": {
                          '$all': [re.compile(f'^{cat}$', re.IGNORECASE)]}}
    news_list = list(get_from_db(regex_expression, {"title": 1, "url": 1}))
    iterate_list(news_list)


# search_by_title('para criar')
# search_by_date('2020-09-13')
# search_by_source('Source 1')
# search_by_category('categoria 2adas')
