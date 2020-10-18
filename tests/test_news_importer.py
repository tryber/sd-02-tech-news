import pytest

from collector.news_importer import csv_importer

from tests.test_news_importer_fakers import (
    correct_file,
    duplicate_file,
    expected_return,
    incomplete_file,
    some_not_exist_file,
    wrong_fomart_file,
    wrong_header_file
)


def test_csv_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo wrong_file.csv não encontrado"):
        assert csv_importer(some_not_exist_file) is None


def test_csv_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        assert csv_importer(wrong_fomart_file) is None


def test_csv_importer_cabecalho_invalido():
    with pytest.raises(ValueError, match="Cabeçalho inválido"):
        assert csv_importer(wrong_header_file) is None


def test_csv_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        assert csv_importer(incomplete_file) is None


def test_csv_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        assert csv_importer(duplicate_file) is None


# def test_csv_importer_importacao_interrompida_em_caso_de_erro():
#     assert False


def test_csv_importer_sucesso():
    assert csv_importer(correct_file) == expected_return


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
