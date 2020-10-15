from mongo_connection_tech_news_app import mongo_search_by_title


def search_by_title(search):
    all_news = []
    news = mongo_search_by_title(search)
    for new in news:
        title = new["title"]
        url = new["url"]
        all_news.append(f"- {title}: {url}")
    print(all_news)


def search_by_date():
    raise NotImplementedError


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


search_by_title("xablau")