import sys
from pymongo import MongoClient
from datetime import date


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
    try:
        isValid = date.fromisoformat('1999-08-10')
    except ValueError:
        print("Data inválida", file=sys.stderr)
        return
    else:
        return isValid


def search_by_source():
    raise NotImplementedError


def search_by_category():
    raise NotImplementedError


# print(search_by_title("GOO"))
print(search_by_date('1999-08-10'))
