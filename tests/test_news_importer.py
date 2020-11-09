from collector.news_importer import (csv_importer, json_importer)

from contextlib import suppress

from tests.test_news_fakers import (
    mock_data,
    path_correct_csv,
    path_correct_json,
    path_duplicate_url_csv,
    path_duplicate_url_json,
    path_incomplete_csv,
    path_incomplete_json,
    path_not_exists_csv,
    path_not_exists_json,
    path_wrong_fields_csv,
    path_wrong_fomart_file,
    path_wrong_json,
)

from unittest.mock import patch

import os

import pytest


def test_csv_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo not_exist.csv não encontrado"):
        csv_importer(path_not_exists_csv)


def test_csv_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        csv_importer(path_wrong_fomart_file)


def test_csv_importer_cabecalho_invalido():
    with pytest.raises(ValueError, match="Cabeçalho inválido"):
        csv_importer(path_wrong_fields_csv)


def test_csv_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        csv_importer(path_incomplete_csv)


def test_csv_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        csv_importer(path_duplicate_url_csv)


def test_csv_importer_importacao_interrompida_em_caso_de_erro():
    with patch("collector.news_importer.create_news") as create_news_mock:
        with suppress(ValueError):
            csv_importer(path_duplicate_url_csv)
            create_news_mock.assert_not_called()


def test_csv_importer_print_on_success(capsys):
    with patch("collector.news_importer.create_news"):
        csv_importer(path_correct_csv)
        out, err = capsys.readouterr()
        assert out == "Importação realizada com sucesso\n"


def test_csv_importer_save_data_on_sucess():
    with patch("collector.news_service.find_new") as find_new_mock:
        with patch("collector.news_importer.create_news") as create_news_mock:
            find_new_mock.return_value = []
            csv_importer(path_correct_csv)
            create_news_mock.assert_called_with(mock_data)


def test_json_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo not_exist.json não encontrado"):
        json_importer(path_not_exists_json)


def test_json_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        json_importer(path_wrong_fomart_file)


def test_json_importer_json_invalido():
    with pytest.raises(ValueError, match="JSON inválido"):
        json_importer(path_wrong_json)


def test_json_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        json_importer(path_incomplete_json)


def test_json_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        json_importer(path_duplicate_url_json)


def test_json_importer_importacao_interrompida_em_caso_de_erro():
    with patch("collector.news_importer.create_news") as create_news_mock:
        with suppress(ValueError):
            json_importer(path_duplicate_url_json)
            create_news_mock.assert_not_called()


def test_json_importer_print_on_success(capsys):
    with patch("collector.news_importer.create_news"):
        json_importer(path_correct_json)
        out, err = capsys.readouterr()
        assert out == "Importação realizada com sucesso\n"


def test_json_importer_save_data_on_sucess():
    with patch("collector.news_service.find_new") as find_new_mock:
        with patch("collector.news_importer.create_news") as create_news_mock:
            find_new_mock.return_value = []
            json_importer(path_correct_json)
            create_news_mock.assert_called_with(mock_data)
