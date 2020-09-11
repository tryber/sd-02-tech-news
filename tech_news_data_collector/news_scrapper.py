import requests
from parsel import Selector


def get_title(selector):
    title = selector.css("h1#js-article-title::text").get()
    return title


def get_timestamp(selector):
    timestamp = selector.css(".tec--timestamp__item > time::attr(datetime)").get()
    return timestamp


def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    return writer


def get_shares_count(selector):
    shares_count = selector.css(".tec--toolbar__item::text").get()
    return shares_count


def get_summary(selector):
    summary = selector.css(".tec--article__body > p:first-child *::text").getall()
    return " ".join(summary)


def scrape():
    base_url = "https://www.tecmundo.com.br/novidades"

    page_text = requests.get(base_url).text
    page_selector = Selector(page_text)

    # news_details_url = page_selector.css("h3 > a::attr(href)").get()
    news_details_url_mock = "http://127.0.0.1:5501/Surface%20Duo%20ganha%20novo%20comercial%20focado%20na%20dobradi%C3%A7a%20-%20TecMundo.htm"
    news_details_text = requests.get(news_details_url_mock).text
    news_details_selector = Selector(news_details_text)

    title = get_title(news_details_selector).strip()
    timestamp = get_timestamp(news_details_selector)
    writer = get_writer(news_details_selector).strip()
    shares_count = get_shares_count(news_details_selector).strip()
    summary = get_summary(news_details_selector)

    return news_details_url_mock, title, timestamp, writer, shares_count, summary


print(scrape())
