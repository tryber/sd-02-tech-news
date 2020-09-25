import requests
from parsel import Selector

user_agent = (
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.4183.83 Safari/537.36 "
)

info_headers = {"User-agent": user_agent, "Accept": "text/html"}

next_page_url = ''


def scrape():
    response = requests.get('https://www.tecmundo.com.br/novidades/', timeout=2, headers=info_headers)
    selector = Selector(text=response.text)
    # titles = selector.css(".tec--card__title__link::text").getall()
    count = 1
    next_page_url = selector.css(".tec--list a.tec--btn::attr(href)").get()
    print(next_page_url)
    # for title in selector.css("h3.tec--card__title a.tec--card__title__link::attr(href)"):
    #     print(title.get())
    #     count += 1


scrape()
