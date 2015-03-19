
"""
    a few local, potentially secret, settings
    do not include this in your repository!
"""

from mu3.settings import DATABASES
from os import path

BASE_DIR = path.dirname(path.dirname(__file__))

SITE_URL = 'markv.nl'

SECRET_KEY = '[secret_key]'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': path.join(BASE_DIR, 'data/default.sqlite3'),
}

ALLOWED_HOSTS = ['.%s' % SITE_URL]

DEBUG = True


