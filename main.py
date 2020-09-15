from tech_news_app.news_search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

from tech_news_app.news_analyser import top_5_news, top_5_categories


search_by_title("CELULAr")
search_by_date("2020-09-14")
search_by_source("The next Web")
search_by_category("Carro")
top_5_news()
top_5_categories()
