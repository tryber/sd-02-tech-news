from tech_news_data_collector.news_scrapper import scrape
from tech_news_data_collector.news_importer import csv_importer, json_importer
from tech_news_data_collector.news_exporter import csv_exporter
from tech_news_app.news_search_engine import search_by_date
from tech_news_app.news_analyser import top_5_categories


# print(top_5_categories())
# csv_importer('mock/arquivo.csv')
# scrape(1)
print(top_5_categories())
