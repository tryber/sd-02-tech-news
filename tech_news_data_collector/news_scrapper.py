import parsel
import requests
import time
from pymongo import MongoClient


def get_simple_text(selector, selector_attributes):
    return selector.css(selector_attributes).get() or ''


def save_db(dict_new_detail):
    with MongoClient() as client:
        db = client.web_scrape_python
        db.news_collection.find_one_and_replace(
            {'url': dict_new_detail['url']},
            dict_new_detail, upsert=True)


def get_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(1)
    except requests.HTTPError:
        return ""
    else:
        return response.text


def fix_line_breaks(string):
    return [item_list.strip() for item_list in string
            if len(item_list.strip()) > 0]


def get_news_details(url, total, current):
    new_detailed = {}

    content = get_urls(url)
    selector = parsel.Selector(content)

    new_detailed['url'] = url

    title = get_simple_text(selector, "#js-article-title ::text")
    new_detailed['title'] = title.strip()

    new_detailed['datetime'] = get_simple_text(selector,
                                               ".tec--timestamp__item time \
                                               ::attr(datetime)")

    writer = get_simple_text(selector, ".tec--author__info__link ::text")
    new_detailed['writer'] = writer.strip()

    if len(selector.css("div.tec--toolbar__item").getall()) == 2:
        share, comments_count = selector.css(
                                   "div.tec--toolbar__item ::text").re(r'\d+')
    else:
        comments_count = get_simple_text(selector, "#js-comments-btn \
                                         ::attr(data-count)")
        share = '0'
    new_detailed['comments_count'] = comments_count
    new_detailed['share'] = share
    new_detailed['summary'] = ''.join(selector.css(".tec--article__body > \
                                    p:first_child *::text").getall()) or ''

    source = ''.join(selector.css(".z--mb-16 a ::text"
                                  ).getall()).strip().split('\n')
    source = fix_line_breaks(source)
    new_detailed['sources'] = source

    categories = selector.css("#js-categories a ::text").getall() or ''
    categories = fix_line_breaks(categories)
    new_detailed['categories'] = categories

    print(f'processando...{current} de {total}')
    time.sleep(1)

    return new_detailed


def scrape(n=1):
    base_url = 'https://www.tecmundo.com.br/novidades?page='
    urls_to_scrape = []

    for number in range(1, n + 1):
        content = get_urls(f"{base_url}/{number}")
        selector = parsel.Selector(content)
        news_urls = selector.css(".tec--list--lg \
                                 .tec--list__item \
                                 .tec--card__thumb__link \
                                 ::attr(href)"
                                 ).getall()

        for img_url in news_urls:
            urls_to_scrape.append(img_url)

    for url in urls_to_scrape:
        save_db(get_news_details(url,
                                 len(urls_to_scrape),
                                 urls_to_scrape.index(url) + 1))
    print('Raspagem de notícias finalizada')


scrape(1)
