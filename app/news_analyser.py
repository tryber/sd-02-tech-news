from database.index import aggregate_news


def top_5_news():
    query = [{"$project": {"url": 1, "title": 1, "orderBySum": {
        "$add": ["$shares_count", "$comments_count"]}}},
        {"$sort": {"orderBySum": -1, "title": 1}}, {"$limit": 5}]
    news = aggregate_news(query)
    news_list = []
    for each in news:
        new = str("- " + each["title"] + ": " + each["url"])
        news_list.append(new)
    return news_list


def top_5_categories():
    query = [{"$unwind": "$categories"}, {"$group": {"_id": "$categories",  "frequency": {"$sum": 1}}},
             {"$sort": {"frequency": -1, "_id": 1}},
             {"$limit": 5}]
    news = aggregate_news(query)
    news_list = []
    for each in news:
        new = str("- " + each["_id"])
        news_list.append(new)
    return news_list
