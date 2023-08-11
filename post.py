
class Post:
    def __init__(self):
        self.user = ''
        self.text = ''
        self.datetime = ''
        self.links = []
        self.imgs = []
        self.videos = []

    def get_text(self):
        return self.text + '$'
    
    def get_links(self):
        return '$'.join(self.links) + '$'

    def get_images(self):
        return '$'.join(self.imgs) + '$'

    def get_videos(self):
        return '$'.join(self.videos) + '$'

    def set_user(self, user):
        self.user = user

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_datetime(self, datetime):
        self.datetime = datetime

    def add_link(self, url):
        self.links.append(url)

    def add_image(self, url):
        self.imgs.append(url)

    def add_video(self, url):
        self.videos.append(url)
        
