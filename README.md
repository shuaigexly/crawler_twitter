# Requisitos

1. instale o firefox

2. instale o selenium
```
pip install -U selenium
```
3. instale o webdriver manager
```
pip install webdriver-manager
```
4. instale o BeautifulSoup (bs4)
```
pip install beautifulsoup4
```

# Crawler de posts do twitter

Captura posts de uma determinada conta, atráves de palavras chaves, do twitter (apenas as que foram publicadas pelo próprio usuário) contendo
todo o texto presente, todas as imagens no tweet (incluindo as que não aparecem), todos os links (incluindo os que não aparecem) e
videos (somente gifs, pois os outros são armazenados em um local diferente) além da data e horário da postagem em UTC -3 e após isso armazena os dados num arquivo csv. O tweets_by_keys.py e o crawler.py realizam a mesma função, porém o crawler.py gera menos erros já que só precisa encontrar o elemento html do post.

## Opções
- Busca completa no twitter
    - Na janela principal (default)
    - Na janela de respostas (with_replies)
    - Na janela de media (media)
- Usando a barra de pesquisa e colocando palavras chaves
    - Na janela principal (main)
    - Na janela dos recentes (live)
    - Na janela das mídias (media)
    - Na janela dos usuários (user)

## Instruções

Preencha o arquivo params.json

```
{
    "username" : "thiago",
    "password" : "1234",
    "limit" : 800,
    "target_user" : "JJKPerfectShots",
    "target_keywords" : ["geto"],
    "search_type" : "full",
    "search_sub_type" : "default",
    "output" : "dados"
}
```

Sendo:

- username o seu usuário
- password a sua senha
- limit o número máximo de posts a serem carregados (caso for -1 é sem limite)
- target_user o usuário alvo
- target_keywords as palavras-chave alvos (um "" dá match em qq post)
- search_type é full se for pelo perfil ou search pela busca
- search_sub_type
    - se search_type é do tipo full
        - se search_sub_type for default é na aba posts
        - se search_sub_type for with_replies é com as respostas
        - se search_sub_type for media é nas mídias
    - se search_type é do tipo search_by_user
        - se search_sub_type for main é na aba principal
        - se search_sub_type for live é na aba dos recentes
        - se search_sub_type for user é na aba dos usuários
        - se search_sub_type for media é na aba da mídias
- output é o nome do arquivo csv

# Bot de unlike

Dá unlike nos posts das contas que passar como parâmetro ou remove todos os likes

## Instruções

Preencha o arquivo dislike_params.json

```
{
    "username" : "thiago",
    "password" : "1234",
    "targets" : ["JJKPerfectShots", "DemonSlayerUSA", "MobPsychoOne", "Chainsaw_EN"]
}
```

Sendo:

- username o seu usuário
- password a sua senha
- targets com as contas para tirar as curtidas (um "*" dá match em qq um)

### Parte 1
[crawler-1.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/e8f6631f-b275-4ad3-8569-5b6556a0a616)

### Parte 2
[crawler-2.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/87c7a47a-1b72-4b41-8c9c-55b839d31636)

### Parte 3
[crawler-3.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/23ff993a-f77d-4ab4-a74e-d136732fc44f)

### Parte 4
[crawler-4.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/a07279f5-03fa-439c-a12b-56c2beffcef7)

### Parte 5
[crawler-5.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/6c803999-76fc-48eb-8dbe-f4e1f148c425)

### Parte 6
[crawler-6.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/9d1c46b0-3ec5-437c-8889-6145bd6501e7)

### Parte 7
[crawler-7.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/26bc8175-4328-4f98-b5f0-b8412ee8c0b9)

### Parte 8
[crawler-8.webm](https://github.com/ThiagoFBastos/crawler_twitter/assets/40869714/c86dabc2-b946-4eac-8e63-c115412112c9)
