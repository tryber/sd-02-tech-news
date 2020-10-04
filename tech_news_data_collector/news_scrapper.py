import requests
from parsel import Selector
from pymongo import MongoClient, UpdateOne
import sys


user_agent = (
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.4183.83 Safari/537.36 "
)


def fetch_content(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": user_agent,
        },
    )
    return response.text


def request_links(search_pages):
    links = []
    URL = "https://www.tecmundo.com.br/novidades"
    aux = 0
    while aux < search_pages:
        content = fetch_content(URL)
        selector = Selector(text=content)
        links = (
            links
            + selector.css(
                ".tec--list__item .tec--card__title a::attr(href)"
                ).getall()
        )
        URL = selector.css(".tec--list .tec--btn::attr(href)").get()
        aux += 1
    return links


def request_details(url):
    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": user_agent,
            },
        )
        response.raise_for_status()
    except ValueError:
        print("Invalid URL " + url, file=sys.stderr)
    else:
        return response.text


def mongo_save(array_infos):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for value in array_infos:
            db["news"].bulk_write(
                [UpdateOne(
                    {"url": value["url"]},
                    {"$set": value},
                    upsert=True)]
            )


def create_title(selector):
    return (
            selector.css(
                ".tec--article__header__title::text"
            ).get()
            or "").strip()


def create_timestamp(selector):
    return(
            selector.css(
                ".tec--timestamp time::attr(datetime)"
            ).get() or ""
        )


def create_writer(selector):
    return (
            selector.css(
                ".tec--author__info__link::text"
            ).get()
            or "").strip()


def create_shares_count(selector):
    return int(
                selector.css(
                    ".tec--toolbar .tec--toolbar__item::text"
                ).re_first(
                    r"\d{1,}"
                )
                or 0
            )


def create_comments_count(selector):
    return int(selector.css(
                    "#js-comments-btn::text"
                ).re_first(
                r"\d{1,}"
            ) or 0)


def create_summary(selector):
    return ("".join(
                    selector.css(
                        ".tec--article__body p:first-child *::text"
                    ).getall() or ""
            ))


def create_sources_categories(selector, text):
    return [
                categorie.strip()
                for categorie in (
                    selector.css(
                        text
                    ).getall()
                    or []
                )
            ]


def create_object(link, selector):
    return ({
                "url": link,
                "title": create_title(selector),
                "timestamp": create_timestamp(selector),
                "writer": create_writer(selector),
                "shares_count": create_shares_count(selector),
                "comments_count": create_comments_count(selector),
                "summary": create_summary(selector),
                "sources": create_sources_categories(
                    selector, ".z--mb-16 div a::text"
                ),
                "categories": create_sources_categories(
                    selector, "#js-categories a::text"
                )
            })


def create_infos(urls_details):
    array_infos = []
    for link in urls_details:
        content = request_details(link)
        if content and False:
            continue
        selector = Selector(text=content)
        array_infos.append(create_object(link, selector))
    return array_infos


def scrape(search_pages=1):
    try:
        urls_details = request_links(search_pages)
        array_infos = create_infos(urls_details)
        mongo_save(array_infos)
    except ValueError:
        print('erro desconhecido')
    else:
        print("Raspagem de notícias finalizada", file=sys.stderr)
