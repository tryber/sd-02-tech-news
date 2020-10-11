from parsel import Selector
import requests
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
    # return news_info
    print(news_info)


def fetch_single_new(url):
    single_new = fetch_content(url)
    selector = Selector(single_new)
    title = selector.css("h1#js-article-title::text").get()
    # print(title.strip())
    # print(title.strip()) # isso aqui pega o título
    timestamp = selector.css("time::attr(datetime)").get()
    # print(timestamp)
    writer = selector.css(".tec--author__info__link::text").get() or ''
    # print(writer.strip())
    shares_count = selector.css(
        ".tec--toolbar__item:first-child *::text").re_first(r"\d") or 0
    # print(int(shares_count))
    comments_count = selector.css(
        ".tec--toolbar__item:nth-child(2)"
        " > button *::text").re_first(r"\d") or 0
    # print(int(comments_count))
    summary = selector.css(
        ".tec--article__body p:first-child *::text").getall()
    # print(''.join(summary))

    def strip_list(src):
        sources_list = []
        for source in src:
            sources_list.append(source.strip())
        return sources_list
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    # print(strip_list(sources))
    categories = selector.css("#js-categories > a::text").getall()
    # print(strip_list(categories))
    single_new_to_dict(url, title, timestamp, writer.strip(),
                       int(shares_count),
                       int(comments_count), ''.join(summary),
                       strip_list(sources), strip_list(categories))


def scrape(n=1):
    base_url = "https://www.tecmundo.com.br/novidades"

    all_news = []

    next_page_url = base_url

    count = 1

    while next_page_url and count <= n:
        response = fetch_content(next_page_url)
        selector = Selector(text=response)
        titles = selector.css("h3 > a::attr(href)").getall()
        print(titles)
        for link in titles:
            url = link
            # print(url)
            fetch_single_new(url)

        sleep(2)
        next_page_url = selector.css(".tec--btn::attr(href)").get()
        count += 1
    print("Raspagem de notícias finalizada")


scrape()
