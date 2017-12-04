try:
    from app import InstaPy
except:
    from instapy import InstaPy
import telepot
import sqlite3


class InstaPyTelegramExtension(InstaPy):

    def __init__(self, bot_key, user_id, session):
        self.bot = telepot.Bot(bot_key)
        self.user_id = user_id
        self.core = session
        self.likes = 0
        self.comments = 0
        self.follows = 0
        self.unfollows = 0
        self.server_calls = 0

    def hello(self):
        self.bot.sendMessage(self.user_id, "Hello World !")

    def send_daily_report(self):
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

        self.bot.sendMessage(
            self.user_id, '# IstaPy Daily Report #\nprofile: {}\nLiked: {}\n'
            'Commented: {}\nFollowed: {}\nUnfollowed: {}\nserver calls: {}'
            .format(self.core.username, self.likes, self.comments,
                    self.follows, self.unfollows, self.server_calls))
