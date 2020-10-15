import csv


def csv_reader(csv_string):
    '''
    encapsulamento da utilização de um recurso
    gerenciamento de contexto
    ações tomadas independente do status da resposta
    '''

    with open(csv_string) as csv_file:
        '''
        Create an object
        that operates like a regular reader
        but maps the information in each row
        to a dict
        whose keys are given by the optional fieldnames parameter
        '''

        csv_reader = csv.DictReader(csv_file, delimiter=";")


def csv_importer():

    raise NotImplementedError


def json_importer():
    raise NotImplementedError
