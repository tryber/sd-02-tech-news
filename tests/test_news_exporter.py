from collector.news_exporter import (csv_exporter, json_exporter)

from tests.test_news_fakers import (
    mock_data,
    mock_wrong_data,
    path_export_correct_csv,
)

from unittest.mock import patch

import os

import pytest


def test_csv_exporter_extensao_invalida():
    with patch("collector.news_exporter.find_news"):
        with pytest.raises(ValueError, match='Formato inválido'):
            csv_exporter("file.txt")


def test_csv_exporter_cria_arquivo_na_raiz():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        csv_exporter("correct.csv")
        assert os.path.exists("correct.csv") is True


def test_csv_exporter_substitui_arquivo_existente():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        if os.path.exists(path_export_correct_csv):
            csv_exporter("correct.csv")
            assert os.path.exists("correct.csv") is True


def test_csv_exporter_cabecalho_invalido():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_wrong_data
        with pytest.raises(ValueError, match="Erro na notícia 0"):
            csv_exporter("wrong_fields.csv")


def test_csv_exporter_sucesso(capsys):
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        csv_exporter("correct.csv")
        out, err = capsys.readouterr()
        assert out == "Exportação realizada com sucesso\n"


def test_json_exporter_extensao_invalida():
    with patch("collector.news_exporter.find_news"):
        with pytest.raises(ValueError, match='Formato inválido'):
            json_exporter("file.txt")


def test_json_exporter_cria_arquivo_na_raiz():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        json_exporter("correct.json")
        assert os.path.exists("correct.json") is True


def test_json_exporter_substitui_arquivo_existente():
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        if os.path.exists("correct.json"):
            json_exporter("correct.json")
            assert os.path.exists("correct.json") is True


def test_json_exporter_sucesso(capsys):
    with patch("collector.news_exporter.find_news") as find_news_mock:
        find_news_mock.return_value = mock_data
        json_exporter("correct.json")
        out, err = capsys.readouterr()
        assert out == "Exportação realizada com sucesso\n"
