from mongo_connection import db
import re


def search_by_title(input):
    regex = f'{input}'
    news = db().pages.find({'title': {'$regex': regex, '$options': 'i'}},{'_id': 0, 'title': 1, 'url': 1 })
    return list(news)


def is_valid_date(date):
    if not bool(re.match('\d{2}-\d{2}-\d{4}', date)):
        print('Data inválida', file=sys.stderr)
        raise ValueError


def search_by_date(date):
    try:
        is_valid_date(date)
        news = db().pages.find({'timestamp': date},{'_id': 0, 'title': 1, 'url': 1})
        return list(news)
    except ValueError:
        print()


def search_by_source(source):
    news = db().pages.find({'$and': [{"sources": {'$regex':  source, '$options': 'i'}}]},{'_id': 0, 'title': 1, 'url': 1})
    return list(news)


def search_by_category(category):
    news = db().pages.find({'$and':[{"categories": '$regex':  category, '$options': 'i'}}]},{'_id': 0, 'title': 1, 'url': 1})
    return list(news)
