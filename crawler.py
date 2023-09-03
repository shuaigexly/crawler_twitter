#!/usr/bin/env python3

from twitter import Account
from sys import argv, stdout
from time import sleep
from bs4 import BeautifulSoup
import json

print = stdout.write

def save_posts(posts, filename):
    from pandas import DataFrame
    from datetime import datetime as dt, timedelta

    with open(filename, 'w') as f:
        users = []

        for post in posts:
            user, datetime, text, link, image, video = post.user, post.datetime, post.get_text(), post.get_links(), post.get_images(), post.get_videos()
            datetime = dt.fromisoformat(datetime) - timedelta(hours = 3)
            users.append([user, str(datetime), text, link, image, video])

        post_df = DataFrame(data = users, columns = ['user', 'datetime', 'text', 'link', 'image', 'gif'])
        post_df.to_csv(filename + ".csv")

def crawler(username, password, target_user, target_keywords, search_type, search_sub_type, limit = -1, output = None):
    try:
        target_user = target_user.lower()
        target_keywords = list(map(lambda key: key.lower(), target_keywords))
        limit = 10 ** 9 if limit == -1 else limit

        if search_type == 'full':
            want = None
            if search_sub_type == 'default':
                want = ''
            elif search_sub_type in ('with_replies', 'media'):
                want = search_sub_type
            else:
                raise Exception('operação não suportada')

        elif search_type == 'search':
            want = None
            if search_sub_type in ('main', 'live', 'user', 'media'):
                want = search_sub_type
            else:
                raise Exception('operação não suportada')

        account = Account(username, password)

        account.login()

        if search_type == 'full':
            account.go_to(f'https://www.x.com/{target_user}/{want}')
        else:
            account.search_by_user(target_keywords, target_user, tab = want)

        tries, max_stop_tries = 0, 100

        posts_set = set()
        posts_list = []
        
        driver = account.driver

        while limit > 0 and tries < max_stop_tries:
            has_new_post, sucesso = False, 0
    
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            articles = soup.find_all('article')

            for article in articles:
    
                post = account.get_post_info_from_soup(article)

                if post is None: continue
                
                text, user, datetime = post.text.lower(), post.user, post.datetime

                found_key = False

                if user.lower() == target_user and (user, datetime) not in posts_set:
                    has_new_post = True
                    posts_set.add((user, datetime))

                    for key in target_keywords:
                        if text.find(key.lower()) != -1:
                            found_key = True
                            break
                
                    if found_key:
                        print(f'user = {user}, datetime = {datetime}, text = {text}\n')
                        limit -= 1
                        posts_list.append(post)
                
                sucesso += 1

            account.scroll_by_amount(0, max(50, sucesso * 200))

            if has_new_post:
                tries = 0
            else:
                tries += 1
                sleep(0.1)

        if output: save_posts(posts_list, output)

        account.logout()
    except Exception as ex:
        print(f'uma exceção acabou de ocorrer: {ex}\n')
    finally:
        account.quit()

def main():
    fp = open('params.json', 'r')

    params = json.load(fp)

    fp.close()

    keys = ['username', 'password', 'limit', 'target_user', 'target_keywords', 'search_type', 'search_sub_type']
 
    for key in params:
        if key not in params:
            raise Exception(f'params.json não contém o campo {key}')
    
    crawler(**params)

if __name__ == '__main__':
    main()
