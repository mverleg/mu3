
'''
    specific settings for your project;
    always extend existing lists
'''


from mu3.settings import *
from local import *  # @UnusedWildImport
from os import path

BASE_DIR = path.dirname(path.dirname(__file__))

''' path of the site-wide base template, which should contain a {% block content %} '''
print '\n\n   SETTINGS NOW!!\n\n'
BASE_TEMPLATE = 'mu3_base.html'

INSTALLED_APPS += (
    'base',
)

MEDIA_ROOT = path.join(BASE_DIR, 'data')

TEMPLATE_CONTEXT_PROCESSORS += (
    'base.context.context_settings.context_settings',
)


