
import datetime

from app.news_service import get_news_list


def search_by_title(term):
    regex = r"\b" + term + r"\b"
    query = {"title": {"$regex": regex, "$options": 'i'}}
    return get_news_list(query)


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    else:
        query = {"timestamp": {"$regex": date, "$options": 'i'}}
        return get_news_list(query)


def search_by_source(source):
    regex = r"\b" + source + r"\b"
    query = {"sources": {"$regex": regex, "$options": 'i'}}
    return get_news_list(query)


def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    return get_news_list(query)
