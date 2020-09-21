from parsel import Selector
from pymongo import MongoClient
import requests
import time


def fetch_content(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(6)
    except requests.HTTPError:
        return ""
    else:
        return response.text


def scrape(n=1):
    client = MongoClient()
    db = client.tech_news

    URL_BASE = "https://www.tecmundo.com.br/novidades"
    next_page_url = URL_BASE

    for i in range(n):
        next_page_text = fetch_content(next_page_url)
        selector = Selector(text=next_page_text)

        for news in selector.css(".tec--list__item"):
            title = news.css("h3 a::text").get()

            detail_page_url = news.css(".tec--card__title__link::attr(href)").get()
            detail_page_text = fetch_content(detail_page_url)
            detail_selector = Selector(text=detail_page_text)

            timestamp = detail_selector.css("time::attr(datetime)").get()
            writer = detail_selector.css(".tec--author__info__link::text").re_first(
                "[A-zÀ-ÿ][A-zÀ-ÿ' ]+"
            )
            shares_count = int(
                detail_selector.css(".tec--toolbar__item::text").re("[0-9]+")[0]
            )
            comments_count = int(
                detail_selector.css("#js-comments-btn::text").re("[0-9]+")[0]
            )
            summary = "".join(
                detail_selector.css(".tec--article__body p")[0].css("*::text").getall()
            )
            sources = detail_selector.css(".z--mb-16.z--px-16 a::text").re(
                "[A-zÀ-ÿ][A-zÀ-ÿ' ]+"
            )
            categories = detail_selector.css("#js-categories a::text").re(
                "[A-zÀ-ÿ][A-zÀ-ÿ' ]+"
            )

            document = {
                "url": detail_page_url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": shares_count,
                "comments_count": comments_count,
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }
            document_exists = db.news.find_one({"url": detail_page_url})
            if document_exists:
                db.news.update_one({"url": detail_page_url}, {"$set": document})
            else:
                db.news.insert_one(document)

        next_page_url = selector.css(
            ".tec--list--lg .tec--btn--primary::attr(href)"
        ).get()

    client.close()
    print("Raspagem de notícias finalizada")
