import requests
from parsel import Selector
import re
from mongo_connection import insert_news_scrapper


def fetch_content(url, timeout=2):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout) as exc:
        print(exc)
        return ""
    else:
        return response.text


def get_title_or_writer(selector, css_selector):
    result = selector.css(css_selector).get()
    return result and result.strip()


def get_timestamp(selector):
    timestamp = selector.css(
        ".tec--timestamp__item > time::attr(datetime)"
    ).get()
    return timestamp


def get_shares_count(selector):
    shares_count = selector.css(
        ".tec--toolbar__item:first-child *::text"
    ).re_first(r"\d") or 0
    return int(shares_count)


def get_comments_count(selector):
    comments_count = selector.css(
        ".tec--toolbar__item:nth-child(2) > button *::text"
    ).re_first(r"\d") or 0
    return int(comments_count)


def get_summary(selector):
    summary = " ".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    return re.sub("\\n|\\xa0", "", summary)


def get_categories_or_sources(selector, css_selector):
    result = selector.css(css_selector).getall()
    result_list = []
    for item in result:
        result_list.append(item.strip())
    return result_list


def extract_news(url, selector):
    news_info = dict()
    news_info["url"] = url
    news_info["title"] = get_title_or_writer(
        selector, "h1#js-article-title::text"
    )
    news_info["timestamp"] = get_timestamp(selector)
    news_info["writer"] = get_title_or_writer(
        selector, ".tec--author__info__link::text"
    )
    news_info["shares_count"] = get_shares_count(selector)
    news_info["comments_count"] = get_comments_count(selector)
    news_info["summary"] = get_summary(selector)
    news_info["sources"] = get_categories_or_sources(
        selector, ".z--mb-16 > div > a::text"
    )
    news_info["categories"] = get_categories_or_sources(
        selector, "#js-categories > a::text"
    )
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
        print(f"raspagem da página {count} em andamento")
        for news_details_url in news_urls:
            news_details_text = fetch_content(news_details_url)
            news_details_selector = Selector(news_details_text)
            news = extract_news(news_details_url, news_details_selector)
            all_news.append(news)
        print(f"dados da página {count} raspados")
        next_page_url = page_selector.css(".tec--btn::attr(href)").get()
        count += 1

    insert_news_scrapper(all_news)
    print("Raspagem de notícias finalizada")
    return all_news


scrape(2)
