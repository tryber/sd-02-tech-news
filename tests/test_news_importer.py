import pytest

from unittest.mock import patch

from contextlib import suppress

from collector.news_importer import csv_importer

from tests.test_news_importer_fakers import (
    data_mock,
    correct_file,
    duplicate_file,
    incomplete_file,
    some_not_exist_file,
    wrong_fomart_file,
    wrong_header_file
)


def test_csv_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo wrong_file.csv não encontrado"):
        csv_importer(some_not_exist_file) is None


def test_csv_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        csv_importer(wrong_fomart_file)


def test_csv_importer_cabecalho_invalido():
    with pytest.raises(ValueError, match="Cabeçalho inválido"):
        csv_importer(wrong_header_file)


def test_csv_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        csv_importer(incomplete_file)


def test_csv_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        csv_importer(duplicate_file)


def test_csv_importer_importacao_interrompida_em_caso_de_erro():
    with patch("database.store.store_news") as store_news_mock:
        with suppress(ValueError):
            csv_importer(duplicate_file)
            store_news_mock.assert_not_called()


# @patch("database.store.store_news")
# def test_csv_importer_importacao_interrompida_em_caso_de_erro_decorador(capsys, monkeypatch):
#     with suppress(ValueError):
#         csv_importer(duplicate_file)
#         monkeypatch.assert_not_called()


# @patch("database.store.store_news")
# def test_csv_importer_sucesso_decorador(capsys, monkeypatch):

#     csv_importer(correct_file)

#     out, _ = capsys.readouterr()

#     assert out == "Exportação realizada com sucesso\n"


def test_csv_importer_sucesso(capsys):
    with patch("database.store.store_news") as store_news_mock:
        csv_importer(correct_file)
        out, err = capsys.readouterr()
        assert out == "Exportação realizada com sucesso\n"
        # store_news_mock.assert_called_with(data_mock)


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
