import pytest

from unittest.mock import patch

from contextlib import suppress

from collector.news_importer import (csv_importer, json_importer)

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
    wrong_json
)


def test_csv_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo not_exist.csv não encontrado"):
        csv_importer(not_exists_csv) is None


def test_csv_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        csv_importer(wrong_fomart_file)


def test_csv_importer_cabecalho_invalido():
    with pytest.raises(ValueError, match="Cabeçalho inválido"):
        csv_importer(wrong_header_file)


def test_csv_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        csv_importer(incomplete_csv)


def test_csv_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        csv_importer(duplicate_csv)


def test_csv_importer_importacao_interrompida_em_caso_de_erro():
    with patch("collector.news_importer.create_news") as create_news_mock:
        with suppress(ValueError):
            csv_importer(duplicate_csv)
            create_news_mock.assert_not_called()


def test_csv_importer_print_on_success(capsys):
    with patch("collector.news_importer.create_news"):
        csv_importer(correct_csv)
        out, err = capsys.readouterr()
        assert out == "Importação realizada com sucesso\n"


@patch("collector.news_importer.create_news")
def test_csv_importer_save_data_on_sucess(create_news_mock):
    csv_importer(correct_csv)
    create_news_mock.assert_called_with(data_mock)


def test_json_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="Arquivo not_exist.json não encontrado"):
        json_importer(not_exists_json)


def test_json_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Formato inválido"):
        json_importer(wrong_fomart_file)


def test_json_importer_json_invalido():
    with pytest.raises(ValueError, match="JSON inválido"):
        json_importer(wrong_json)


def test_json_importer_informacoes_incompletas():
    with pytest.raises(ValueError, match="Erro na notícia 1"):
        json_importer(incomplete_json)


def test_json_importer_urls_duplicadas():
    with pytest.raises(ValueError, match="Notícia 2 duplicada"):
        json_importer(duplicate_json)


def test_json_importer_importacao_interrompida_em_caso_de_erro():
    with patch("collector.news_importer.create_news") as create_news_mock:
        with suppress(ValueError):
            json_importer(duplicate_json)
            create_news_mock.assert_not_called()


def test_json_importer_print_on_success(capsys):
    with patch("collector.news_importer.create_news"):
        json_importer(correct_json)
        out, err = capsys.readouterr()
        assert out == "Importação realizada com sucesso\n"


@patch("collector.news_importer.create_news")
def test_json_importer_save_data_on_sucess(create_news_mock, capsys):
    json_importer(correct_json)
    create_news_mock.assert_called_with(data_mock)
