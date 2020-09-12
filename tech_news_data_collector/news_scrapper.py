import requests
from parsel import Selector
import re
from mongo_connection import insert_news


def fetch_content(url, timeout=2):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout) as exc:
        print(exc)
        return ""
    else:
        return response.text


def get_title(selector):
    title = selector.css("h1#js-article-title::text").get()
    return title and title.strip()


def get_timestamp(selector):
    timestamp = selector.css(
        ".tec--timestamp__item > time::attr(datetime)"
    ).get()
    return timestamp


def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    return writer and writer.strip()


def get_shares_count(selector):
    shares_count = selector.css(
        ".tec--toolbar__item:first-child *::text"
    ).re_first(r"\d")
    return shares_count


def get_comments_count(selector):
    comments_count = selector.css(
        ".tec--toolbar__item:nth-child(2) > button *::text"
    ).re_first(r"\d")
    return comments_count


def get_summary(selector):
    summary = " ".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    return re.sub("\\n|\\xa0", "", summary)


def get_sources(selector):
    sources = selector.css(".z--mb-16 > div > a::text").getall()
    sources_list = []
    for source in sources:
        sources_list.append(source.strip())
    return ", ".join(sources_list)


def get_categories(selector):
    categories = selector.css("#js-categories > a::text").getall()
    categories_list = []
    for category in categories:
        categories_list.append(category.strip())
    return ", ".join(categories_list)


def extract_news(url, selector):
    news_info = dict()
    news_info["url"] = url
    news_info["title"] = get_title(selector)
    news_info["timestamp"] = get_timestamp(selector)
    news_info["writer"] = get_writer(selector)
    news_info["shares_count"] = get_shares_count(selector)
    news_info["comments_count"] = get_comments_count(selector)
    news_info["summary"] = get_summary(selector)
    news_info["sources"] = get_sources(selector).strip()
    news_info["categories"] = get_categories(selector)
    return news_info


def scrape(n=1):
    base_url = "https://www.tecmundo.com.br/novidades"

    all_news = []

    next_page_url = base_url

    count = 1

    while next_page_url and count <= n:
        page_text = fetch_content(next_page_url)
        page_selector = Selector(page_text)
        news_urls = page_selector.css("h3 > a::attr(href)").getall()
        for news_details_url in news_urls:
            news_details_text = fetch_content(news_details_url)
            news_details_selector = Selector(news_details_text)
            news = extract_news(news_details_url, news_details_selector)
            all_news.append(news)
        next_page_url = page_selector.css(".tec--btn::attr(href)").get()
        count += 1

    insert_news(all_news)
    print("Raspagem de notícias finalizada")
    return all_news


print(scrape(2))
