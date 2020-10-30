import requests
import parsel
from requests.exceptions import HTTPError

URL_BASE = "https://www.tecmundo.com.br/novidades"

URL_SELECTOR = "h3.tec--card__title > a::attr(href)"

TITLE_SELECTOR = "#js-article-title::text"

TIMESTAMP_SELECTOR = "#js-article-date::attr(datetime)"

WRITER_SELECTOR = "a.tec--author__info__link::text"
# not done
SHARES_COUNT = ".tec--toolbar .tec--toolbar__item::text"

COMMENTS_COUNT = "#js-comments-btn::attr(data-count)"
# not done
SUMARRY_SELECTOR = ".tec--article__body p:first-child *::text"

SOURCES_SELECTOR = "div.z--mb-16 > div a.tec--badge::text"

CATEGORIES_SELECTOR = "#js-categories > a::text"

available_fields = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]

directory = "/home/anderson.bolivar/Documents/projects/sd-02-tech-news"

headers = [
    {"name": "url", "selector": URL_SELECTOR},
    {"name": "title", "selector": TITLE_SELECTOR},
    {"name": "timestamp", "selector": TIMESTAMP_SELECTOR},
    {"name": "writer", "selector": WRITER_SELECTOR},
    {"name": "shares_count", "selector": SHARES_COUNT},
    {"name": "comments_count", "selector": COMMENTS_COUNT},
    {"name": "summary", "selector": SUMARRY_SELECTOR},
    {"name": "sources", "selector": SOURCES_SELECTOR},
    {"name": "categories", "selector": CATEGORIES_SELECTOR}
]


def check_extension(path, expected_extension):
    current_extension = path.split(".").pop()
    if current_extension != expected_extension:
        raise ValueError("Formato inválido")


def check_field(field, line):
    if not field:
        raise ValueError("Erro na notícia {}".format(line))


def check_fields(file_fields, err_message):
    if file_fields != available_fields:
        raise ValueError(err_message)


def check_url(urls, url, line):
    if urls.count(url) > 0:
        raise ValueError("Notícia {} duplicada".format(line))


def file_not_found(path):
    file = path.split("/").pop()

    return "Arquivo {} não encontrado".format(file)


def get_urls(content):
    selector = parsel.Selector(content)

    return selector.css(URL_SELECTOR).getall()


def fetch_content(url, timeout=1000):
    try:
        # Conferir timeout
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except HTTPError as http_err:
        raise ValueError("HTTP error occurred: {}".format(http_err))
    else:
        return response.text


def get_field_data(field, selector, selector_string):
    if field == "categories":
        return selector.css(selector_string).getall()
    else:
        return selector.css(selector_string).get()


def fill_object(obj, field, data):
    if field == "comments_count":
        obj[field] = int(data)
    elif field == "shares_count":
        obj[field] = int(data[1])
    elif field == "categories":
        obj[field] = [each.strip() for each in data]
    else:
        obj[field] = data


def get_news(content, url):
    selector = parsel.Selector(content)

    obj = {"url": url}

    fields = headers.copy()

    fields.pop(0)

    for element in fields:
        field = element["name"]
        selector_string = element["selector"]
        data = get_field_data(field, selector, selector_string)
        if data:
            fill_object(obj, field, data)
        else:
            obj = {}
            break

    return obj
