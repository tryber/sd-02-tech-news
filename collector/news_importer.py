import csv


def file_not_found(path):
    return "Arquivo {} não encontrado".format(path)


# def check_extension(string):
#     extension = string.split(".").pop()

#     wrong_format = "Formato inválido"
#     if extension != "csv":
#         raise ValueError(wrong_format)


def csv_importer(csv_string):
    # check_extension(csv_string)

    try:
        '''
        encapsulamento da utilização de um recurso
        gerenciamento de contexto
        ações tomadas independente do status da resposta
        '''
        with open(csv_string) as csv_file:
            '''
            return a reader object
            which will iterate over lines
            in the given csvfile
            '''
            csv_reader = csv.reader(csv_file, delimiter=";")

            data = []

            for csv_row in csv_reader:
                data.append(csv_row)

    except(FileNotFoundError):
        raise ValueError(file_not_found(csv_string))

    return data


def json_importer():
    raise NotImplementedError
