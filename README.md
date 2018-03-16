InstaPy Telegram Extension
--
### Available methods

- hello (print Hello World to your Telegram)
- send_daily_report
  (send daily activity report (likes, comments, follows, unfollows))

### How to install

- pip install git@github.com:converge/instapy_telegram_extension.git

### Usage example

```python
from instapy import InstaPy
from instapy_telegram.extension import InstaPyTelegramExtension

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
