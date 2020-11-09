# from unittest.mock import patch

# from unittest.mock import Mock


# from tests.test_news_fakers import (
#     data_mock,
#     wrong_url
# )

# from collector.news_scrapper import scrape

# import pytest


# def test_scrape_raspa_primeira_pagina_por_padrao():
#     scrape(2)
#     assert False


# def test_scrape_raspa_n_paginas_se_definido():
#     assert False


# def test_scrape_trata_404():
#     with patch("collector.news_scrapper.create_or_update_news"):
#         with pytest.raises(ValueError, match='Formato inválido'):
#             json_exporter("file.txt")


# def test_scrape_atributos_obrigatorios():
#     assert False


# def test_scrape_atualiza_noticias_repetidas():
#     assert False


# def test_scrape_exibe_mensagem_apos_finalizar(capsys):
#     scrape(2000)
#     assert False
#     # with patch("collector.news_scrapper.fetch_content") as fetch_content_mock:
#     #     fetch_content_mock.return_value = data_mock
#     #     with patch("collector.news_scrapper.create_or_update_news"):
#     #         scrape()
#     #         out, err = capsys.readouterr()
#     #         assert out == "Raspagem de notícias finalizada\n"
