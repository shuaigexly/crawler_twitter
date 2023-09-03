from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep
from post import Post
from sys import stdin, stdout
from bs4 import BeautifulSoup

input, print = stdin.readline, stdout.write

class Account:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
        self.driver.set_window_size(400, 600)        
        self._username = username
        self._password = password

    def go_to(self, url):
        self.driver.get(url)

    def backward(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def scroll_by_amount(self, dx, dy):
        ActionChains(self.driver).scroll_by_amount(dx, dy).perform()

    def login(self):
        tries = 0

        driver = self.driver

        login_url = 'https://x.com/i/flow/login?redirect_after_login=%2F'

        while True:
            try:

                if driver.current_url != login_url:
                    driver.get(login_url)

                usernameInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='text']")))

                usernameInput.send_keys(self._username)

                WebDriverWait(usernameInput, 5).until(lambda inp: inp.get_attribute('value') == self._username)

                usernameInput.send_keys(Keys.ENTER)

                passwordInput = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
      
                passwordInput.send_keys(self._password)

                WebDriverWait(passwordInput, 5).until(lambda inp: inp.get_attribute('value') == self._password)

                passwordInput.send_keys(Keys.ENTER)

                break        
            except Exception as ex:
                print(f'erro ao tentar logar: {ex}\n')

                tries += 1

                if tries == 5:
                    tries = 0
                    driver.refresh()

        print(f'usuário {self._username} logado\n')
        sleep(5)

    def logout(self):
        tries = 0
        logout_url = 'https://www.x.com/logout'

        while True:
            try:

                if self.driver.current_url != logout_url:
                    self.driver.get(logout_url)

                button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="confirmationSheetConfirm"]')))

                button.click()

                break
            except Exception as ex:
                print(f'erro ao deslogar: {ex}\n')

                tries += 1

                if tries == 5:
                    tries = 0
                    self.driver.refresh()

    def search(self, keywords, tab = 'main'):
        driver = self.driver

        query = " OR ".join(map(lambda s: '"' + s + '"', keywords))

        query_url = 'https://x.com/search?q=' + query + "&src=typeahead_click"

        if tab == 'main':
            driver.get(query_url)
        else:
            driver.get(f'{query_url}&f={tab}')

    def search_by_user(self, keywords, user, tab = 'main'):
        driver = self.driver

        query = 'from:@' + user + ' ' + " OR ".join(map(lambda s: '"' + s + '"', keywords))

        query_url = 'https://x.com/search?q=' + query + "&src=typeahead_click"

        if tab == 'main':
            driver.get(query_url)
        else:
            driver.get(f'{query_url}&f={tab}')

    def search_by_users(self, users_keywords, tab = 'principal'):
        driver = self.driver

        query = str()

        for i, items in enumerate(users_keywords):
            user, keywords = items
            query += '(from:@' + user + ' ' + ' OR '.join(map(lambda s: '"' + s + '"', keywords)) + ')'
            if i + 1 < len(users_keywords):
                query += ' OR '

        query_url = 'https://x.com/search?q=' + query + "&src=typeahead_click"

        if tab == 'main':
            driver.get(query_url)
        else:
            driver.get(f'{query_url}&f={tab}')

    def like_post(self, element, want = 'like'):
        status = 1

        try:
            like = WebDriverWait(element, 20).until(EC.presence_of_element_located((By.XPATH, ".//div[@data-testid='unlike' or @data-testid='like']")))

            tipo = like.get_attribute('data-testid')

            if tipo == want:
                sleep(0.75)
                like.click()
            else:
                status = 0

        except Exception as ex:
            status = -1
            print(f'erro ao dar {want} no post: {ex}\n')

        finally:
            return status

    def get_next_posts(self):
        try:
            elements = WebDriverWait(self.driver, 2.5).until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))
            return elements
        except Exception as ex:
            print(f'erro ao capturar os próximos posts: {ex}\n')
            return []

    def get_post_info(self, element):
        try:
            soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
            return self.get_post_info_from_soup(soup)
        except Exception as ex:
            print(f'erro ao obter o innerHTML do article: {ex}')

    def delete_post(self, article):
        status = True

        try:
            caret = article.find_element(By.XPATH, "//div[@data-testid='caret']")

            caret.click()

            dropdown = WebDriverWait(self.driver, 1.0).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='Dropdown']")))
            
            menuitem = dropdown.find_element(By.TAG_NAME, "div")

            menuitem.click()

            confirmationSheetConfirm = WebDriverWait(self.driver, 1.0).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='confirmationSheetConfirm']")))

            confirmationSheetConfirm.click()
        except Exception as ex:
            status = False
            print(f'erro ao exlcluir post: {ex}\n')

        return status

    def get_post_info_from_soup(self, soup):
        try:
            post = Post()

            user_name_div = soup.find('div', attrs = {'data-testid': 'User-Name'})

            user_name_link = user_name_div.find('a')

            user = user_name_link['href'].split('/')[-1]

            tweetText_divs = soup.find_all('div', attrs = {'data-testid': 'tweetText'}) or []
            text = "".join([span.get_text() for div in tweetText_divs for span in div.find_all('span')])
            
            timetag = soup.find('time')
            datetime = timetag['datetime']

            link_tags = soup.find_all('a')

            for link in link_tags:
                post.add_link(link['href'])

            image_tags = soup.find_all('img')
            
            for img in image_tags:
                post.add_image(img['src'])

            videos_tags = soup.find_all('video')

            for video in videos_tags:
                src = video['src']
                if not src.startswith('blob'):
                    post.add_video(src)

            post.set_user(user)
            post.set_text(text)
            post.set_datetime(datetime)
           
            return post
        except Exception as ex:
            print(f'erro ao capturar informações do post: {ex}\n')
    
    
