
'''
    a few local, potentially secret, settings
    do not include this in your repository!
'''

from mu3.settings import DATABASES  # @UnresolvedImport
from os import path

BASE_DIR = path.dirname(path.dirname(__file__))


SECRET_KEY = '[secret_key]'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': path.join(BASE_DIR, 'data/default.sqlite3'),
}

