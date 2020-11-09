# Bolivar, boas vindas ao repositório do projeto de Tech News!

_Relaxa lindo você vai conseguir, não surta, é só uma nova linguagem, novos desafios auuuuuuuuuuuuuuuu how you like that that that_

## CLI:

### Virtual Environment

// Semi-isolated Python environment that allows packages to be installed for use by a particular application, rather than being installed system wide

-   `python3 -m venv .venv && source .venv/bin/activate`

### Install

// Requirements files; list of pip install arguments placed in a file

-   `python3 -m pip install -r requirements.txt`

### Test

```bash
$ python3 -m pytest --cov

ptw
```

### Python Style

```bash
$ python3 -m flake8
```

### Caching GitHub credentials

```bash
git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=36000'
```

### Configure PYTHONPATH

export PYTHONPATH="\${PYTHONPATH}:/home/anderson.bolivar/Documents/projects/sd-02-tech-news"

## Project

Main Goal: Create and Fill a tech news database, research(news_search_engine) and analyse(news_analyser) it;

Get the tech news (tech_news_data_collector):

-   Import `CSV` file
-   Import `JSON` file
-   Scrape [últimas notícias do TecMundo](https://www.tecmundo.com.br/novidades)

Export tech news (tech_news_data_collector);

Test application (tests);

_Legal, não é?_

_yaaas girl_

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── README.md
├── requirements.txt
├── setup.cfg
├── tech_news_app
│   ├── news_analyser.py
│   └── news_search_engine.py
├── tech_news_data_collector
│   ├── news_exporter.py
│   ├── news_importer.py
│   └── news_scrapper.py
├── tests
│   ├── test_news_analyser.py
│   ├── test_news_exporter.py
│   ├── test_news_importer.py
│   ├── test_news_scrapper.py
│   └── test_news_search_engine.py
```

O with serve para is

## Dados

### Importação e exportação de CSV (csv_importer)

Os arquivos CSV devem seguir o modelo abaixo, utilizando ponto e vírgula (`;`) como separador:

```csv
url;title;timestamp;writer;shares_count;comments_count;summary;sources;categories
https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155348-alemanha-trabalha-regulamentacao-carros-autonomos.htm;Alemanha já trabalha na regulamentação de carros autônomos;2020-07-20T15:30:00;Reinaldo Zaruvni;0;0;Recentemente, a Alemanha fez a Tesla “pisar no freio” quanto ao uso de termos comerciais relacionados a carros autônomos, mas quem pensa que esse é um sinal de resistência à introdução de novas tecnologias se engana. Isso porque, de acordo o Automotive News Europe, o país está se preparando para se tornar o primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos de nível 4.;The Next Web,The Next Web,Automotive News Europe;Mobilidade Urbana/Smart Cities,Veículos autônomos,Carro,Política
```

### Importação e exportação de JSON

Os arquivos JSON devem seguir o seguinte modelo:

```json
[
    {
        "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155348-alemanha-trabalha-regulamentacao-carros-autonomos.htm",
        "title": "Alemanha já trabalha na regulamentação de carros autônomos",
        "timestamp": "2020-07-20T15:30:00",
        "writer": "Reinaldo Zaruvni",
        "shares_count": 0,
        "comments_count": 0,
        "summary": "Recentemente, a Alemanha fez a Tesla “pisar no freio” quanto ao uso de termos comerciais relacionados a carros autônomos, mas quem pensa que esse é um sinal de resistência à introdução de novas tecnologias se engana. Isso porque, de acordo o Automotive News Europe, o país está se preparando para se tornar o primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos de nível 4.",
        "sources": ["The Next Web", "The Next Web", "Automotive News Europe"],
        "categories": [
            "Mobilidade Urbana/Smart Cities",
            "Veículos autônomos",
            "Carro",
            "Política"
        ]
    }
]
```

### Raspagem de notícias

As notícias a serem raspadas estarão disponíveis na aba de últimas notícias do TecMundo: https://www.tecmundo.com.br/novidades.

Essas notícias devem ser salvas no banco de dados, utilizando os mesmos atributos já descritos nas importações/exportações citadas anteriormente.

### MongoDB

Para a realização desse projeto, **sugere-se** que você crie um banco de dados, chamado `tech_news`, para a aplicação e um banco de dados separado, chamado `tech_news_test`, para o ambiente de testes. Dessa forma, ambos os ambientes estarão isolados, o que garante que os testes não poluirão sua base de dados.

Para garantir que os dados gerados para um teste não influencie em outro teste, você deve popular e deletar as coleções ao início e ao fim de cada teste, respectivamente.

_Dica:_ Utilize a função `drop` do mongo no final do teste.

---

## Requisitos obrigatórios:

### Pacote `tech_news_data_collector`

#### 1 - Deve haver uma função `scrape` dentro do módulo `news_scrapper` capaz de raspar as últimas notícias das N primeiras páginas, armazenando suas informações no banco de dados.

> Observação: Utilizar os seguintes atributos: `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`. Notícias que já existirem no banco de dados devem ser atualizadas (verifique pela URL).

**Dica:** Caso uma tag possua outras tags aninhadas, para obter todos os textos da tag ancestral e de suas tags descendentes, utilize `*::text` no seletor.

**Exemplo:**

```html
<p>
    Recentemente, a Alemanha fez a
    <a
        href="https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
        rel="noopener noreferrer"
        target="_blank"
        >Tesla</a
    >
    “pisar no freio” quanto ao uso de termos comerciais relacionados a carros
    autônomos, mas quem pensa que esse é um sinal de resistência à introdução de
    novas tecnologias se engana. Isso porque, de acordo o
    <em>Automotive News Europe</em>, o país está se preparando para se tornar o
    primeiro do mundo a criar uma ampla estrutura para regulamentar tais
    veículos de nível 4.
</p>
```

Repare que no exemplo dentro da tag _p_ encontram-se duas outras tags. Esse é um caso onde a tag _p_ é um ancestral e as tags _a_ e _em_ são as descendentes. Para obter todo o texto do exemplo, utiliza-se `*::text` no seletor.

##### As seguintes verificações serão feitas:

<!--  -->

-   Por padrão deve-se raspar apenas as notícias da primeira página;

-   Um número de páginas para serem raspadas pode ser passado para a função. Caso o número de páginas seja definido, deve-se raspar os dados das N primeiras páginas;

-   O scrapper deve ser capaz de tratar um erro de `status 404` ao acessar uma notícia. Devemos considerar que é possível que haja alguma notícia com link quebrado;

-   Todas as notícias devem conter obrigatoriamente os atributos `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`;

-   Caso a notícia já exista no banco de dados, ela deve ser atualizada;

-   Ao finalizar o scrapping, deve-se exibir a mensagem "Raspagem de notícias finalizada".

#### 2 - Deve haver uma função `csv_importer` dentro do módulo `news_importer` capaz de importar notícias a partir de um arquivo CSV, utilizando ";" como separador. Todas as mensagens de erro devem ir para a `stderr`.

##### As seguintes verificações serão feitas:

-   Caso o arquivo CSV não exista, deve ser exibida a mensagem "Arquivo {path/to/file.csv} não encontrado";

-   Caso a extensão do arquivo seja diferente de `.csv`, deve ser exibida uma mensagem "Formato inválido";

-   O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`. Caso contrário, deve ser exibida uma mensagem "Cabeçalho inválido";

-   Todos as informações devem ser obrigatórias. Caso haja alguma informação faltando, deve ser exibida uma mensagem "Erro na notícia {numero-da-linha}";

-   Como não sabemos se a notícia importada está na versão mais atual, não deve ser possível adicionar notícias com URLs duplicadas. Em caso de erro, exiba a mensagem "Notícia {numero-da-linha} duplicada";

-   Em caso de erros, a importação deve ser interrompida e nenhuma notícia deve ser salva;

-   Em caso de sucesso, todas as notícias devem ser salvas no banco de dados e a mensagem "Importação realizada com sucesso" deve ser exibida na `stdout`.

#### 3 - Deve haver uma função `csv_exporter` dentro do módulo `news_exporter` capaz de exportar todas as notícias do banco de dados para um arquivo CSV, utilizando ";" como separador.

##### As seguintes verificações serão feitas:

-   O arquivo exportado deve possuir o formato CSV. Caso contrário, deve ser exibida uma mensagem de erro "Formato inválido" na `stderr`;

-   O arquivo deve ser criado na raiz do projeto;

-   Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

-   O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`;

-   Todas as notícias salvas no banco de dados devem ser exportadas. Em caso de sucesso na exportação, a mensagem "Exportação realizada com sucesso" deve ser exibida na `stdout`.

#### 4 - Deve haver uma função `json_importer` dentro do módulo `news_importer` capaz de importar notícias a partir de um arquivo JSON. Todas as mensagens de erro devem ir para a `stderr`.

> Observação: considere o número da notícia como índice da lista + 1.

##### As seguintes verificações serão feitas:

-   Caso o arquivo não exista, deve ser exibida a mensagem "Arquivo {path/to/file.json} não encontrado";

-   Caso a extensão do arquivo seja diferente de `.json`, deve ser exibida a mensagem "Formato inválido";

-   Caso o JSON seja inválido por qualquer erro no arquivo, deve ser exibida a mensagem "JSON inválido";

-   Todas as informações devem ser obrigatórias. Caso haja alguma informação faltando, deve ser exibida a mensagem "Erro na notícia {numero-da-notícia}";

-   Não deve ser possível adicionar notícias com URLs duplicadas, exibindo a mensagem "Notícia {numero-da-notícia} duplicada" em caso de erro;

-   Em caso de erros, a importação deve ser interrompida e nenhuma notícia deve ser salva;

-   Em caso de sucesso, todas as notícias devem ser salvas no banco de dados e a mensagem "Importação realizada com sucesso" deve ser exibida na `stdout`.

#### 5 - Deve haver uma função `json_exporter` dentro do módulo `news_exporter` capaz de exportar todas as notícias do banco de dados para um arquivo JSON.

##### As seguintes verificações serão feitas:

-   O arquivo exportado deve possuir o formato `.json`. Caso contrário, deve ser exibida a mensagem de erro "Formato inválido" na `stderr`;

-   O arquivo deve ser criado na raiz do projeto;

-   Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

-   Todas as notícias salvas no banco de dados devem ser exportadas e a mensagem "Exportação realizada com sucesso" deve ser exibida na `stdout`.

### Pacote `tech_news_app`

#### 6 - Deve haver uma função `search_by_title` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por título (parcial ou completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

-   A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

-   Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 7 - Deve haver uma função `search_by_date` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por data e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

-   A busca deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

-   A data deve estar no formato "aaaa-mm-dd" e deve ser válida. Caso seja inválida, deve-se exibir a mensagem "Data inválida";

-   Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 8 - Deve haver uma função `search_by_source` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por fonte (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

-   A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

-   Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 9 - Deve haver uma função `search_by_category` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por categoria (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

-   A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

-   Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 10 - Deve haver uma função `top_5_news` dentro do módulo `news_analyser`, que liste as cinco notícias com a maior soma de compartilhamentos e comentários do banco de dados. As notícias devem ser ordenadas pela popularidade. Em caso de empate, o desempate deve ser por ordem alfabética de título.

##### As seguintes verificações serão feitas:

-   As top 5 notícias da análise devem ser retornadas em uma lista de notícias no formato `["- {title}: {url}"]`;

-   Caso haja menos de cinco notícias, no banco de dados, deve-se retornar todas as notícias existentes;

-   Caso não haja notícias disponíveis, deve-se retornar uma lista vazia.

#### 11 - Deve haver uma função `top_5_categories` dentro do módulo `news_analyser`, que liste as cinco categorias com maior ocorrência no banco de dados. As categorias devem ser ordenadas por ordem alfabética.

##### As seguintes verificações serão feitas:

-   As top 5 categorias da análise devem ser retornadas em uma lista de categorias no formato `["- {category}"]`;

-   Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;

-   Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

---

## Requisitos bônus:

### Pacote `tech_news_data_collector`

#### 12 - Crie um módulo `news_data_collector_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação. O texto exibido pelo menu deve ser exatamente:

**Dica**: Utilize o `__main__`.

```md
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Importar notícias a partir de um arquivo JSON;
4 - Exportar notícias para JSON;
5 - Raspar notícias online;
6 - Sair.
```

##### As seguintes verificações serão feitas:

-   A mensagem de menu deve ser exibida corretamente;

-   Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o path do arquivo CSV a ser importado:";

-   Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo CSV a ser exportado:";

-   Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite o path do arquivo JSON a ser importado:";

-   Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo JSON a ser exportado:";

-   Caso a opção `5` seja selecionada, deve-se exibir a mensagem "Digite a quantidade de páginas a serem raspadas:";

-   Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

#### 13 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada.

##### As seguintes verificações serão feitas:

-   Caso a opção `1` seja selecionada, a importação deve ser feita utilizando função `csv_importer`;

-   Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando função `csv_exporter`;

-   Caso a opção `3` seja selecionada, a importação deve ser feita utilizando função `json_importer`;

-   Caso a opção `4` seja selecionada, exportação deve ser feita utilizando função `json_exporter`;

-   Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando função `scrape`;

-   Caso a opção `6` seja selecionada, deve-se encerrar a execução do script (dica: verifique o `exit code`);

-   Após finalizar a execução de uma ação, deve-se encerrar a execução do script (dica: verifique o `exit code`).

### Pacote `tech_news_app`

#### 14 - Crie um módulo `news_app_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias disparar uma ação. O texto exibido pelo menu deve ser exatamente:

**Dica**: Utilize o `__main__`.

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

-   A mensagem de menu deve ser exibida corretamente;

-   Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o título:";

-   Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a data:";

-   Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a fonte:";

-   Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite a categoria:";

-   Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

#### 15 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada e seu resultado deve ser exibido.

##### As seguintes verificações serão feitas:

-   Caso a opção `1` seja selecionada, a importação deve ser feita utilizando a função `search_by_title` e seu resultado deve ser impresso em tela;

-   Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando a função `search_by_date` e seu resultado deve ser impresso em tela;

-   Caso a opção `3` seja selecionada, a importação deve ser feita utilizando a função `search_by_source` e seu resultado deve ser impresso em tela;

-   Caso a opção `4` seja selecionada, a exportação deve ser feita utilizando a função `search_by_category` e seu resultado deve ser impresso em tela;

-   Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_news` e seu resultado deve ser impresso em tela;

-   Caso a opção `6` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_categories` e seu resultado deve ser impresso em tela;

-   Caso a opção `7` seja selecionada, deve-se encerrar a execução do script.

## Requisitos extras:

⚠️ Requisitos não serão avaliados ⚠️

### Pacote `tech_news_data_collector`

#### 16 - A cobertura de testes unitários do pacote deve ser de no mínimo 90%.

##### As seguintes verificações serão feitas:

-   Todos os testes que envolvem mensagens na saída padrão ou de erro, devem ter sua saída redirecionada para _Fakes_ com `StringIO`;

-   Todos os testes que envolvem manipulação de arquivos criam _Fakes_ com `StringIO`;

-   Todas as requisições externas utilizam _Mocks_;

-   A cobertura de testes é de no mínimo 90%.

### Pacote `tech_news_app`

#### 17 - A cobertura de testes unitários do pacote deve ser de no mínimo 90%.

---
