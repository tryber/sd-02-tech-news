from tech_news_data_collector.news_scrapper import scrape
from tech_news_data_collector.news_importer import csv_importer
from tech_news_app.news_search_engine import search_by_title, search_by_source

csv_importer('exported.csv')
scrape(1)
search_by_title('coisa')
search_by_source('source')
