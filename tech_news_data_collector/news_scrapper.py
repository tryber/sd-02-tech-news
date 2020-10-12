from parsel import Selector
import requests
from mongo_connection import news_to_database
from time import sleep


def req_answer():
    with open('tech_news_data_collector/Novidades - TecMundo.html') as page:
        return page.read()


def fetch_content(url, timeout=2):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError) as exc:
        print(exc)
        return ''
    else:
        return response.text


def single_new_to_dict(
        url,
        title,
        timestamp,
        writer,
        shares_count,
        comments_count,
        summary, sources,
        categories):
    news_info = dict()
    news_info["url"] = url
    news_info["title"] = title
    news_info["timestamp"] = timestamp
    news_info["writer"] = writer
    news_info["shares_count"] = shares_count
    news_info["comments_count"] = comments_count
    news_info["summary"] = summary
    news_info["sources"] = sources
    news_info["categories"] = categories
    return news_info


def fetch_single_new(url):
    single_new = fetch_content(url)
    selector = Selector(single_new)
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get() or ''
    shares_count = selector.css(
        ".tec--toolbar__item:first-child *::text").re_first(r"\d") or 0
    comments_count = selector.css(
        ".tec--toolbar__item:nth-child(2)"
        " > button *::text").re_first(r"\d") or 0
    summary = selector.css(
        ".tec--article__body p:first-child *::text").getall()

    def strip_list(src):
        sources_list = []
        for source in src:
            sources_list.append(source.strip())
        return sources_list
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories > a::text").getall()
    dict_new = single_new_to_dict(url, title, timestamp, writer.strip(),
                                  int(shares_count),
                                  int(comments_count), ''.join(summary),
                                  strip_list(sources), strip_list(categories))
    return dict_new


def scrape(n=1):
    base_url = "https://www.tecmundo.com.br/novidades"

    all_news = []

    next_page_url = base_url

    count = 1

    while next_page_url and count <= n:
        response = fetch_content(next_page_url)
        selector = Selector(text=response)
        print(f'Raspagem da página {count} em andamento')
        titles = selector.css("h3 > a::attr(href)").getall()
        for link in titles:
            url = link
            single_new = fetch_single_new(url, count)
            all_news.append(single_new)
        sleep(2)
        next_page_url = selector.css(".tec--btn::attr(href)").get()
        count += 1
    news_to_database(all_news)
    print("Raspagem de notícias finalizada")


scrape()
