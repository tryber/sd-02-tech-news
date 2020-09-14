from io import StringIO
from contextlib import redirect_stderr
from tech_news_data_collector.news_exporter import csv_exporter


def test_csv_exporter_extensao_invalida():
  stub_output = StringIO()
  expected_output = "Formato inválido\n"
  with redirect_stderr(stub_output):
    csv_exporter("imported.json")
  assert stub_output.getvalue() == expected_output


def test_csv_exporter_cria_arquivo_na_raiz():
  assert False


def test_csv_exporter_substitui_arquivo_existente():
  assert False


def test_csv_exporter_cabecalho_invalido():
  assert False


def test_csv_exporter_sucesso():
  assert False


def test_json_exporter_extensao_invalida():
  assert False


def test_json_exporter_cria_arquivo_na_raiz():
  assert False


def test_json_exporter_substitui_arquivo_existente():
  assert False


def test_json_exporter_sucesso():
  assert False
