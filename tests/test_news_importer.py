from io import StringIO
from contextlib import redirect_stderr, redirect_stdout
from tech_news_data_collector.news_importer import csv_importer, json_importer


def test_csv_importer_arquivo_nao_existe():
  stub_output = StringIO()
  expected_output = "Arquivo { nao_existe.csv } não encontrado\n"
  with redirect_stderr(stub_output):
    csv_importer("nao_existe.csv")
  assert stub_output.getvalue() == expected_output


def test_csv_importer_extensao_invalida():
  stub_output = StringIO()
  expected_output = "Formato inválido\n"
  with redirect_stderr(stub_output):
    csv_importer("mock/imported.json")
  assert stub_output.getvalue() == expected_output


def test_csv_importer_cabecalho_invalido():
  stub_output = StringIO()
  expected_output = "Cabeçalho inválido\n"
  with redirect_stderr(stub_output):
    csv_importer("mock/cabecalho_invalido.csv")
  assert stub_output.getvalue() == expected_output


def test_csv_importer_informacoes_incompletas():
  stub_output = StringIO()
  expected_output = "Erro na notícia 0\n"
  with redirect_stderr(stub_output):
    csv_importer("mock/informaçao_faltando.csv")
  assert stub_output.getvalue() == expected_output


def test_csv_importer_urls_duplicadas():
  stub_output = StringIO()
  expected_output = "Notícia 1 duplicada\n"
  with redirect_stderr(stub_output):
    csv_importer("mock/url_duplicada.csv")
  assert stub_output.getvalue() == expected_output


def test_csv_importer_importacao_interrompida_em_caso_de_erro():
  assert False


def test_csv_importer_sucesso():
  stub_output = StringIO()
  expected_output = "Importação realizada com sucesso\n"
  with redirect_stdout(stub_output):
    csv_importer("mock/imported.csv")
  assert stub_output.getvalue() == expected_output


def test_json_importer_arquivo_nao_existe():
  stub_output = StringIO()
  expected_output = "Arquivo { nao_existe.json } não encontrado\n"
  with redirect_stderr(stub_output):
    json_importer("nao_existe.json")
  assert stub_output.getvalue() == expected_output


def test_json_importer_extensao_invalida():
  stub_output = StringIO()
  expected_output = "Formato inválido\n"
  with redirect_stderr(stub_output):
    json_importer("mock/imported.csv")
  assert stub_output.getvalue() == expected_output


def test_json_importer_json_invalido():
  stub_output = StringIO()
  expected_output = "Erro na notícia 0\n"
  with redirect_stderr(stub_output):
    json_importer("mock/informacao_faltando.json")
  assert stub_output.getvalue() == expected_output


def test_json_importer_informacoes_incompletas():
  stub_output = StringIO()
  expected_output = "Notícia 1 duplicada\n"
  with redirect_stderr(stub_output):
    json_importer("mock/url_duplicado.json")
  assert stub_output.getvalue() == expected_output


def test_json_importer_urls_duplicadas():
  stub_output = StringIO()
  expected_output = "Notícia 1 duplicada\n"
  with redirect_stderr(stub_output):
    json_importer("mock/url_duplicado.json")
  assert stub_output.getvalue() == expected_output


def test_json_importer_importacao_interrompida_em_caso_de_erro():
  assert False


def test_json_importer_sucesso():
  stub_output = StringIO()
  expected_output = "Importação realizada com sucesso\n"
  with redirect_stdout(stub_output):
    csv_importer("mock/imported.json")
  assert stub_output.getvalue() == expected_output
