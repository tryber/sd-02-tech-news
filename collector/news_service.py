available_extensions = ("csv", "json")

exported_directory = "/home/anderson.bolivar/Documents/projects/sd-02-tech-news"

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


def check_extension(string):
    extension = string.split(".").pop()

    wrong_format = "Formato inválido"

    if extension not in available_extensions:
        raise ValueError(wrong_format)


def check_field(field, line):
    if not field:
        raise ValueError("Erro na notícia {}".format(line))


def check_headers(file_headers, err_message):
    if file_headers != headers:
        raise ValueError(err_message)


def check_url(urls, url, line):
    if urls.count(url) > 0:
        raise ValueError("Notícia {} duplicada".format(line))


def file_not_found(path):
    file = path.split("/").pop()

    return "Arquivo {} não encontrado".format(file)


def remove_id(row):
    row.pop("_id")
    return row
