## InstaPy Telegram Extension

### Available methods

- hello (print Hello World to your Telegram)
- send_daily_report
  (send daily activity report (likes, comments, follows, unfollows))

### How to install

- git clone this repository
- move instapy_telegram_extension (folder) to InstaPy/extensions
- install dependencies with `pip install -r requirements.txt`
- add `from extensions.instapy_telegram_extension import InstaPyTelegramExtension`
  to your config file (config.py / quickstart.py) file.

### Usage example

```python
from instapy import InstaPy
from extensions.instapy_telegram_extension import InstaPyTelegramExtension

insta_username = ''
insta_password = ''

session = InstaPy(username=insta_username, password=insta_password)

telegram_ext = InstaPyTelegramExtension(
    'telegram bot key',
    'your user id',
    session)

session.login()
telegram_ext.hello()
session.like_by_tags(['food'], amount=1)
telegram_ext.send_daily_report()

session.end()
```
