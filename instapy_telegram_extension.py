from app import InstaPy
import telepot
import sqlite3


class InstaPyTelegramExtension(InstaPy):

    bot_key = ''

    def __init__(self):
        self.bot = telepot.Bot(self.bot_key)
        self.likes = 0
        self.comments = 0
        self.follows = 0
        self.unfollows = 0
        self.server_calls = 0

    def go_to_google(self, session):
        session.browser.get('http://www.google.com')

    def collect_data(self):
        conn = sqlite3.connect('./db/instapy.db')
        with conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            sql = "SELECT * FROM statistics WHERE created == date('now')"
            cur.execute(sql)
            data = cur.fetchone()

        if data is not None:
            data = dict(data)
            self.likes = data['likes']
            self.comments = data['comments']
            self.follows = data['follows']
            self.unfollos = data['unfollows']
            self.server_calls = data['server_calls']

    def send_report(self, username):
        self.bot.sendMessage(
            148053207, 'IstaPy Report!\nprofile: {}\nLiked: {}\n'
            'Commented: {}\nFollowed: {}\nUnfollowed: {}\nserver calls: {}'
            .format(username, self.likes, self.comments, self.follows,
                    self.unfollows, self.server_calls))
