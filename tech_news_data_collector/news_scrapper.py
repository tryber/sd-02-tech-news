import requests
import time
from parsel import Selector
from pymongo import MongoClient


user_agent = (
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.4183.83 Safari/537.36 "
)

info_headers = {"User-agent": user_agent, "Accept": "text/html"}

news_urls = []
result = []


def add_to_mongo(results):
    with MongoClient() as client:
        db = client["tech_news"]
        collection = db["news_raspadas"]
        for result in results:
            result = collection.update_one(
                {"url": result["url"]}, {"$set": result}, upsert=True
            )


def page_links(page_number):
    base_url = "https://www.tecmundo.com.br/novidades"
    query_number = 1
    while base_url and query_number <= page_number:
        print('for q', query_number)
        print('for b', base_url)
        time.sleep(1)
        response = requests.get(base_url, headers=info_headers)
        selector = Selector(response.text)
        news_urls.extend(selector.css(
            "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall())
        base_url = selector.css(
            ".tec--list.tec--list--lg > .tec--btn.tec--btn--lg::attr(href)"
        ).get()
        query_number = int(selector.css(
            ".tec--list.tec--list--lg > .tec--btn.tec--btn--lg::attr(href)"
        ).re_first(r"\d"))


def scrape(page_number=1):
    page_links(page_number)
    
    for index, news in enumerate(news_urls):
        time.sleep(0.1)
        resp_news = requests.get(news, headers=info_headers)
        sel_news = Selector(resp_news.text)

        result.append({
            "url": news,

            "title": (sel_news.css(
                "#js-article-title::text"
            ).get() or "").strip(),

            "timestamp": (sel_news.css(
                "#js-article-date::attr(datetime)"
            ).get() or ""),

            "writer": (sel_news.css(
                ".tec--author__info__link::text"
            ).get() or "").strip(),

            "shares_count": ((
                sel_news.css(".tec--toolbar .tec--toolbar__item::text")
                .re_first(r"\d")) or "0").strip(),

            "comments_count": ((
                sel_news.css("#js-comments-btn::attr(data-count)").get()
            ) or "0").strip(),

            "summary": (("".join(
                sel_news.css(".tec--article__body > p:first-child *::text")
                .getall())) or "").strip(),

            "sources": [source.strip() for source in ((
                sel_news.css(
                    ".z--mb-16.z--px-16 div:last-child a::text").getall()
            ) or [])],

            "categories": [category.strip() for category in ((
                sel_news.css("#js-categories a::text").getall()
            ) or [])]
        })
        print(index)
    # add_to_mongo(result)
    print(result)


scrape(3)
