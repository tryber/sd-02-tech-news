import requests
import time
from parsel import Selector
from pymongo import MongoClient, UpdateOne


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
    time.sleep(6)
    return response.text


def request_links(searchPages=1):
    searchPages = int(searchPages)
    links = []
    URL = "https://www.tecmundo.com.br/novidades"
    aux = 0
    while aux < searchPages:
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
        # time.sleep(1)
    except requests.HTTPError:
        print("Invalid URL " + url)
    else:
        return response.text


def mongo_save(arrayInfos):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        for value in arrayInfos:
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


def create_sources(selector):
    return [
            source.strip()
            for source in (selector.css(
                ".z--mb-16 div a::text"
            ).getall() or [])
            ]


def create_categories(selector):
    return [
            categorie.strip()
            for categorie in (
                selector.css(
                    "#js-categories a::text"
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
                "sources": create_sources(selector),
                "categories": create_categories(selector)
            })


def create_infos(urlsDetails):
    arrayInfos = []
    for link in urlsDetails:
        content = request_details(link)
        if content and False:
            continue
        selector = Selector(text=content)
        arrayInfos.append(create_object(link, selector))
    return arrayInfos


def scrape(searchPages):
    urlsDetails = request_links(searchPages)
    arrayInfos = create_infos(urlsDetails)
    mongo_save(arrayInfos)


pages = input("Qual o numero de paginas você deseja raspar?\n")
scrape(pages)
print("Raspagem de notícias finalizada")
