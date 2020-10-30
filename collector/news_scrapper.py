from collector.news_service import (
    fetch_content,
    URL_BASE,
    get_urls,
    get_news
)

from database.index import create_or_update_news


def scrape(pages_number=1):
    current_page = 1

    news_data = []

    while current_page <= pages_number:
        content_news = fetch_content(URL_BASE + "?page=" + str(pages_number))
        urls = get_urls(content_news)
        print("urls", urls)
        for url in urls:
            content_details = fetch_content(url)
            news = get_news(content_details, url)
            if news:
                news_data.append(news)

        current_page += 1

    create_or_update_news(news_data)

    print("Raspagem de notícias finalizada")
