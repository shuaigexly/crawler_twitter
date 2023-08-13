#!/usr/bin/env python3

from twitter import Account
from sys import stdout
from time import sleep

print = stdout.write

def main():

    try:
        print('iniciando o seu login\n')

        username = input('digite seu usuário: ')
        password = input('digite sua senha: ')

        cnt_accounts = int(input('quantidade de contas: '))

        targets = set([input('próxima conta: ').lower() for i in range(cnt_accounts)])

        conta = Account(username, password)

        conta.login()

        conta.go_to(f'https://www.x.com/{username}/likes')

        tries, max_stop_tries = 0, 10 ** 3
        cur_max_y = -10 ** 9

        post_set = dict()

        can_all = '*' in targets

        while tries < max_stop_tries:
            max_y, sucesso = 0, 0
        
            elements = conta.get_next_posts() or []

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

if __name__ == '__main__':
    main()
