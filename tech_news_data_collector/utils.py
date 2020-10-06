def check_comparison(item, item_to_check, exception_message):
    if item != item_to_check:
        raise ValueError(exception_message)


correct_header = ['url', 'title', 'timestamp', 'writer', 'shares_count',
                  'comments_count', 'summary', 'sources', 'categories']
