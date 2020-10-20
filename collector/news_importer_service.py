available_extensions = ("csv", "json")


def check_extension(string):
    extension = string.split(".").pop()

    wrong_format = "Formato inválido"

    if extension not in available_extensions:
        raise ValueError(wrong_format)


def check_field(field, line):
    if not field:
        raise ValueError("Erro na notícia {}".format(line))


def check_headers(file_headers, err_message):
    headers = [
        "url",
        "title",
        "timestamp",
        "writer",
        "shares_count",
        "comments_count",
        "summary",
        "sources",
        "categories"
    ]

    if file_headers != headers:
        raise ValueError(err_message)


def check_url(urls, url, line):
    if urls.count(url) > 0:
        raise ValueError("Notícia {} duplicada".format(line))


def file_not_found(path):
    return "Arquivo {} não encontrado".format(path)
