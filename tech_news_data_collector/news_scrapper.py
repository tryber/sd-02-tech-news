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
        ).re_first(r"\d") or 0)


def getter_strip(sel_news, css_info, fail):
    answer = (sel_news.css(css_info).get() or fail).strip()
    return answer


def getterall_strip(sel_news, css_info, fail):
    answer = (("".join(sel_news.css(css_info).getall()))
              or fail).strip()
    return answer


def getter_only(sel_news, css_info, fail):
    answer = (sel_news.css(css_info).get() or fail)
    return answer


def list_getterall(sel_news, css_info):
    answer = [item.strip() for item in ((
        sel_news.css(css_info).getall()
    ) or [])]
    return answer


def scrape(page_number=1):
    page_links(page_number)

    for index, news in enumerate(news_urls):
        time.sleep(0.1)
        resp_news = requests.get(news, headers=info_headers)
        sel_news = Selector(resp_news.text)

        result.append({
            "url": news,

            "title": getter_strip(sel_news, "#js-article-title::text", ""),

            "timestamp": getter_only(
                sel_news, "#js-article-date::attr(datetime)", ""
            ),

            "writer": getter_strip(
                sel_news, ".tec--author__info__link::text", ""
            ),

            "shares_count": ((
                sel_news.css(".tec--toolbar .tec--toolbar__item::text")
                .re_first(r"\d")) or "0").strip(),

            "comments_count": getter_strip(
                sel_news, "#js-comments-btn::attr(data-count)", "0"
            ),

            "summary": getterall_strip(
                sel_news, ".tec--article__body > p:first-child *::text", ""
            ),

            "sources": list_getterall(
                sel_news, ".z--mb-16.z--px-16 div:last-child a::text"),

            "categories": list_getterall(sel_news, "#js-categories a::text")
        })
        print(index, result)
    add_to_mongo(result)


scrape(9)
