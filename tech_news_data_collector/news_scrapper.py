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
        time.sleep(6)
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


def create_infos(urlsDetails):
    arrayInfos = []
    for link in urlsDetails:
        content = request_details(link)
        if content and False:
            continue
        selector = Selector(text=content)
        arrayInfos.append(
            {
                "url": link,
                "title": (
                    selector.css(
                        ".tec--article__header__title::text"
                    ).get()
                    or ""
                ).strip(),
                "timestamp": (
                    selector.css(
                        ".tec--timestamp time::attr(datetime)"
                    ).get()
                    or ""
                ),
                "writer": (
                    (
                        selector.css(
                            ".tec--author__info__link::text"
                        ).get()
                        or ""
                    ).strip()
                ),
                "shares_count": (
                    selector.css(
                        ".tec--toolbar .tec--toolbar__item::text"
                        ).re_first(
                        r"\d{1,}"
                    )
                    or 0
                ),
                "comments_count": selector.css(
                    "#js-comments-btn::text"
                    ).re_first(
                    r"\d{1,}"
                )
                or 0,
                "summary": "".join(
                    selector.css(
                        ".tec--article__body p:first-child *::text"
                        ).getall() or ""
                ),
                "sources": [
                    source.strip()
                    for source in (selector.css(
                        ".z--mb-16 div a::text"
                        ).getall() or [])
                ],
                "categories": [
                    categorie.strip()
                    for categorie in (
                        selector.css(
                            "#js-categories a::text"
                        ).getall()
                        or []
                    )
                ],
            }
        )
    return arrayInfos


def scrape(searchPages):
    urlsDetails = request_links(searchPages)
    arrayInfos = create_infos(urlsDetails)
    mongo_save(arrayInfos)


pages = input("Qual o numero de paginas você deseja raspar?\n")
scrape(pages)
print("Raspagem de notícias finalizada")
