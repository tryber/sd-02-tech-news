import csv


def csv_importer(csv_string):
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

        return data

    raise NotImplementedError


def json_importer():
    raise NotImplementedError
