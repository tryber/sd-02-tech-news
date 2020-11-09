from database.index import find_new

from requests.exceptions import HTTPError

import parsel

import requests

CATEGORIES_SELECTOR = "#js-categories > a::text"

COMMENTS_COUNT = "#js-comments-btn::attr(data-count)"

SHARES_COUNT = ".tec--toolbar .tec--toolbar__item::text"

SOURCES_SELECTOR = "div.z--mb-16 > div a.tec--badge::text"

SUMARRY_SELECTOR = ".tec--article__body p:first-child *::text"

TIMESTAMP_SELECTOR = "#js-article-date::attr(datetime)"

TITLE_SELECTOR = "#js-article-title::text"

URL_BASE = "https://www.tecmundo.com.br/novidades"

URL_NEXT_PAGE = ".tec--btn.tec--btn--lg.tec--btn--primary.z--mx-auto.z--mt-48::attr(href)"

URL_SELECTOR = "h3.tec--card__title > a::attr(href)"

WRITER_SELECTOR = "a.tec--author__info__link::text"

available_fields = [
    "categories",
    "comments_count",
    "shares_count",
    "sources",
    "summary",
    "timestamp",
    "title",
    "url",
    "writer",
]

directory = "/home/anderson.bolivar/Documents/projects/sd-02-tech-news"

selectors = {
    "title": TITLE_SELECTOR,
    "timestamp": TIMESTAMP_SELECTOR,
    "writer": WRITER_SELECTOR,
    "shares_count": SHARES_COUNT,
    "comments_count": COMMENTS_COUNT,
    "summary": SUMARRY_SELECTOR,
    "sources": SOURCES_SELECTOR,
    "categories": CATEGORIES_SELECTOR
}


def check_extension(path, expected_extension):
    if expected_extension not in path:
        raise ValueError("Formato inválido")


def check_field(field, line):
    if not field:
        raise ValueError("Erro na notícia {}".format(line))


def check_fields(file_fields, err_message):
    if sorted(file_fields) != available_fields:
        raise ValueError(err_message)


def check_url(urls, url, line):
    urls.append(url)
    if urls.count(url) > 1:
        raise ValueError("Notícia {} duplicada".format(line))


def fetch_content(url, timeout=2000):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except HTTPError as http_err:
        raise ValueError("HTTP error occurred: {}".format(http_err))
    else:
        return response.text


def file_not_found(path):
    file = path.split("/").pop()
    return "Arquivo {} não encontrado".format(file)


def fill_news_data(news_data, data_row):
    new = find_new(data_row["url"])
    if not new:
        data_row["comments_count"] = int(data_row["comments_count"])
        data_row["shares_count"] = int(data_row["shares_count"])
        categories = data_row["categories"]
        sources = data_row["sources"]
        if type(categories) is str:
            data_row["categories"] = categories.split(",")
        if type(sources) is str:
            data_row["sources"] = sources.split(",")
        news_data.append(data_row)


def fill_news_field(obj, field, data):
    if field == "comments_count":
        obj[field] = int(data)
    elif field == "shares_count":
        obj[field] = int(data[1])
    elif field == "categories":
        obj[field] = [each.strip() for each in data]
    elif field == "sources":
        obj[field] = data.split()
    else:
        obj[field] = data


def get_field_data(field, selector, field_selector):
    if field == "categories":
        return selector.css(field_selector).getall()
    else:
        return selector.css(field_selector).get()


def get_next_page_url(content):
    selector = parsel.Selector(content)
    return selector.css(URL_NEXT_PAGE).get()


def get_urls(content):
    selector = parsel.Selector(content)
    return selector.css(URL_SELECTOR).getall()


def get_news(content, url):
    selector = parsel.Selector(content)
    obj = {"url": url}
    for field, field_selector in selectors.items():
        data = get_field_data(field, selector, field_selector)
        if data:
            fill_news_field(obj, field, data)
        else:
            obj = {}
            break
    return obj
