import requests
import time
import re
from parsel import Selector
from pymongo import MongoClient

user_agent = (
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.4183.83 Safari/537.36 "
)

info_headers = {"User-agent": user_agent, "Accept": "text/html"}


def insert_mongo(dict_news):
    with MongoClient() as client:
        db = client.tech_news
        for news in dict_news:
            db.news_details.find_one_and_replace(
                {"url": news["url"]}, news, upsert=True
            )


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout, headers=info_headers)
        response.raise_for_status()
        time.sleep(1)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def remove_spaces(string):
    return [
        newstr.strip()
        for newstr in re.split(r"\s{2,}", ("".join(string)))
        if newstr
    ]


def get_title(selector, css_path):
    title = selector.css(css_path).get() or ""
    return title.strip()


def get_timestamp(selector, css_path):
    timestamp = selector.css(css_path).get() or ""
    return timestamp


def get_writer(selector, css_path):
    writer = selector.css(css_path).get() or ""
    return writer.strip()


def get_shares(selector, css_path):
    share_count = selector.css(css_path).re_first(r"\d+") or 0
    return int(share_count)


def get_comments(selector, css_path):
    comments_count = selector.css(css_path).get() or 0
    return int(comments_count)


def get_summary(selector, css_path):
    summary = selector.css(css_path).getall() or ""
    return ("".join(summary)).strip()


def get_source(selector, css_path):
    source = selector.css(css_path).getall() or ""
    return remove_spaces(source)


def get_categories(selector, css_path):
    categories = selector.css(css_path).getall() or ""
    return remove_spaces(categories)


def get_news(news_links):
    count = 0
    details_news = []
    for news_link in news_links:
        details_response = fetch_content(news_link, timeout=2)
        details_selector = Selector(text=details_response)
        dict_news = {
            "url": news_link,
            "title": get_title(details_selector, "#js-article-title::text"),
            "timestamp": get_timestamp(
                details_selector, "#js-article-date::attr(datetime)"
            ),
            "writer": get_writer(
                details_selector, ".tec--author__info__link::text"
            ),
            "shares_count": get_shares(
                details_selector, "div.tec--toolbar__item::text"
            ),
            "comments_count": get_comments(
                details_selector, "#js-comments-btn::attr(data-count)"
            ),
            "summary": get_summary(
                details_selector,
                ".tec--article__body p:first_child *::text",
            ),
            "sources": get_source(
                details_selector, ".z--mb-16 .tec--badge::text"
            ),
            "categories": get_categories(
                details_selector, "#js-categories .tec--badge::text"
            ),
        }
        details_news.append(dict_news)
        count += 1
        print(f'Finalizada a raspagem de numero {count}')
    return details_news


def scrape(n=1):
    URL_BASE = "https://www.tecmundo.com.br/novidades?page=1"
    count = 0
    response = fetch_content(URL_BASE, timeout=2)
    while count < n or response == "":
        selector = Selector(text=response)
        news_links = selector.css(
            ".tec--list__item article .tec--card__info h3 a::attr(href)"
        ).getall()
        insert_mongo(get_news(news_links))
        URL_BASE = selector.css(".tec--list .tec--btn::attr(href)").get() or ""
        response = fetch_content(URL_BASE, timeout=2)
        count += 1
    print('Raspagem de notícias finalizada.')


# scrape(1)
