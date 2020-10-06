pipeline = [
  {
    "$unwind": '$categories'
  },
  {
    '$group': {
      '_id': '$categories',
      'quantity': { $sum: 1 }
    }
  },
  {
    '$sort': {
      'quantity': - 1
    }
  },
  {
    '$limit': 5
  },
  {
    '$sort': {
      '_id': 1
    }
  },
]

pipeline = [
  {
    "$unwind": '$categories'
  },
  {
    '$group': {
      '_id': '$categories',
      'quantity': { $sum: 1 }
    }
  },
  {
    '$sort': {
      'quantity': - 1
    }
  }
]