from pymongo import MongoClient
import sys


def news_to_database(array_news):
    client = MongoClient()
    db = client.tech_news_test  # determina o banco de dados
    for new in array_news:
        db.news_collection.find_one_and_replace(
            {"url": new["url"]},
            {
                "url": new["url"],
                "title": new["title"],
                "timestamp": new["timestamp"],
                "writer": new["writer"],
                "shares_count": new["shares_count"],
                "comments_count": new["comments_count"],
                "summary": new["summary"],
                "sources": new["sources"],
                "categories": new["categories"],
            },
            upsert=True,
        )


def find_duplicate(array_news):
    client = MongoClient()
    db = client.tech_news_test  # determina o banco de dados
    line = 1
    for new in array_news:
        duplicate = db.news_collection.find_one({"url": new["url"]})
        if duplicate:
            return line
        line += 1

def export_to_csv():
    client = MongoClient()
    db = client.tech_news_test  # determina o banco de dados
    all_news = db.news_collection.find({}, {"_id": 0})
    # list_all_news = []
    # for new in all_news:
    #     new_dict = dict()
    #     new_dict["url"] = new["url"]
    #     new_dict["title"] = new["title"]
    #     new_dict["timestamp"] = new["timestamp"]
    #     new_dict["writer"] = new["writer"]
    #     new_dict["shares_count"] = new["shares_count"]
    #     new_dict["comments_count"] = new["comments_count"]
    #     new_dict["summary"] = new["summary"]
    #     new_dict["sources"] = ", ".join(new['sources'])
    #     new_dict["categories"] = ", ".join(new["categories"])
    #     list_all_news.append(new_dict)
    return all_news
