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


def insert_mongo():
    with MongoClient() as client:
        db = client.tech_news
        db.teste


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout, headers=info_headers)
        response.raise_for_status()
        time.sleep(1)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def scrape(n=1):
    URL_BASE = 'https://www.tecmundo.com.br/novidades?page=1'
    count = 0
    response = fetch_content(URL_BASE, timeout=2)
    while count < n or response == "":
        selector = Selector(text=response)
        news_links = selector.css(".tec--list__item article .tec--card__info h3 a::attr(href)").getall()
        for news_link in news_links:
            details_response = fetch_content(news_link, timeout=2)
            details_selector = Selector(text=details_response)
            details_title = details_selector.css("#js-article-title::text").get() or ""
            details_timestamp = details_selector.css("#js-article-date::attr(datetime)").get()
            details_writer = details_selector.css(".tec--author__info__link::text").get() or ""
            details_share_count = details_selector.css("div.tec--toolbar__item::text").re_first(r"\d+") or 0
            details_comments_count = details_selector.css("#js-comments-btn::attr(data-count)").get() or 0
            details_summary = details_selector.css(".tec--article__body p:first_child *::text").getall()
            details_source = details_selector.css(".z--mb-16 .tec--badge::text").getall()
            details_category = details_selector.css("#js-categories .tec--badge::text").getall()
            dict_news = {
                'url': news_link,
                'title': details_title.strip(),
                'timestamp': details_timestamp,
                'writer': details_writer.strip(),
                'share_count': int(details_share_count),
                'comments_count': int(details_comments_count),
                'summary': ("".join(details_summary)).strip(),
                'source': ("".join(details_source)).split(),
                'categories': ("".join(details_category)).split(),
            }
            print(dict_news)
        URL_BASE = selector.css('.tec--list .tec--btn::attr(href)').get() or ''
        response = fetch_content(URL_BASE, timeout=2)
        print(URL_BASE)
        count += 1
        print(count)


scrape(2)
