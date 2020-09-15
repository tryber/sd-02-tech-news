from tech_news_data_collector.mongo_connection import (
    get_top_5_news,
    get_top_5_categories,
)


def top_5_news():
    news_list = []
    news = get_top_5_news()
    for item in news:
        title = item["title"]
        url = item["url"]
        news_list.append(f"- {title}: {url}")
    print(news_list)


def top_5_categories():
    news_list = []
    news = get_top_5_categories()
    for item in news:
        category = item["category"]
        news_list.append(f"- {category}")
    print(news_list)
