import spider
from unittest.mock import patch
from tech_news_data_collector.news_scrapper import scrape


@patch("spider.requests.get")
def test_scrape_raspa_primeira_pagina_por_padrao(mock_get):
    content = """
    fake content
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = content

    response = spider.fetch_content("https://www.tecmundo.com.br/novidades")
    print('response', response)
    assert response == content


# def test_scrape_raspa_n_paginas_se_definido():
#     assert False


# def test_scrape_trata_404():
#     assert False


# def test_scrape_atributos_obrigatorios():
#     assert False


# def test_scrape_atualiza_noticias_repetidas():
#     assert False


# def test_scrape_exibe_mensagem_apos_finalizar():
#     assert False
