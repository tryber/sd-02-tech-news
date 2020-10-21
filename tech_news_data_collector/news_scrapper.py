import requests
import sys
import time
from parsel import Selector
from pymongo import MongoClient


def add_scrapped_db(scrapped_pages):
    with MongoClient() as connection:
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        for page in scrapped_pages:
            page = collection.update_one(
                {"url": page["url"]}, {"$set": page}, upsert=True
            )


def fetch_content(url, timeout=1):
    try:
        response = requests.get(
            url, timeout=timeout, headers={"Accept": "text/html"}
        )
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError) as status_error:
        print(status_error, file=sys.stderr)
        return ''
    else:
        return response


def get_news_links(page_num, news_links):
    url_tech = "https://www.tecmundo.com.br/novidades"
    # linha do for
    index = 1
    while not url_tech == '' and index <= page_num:
        time.sleep(1)
        response = fetch_content(url_tech, 2)
        selector = Selector(text=response.text)
        news_links.extend(selector.css(
            "h3 .tec--card__title__link::attr(href)"
        ).getall())
        url_tech = selector.css(
            "a.tec--btn.tec--btn--lg.tec--btn--primary::attr(href)"
        ).get()
        index += 1


def scrape(page_num=1):
    news_links = []
    scrapped_pages = []

    get_news_links(int(page_num), news_links)

    for index, link in enumerate(news_links):
        time.sleep(0.1)
        response = fetch_content(link, 2)
        selector = Selector(text=response.text)
        print(f'Raspando a notícia {index + 1}')
        scrapped_pages.append({
            "url": link,
            "title": (selector.css(
                "#js-article-title::text"
            ).get() or "").strip(),
            "timestamp": selector.css(
                "#js-article-date::attr(datetime)"
            ).get() or "",
            "writer": (selector.css(
                "p .tec--author__info__link::text"
            ).get() or "").strip(),
            "shares_count": int(selector.css(
                ".tec--toolbar__item::text"
            ).re_first(r"\d") or 0),
            "comments_count": int(selector.css(
                "#js-comments-btn::text"
            ).re_first(r"\d") or 0),
            "summary": "".join(selector.css(
                ".tec--article__body p:first-child *::text"
            ).getall() or "").strip(),
            "sources": [
                source.strip()
                for source in selector.css(".tec--badge ::text").getall() or []
            ],
            "categories": [
                category.strip()
                for category in selector.css(
                    ".tec--badge.tec--badge--primary::text"
                ).getall() or []
            ],
        })
    add_scrapped_db(scrapped_pages)
    print("Raspagem de notícias finalizada")
