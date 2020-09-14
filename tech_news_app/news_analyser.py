from mongo_connection import db


def top_5_news():
  news = db().pages.aggregate([
    {
      $addFields: {
        total: {
          $sum: [
            { $toInt: "$comments_count" },
            { $toInt: "$shares_count" }
          ]
        },
      }
    },
    {
      $sort: { title: 1 }
    },
    {
      $limit: 5
    },
    {
      $project: {
        _id: 0,
        title: 1,
        url: 1,
      }
    }
  ])
  return list(news)


def top_5_categories():

