from pymongo import MongoClient


def get_from_db(filter_query={}):
    with MongoClient() as client:
        db = client['web_scrape_python']
        return db['news_collection'].aggregate(filter_query)


def iterate_list(news_list):
    for item in news_list:
        print(f"- {item['title']} : {item['url']}")
    if not len(news_list):
        print([])


def iterate_categorie(news_list):
    for item in news_list:
        print(f"- {item['_id']}")
    if not len(news_list):
        print([])


def top_5_news():
    pipeline = [{'$project': {
        'url': '$url',
        'title': '$title',
        'comments_count': '$comments_count',
        'shares_count': '$shares_count',
        'totalInteraction': {'$add': [{
          '$convert': {'input': '$comments_count', 'to': 'int', 'onError': 0}},
                        {'$convert': {'input': '$shares_count',
                         'to': 'int', 'onError': 0}}]},
    }}, {'$sort': {'totalInteraction': -1, 'title': 1}}, {'$limit': 5}]

    news_list = list(get_from_db(pipeline))
    iterate_list(news_list)


def top_5_categories():
    pipeline = [{'$unwind': '$categories'}, {'$group': {'_id': '$categories',
                'quantity': {'$sum': 1}}}, {'$sort': {'quantity': -1}},
                {'$limit': 5}, {'$sort': {'_id': 1}}]
    news_list = list(get_from_db(pipeline))
    iterate_categorie(news_list)


# top_5_news()
top_5_categories()
