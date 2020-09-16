from parsel import Selector
import requests

def req_answer():
    with open('tech_news_data_collector/Novidades - TecMundo.html') as page:
        return page.read()

def fetch_content(url, timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError) as exc:
        print(exc)
        return ''
    else:
        return response.text
    
def scrape(n = 1):
    response = req_answer()
    selector = Selector(response)
    titles = selector.css("h3 .tec--card__title__link::attr(href)").getall()
    for link in titles:
        url = link
        print(url)
        single_new = fetch_content('http://127.0.0.1:5500/tech_news_data_collector/Surface%20Duo%20ganha%20novo%20comercial%20focado%20na%20dobradi%C3%A7a%20-%20TecMundo.html')
        # single_new = requests.get('http://127.0.0.1:5500/tech_news_data_collector/Surface%20Duo%20ganha%20novo%20comercial%20focado%20na%20dobradi%C3%A7a%20-%20TecMundo.html')
        # selector = Selector(single_new.text)
        title = selector.css(".tec--article__header__title::text").get()
        print(title)
        # print(title.strip()) # isso aqui pega o título
        timestamp = selector.css("time::attr(datetime)").get()
        print(timestamp)
        writer = selector.css(".tec--author__info__link::text").get()
        # print(writer.strip())
        shares_count = selector.css(".tec--toolbar__item:first-child *::text").re_first(r"\d") or 0
        # print(int(shares_count))
        comments_count = selector.css(".tec--toolbar__item:nth-child(2) > button *::text").re_first(r"\d") or 0
        # print(int(comments_count))
        summary = selector.css(".tec--article__body p:first-child *::text").getall()
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
    print("Raspagem de notícias finalizada")

scrape()
