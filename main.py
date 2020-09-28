from tech_news_app.news_search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

from tech_news_app.news_analyser import top_5_news, top_5_categories


print(search_by_title("ale"))
print(search_by_date("2020-07-20"))
print(search_by_source("the next web"))
print(search_by_category("carro"))
print(top_5_news())
print(top_5_categories())
