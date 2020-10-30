import requests
import time
import sys
import parsel
from mongo_connection import tech_news_db


base_url = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(4)
    except (requests.HTTPError or requests.ReadTimeout) as exc:
        print(exc, file=sys.stderr)
        return
    else:
        return response.text


def string_formatter(str):
    return str.strip()


def create_title(selector):
    return (
        selector.css("#js-article-title::text").get() or ""
    )


def create_timestamp(selector):
    return string_formatter(
        selector.css("div.tec--timestamp__item > time::attr(datetime)").get()
        or ""
    )


def create_writer(selector):
    string_formatter(
        selector.css("#js-author-bar p.z--m-none > a::text").get() or ""
    )


def create_summary(selector):
    return "".join(
        selector.css("div.tec--article__body > p:first-child *::text").getall()
    )


def create_shares_count(selector):
    return selector.css(
        "#js-author-bar div.tec--toolbar__item::text"
    ).re_first(r"\d+") or 0


def create_comments_count(selector):
    return selector.css("#js-comments-btn::text").re_first(r"\d+") or 0


def create_sources(selector):
    return list(
        map(
            string_formatter,
            selector.css("#js-main div.z--mb-16.z--px-16 a::text").getall(),
        )
    )


def create_categories(selector):
    return list(
        map(
            string_formatter,
            selector.css("#js-categories a::text").getall(),
        )
    )


def scrape_page_new(page_url):
    new_page = fetch_content(page_url)
    selector = parsel.Selector(new_page)

    return {
        "title": create_title(selector),
        "timestamp": create_timestamp(selector),
        "writer": create_writer(selector),
        "summary": create_summary(selector),
        "shares_count": int(create_shares_count(selector)),
        "comments_count": int(create_comments_count(selector)),
        "sources": create_sources(selector),
        "categories": create_categories(selector),
    }


def find(url):
    if tech_news_db().pages.find_one({"url": url}):
        return True
    return False


def insert(url, obj):
    obj["url"] = url
    tech_news_db().pages.insert_one(obj)


def delete(url, obj):
    tech_news_db().pages.delete_one({"url": url})


def scrape_main_page(url):
    main_page = fetch_content(url)
    selector = parsel.Selector(main_page)
    pages_url = selector.css(
        "div.tec--list__item figure.tec--card__thumb > a::attr(href)"
    ).getall()

    for page_url in pages_url:
        obj = scrape_page_new(page_url)
        print(obj)
        if find(page_url):
            insert(page_url, obj)
        else:
            delete(page_url, obj)
            insert(page_url, obj)


def scrape(N=1):
    main_url = base_url
    for i in range(N):
        scrape_main_page(main_url)
        main_page = fetch_content(main_url)
        print(main_page)
        selector = parsel.Selector(main_page)
        main_url = selector.css("div.tec--list > a.tec--btn::attr(href)").get()
    print("Raspagem de notícias finalizada")
