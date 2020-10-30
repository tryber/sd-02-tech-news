from database.index import search_news
import datetime


def search_by_title(term):
    regex = r"\b" + term + r"\b"
    query = {"title": {"$regex": regex, "$options": 'i'}}
    news = search_news(query)
    news_list = []
    for each in news:
        new = str("- " + each["title"] + ": " + each["url"])
        news_list.append(new)
    return news_list


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    else:
        query = {"timestamp": {"$regex": date, "$options": 'i'}}
        news = search_news(query)
        news_list = []
        for each in news:
            new = str("- " + each["title"] + ": " + each["url"])
            news_list.append(new)
        return news_list


def search_by_source(source):
    regex = r"\b" + source + r"\b"
    query = {"sources": {"$regex": regex, "$options": 'i'}}
    news = search_news(query)
    news_list = []
    for each in news:
        new = str("- " + each["title"] + ": " + each["url"])
        news_list.append(new)
    return news_list


def search_by_category(category):
    query = {"categories": category}
    news = search_news(query)
    news_list = []
    for each in news:
        new = str("- " + each["title"] + ": " + each["url"])
        news_list.append(new)
    return news_list
