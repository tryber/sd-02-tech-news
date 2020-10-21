# Boas vindas ao repositório do projeto de Tech News!

### ANTES DE COMEÇAR:

1. Clone o repositório

- `git clone git@github.com:git@github.com:EddyeBoy27/tech_news.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-02-tech-news`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r requirements.txt`


## O que foi desenvolvido

Para fixar o conteúdo sobre Python visto até agora, fiz um projeto que tem como principal objetivo criar um banco de dados de notícias sobre tecnologia e realizar algumas consultas nas notícias registradas.

Essas notícias podem ser obtidas de diferentes formas. Sendo elas:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- E através da raspagem das [últimas notícias do TecMundo](https://www.tecmundo.com.br/novidades).

Além de importar ou raspar as notícias, também deve é possível exportá-las e realizar buscas ou análises nas notícias coletadas.

Legal, não é?

---

Para executar, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto.

---

#### - Criei um módulo `news_data_collector_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação.

```md
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Importar notícias a partir de um arquivo JSON;
4 - Exportar notícias para JSON;
5 - Raspar notícias online;
6 - Sair.
```

##### As seguintes ações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, será exibido a mensagem "Digite o path do arquivo CSV a ser importado:";

- Caso a opção `2` seja selecionada, será exibido a mensagem "Digite o nome do arquivo CSV a ser exportado:";

- Caso a opção `3` seja selecionada, será exibido a mensagem "Digite o path do arquivo JSON a ser importado:";

- Caso a opção `4` seja selecionada, será exibido a mensagem "Digite o nome do arquivo JSON a ser exportado:";

- Caso a opção `5` seja selecionada, será exibido a mensagem "Digite a quantidade de páginas a serem raspadas:";

- Caso a opção não exista, será exibido a mensagem de erro "Opção inválida" na `stderr`.

### Pacote `tech_news_app`

#### - Criei um módulo `news_app_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias disparar uma ação.

```md
Selecione uma das opções a seguir:

1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por fonte;
4 - Buscar notícias por categoria;
5 - Listar top 5 notícias;
6 - Listar top 5 categorias;
7 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, será exibida a mensagem "Digite o título:";

- Caso a opção `2` seja selecionada, será exibida a mensagem "Digite a data:";

- Caso a opção `3` seja selecionada, será exibida a mensagem "Digite a fonte:";

- Caso a opção `4` seja selecionada, será exibida a mensagem "Digite a categoria:";

- Caso a opção não exista, será exibida a mensagem de erro "Opção inválida" na `stderr`.
