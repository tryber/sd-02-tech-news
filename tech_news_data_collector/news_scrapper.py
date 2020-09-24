from parsel import Selector
from pymongo import MongoClient
import time
import requests

url = "https://www.tecmundo.com.br/novidades"

client = MongoClient()

db = client.allnews


def fetch_content(url):
    user_agent = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    try:
        response = requests.get(url, user_agent)
        time.sleep(6)
    except (requests.HTTPError or requests.ReadTimeout) as error:
        print(error)
        return
    else:
        return response.text


def strip_content(content):
    return content.strip()


def catch_news_info(url):
    page_text = fetch_content(url)
    selector = Selector(page_text)
    data_extract = {
        "url": url or "",
        "title": (selector.css("#js-article-title::text").get() or "").strip(),
        "timestamp": (
            selector.css("#js-article-date::attr(datetime)").get() or ""
        ).strip(),
        "writer": (
            selector.css(".tec--author__info__link::text").get() or ""
        ).strip(),
        "shares_count": selector.css(
            ".tec--toolbar__item:nth-child(1)::text"
        ).re_first(r"[0-9]{1,}")
        or None,
        "comments_count": selector.css("#js-comments-btn::text").re_first(
            r"[0-9]{1,}"
        )
        or None,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:nth-child(1) *::text"
            ).getall()
        )
        or None,
        "sources": list(
            map(
                strip_content,
                selector.css(
                    ".z--mb-16 > div:nth-child(2) > a::text"
                ).getall(),
            )
        )
        or None,
        "categories": list(
            map(
                strip_content,
                selector.css("a.tec--badge--primary::text").getall(),
            )
        )
        or None,
    }
    db.news.insert_one(data_extract)
    return data_extract


def scrape(url, num_pages=1):
    for num in range(num_pages):
        print("Buscando notícias da Página", num + 1)
        page = Selector(fetch_content(url))
        links = page.css(
            ".tec--list__item > article > div > h3 > a::attr(href)"
        ).getall()
        for i, href in enumerate(links):
            catch_news_info(href)
            print("Noticia", i + 1, "Inserida com sucesso")
        url = (page.css(".tec--btn::attr(href)").get() or "").strip()


scrape(url)
