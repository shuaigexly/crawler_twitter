#!/usr/bin/env python3

from twitter import Account
from sys import stdout
from time import sleep
import json

print = stdout.write

def unlike(username, password, targets):
    try:
        conta = Account(username, password)

        conta.login()

        conta.go_to(f'https://www.x.com/{username}/likes')

        tries, max_stop_tries = 0, 10 ** 3
        cur_max_y = -10 ** 9

        post_set = dict()

        can_all = '*' in targets

        while tries < max_stop_tries:
            max_y, sucesso = 0, 0
        
            elements = conta.get_next_posts()

            for element in elements:
                try:
                    y = element.location['y']
                    max_y = max(max_y, y)
                except:
                    pass

                post = conta.get_post_info(element)

                if post == None:
                    continue

                user, datetime = post.user, post.datetime

                if (can_all or user.lower() in targets) and (user, datetime) not in post_set:
                    print(f'usuário = {user}, datetime = {datetime}\n')
                    post_set[(user, datetime)] = post
                    conta.like_post(element, want = 'unlike')
                
                sucesso += 1

            conta.scroll_by_amount(0, max(50, 200 * sucesso))

            if max_y - cur_max_y <= 0:
                tries += 1
                sleep(0.1)
            else:
                tries = 0
                cur_max_y = max_y

        conta.logout()

    except Exception as ex:
        print(f'uma exceção acabou de ocorrer: {ex}\n')
    finally:
        conta.quit()

def main():
    fp = open('dislike_params.json')

    params = json.load(fp)

    fp.close()

    keys = ['username', 'password', 'targets']

    for key in keys:
        if key not in params:
            raise Exception(f'dislike_params.json não contém o campo {key}')

    unlike(**params)

if __name__ == '__main__':
    main()
