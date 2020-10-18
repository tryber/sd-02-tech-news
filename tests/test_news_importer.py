import pytest

from collector.news_importer import csv_importer


def test_csv_importer_arquivo_nao_existe():
    some_not_exist_file = "wrong_file.csv"

    with pytest.raises(ValueError):
        assert csv_importer(some_not_exist_file)


# def test_csv_importer_extensao_invalida():
#     assert False


# def test_csv_importer_cabecalho_invalido():
#     assert False


# def test_csv_importer_informacoes_incompletas():
#     assert False


# def test_csv_importer_urls_duplicadas():
#     assert False


# def test_csv_importer_importacao_interrompida_em_caso_de_erro():
#     assert False


# def test_csv_importer_sucesso():
#     assert False


# def test_json_importer_arquivo_nao_existe():
#     assert False


# def test_json_importer_extensao_invalida():
#     assert False


# def test_json_importer_json_invalido():
#     assert False


# def test_json_importer_informacoes_incompletas():
#     assert False


# def test_json_importer_urls_duplicadas():
#     assert False


# def test_json_importer_importacao_interrompida_em_caso_de_erro():
#     assert False


# def test_json_importer_sucesso():
#     assert False
