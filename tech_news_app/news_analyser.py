from pymongo import MongoClient


def print_content(findForText):
    boolean = True
    for index, content in enumerate(findForText):
        if index == 5:
            break
        boolean = False
        print([f'- {content["title"]}: {content["url"]}'])
        print(content["shares_count"], content["comments_count"])
    if boolean:
        print([])


def mongoQuery():
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["tech_news"]
        findForText = db["news"].aggregate(
            [
                {
                    "$project": {
                        "title": 1,
                        "url": 1,
                        "_id": 0,
                        "shares_count": 1,
                        "comments_count": 1,
                    }
                },
            ]
        )
    return findForText


# def get_my_key(obj):
#     return int(obj["shares_count"]) + int(obj["comments_count"])


# def get_my_scond_key(obj):
#     return obj["title"]


def top_5_news():
    results = mongoQuery()
    newarray = [result for result in results]
    # (newarray.sort(key=get_my_key, reverse=True))
    newarray = sorted(
        newarray,
        key=lambda x: ((int(x["shares_count"]) + int(x["comments_count"])), x["title"]),
        reverse=True
    )
    
    print_content(newarray)


def top_5_categories():
    raise NotImplementedError


top_5_news()