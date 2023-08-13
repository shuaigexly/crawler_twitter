# Requisitos

1. instale o selenium
    - pip install -U selenium
2. instale o webdriver manager
    - pip install webdriver-manager
3. instale o BeautifulSoup (bs4)
    - pip install beautifulsoup4

# Crawler de posts do twitter - ./tweets_by_keys.py

Captura posts de uma determinada conta, atráves de palavras chaves, do twitter (apenas as que foram publicadas pelo próprio usuário) contendo
todo o texto presente, todas as imagens no tweet (incluindo as que não aparecem), todos os links (incluindo os que não aparecem) e
videos (somente gifs, pois os outros são armazenados em um local diferente) além da data e horário da postagem em UTC e após isso armazena os dados num arquivo csv.

# Opções
- Busca completa no twitter
    - Na janela principal (default)
    - Na janela de respostas (with_replies)
    - Na janela de media (media)
- Usando a barra de pesquisa e colocando palavras chaves
    - Na janela principal (principal)
    - Na janela dos recentes (recentes)
    - Na janela das fotos (foto)
    - Na janela dos videos (video)

# Instrução

1. digite seu usuário (não é o email nem número de celular)
2. digite sua senha
3. digite a quantidade de posts que serão capturados
4. digite o nome do usuário alvo
5. digite a quantidade keywords (pode ter espaço) - se passar uma linha em branco dá match com qualquer post
6. insira as keywords (uma por linha)
7. digite a opção da busca: busca completa(full) ou por busca de palavras chaves(search)
8. digite a janela da busca: uma das opções do tipo de busca feita em (7)
9. após a captura das informações digite se quer salvar ou não em um arquivo Y ou N
10. caso queira salvar digite o nome do arquivo


# Bot de unlike - ./dislike.py

Dá unlike nos posts das contas que passar como parâmetro ou remove todos os likes

# Instruções

1. digite seu usuário (não é o email nem número de celular)
2. digite sua senha
3. digite a quantidade de contas alvos
4. digite os nomes dessas contas (uma por linha) - se passar um * dá match com qualquer conta

