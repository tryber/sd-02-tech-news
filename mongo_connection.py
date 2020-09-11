from pymongo import MongoClient

def db():
  client = MongoClient()
  return client.tech_news
