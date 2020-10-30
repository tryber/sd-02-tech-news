from collector.news_service import (
    fetch_content,
    get_urls,
    URL_BASE,
    get_news,
    get_next_page_url,
)

from database.index import upsert_news


def scrape(pages_number=1):
    content_news = fetch_content(URL_BASE)
    current_page = 1
    news_data = []
    while current_page <= pages_number:
        urls = get_urls(content_news)
        for url in urls:
            content_details = fetch_content(url)
            news = get_news(content_details, url)
            if news:
                news_data.append(news)

        next_url = get_next_page_url(content_news)
        if next_url:
            content_news = fetch_content(next_url)
            current_page += 1
        else:
            raise ValueError(
                "Page Limit Achieved: {} pages".format(current_page))

    upsert_news(news_data)

    print("Raspagem de notícias finalizada")
