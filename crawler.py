#!/usr/bin/env python3

from twitter import Account
from sys import argv, stdout
from time import sleep
from bs4 import BeautifulSoup

print = stdout.write

def save_posts(posts, filename):
    from pandas import DataFrame
    from datetime import datetime as dt, timedelta

    with open(filename, 'w') as f:
        users = []

        for post in posts.values():
            user, datetime, text, link, image, video = post.user, post.datetime, post.get_text(), post.get_links(), post.get_images(), post.get_videos()
            datetime = dt.fromisoformat(datetime) - timedelta(hours = 3)
            users.append([user, str(datetime), text, link, image, video])

        post_df = DataFrame(data = users, columns = ['user', 'datetime', 'text', 'link', 'image', 'gif'])
        post_df.to_csv(filename + ".csv")

def main():
    try:
        print('iniciando o seu login\n')

        username = input('usernamee: ')
        password = input('password: ')

        n_posts = int(input('quantidade de posts: '))
       
        target_user = input('nome do usuário alvo: ').lower()
        target_keywords = []

        cnt_keys = int(input('quantidade de keywords: '))
        
        for j in range(cnt_keys):
            keyword = input(f'qual é a {j+1}ª keyword: ')
            target_keywords.append(keyword.lower())

        tipo = input('tipo da busca[full/search]: ')

        if tipo == 'full':
            subtipo = input('qual é o subtipo[default/with_replies/media]: ')
            want = None
            if subtipo == 'default':
                want = ''
            elif subtipo == 'with_replies' or subtipo == 'media':
                want = subtipo
            else:
                raise Exception('operação não suportada')

        elif tipo == 'search':
            subtipo = input('qual é o subtipo[principal/recentes/foto/video]: ')
            want = None
            if subtipo == 'principal':
                want = 'principal'
            elif subtipo == 'recentes':
                want = 'recente'
            elif subtipo == 'foto':
                want = 'foto'
            elif subtipo == 'video':
                want = 'video'
            else:
                raise Exception('operação não suportada')

        account = Account(username, password)

        account.login()

        if tipo == 'full':
            account.go_to(f'https://www.x.com/{target_user}/{want}')
        else:
            account.search_by_user(target_user, tab = want)

        tries, max_stop_tries = 0, 500

        posts_set = dict()
        
        driver = account.driver

        while n_posts > 0 and tries < max_stop_tries:
            has_new_post, sucesso = False, 0
    
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            articles = soup.find_all('article')

            for article in articles:
    
                post = account.get_post_info_from_soup(article)

                if post is None: continue
                
                text, user, datetime = post.text.lower(), post.user, post.datetime

                found_key = False

                if user.lower() == target_user:
                    has_new_post = has_new_post or (user, datetime) not in posts_set

                    for key in target_keywords:
                        if text.find(key.lower()) != -1:
                            found_key = True
                            break
                
                if found_key and (user, datetime) not in posts_set:
                    print(f'user = {user}, datetime = {datetime}, text = {text}\n')
                    n_posts -= 1
                    posts_set[(user, datetime)] = post
                
                sucesso += 1
                
            account.scroll_by_amount(0, max(50, sucesso * 200))

            if has_new_post:
                tries = 0
            else:
                tries += 1
                sleep(0.1)
            
        opcao = input('quer salvar os dados[Y/N]?: ')

        if opcao == 'Y' or opcao == 'y':
            filename = input('digite o nome do arquivo: ')
            save_posts(posts_set, filename)

        account.logout()
    except Exception as ex:
        print(f'uma exceção acabou de ocorrer: {ex}\n')
    finally:
        account.quit()
    
if __name__ == '__main__':
    main()
