# import pytest

# from unittest.mock import patch

# from collector.news_exporter import (csv_exporter, json_exporter)

# from tests.test_news_fakers import (
#     data_mock,
#     wrong_data,
#     export_correct_csv,
#     export_wrong_csv,
#     export_no_exists_csv,
#     export_no_exists_json
# )

# import os


# def test_csv_exporter_extensao_invalida():
#     with patch("collector.news_exporter.find_news"):
#         with pytest.raises(ValueError, match='Formato inválido'):
#             csv_exporter("file.txt")


# def test_csv_exporter_cria_arquivo_na_raiz():
#     with patch("collector.news_exporter.find_news"):
#         csv_exporter("not_exists.csv")
#         assert os.path.exists("not_exists.csv") is True
#         os.remove(export_no_exists_csv)


# def test_csv_exporter_substitui_arquivo_existente():
#     with patch("collector.news_exporter.find_news") as find_news_mock:
#         find_news_mock.return_value = data_mock
#         if os.path.exists(export_correct_csv):
#             csv_exporter("example.csv")
#             assert os.path.exists("example.csv") is True
#         else:
#             assert False


# def test_csv_exporter_cabecalho_invalido():
#     with patch("collector.news_exporter.find_news") as find_news_mock:
#         find_news_mock.return_value = wrong_data
#         with pytest.raises(ValueError, match="Erro na notícia 0"):
#             csv_exporter("wrong_headers.csv")
#             assert os.path.exists(export_wrong_csv) is False


# def test_csv_exporter_sucesso(capsys):
#     with patch("collector.news_exporter.find_news"):
#         csv_exporter("test_example.csv")
#         out, err = capsys.readouterr()
#         assert out == "Exportação realizada com sucesso\n"


# def test_json_exporter_extensao_invalida():
#     with patch("collector.news_exporter.find_news"):
#         with pytest.raises(ValueError, match='Formato inválido'):
#             json_exporter("file.txt")


# def test_json_exporter_cria_arquivo_na_raiz():
#     with patch("collector.news_exporter.find_news") as find_news_mock:
#         find_news_mock.return_value = data_mock
#         json_exporter("not_exists.json")
#         assert os.path.exists("not_exists.json") is True
#         os.remove(export_no_exists_json)


# def test_json_exporter_substitui_arquivo_existente():
#     with patch("collector.news_exporter.find_news") as find_news_mock:
#         find_news_mock.return_value = data_mock
#         if os.path.exists("example.json"):
#             json_exporter("example.json")
#             assert os.path.exists("example.json") is True
#         else:
#             assert False


# def test_json_exporter_sucesso(capsys):
#     with patch("collector.news_exporter.find_news") as find_news_mock:
#         find_news_mock.return_value = data_mock
#         json_exporter("test_example.json")
#         out, err = capsys.readouterr()
#         assert out == "Exportação realizada com sucesso\n"
