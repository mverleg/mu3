
'''
    specific settings for your project;
    always extend existing lists
'''


from mu3.settings import *
from local import *  # @UnusedWildImport
from os import path

BASE_DIR = path.dirname(path.dirname(__file__))

''' path of the site-wide base template, which should contain a {% block content %} '''
BASE_TEMPLATE = 'base.html'

AUTH_USER_MODEL = 'account.MuUser'

INSTALLED_APPS += (
    'base',
    'account',
    'testapp',
)

MEDIA_ROOT = path.join(BASE_DIR, 'data')

TEMPLATE_CONTEXT_PROCESSORS += (
    'base.context.context_settings.context_settings',
)


