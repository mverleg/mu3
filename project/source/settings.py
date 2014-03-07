
'''
    specific settings for your project;
    always extend existing lists
'''


from mu3.settings import *
from local import *  # @UnusedWildImport
from os import path

BASE_DIR = path.dirname(path.dirname(__file__))

''' path of the site-wide base template, which should contain a {% block content %} '''
BASE_TEMPLATE = 'mu3_base.html'


