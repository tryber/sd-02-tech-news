from parsel import Selector
import requests
import time


def scrape(n=1):
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    # Define a primeira página como próxima a ter seu conteúdo recuperado
    next_page_url = URL_BASE
    print(n)

    for i in range(n):
        print('olaa', i)
        # Busca o conteúdo da próxima página
        response = requests.get(next_page_url, timeout=10)
        time.sleep(6)
        selector = Selector(text=response.text)
        # Imprime as notícias de uma determinada página
        for news in selector.css(".tec--list__item"):
            # Busca e extrai o título e timestamp?????????????????????????????????????????
            title = news.css("h3 a::text").get()
            # price = product.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")
            print(title)

            # Busca o detalhe de uma notícia
            detail_page_url = news.css(".tec--card__title__link::attr(href)").get()
            print(detail_page_url)
            outra_url = "https://www.tecmundo.com.br/dispositivos-moveis/177596-surface-duo-ganha-novo-comercial-focado-dobradica.htm"

            # Baixa o conteúdo da página de detalhes
            detail_response = requests.get(outra_url, timeout=10)
            time.sleep(6)
            detail_selector = Selector(text=detail_response.text)

            # Extrai detalhes do produto
            timestamp = detail_selector.css("time::attr(datetime)").get()
            print(timestamp)
            writer = detail_selector.css(".tec--author__info__link::text").get()
            print(writer)
            shares_count = detail_selector.css(".tec--toolbar__item::text").re(
                "[0-9]+"
            )[0]
            print(shares_count)
            comments_count = detail_selector.css("#js-comments-btn::text").re("[0-9]+")[
                0
            ]
            print(comments_count)

            # summary, sources, categories??W??????w?w???w????d????w?wwwwwwwwwwwwwwwwwwwwwwwwwww????wW??????wwW??????wwwww
            summary = "".join(
                detail_selector.css(".tec--article__body p")[0].css("*::text").getall()
            )
            print(summary)
            sources = detail_selector.css(".z--mb-16.z--px-16 a::text").re("[A-zÀ-ÿ][A-zÀ-ÿ' ]+")
            print(sources)
            categories = detail_selector.css("#js-categories a::text").re("[A-zÀ-ÿ][A-zÀ-ÿ' ]+")
            print(categories)

            # description = detail_selector.css("#product_description ~ p::text").get()
            # suffix = "...more"
            # if description.endswith(suffix):
            # description = description[: -len(suffix)]
            # print(description)

        # Descobre qual é a próxima página
        print('antes', next_page_url)
        next_page_url = selector.css(
            ".tec--list--lg .tec--btn--primary::attr(href)"
        ).get()
        print('depois', next_page_url)


# print('sem parametro')
# scrape()
# print('parametro 1')
# scrape(1)
# print('parametro 2')
# scrape(2)
print('parametro 3')
scrape(3)
