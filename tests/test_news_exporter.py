import pytest

from unittest.mock import patch

from collector.news_exporter import (csv_exporter)

from tests.test_news_fakers import (
    data_mock,
    correct_csv,
    correct_json,
    duplicate_csv,
    duplicate_json,
    incomplete_csv,
    incomplete_json,
    not_exists_csv,
    not_exists_json,
    wrong_fomart_file,
    wrong_header_file,
    wrong_json,
    wrong_data
)

import os


def test_csv_exporter_extensao_invalida():
    with patch("collector.news_exporter.find_news"):
        with pytest.raises(ValueError, match='Formato inválido'):
            csv_exporter("file.txt")


def test_csv_exporter_cria_arquivo_na_raiz():
    with patch("collector.news_exporter.find_news"):
        csv_exporter("not_exists.csv")
        assert os.path.exists("not_exists.csv") is True
        os.remove("not_exists.csv")


def test_csv_exporter_substitui_arquivo_existente():
    with patch("collector.news_exporter.find_news"):
        if os.path.exists(correct_csv):
            csv_exporter("example.csv")
            assert os.path.exists("example.csv") is True
        else:
            assert False


def test_csv_exporter_cabecalho_invalido():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = wrong_data
        with pytest.raises(ValueError, match="Erro na notícia 0"):
            csv_exporter("wrong_file.csv")


def test_csv_exporter_sucesso(capsys):
    with patch("collector.news_exporter.find_news"):
        csv_exporter("test_example.csv")
        out, err = capsys.readouterr()
        assert out == "Exportação realizada com sucesso\n"


# def test_json_exporter_extensao_invalida():
#     assert False


# def test_json_exporter_cria_arquivo_na_raiz():
#     assert False


# def test_json_exporter_substitui_arquivo_existente():
#     assert False


# def test_json_exporter_sucesso():
#     assert False
