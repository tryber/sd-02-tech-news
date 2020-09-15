import os
from io import StringIO
from contextlib import redirect_stderr, redirect_stdout
from tech_news_data_collector.news_exporter import csv_exporter, json_exporter


def test_csv_exporter_extensao_invalida():
    stub_output = StringIO()
    expected_output = "Formato inválido\n"
    with redirect_stderr(stub_output):
        csv_exporter("mock/arquivo.json")
    assert stub_output.getvalue() == expected_output


def test_csv_exporter_cria_arquivo_na_raiz():
    file = "mock/exported.csv"
    csv_exporter(file)
    boo = os.path.exists(file)
    assert boo is True
    os.remove(file)


def test_csv_exporter_substitui_arquivo_existente():
    assert False


def test_csv_exporter_cabecalho_invalido():
    assert False


def test_csv_exporter_sucesso():
    file = "mock/exported.csv"
    stub_output = StringIO()
    expected_output = "Exportação realizada com sucesso\n"
    with redirect_stdout(stub_output):
        csv_exporter(file)
    boo = os.path.exists(file)
    assert stub_output.getvalue() == expected_output
    assert boo is True
    os.remove(file)


def test_json_exporter_extensao_invalida():
    stub_output = StringIO()
    expected_output = "Formato inválido\n"
    with redirect_stderr(stub_output):
        json_exporter("mock/arquivo.csv")
    assert stub_output.getvalue() == expected_output


def test_json_exporter_cria_arquivo_na_raiz():
    file = "mock/exported.json"
    json_exporter(file)
    boo = os.path.exists(file)
    assert boo is True
    os.remove(file)


def test_json_exporter_substitui_arquivo_existente():
    assert False


def test_json_exporter_sucesso():
    file = "mock/exported.json"
    stub_output = StringIO()
    expected_output = "Exportação realizada com sucesso\n"
    with redirect_stdout(stub_output):
        json_exporter(file)
    boo = os.path.exists(file)
    assert stub_output.getvalue() == expected_output
    assert boo is True
    os.remove(file)
