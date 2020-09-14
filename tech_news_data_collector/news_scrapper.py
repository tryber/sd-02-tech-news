import parsel
import requests
import time
import re
from mongo_connection import db

base_url = 'https://www.tecmundo.com.br/novidades'


def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        time.sleep(2)
    except (requests.HTTPError or requests.ReadTimeout) as exc:
        print(exc, file = sys.stderr)
        return
    else:
        return response.text


def stringFormatter(str):
    whithoutN = re.sub('\\n', '', str)
    return re.sub('\s{2,}', '', whithoutN)


def scrape_page_new(page_url):
    new_page = fetch_content(page_url)
    selector = parsel.Selector(new_page)

    title = stringFormatter(selector.css("#js-article-title::text").get() or '')
    timestamp = stringFormatter(selector.css("div.tec--timestamp__item > time > strong::text").get() or '')
    writer = stringFormatter(selector.css("#js-author-bar p.z--m-none > a::text").get() or '')
    shares_count = selector.css("#js-author-bar div.tec--toolbar__item::text").re_first(r"\d" or 0)
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d" or 0)
    categories = list(map(stringFormatter, selector.css("#js-categories a::text").getall()))
    sources = list(map(stringFormatter, selector.css("#js-main div.z--mb-16.z--px-16 a::text").getall()))
    summary = selector.css("div.tec--article__body > p:first-child *::text").getall()
    summary = ''.join(summary)

    return {
      'title': title,
      'timestamp': timestamp,
      'writer': writer,
      'summary': summary,
      'shares_count': shares_count,
      'comments_count': comments_count,
      'sources': sources,
      'categories': categories,
    }



def find(url):
    if db().pages.find_one({ 'url': url }):
        return True
    return False


def insert(url, obj):
    obj['url'] = url
    db().pages.insert_one(obj)


def delete(url, obj):
    db().pages.delete_one({ 'url': url })


def scrape_main_page(url):
    main_page = fetch_content(url)
    selector = parsel.Selector(main_page)
    pages_url = selector.css("div.tec--list__item figure.tec--card__thumb > a::attr(href)").getall()

    for page_url in pages_url:
        obj = scrape_page_new(page_url)
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
        print('main_page', main_page)
        selector = parsel.Selector(main_page)
        main_url = selector.css('div.tec--list > a.tec--btn::attr(href)').get()
    print('Raspagem de notícias finalizada')
