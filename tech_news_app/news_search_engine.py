from pymongo import MongoClient


def search_by_title(search):
    client = MongoClient()
    db = client.tech_news

    searched_news = list(db.news.find(
        {"title": {"$regex": search, "$options": 'i'}},
        {"title": 1, "url": 1, "_id": 0}
    ))

    return [
        f"- {news['title']}: {news['url']}"
        for news in searched_news
    ]


def search_by_date():
    raise NotImplementedError


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError
