from setuptools import setup, find_packages

__version__ = '0.0.1'
__author__ = u'João Paulo Vanzuita'

REQUIREMENTS = (
    'instagram_py',
)


setup(
    name='instapy_telegram_extension',
    version=__version__,
    author=__author__,
    author_email='joaovanzuita@me.com',
    url='https://github.com/converge/instapy_telegram_extension',
    description='Telegram extension for InstaPy',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
)
