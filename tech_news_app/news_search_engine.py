import sys
from pymongo import MongoClient
from datetime import datetime


def search_by_title(title):
    with MongoClient() as connection:
        new_format = []
        db = connection["tech_news"]
        collection = db["scrapped_news"]
        answer = collection.aggregate([
            {"$match": {"title": {"$regex": title, "$options": "i"}}},
            {"$project": {"_id": 0, "title": "$title", "url": "$url"}}
        ])
        result = list(answer)
        for item in result:
            new_format.append(f"- {item['title']}: {item['url']}")
    return new_format


def search_by_date(date_user):
    date_format = "%Y-%m-%d"
    new_format = []
    try:
        isValid = datetime.strptime(date_user, date_format)
        date_string = str(isValid).split(" ")[0]
    except ValueError:
        print("Data inválida", file=sys.stderr)
        return
    else:
        with MongoClient() as connection:
            db = connection["tech_news"]
            collection = db["scrapped_news"]
            answer = collection.aggregate([
                {
                    "$match": {
                        "timestamp": {"$regex": date_string}
                    }
                },
                {"$project": {"_id": 0, "title": "$title", "url": "$url"}}
            ])
            result = list(answer)
            for item in result:
                new_format.append(f"- {item['title']}: {item['url']}")
        return new_format


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


# print(search_by_title("GOO"))
print(search_by_date("2020-10-05"))
