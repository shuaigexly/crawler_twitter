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
    - Na janela principal (principal)
    - Na janela dos recentes (recentes)
    - Na janela das fotos (foto)
    - Na janela dos videos (video)

## Instruções

1. abra o seu terminal e digite python3 tweets_by_keys.py ou crawler.py
2. digite seu usuário (não é o email nem número de celular)
3. digite sua senha
4. digite a quantidade de posts que serão capturados
5. digite o nome do usuário alvo
6. digite a quantidade de keywords (pode ter espaço) - se passar uma linha em branco dá match com qualquer post
7. insira as keywords (uma por linha)
8. digite a opção da busca: busca completa(full) ou por busca de palavras chaves(search)
9. digite a janela da busca: uma das opções do tipo de busca feita em (7)
10. após a captura das informações digite se quer salvar ou não em um arquivo Y ou N
11. caso queira salvar digite o nome do arquivo


# Bot de unlike

Dá unlike nos posts das contas que passar como parâmetro ou remove todos os likes

## Instruções

1. abra o terminal e digite python3 dislike.py
2. digite seu usuário (não é o email nem número de celular)
3. digite sua senha
4. digite a quantidade de contas alvos
5. digite os nomes dessas contas (uma por linha) - se passar um * dá match com qualquer conta

