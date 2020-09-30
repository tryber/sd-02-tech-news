from tech_news_data_collector.news_scrapper import scrape

from tech_news_data_collector.news_importer import csv_importer, json_importer

from tech_news_data_collector.news_exporter import csv_exporter, json_exporter

from tech_news_app.news_search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

from tech_news_app.news_analyser import top_5_news, top_5_categories

scrape(2)

csv_importer("./news_files_mocks/news.csv")
csv_exporter("news.csv")

json_importer("./news_files_mocks/news.json")
json_exporter("news.json")

search_by_title("Série")
search_by_date("2020-09-29")
search_by_source("push Square")
search_by_category("voxel")
top_5_news()
top_5_categories()
